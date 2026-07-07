# The Cognition Factory

**Systems for accelerated mastery under real constraints.**

This repository contains the public marketing site for [The Cognition Factory](https://thecognitionfactory.com), featuring **HAL-E** (Hyper Accelerated Learning Engine) and **AAE** (Adaptive Assessment Engine).

HAL-E is a learning operating system focused on building durable conceptual architecture.  
AAE is a high-precision assessment operating system that measures mastery, classifies errors, and drives targeted remediation.

> HAL-E teaches. AAE examines.

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
├── .github/workflows/deploy.yml   # Cloudflare Pages deployment
├── src/
│   └── input.css                  # Tailwind source
├── css/
│   └── styles.css                 # Built output (committed)
├── js/
│   └── main.js                    # Site interactions (nav, videos, form, etc.)
├── assets/
│   ├── images/                    # Branding images + posters
│   ├── videos/                    # Hero + section videos
│   └── docs/                      # White papers & SOPs (some placeholders)
├── index.html
├── 404.html
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
- Runs `npm ci` → `npm run build` → `wrangler pages deploy .`

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

**Note**: Several PDFs linked from the Research section are intentional placeholders and have not been created yet.

## Contact Form

The contact form on the site is currently a frontend-only stub.  
It shows a temporary "Message Sent" state and resets.

See:
- `js/main.js` → `initContactForm()`
- `index.html` → form comments

To wire it up, connect it to Formspree, a Cloudflare Worker, or another backend.

## Notes & Gotchas

- **CSS cache busting**: `index.html` and `404.html` reference `css/styles.css?v=4281b51`. Update the version string (or remove it) when making significant CSS changes.
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