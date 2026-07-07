const DEFAULT_TO = "phillipjohnhekmati@outlook.com";

export default {
  async fetch(request, env) {
    if (request.method !== "POST") {
      return new Response("Method not allowed", { status: 405 });
    }

    try {
      if (!env.EMAIL) {
        console.error("contact-email: EMAIL binding missing");
        return json({ success: false, error: "Email service is not configured." }, 500);
      }

      const toAddress = (env.CONTACT_TO_EMAIL || DEFAULT_TO).toString().trim();
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

      console.log("contact-email sent:", { messageId: result?.messageId, to: toAddress });
      return json({ success: true });
    } catch (err) {
      console.error("contact-email failed:", err?.message || err);
      return json(
        {
          success: false,
          error: "Sorry, something went wrong while sending your message. Please try again or email us directly.",
        },
        500
      );
    }
  },
};

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}