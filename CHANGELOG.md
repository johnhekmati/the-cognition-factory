# Site changelog

Public marketing site (`tcf-site` / thecognitionfactory.com). Newest first.

**Release rule:** every ship to `main` that changes public behavior or legal/surface copy gets an entry here *before or with* the commit. Date = ship day (operator local).

---

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

## 2026-07-28 — Contact API abuse harden (audit re-gate)

- **Origin fail-closed:** reject POST when Origin and Referer both missing (no bare curl spam)
- **Dual rate limit:** isolate Map + Cache API; cap 5/min/IP (still pair CF WAF)
- **POST only:** `onRequest` rejects non-POST; forms `method="post" action="/api/contact"`
- Email field header-sanitized for replyto

---

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

## 2026-07-28 — Guides legal triad + media row

- Guides: separate **Privacy / Terms / EULA** cards (full 3-col row)
- **Security & Compliance** + **Partner & media packet** share a tail row (1/3 + 2/3 via `md:col-span-2`)

---

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

## 2026-07-28 — Hero ritual chips brand color

- Hero MAP / PRACTICE / SAVE PLACE chips use triad colorway (electric / amber / plasma), shared modifiers with Connect doors

---

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

## 2026-07-28 — Story spine reorg

### Information architecture
- Section order: Hero → Problem → Solution → How → HAL-E → AAE → Dojo → **Save place** → Who → What you work with → Product → **Proof + First 10** → Why → **Guides** → Connect → footer
- **First 10 minutes** moved out of hero into `#proof` (hero stays banner + H1 + loop strip)
- Nav / footer / hero secondary CTAs slimmed to story spine: Problem · How · Product · Proof · Why · Guides · Talk

---

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

## 2026-07-28 — Maturity pack (legal, brand, human loops, harden)

### Legal
- Knowledge-base HTML: **Privacy Policy**, **Terms of Service**, **EULA** (`assets/docs/`, doc-theme)
- Footer links + Guides card (Privacy · Terms · EULA)
- **Install & updates** guide for second machine / second person

### Brand / UI
- CF monogram hero: static → spinner one-shot + quiet click-to-replay; dual-tone electric/plasma edge glow (half-weight)
- Flat OS-style mark for favicon / header / footer; Connect **three-doors** banner v2 + full-width MAP / PRACTICE / SAVE PLACE chips
- Hero reduced-motion fix (no empty frame)
- **How we show up** rails on `#promise` — what we do / what we don’t (no theater, no cape, no guaranteed outcomes, no logo endorsement claims); Connect walk-away tightened

### Human maturity (not feature sprawl)
- **First 10 minutes** definition of done on hero
- Connect **offer ladder** (solo · team · institution · walk-away) + support ritual copy
- **Proof of a loop** section (`#proof`) — park note as proof, not fake metrics

### Security / ops
- Contact API: rate limit, origin allowlist, field caps, subject sanitize, safe errors
- Headers: CSP, HSTS, tighter Permissions-Policy
- Deploy prune: keep `wrangler.jsonc`, pass `.` to Pages deploy (fixes failed Actions after over-prune)
- Form: no double-submit race; lightbox focus trap; noscript reveal

### Cache
- Prefer `main.js?v=audit-march1` (and later) for JS after form/hero changes

### Release hygiene
- Changelog required on ship; footer **Changelog** link to this file on GitHub
- Operator ship checklist: `tcf-private/John-eyes-only/SHIP_CHECKLIST.md` (not public)

---

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

## 2026-07-25 — Dojo + Who trains here (funnel pass)

### New sections (`index.html`)
- **`#dojo`** (after `#aae`, plasma accent): scenario-pack practice — *deliver it when it's messy*
  - Recognize → recall → **deliver** ladder strip
  - Three public-safe scenario teasers (closed period / 3-way disagreement / messy dump → plan) — flavor only, no cart IDs or core paths from `tcf-production`
  - CMS as quiet layer: one line ("same map … all three telling one story"); no ERP/Dynamics, no cert claims, no job guarantees
- **`#who`** (after `#dojo`): three ICP cards — Solo learners (electric) · Teams ramp/cross-skill (amber) · Partners screening for delivery over cert walls (plasma); each with `#contact` CTA

