# Deprecated — contact-email Worker

This Worker used **Cloudflare Email Routing** (`send_email` binding) to deliver
contact form mail. Email for `thecognitionfactory.com` now uses **Proton** MX;
CF Email Routing is disabled.

**Current path:** Pages Function `functions/api/contact.js` → [Web3Forms](https://web3forms.com)
→ Proton inbox (`contact@thecognitionfactory.com` by default).

Do not redeploy this Worker unless you intentionally re-enable CF Email Routing.
