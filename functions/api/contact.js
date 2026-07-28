/**
 * Contact form handler — delivers to Proton inbox via Web3Forms.
 *
 * Cloudflare Email Routing / send_email is no longer used (MX points at Proton).
 * Set Pages secret: WEB3FORMS_ACCESS_KEY
 *   Create free key at https://web3forms.com with contact@thecognitionfactory.com
 *
 * Optional var: CONTACT_TO_EMAIL (defaults to contact@thecognitionfactory.com)
 *
 * Abuse controls:
 * - Origin/Referer allowlist (fail closed if both missing)
 * - Field length caps + subject sanitize
 * - Dual rate limit: isolate Map + Cache API (edge), still pair with CF WAF
 */

const DEFAULT_TO = 'contact@thecognitionfactory.com';
const ALLOWED_HOSTS = new Set([
  'thecognitionfactory.com',
  'www.thecognitionfactory.com',
  'localhost',
  '127.0.0.1',
]);

const CAPS = {
  firstName: 100,
  lastName: 100,
  email: 254,
  organization: 200,
  interest: 120,
  message: 5000,
};

/** @type {Map<string, { count: number, reset: number }>} */
const rateBuckets = new Map();
const RATE_WINDOW_MS = 60_000;
const RATE_MAX = 5;

/** POST only — reject GET form fallbacks. */
export async function onRequest(context) {
  if (context.request.method !== 'POST') {
    return json(
      {
        success: false,
        error: 'Method not allowed. Use POST.',
      },
      405
    );
  }
  return onRequestPost(context);
}

export async function onRequestPost({ request, env }) {
  const accessKey = (env.WEB3FORMS_ACCESS_KEY || '').toString().trim();
  if (!accessKey) {
    console.error('Contact form: WEB3FORMS_ACCESS_KEY is not set.');
    return json(
      {
        success: false,
        error:
          'Contact form is not configured yet. Email contact@thecognitionfactory.com directly.',
      },
      503
    );
  }

  if (!originAllowed(request)) {
    return json({ success: false, error: 'Invalid request origin.' }, 403);
  }

  const ip = clientIp(request);
  if (!(await rateAllow(ip))) {
    return json(
      {
        success: false,
        error: 'Too many requests. Please wait a minute and try again.',
      },
      429
    );
  }

  let formData;
  try {
    formData = await request.formData();
  } catch {
    return json({ success: false, error: 'Invalid form submission.' }, 400);
  }

  // Honeypot — bots fill hidden "botcheck"
  const bot = (formData.get('botcheck') || '').toString().trim();
  if (bot) {
    return json({ success: true });
  }

  const firstName = clip(
    (formData.get('first-name') || '').toString().trim(),
    CAPS.firstName
  );
  const lastName = clip(
    (formData.get('last-name') || '').toString().trim(),
    CAPS.lastName
  );
  const email = sanitizeHeader(
    clip((formData.get('email') || '').toString().trim(), CAPS.email)
  );
  const organization =
    clip(
      (formData.get('organization') || '').toString().trim(),
      CAPS.organization
    ) || 'Not provided';
  const interest =
    clip((formData.get('interest') || '').toString().trim(), CAPS.interest) ||
    'Not specified';
  const message = clip(
    (formData.get('message') || '').toString().trim(),
    CAPS.message
  );

  if (!firstName || !lastName || !email || !message) {
    return json(
      { success: false, error: 'Please fill out all required fields.' },
      400
    );
  }

  if (!isPlausibleEmail(email)) {
    return json(
      { success: false, error: 'Please provide a valid email address.' },
      400
    );
  }

  const toAddress = (env.CONTACT_TO_EMAIL || DEFAULT_TO).toString().trim();
  const fullName = sanitizeHeader(`${firstName} ${lastName}`);
  const interestSafe = sanitizeHeader(interest);
  const interestLower = interestSafe.toLowerCase();
  const isPartnerPacket =
    interestSafe === 'partner-packet' ||
    (interestLower.includes('partner') && interestLower.includes('packet'));
  const subject = sanitizeHeader(
    isPartnerPacket
      ? `TCF partner packet request: ${fullName}`
      : `TCF contact: ${fullName} — ${interestSafe}`
  ).slice(0, 180);

  const body = [
    `Name: ${fullName}`,
    `Email: ${email}`,
    `Organization: ${organization}`,
    `Path: ${interestSafe}`,
    isPartnerPacket
      ? 'Artifact: Partner & media prospectus (lineage map) — share out of band; not on public site'
      : null,
    '',
    'Message:',
    message,
    '',
    '—',
    isPartnerPacket
      ? 'Sent from thecognitionfactory.com partner-packet request'
      : 'Sent from thecognitionfactory.com contact form',
    `Deliver-to preference: ${toAddress}`,
  ]
    .filter((line) => line !== null)
    .join('\n');

  try {
    const res = await fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
      body: JSON.stringify({
        access_key: accessKey,
        subject,
        name: fullName,
        email,
        from_name: 'The Cognition Factory site',
        message: body,
        replyto: email,
      }),
    });

    const result = await res.json().catch(() => ({}));

    if (res.ok && (result.success === true || result.success === 'true')) {
      return json({ success: true });
    }

    console.error('Web3Forms error:', result);
    return json(
      {
        success: false,
        error:
          'Sorry, something went wrong while sending your message. Please email contact@thecognitionfactory.com directly.',
      },
      502
    );
  } catch (err) {
    console.error('Contact form failed:', err?.message || err);
    return json(
      {
        success: false,
        error:
          'Sorry, something went wrong while sending your message. Please email contact@thecognitionfactory.com directly.',
      },
      500
    );
  }
}