### Tie-ins
- Nav + mobile menu + footer site map: **Dojo** link after Practice (desktop nav gap 7→6)
- Hero: third register line — *For partners who need proof of delivery — not a wall of certs*
- `#loop`: map/pack paragraph now points to the Dojo for real-world reps
- `#aae`: "Then step into the Dojo →" handoff link
- `#systems`: teams glass-card trimmed to a one-line briefing link (was duplicating `#who`)

### Hero — stick the landing
- Hero banner no longer loops forever: **two full passes → decelerate (~1.6s window, down to 0.45×) → hold the composed CF mark**
- Frame chrome settles with the landing: border + soft electric bloom ease in over 1.6s (`#hero-video-wrap.is-landed`)
- Click the landed banner for one quiet replay pass; reduced-motion still gets the static poster
- `js/main.js` single-video path only; section/context videos untouched

### Cache
- `styles.css?v=tcf-dojo1` · `main.js?v=hero-land1`

---

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

## 2026-07-19 — Product gallery (real SSes, sharp scrub)

### `#product`
- Live desktop screenshots: Deep · Practice · Save place · thin SoR · Help/shell
- Story order matches the ritual: map · practice · save place, then workflow, then shell
- Public scrub: no school chip (WGU→Accounting), LLM label = **Assistant** (provider customizable), no last-name chrome
- Sharp pipeline: `scripts/scrub_product_screenshots.py` from original W11 PNGs (no multi-pass generative smear)
- Image cache bust `?v=pg1`
- Profiles tile **skipped** (parked)
- **Click-to-enlarge lightbox:** full-res `object-contain` popup (Esc / backdrop / ×); `cursor-zoom-in` + “Click to enlarge” hint
- Top-bar display name → **Learner** (pixel scrub from originals; no generative smear); image cache `?v=pg2`
- Footer site map: **Product** → `#product` (same order as top nav)
- Product platforms: **Windows + Android** now; **macOS & iOS — coming soon** (readiness, not Capes)
- Android gallery strip: Deep · Practice · Save · chat (from device SSes; Grok→Assistant pixel scrub); `scripts/scrub_android_screenshots.py`

### Docs
- `docs/SITE_PRODUCT_GALLERY_NOTES.md` — brand rules, scrub policy, legibility rule

---

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

## 2026-07-17 — Copy bonsai (idioms & one-liners)

### Narrative clarity (`index.html`)
- **Canon once:** hero ritual strip owns “Map · practice · save place — that is the whole idea”
- **Prune loop restarts:** cut duplicate “whole idea” / three-moves stackers in Solution + How it works
- **Plain language:** closed loop → *loop that holds when life interrupts*; honest pressure (not “real”); You — alone or with a team
- **Skill stickiness:** one phrase — *still works next month* (drop “survives the calendar” on first path)
- **Save place first-time path:** lead with public names; demote CSS/CMS monograms; surveillance → chat archive
- **Guides blurbs:** no *sausage* / *thrash* — plain product / re-finding yourself
- **Why:** quality bar alone as closer; less engine recitation

### Cache
- `styles.css?v=tcf-copy-bonsai1`

---

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

## 2026-07-15 — Hero funnel, kbase product docs, motion mark

### Funnel
- Dual-hemisphere logo motion: `cogfacheromotion.mp4` + still poster
- Hero copy: upskilling taglines + reverse gradient; H1 “A way to upskill that just works”
- Problem: text-only (no brand brain video)
- **The solution** section bridges Problem → How it works

### Guides
- `Desktop_App_Overview.html` · `Between_Sessions.html` (public-safe, shallow)
- Partner media form full-width under grid
- Security SOP blurb densified

---

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

## 2026-07-15 — TCF hero banner (cogfag)

- Replace dual HAL-E/AAE hero crossfade with single **The Cognition Factory** banner loop
- Assets: `assets/videos/cogfagherobanner.mp4` + poster `assets/images/cogfacherobanner.jpg`
- Restrained centered card (max ~56rem); aspect-ratio locked to video so media fills the frame border
- Badge fixed to product name; no full-bleed wall

---

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

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

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

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

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

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

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

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

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

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

## 2026-07-29 — Meta / title slogan clean

- Browser title + OG/Twitter: **Skill that sticks when life is loud. Map. Practice. Save your place.**
- No literal `\n` / broken hero string in share cards

## Earlier

- Second-pass Continuity copy, HTML knowledge base, Solo Guide v1.1  
- Dual-audience story, contact Worker, CF Pages deploy  
