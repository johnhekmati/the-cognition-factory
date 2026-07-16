# Site changelog

Public marketing site (`tcf-site` / thecognitionfactory.com). Newest first.

---

## 2026-07-15 — TCF hero banner (cogfag)

- Replace dual HAL-E/AAE hero crossfade with single **The Cognition Factory** banner loop
- Assets: `assets/videos/cogfagherobanner.mp4` + poster `assets/images/cogfacherobanner.jpg`
- Restrained centered card (max ~56rem); aspect-ratio locked to video so media fills the frame border
- Badge fixed to product name; no full-bleed wall

---

## 2026-07-15 — Partner packet request-only + plain-English brand pass

### Guides
- **Request only** filter + card: Partner & media packet (no public download)
- Form posts to existing `/api/contact` (Web3Forms); subject `TCF partner packet request: …`
- Contact dropdown option: Partner & media packet (request)

### Collateral location
- Partner prospectus + lineage map live under **private sibling** `C:\Grok\tcf-private\` (not in this repo / not Pages)
- Public site never ships that HTML

### Copy / brand
- House compounds: HAL-E Deep Learning · AAE Practice · CSS Save Place
- Full-page Engineerlish pass; founder A→B→C narrative polish

---

## 2026-07-15 — Learner-clarity editorial pass

### Voice (Kristi-class / busy adult first)
- Hero, enemy, loop, engines, map, save place rewritten in plain jobs language
- Nav: Your map · Guides · About (was Cores · Research · Architect)
- Ritual strip: **MAP · PRACTICE · SAVE PLACE**
- Softened “engines / lattice / Factory / SSOT / L0–L3” on the public path
- Partner/institutional path retained, demoted (not the lead story)

### Still true under the hood
- TCF remains the offering; HAL-E / AAE / CSS engines and CMS lattice exist for operators
- Solo everyday + power guides already dual-path

---

## 2026-07-15 — TCF is the offering (comprehensive copy pass)

### Positioning
- **The Cognition Factory** leads all public copy — not co-equal “two engines”
- **Engines:** HAL-E (deep learning) · AAE (practice) · CSS (save place)
- **Lattice:** CMS (orientation) — explicitly not a peer product
- Nav / footer: plain rails (Deep learning · Practice · Save place) with engine codes as secondary mono

### Surfaces updated
- `index.html` — meta, hero, enemy, loop, engines, cores, save place, research cards, architect, contact, footer
- `js/main.js` — hero badge labels under TCF
- `Solo_Learner_Everyday.html` v1.1 — TCF-first everyday path
- `Solo_Learner_Guide.html` v1.2 — offering first, engines + lattice named
- `README.md` — hierarchy SSOT

### Next (queued)
- TCF brand GFX (hero, logo, favicon) aligned to site/app colorway — **after** this copy pass

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
