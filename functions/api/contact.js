import { EmailMessage } from "cloudflare:email";

/**
 * Contact form handler for The Cognition Factory.
 *
 * Expects a POST with form fields:
 *   first-name, last-name, email, organization, interest, message
 *
 * Sends the submission via Cloudflare Email Routing (send_email binding).
 *
 * Binding required:
 *   - Name: EMAIL (type: Send Email)
 *
 * Configure the binding in the Cloudflare Pages dashboard:
 *   Project → Settings → Functions → Bindings → Add binding → Send Email
 *
 * The "from" address must be allowed by your Email Routing domain setup.
 */
export async function onRequestPost({ request, env }) {
  try {
    const formData = await request.formData();

    const firstName = (formData.get("first-name") || "").toString().trim();
    const lastName = (formData.get("last-name") || "").toString().trim();
    const email = (formData.get("email") || "").toString().trim();
    const organization = (formData.get("organization") || "").toString().trim() || "Not provided";
    const interest = (formData.get("interest") || "").toString().trim() || "Not specified";
    const message = (formData.get("message") || "").toString().trim();

    // Basic validation (HTML also has required attributes)
    if (!firstName || !lastName || !email || !message) {
      return json({ success: false, error: "Please fill out all required fields." }, 400);
    }

    // Basic email format sanity check
    if (!email.includes("@") || email.length < 5) {
      return json({ success: false, error: "Please provide a valid email address." }, 400);
    }

    const subject = `Contact: ${firstName} ${lastName} — ${interest}`;

    const body = [
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

    // Build a minimal RFC-compliant raw message.
    // Using the submitter's email as Reply-To so you can reply directly.
    const rawMessage = [
      `From: contact@thecognitionfactory.com`,
      `To: contact@thecognitionfactory.com`,
      `Reply-To: ${email}`,
      `Subject: ${subject}`,
      `Content-Type: text/plain; charset="UTF-8"`,
      "",
      body,
    ].join("\r\n");

    // Send via the configured Email Routing send binding.
    // The binding name "EMAIL" must match what you set in the dashboard.
    await env.EMAIL.send(
      new EmailMessage("contact@thecognitionfactory.com", "contact@thecognitionfactory.com", rawMessage)
    );

    return json({ success: true });
  } catch (err) {
    // Log for debugging in Cloudflare dashboard
    console.error("Contact form submission failed:", err);

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
