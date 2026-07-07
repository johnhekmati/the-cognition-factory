/**
 * Contact form handler for The Cognition Factory.
 *
 * Expects a POST with form fields:
 *   first-name, last-name, email, organization, interest, message
 *
 * Sends via the EMAIL send_email binding (wrangler.jsonc).
 *
 * Important: `to` must be a verified Email Routing *destination address*
 * (e.g. your Gmail), not a custom routing alias like contact@yourdomain.com.
 */
export async function onRequestPost({ request, env }) {
  try {
    if (!env.EMAIL) {
      console.error("Contact form: EMAIL binding is missing on this deployment.");
      return json(
        { success: false, error: "Email service is not configured. Please try again later." },
        500
      );
    }

    const toAddress = (env.CONTACT_TO_EMAIL || "").toString().trim();
    if (!toAddress) {
      console.error("Contact form: CONTACT_TO_EMAIL is not set.");
      return json(
        { success: false, error: "Email service is not configured. Please try again later." },
        500
      );
    }

    const formData = await request.formData();

    const firstName = (formData.get("first-name") || "").toString().trim();
    const lastName = (formData.get("last-name") || "").toString().trim();
    const email = (formData.get("email") || "").toString().trim();
    const organization = (formData.get("organization") || "").toString().trim() || "Not provided";
    const interest = (formData.get("interest") || "").toString().trim() || "Not specified";
    const message = (formData.get("message") || "").toString().trim();

    if (!firstName || !lastName || !email || !message) {
      return json({ success: false, error: "Please fill out all required fields." }, 400);
    }

    if (!email.includes("@") || email.length < 5) {
      return json({ success: false, error: "Please provide a valid email address." }, 400);
    }

    const subject = `Contact: ${firstName} ${lastName} — ${interest}`;

    const text = [
      `Name: ${firstName} ${lastName}`,
      `Email: ${email}`,
      `Organization: ${organization}`,
      `Area of Interest: ${interest}`,
      "",
      "Message:",
      message,
      "",
      "—",
      "Sent from thecognitionfactory.com contact form",
    ].join("\n");

    const result = await env.EMAIL.send({
      from: { email: "contact@thecognitionfactory.com", name: "The Cognition Factory" },
      to: toAddress,
      replyTo: email,
      subject,
      text,
    });

    console.log("Contact form sent:", { messageId: result?.messageId, to: toAddress });

    return json({ success: true });
  } catch (err) {
    console.error("Contact form submission failed:", err?.message || err);

    return json(
      {
        success: false,
        error: "Sorry, something went wrong while sending your message. Please try again or email us directly.",
      },
      500
    );
  }
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}