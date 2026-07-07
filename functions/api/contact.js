/**
 * Contact form handler — proxies to the contact-email Worker via service binding.
 * Pages Functions cannot use send_email directly; the Worker sends mail.
 */
export async function onRequestPost({ request, env }) {
  if (!env.CONTACT_MAILER) {
    console.error("Contact form: CONTACT_MAILER service binding is missing.");
    return json(
      { success: false, error: "Email service is not configured. Please try again later." },
      500
    );
  }

  return env.CONTACT_MAILER.fetch(request);
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}