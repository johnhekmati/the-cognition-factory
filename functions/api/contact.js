/**
 * Contact form handler — delivers to Proton inbox via Web3Forms.
 *
 * Cloudflare Email Routing / send_email is no longer used (MX points at Proton).
 * Set Pages secret: WEB3FORMS_ACCESS_KEY
 *   Create free key at https://web3forms.com with contact@thecognitionfactory.com
 *
 * Optional var: CONTACT_TO_EMAIL (defaults to contact@thecognitionfactory.com)
 */

const DEFAULT_TO = 'contact@thecognitionfactory.com';

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

  let formData;
  try {
    formData = await request.formData();
  } catch {
    return json({ success: false, error: 'Invalid form submission.' }, 400);
  }

  const firstName = (formData.get('first-name') || '').toString().trim();
  const lastName = (formData.get('last-name') || '').toString().trim();
  const email = (formData.get('email') || '').toString().trim();
  const organization =
    (formData.get('organization') || '').toString().trim() || 'Not provided';
  const interest =
    (formData.get('interest') || '').toString().trim() || 'Not specified';
  const message = (formData.get('message') || '').toString().trim();

  if (!firstName || !lastName || !email || !message) {
    return json(
      { success: false, error: 'Please fill out all required fields.' },
      400
    );
  }

  if (!email.includes('@') || email.length < 5) {
    return json(
      { success: false, error: 'Please provide a valid email address.' },
      400
    );
  }

  // Honeypot (optional field) — bots fill hidden "botcheck"
  const bot = (formData.get('botcheck') || '').toString().trim();
  if (bot) {
    return json({ success: true });
  }

  const toAddress = (env.CONTACT_TO_EMAIL || DEFAULT_TO).toString().trim();
  const fullName = `${firstName} ${lastName}`;
  const subject = `TCF contact: ${fullName} — ${interest}`;
  const body = [
    `Name: ${fullName}`,
    `Email: ${email}`,
    `Organization: ${organization}`,
    `Path: ${interest}`,
    '',
    'Message:',
    message,
    '',
    '—',
    'Sent from thecognitionfactory.com contact form',
    `Deliver-to preference: ${toAddress}`,
  ].join('\n');

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
        // Helps some inboxes; reply goes to submitter via Web3Forms reply-to
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
          result.message ||
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

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}