function clip(s, max) {
  if (s.length <= max) return s;
  return s.slice(0, max);
}

function sanitizeHeader(s) {
  return s.replace(/[\r\n\x00-\x1f\x7f]/g, ' ').replace(/\s+/g, ' ').trim();
}

function isPlausibleEmail(email) {
  if (email.length < 5 || email.length > 254) return false;
  // Single @, local + domain with a dot; no spaces/control chars
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return false;
  if ((email.match(/@/g) || []).length !== 1) return false;
  return true;
}

/**
 * Fail closed: require Origin and/or Referer, and hostname must be allowlisted.
 * Bare curl without those headers is rejected (RED-01).
 */
function originAllowed(request) {
  const origin = request.headers.get('Origin');
  const referer = request.headers.get('Referer');
  if (!origin && !referer) return false;

  const candidates = [origin, referer].filter(Boolean);
  for (const raw of candidates) {
    try {
      const u = new URL(raw);
      if (ALLOWED_HOSTS.has(u.hostname)) return true;
      // Cloudflare Pages preview deploys
      if (
        u.hostname.endsWith('.pages.dev') &&
        u.hostname.includes('the-cognition-factory')
      ) {
        return true;
      }
    } catch {
      /* ignore */
    }
  }
  return false;
}

function clientIp(request) {
  return (
    request.headers.get('CF-Connecting-IP') ||
    request.headers.get('X-Forwarded-For')?.split(',')[0]?.trim() ||
    'unknown'
  );
}

/**
 * Dual rate limit: isolate memory + Cache API (shareder across isolates/colos).
 * Still pair with Cloudflare WAF rate rules for hard multi-IP defense.
 */
async function rateAllow(ip) {
  const now = Date.now();
  const key = String(ip || 'unknown');

  // Layer 1 — this isolate (fast fail)
  let bucket = rateBuckets.get(key);
  if (!bucket || now > bucket.reset) {
    bucket = { count: 0, reset: now + RATE_WINDOW_MS };
    rateBuckets.set(key, bucket);
  }
  bucket.count += 1;
  if (rateBuckets.size > 5000) {
    for (const [k, v] of rateBuckets) {
      if (now > v.reset) rateBuckets.delete(k);
    }
  }
  if (bucket.count > RATE_MAX) return false;

  // Layer 2 — Cache API (edge, survives isolate recycle better than Map alone)
  try {
    const cache = caches.default;
    const cacheKey = new Request(
      `https://tcf-rate-limit.internal/contact/${encodeURIComponent(key)}`
    );
    const hit = await cache.match(cacheKey);
    let count = 0;
    let reset = now + RATE_WINDOW_MS;
    if (hit) {
      const data = await hit.json().catch(() => null);
      if (data && typeof data.count === 'number' && typeof data.reset === 'number') {
        if (now <= data.reset) {
          count = data.count;
          reset = data.reset;
        }
      }
    }
    count += 1;
    const ttlSec = Math.max(1, Math.ceil((reset - now) / 1000));
    await cache.put(
      cacheKey,
      new Response(JSON.stringify({ count, reset }), {
        headers: {
          'Content-Type': 'application/json',
          'Cache-Control': `public, max-age=${ttlSec}`,
        },
      })
    );
    if (count > RATE_MAX) return false;
  } catch {
    // Cache API unavailable (local) — isolate Map already applied
  }

  return true;
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'no-store',
      'X-Content-Type-Options': 'nosniff',
    },
  });
}
