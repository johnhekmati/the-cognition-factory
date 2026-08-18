/**
 * Contact form — Web3Forms → Proton.
 * Vercel Edge port of functions/api/contact.js (kept for CF until DNS flips).
 *
 * Project env: WEB3FORMS_ACCESS_KEY (required), CONTACT_TO_EMAIL (optional).
 */

export const config = { runtime: 'edge' };

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

export default async function handler(request) {
  if (request.method !== 'POST') {
    return json(
      { success: false, error: 'Method not allowed. Use POST.' },
      405
    );
  }

  const env = {
    WEB3FORMS_ACCESS_KEY: process.env.WEB3FORMS_ACCESS_KEY,
    CONTACT_TO_EMAIL: process.env.CONTACT_TO_EMAIL,
  };

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
  if (!rateAllow(ip)) {
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
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return false;
  if ((email.match(/@/g) || []).length !== 1) return false;
  return true;
}

function originAllowed(request) {
  const origin = request.headers.get('Origin');
  const referer = request.headers.get('Referer');
  if (!origin && !referer) return false;

  const candidates = [origin, referer].filter(Boolean);
  for (const raw of candidates) {
    try {
      const u = new URL(raw);
      if (ALLOWED_HOSTS.has(u.hostname)) return true;
      if (
        u.hostname.endsWith('.pages.dev') &&
        u.hostname.includes('the-cognition-factory')
      ) {
        return true;
      }
      if (
        u.hostname.endsWith('.vercel.app') &&
        (u.hostname.includes('cognition') ||
          u.hostname.includes('the-cognition-factory'))
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
    request.headers.get('x-forwarded-for')?.split(',')[0]?.trim() ||
    request.headers.get('x-real-ip') ||
    'unknown'
  );
}

function rateAllow(ip) {
  const now = Date.now();
  const key = String(ip || 'unknown');
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
  return bucket.count <= RATE_MAX;
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
