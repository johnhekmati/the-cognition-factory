# The Cognition Factory

**Systems for accelerated mastery under real constraints.**

**Local path:** `C:\Grok\tcf-site`  
**Session spine (multi-repo):** `C:\Grok\tcf-ground-truth`

Public marketing site for [The Cognition Factory](https://thecognitionfactory.com).

## Offering hierarchy (copy SSOT)

| Layer | Nouns | Role |
|-------|--------|------|
| **Offering** | **The Cognition Factory (TCF)** | The product — closed-loop mastery under real constraints |
| **Engines** | **HAL-E** (deep learning) · **AAE** (practice) · **CSS** (save place) | How work moves inside TCF |
| **Lattice** | **CMS** | Orientation, bridges, offramps — not a peer SKU |

> Depth builds. Practice proves. Save place keeps the loop alive. **That is TCF.**

**Funnel (page order):** Hero → Enemy → How it works → Deep learning → Practice → Cores → Save place → Research → Architect → Contact.

### Selective collateral (private · request only)

| Item | Where | Notes |
|------|--------|--------|
| **Partner & media packet** | **`C:\Grok\tcf-private\partner-media\`** (sibling folder — **not** in this public repo / not deployed) | Lineage map + partner brief. Guides shows a **request-only** card → `/api/contact` (Web3Forms) with `interest=partner-packet`. Share out of band after review. |
| Public site | No downloadable HTML for this packet | Filter: **Request only** |

## Live Site

- **Production**: [https://thecognitionfactory.com](https://thecognitionfactory.com)

## Tech Stack

- Static single-page site (`index.html`)
- Tailwind CSS v3 (CLI build)
- Vanilla JavaScript (no frameworks)
- Deployed to Cloudflare Pages via GitHub Actions

## Project Structure

```
.
├── .github/workflows/deploy.yml   # Worker + Cloudflare Pages deployment
├── functions/
│   └── api/contact.js             # Pages Function → Web3Forms → Proton inbox
├── workers/
│   └── contact-email/             # Deprecated (CF Email Routing removed)
├── src/
│   └── input.css                  # Tailwind source
├── css/
│   └── styles.css                 # Built output (committed)
├── js/
│   └── main.js                    # Site interactions (nav, videos, form, etc.)
├── assets/
│   ├── images/                    # Branding images + posters
│   ├── videos/                    # Hero + section videos
│   └── docs/                      # Knowledge Base PDFs + brand reference files
├── index.html
├── 404.html
├── wrangler.jsonc                 # Cloudflare Pages project config
├── tailwind.config.js
├── package.json
├── _redirects                     # Legacy Netlify redirects (see notes)
├── _headers                       # Cloudflare Pages headers (security + caching)
└── README.md
```

## Getting Started

### Prerequisites

- Node.js 18+
- npm

### Install

```bash
npm install
```

### Development (watch mode)

```bash
npm run dev
```

This runs Tailwind in watch mode and outputs to `css/styles.css`.

### Build for production

```bash
npm run build
```

Minifies the CSS output.

### Preview locally

```bash
npm run preview
```

Uses the `serve` package to serve the root directory.

## Deployment

Deployment is handled automatically by GitHub Actions:

- Triggers on push to `main`
- Also supports manual `workflow_dispatch`
- Runs `npm ci` → `npm run build` → `wrangler pages deploy`

**Required repository secrets** (Settings → Secrets and variables → Actions):

- `CLOUDFLARE_API_TOKEN`
- `CLOUDFLARE_ACCOUNT_ID`

The site is deployed directly from the project root (no separate `dist` folder).

## Assets

Media files are stored in:

- `assets/images/`
- `assets/videos/`
- `assets/docs/`

See the `.gitkeep` files in each directory for the current list of expected files. These `.gitkeep` files are kept up to date with what `index.html` actually references.

### Knowledge base (`#resources`)

**Browser-native HTML** (preferred entry) plus PDFs where available.

| Card | File | Notes |
|------|------|--------|
| Solo Path for Busy Adults | `Solo_Learner_Everyday.html` | Everyday · amber Solo filter |
| Solo Path for Power Users | `Solo_Learner_Guide.html` | Operator depth · v1.1 |
| HAL-E + AAE Methodology | `Methodology.html` (+ PDF) | |
| HAL-E + AAE Executive Whitepaper | `Executive_Whitepaper.html` (+ PDF) | |
| LMS Integration Guide | `LMS_Integration_Guide.html` (+ PDF) | |
| Enterprise Deployment SOP | `Enterprise_Deployment_SOP.html` (+ PDF) | |
| Security & Compliance SOP | `Security_and_Compliance_SOP.html` (+ PDF) | |

Shared theme: `assets/docs/doc-theme.css` (includes AAE amber).  
Solo filter/tag: amber/gold (`resource-filter--solo`, `resource-tag--solo`).

To add a doc: drop under `assets/docs/`, add a kbase card in `index.html`, filter category as needed.

See **`CHANGELOG.md`** for the 2026-07-13 funnel + branding pass.

## Contact Form

Domain mail is **Proton** (MX / TXT as Proton requires). Cloudflare Email Routing is **not** used.

The contact form (`#contact-form`) posts to Pages Function `/api/contact`, which validates fields and submits via [Web3Forms](https://web3forms.com) to your Proton inbox.

See:
- `functions/api/contact.js`
- `js/main.js` → `initContactForm()`

### Required setup (one-time)

1. Create a free access key at [web3forms.com](https://web3forms.com) using **`contact@thecognitionfactory.com`** (or another catch-all you read).
2. In Cloudflare dashboard → **Workers & Pages** → project **the-cognition-factory** → **Settings** → **Environment variables**:
   - Secret: `WEB3FORMS_ACCESS_KEY` = your access key
   - Optional plain var: `CONTACT_TO_EMAIL` = `contact@thecognitionfactory.com` (label only; Web3Forms delivers to the email used when the key was created)
3. Redeploy Pages (or push to `main`) so the Function picks up the secret.
4. Test the live form; confirm mail arrives in Proton.

Direct email fallback (always on the page): `mailto:contact@thecognitionfactory.com`.

GitHub Actions deploys the Worker first, then Pages (see Deployment above).

## Notes & Gotchas

- **CSS cache busting**: `index.html` references `css/styles.css?v=hybrid*` (bump when styles change).
- **Redirects**: `_redirects` uses Netlify syntax. It currently only contains legacy video filename redirects. These have no effect on Cloudflare Pages unless converted to Cloudflare-compatible routing.
- **Headers**: `_headers` provides security headers and caching rules for Cloudflare Pages.
- **Built CSS is committed**: `css/styles.css` is checked in so the site can be served directly from the repo root.
- **Heavy video usage**: The site relies on several autoplay, muted, looping videos with poster fallbacks and reduced-motion handling.

## Brand Documentation

Brand guidelines and system descriptions live in `assets/docs/`:

- `AAE Brand System (HAL‑E Family).md`
- `HAL-E Brand Guidelines.txt`

## License

Private project. All rights reserved.

---

Built for people who need to develop genuine expertise quickly and maintain it under pressure.