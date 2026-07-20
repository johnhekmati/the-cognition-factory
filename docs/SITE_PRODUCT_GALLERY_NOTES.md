# Site product gallery + SoR mention — operator notes

**Date:** 2026-07-20  
**Live section:** `#product` on `index.html`

## UI design principles (from thecognitionfactory.com)

| Do (brand) | Don’t (script-kiddie risk) |
|------------|----------------------------|
| **Void** `#050810` + **one** energy accent (electric / amber / plasma by surface) | Rainbow neon, matrix rain, cyberpunk HUD spam |
| Dark-first marketing; light type on void | Invert whole brand to pure white SaaS without reason |
| Gradient = **one focal energy**, sparse | Glow on every edge |
| Space Grotesk + Inter; short declarations | Ed-tech hype, owl-tutor voice |
| Product surfaces may diverge: learning shell stays void+electric; **workflow floor stays light enterprise** | Making SoR look like a second neon “hacker app” |

**Rule of thumb:** If it looks like a crypto landing page, rewrite. If it looks like a calm keynote + one electric aperture, keep it.

## Narrative: mention thin ERP/CRM for practice?

| Verdict | Framing |
|---------|---------|
| **Yes, carefully** | As **workflow practice floor** / hands-on process reps after map + honest practice |
| **Not** | “We built an ERP,” “Dynamics alternative,” “full CRM for your nonprofit,” public multi-tenant SaaS |
| **Where** | `#product` gallery + Desktop App Overview (shallow); **not** hero/H1; not Capes on podcasts without readiness |
| **Always pair** | Same story as map · practice · save place; safe sandbox; not a vendor product |

**One-line public:**  
*After the map and the quiz, some skills need hands on a process — we run a thin, Dynamics-shaped practice floor for that muscle. Not a Microsoft product. Not full ERP theater.*

## Assets (operator pick — 2026-07-20)

| File | Source | Subject | Scrub |
|------|--------|---------|--------|
| `tcf-desktop-app-mockup.jpg` | W11 SS 200002 | Deep learning + chat | **Grok → Assistant**; name chip → **Learner** |
| `tcf-practice-aae-screenshot.jpg` | W11 SS 200406 | Practice / AAE + MCQ | **WGU → Accounting**; **Grok → Assistant**; name → **Learner** |
| `tcf-ops-sor-mockup.jpg` | Session `images/1.jpg` | Thin SoR Finance | Clean (no personal name) |
| `tcf-save-place-screenshot.jpg` | W11 SS 200524 | Save place + CSS chat | **Grok → Assistant**; name → **Learner** |
| `tcf-settings-help-screenshot.jpg` | W11 SS 200740 | Help + More menu | **Grok → Assistant**; name → **Learner** |
| Profiles dedicated SS | **Skipped** (2026-07-19) | Not required for v1 gallery | Revisit only if partner asks |

**Name chip (2026-07-19):** Pixel scrub only (not generative) — keep people icon, paint display name → **Learner**. Re-run `python scripts/scrub_product_screenshots.py` from original W11 PNGs. Cache bust `?v=pg2`.

### Public scrub policy (marketing SSes)

| Scrub | Why |
|-------|-----|
| Last name / Hekmati | Neutral chrome; no IRL person brand on public site |
| WGU (and school chips) | Partner/client surfaces should not hard-code one school |
| **Grok → Assistant** | House LLM core can stay Grok; **client builds = customizable provider**. Marketing never locks the story to one vendor |

### Legibility rule (2026-07-19)

**Do not multi-pass generative `image_edit` on product SSes.** Each model pass smears UI text.

**Do:** one-pass pixel scrub from original Windows PNGs:

```text
python C:\Grok\tcf-site\scripts\scrub_product_screenshots.py
```

Script covers only dirty boxes and redraws with Segoe UI → JPEG quality 95, no chroma subsampling. Unedited chrome stays near-original sharpness (MAE ≈ JPEG only).

**pref 1 > 3:** SoR uses image **1** aesthetic, not thinner gen **3**.

## Site roll-up (v1 gallery — ship shape)

| Layer | Status |
|-------|--------|
| Assets in `assets/images/product/` | Done (5 tiles, sharp scrub) |
| `#product` story order on `index.html` | Done |
| Profiles tile | **Skipped** |
| Hero / H1 Capes about ERP | **Must not** — gallery only |
| Cache bust `?v=pg1` | Done |
| Local preview | `npm run preview` from `tcf-site` |
| Git commit + push `origin/main` | Operator go |
| Cloudflare Pages → thecognitionfactory.com | Follows push (or manual Pages deploy) |

**Public story (one breath):**  
Map the subject → prove the gaps → park when life hits → optional hands on a thin process floor → plain house tools under Help.

**Platforms (public):** Windows + Android now. macOS & iOS — coming soon (readiness, not a date promise).

### Android assets (`?v=and1`)

| File | Source | Subject | Scrub |
|------|--------|---------|--------|
| `tcf-android-deep.jpg` | 10362 | Deep learning home | None needed |
| `tcf-android-practice.jpg` | 10366 | Practice / AAE | None (Accounting already) |
| `tcf-android-save.jpg` | 10369 | Save place | None |
| `tcf-android-chat.jpg` | 10364 | Side chat | **Grok → Assistant** |
| `tcf-android-shell.jpg` | 10371 | Nav + Account & help | Installed spare (not in grid yet) |

```text
python C:\Grok\tcf-site\scripts\scrub_android_screenshots.py
```

## Type stack (ape the site)

| Role | Font | Where |
|------|------|--------|
| Wordmark / titles | **Space Grotesk** | Site display · tcf-ops brand · Flutter titles |
| Body UI | **Inter** | Site body · tcf-ops body · Flutter body |
| Enterprise density | Segoe as OS fallback | SoR forms/grids only |

W11 app: `google_fonts` SpaceGrotesk + Inter via `TcfTokens.darkTheme`.
SoR: Google Fonts link in `apps/web/index.html` + CSS vars.
