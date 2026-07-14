# Site changelog

Public marketing site (`tcf-site` / thecognitionfactory.com). Newest first.

---

## 2026-07-13 — Contact form → Proton (Web3Forms) + light plain-English

### Contact
- Removed Cloudflare Email Routing / `contact-email` Worker from deploy path
- `/api/contact` Pages Function delivers via **Web3Forms** to Proton inbox
- Secret: `WEB3FORMS_ACCESS_KEY` on Pages project (see README)
- Honeypot field on form; direct `mailto:contact@…` remains as fallback

### Prose (surgical)
- Hero institutional line: skill on the job, not hours logged
- Loop: “two tools / one loop”; between-session save language
- CTA: “How each tool works”
- Architect + contact micro-copy slightly plainer

---

## 2026-07-13 — Funnel polish, dual Solo paths, Between sessions

**Ship:** `main` `2335a7b` (and follow-on copy if any).

### Funnel & prose
- Page order: **Hero → Enemy → Loop → engines → Cores → Between sessions → Research → Architect → Contact**
- Executive-summary plain English; CTAs ladder (See the problem first → loop → engines → contact)
- Ritual strip: MAP · PRACTICE · PROVE · CONTINUE

### Solo knowledge base
- **Solo Path for Busy Adults** (`Solo_Learner_Everyday.html`) — Kristi-class feedback
- **Solo Path for Power Users** (`Solo_Learner_Guide.html`) — operator field picture; cross-links both ways
- Solo filter + tag + card hover: **AAE amber/gold**

### Between sessions
- Nav/footer/section renamed from Continuity product framing → **Between sessions**
- CSS + CMS remain connective tissue (not peer products)

### Brand
- AAE amber/gold tokens in Tailwind + `doc-theme.css`
- Dual colorways consistent with household app

### Next
- Optional: PDF exports of new Solo everyday HTML  
- Curriculum Client_0 still owned by Production (not this repo)

---

## Earlier

- Second-pass Continuity copy, HTML knowledge base, Solo Guide v1.1  
- Dual-audience story, contact Worker, CF Pages deploy  
