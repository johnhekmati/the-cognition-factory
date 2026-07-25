# Mail / LinkedIn asset wire — local review

**Date:** 2026-07-20 · **No commit/push required for review**  
**Stills:** Imagine cycle `tcf-mark-void-electric-v1` · `tcf-three-doors-banner-v1`

## Site (wired in `index.html` — local)

| Surface | Asset | How |
|---------|-------|-----|
| Open Graph / Twitter card | `assets/images/tcf-mark-void-electric-v1.jpg?v=img1` | `og:image` + `twitter:image` |
| Contact section | `assets/images/tcf-three-doors-banner-v1.jpg?v=img1` | Decorative still above contact copy (`alt=""`) |

**Local preview:** from `tcf-site`, `npm run preview` (or static serve) → open `http://127.0.0.1:…` · check contact block + view-source for meta tags.  
**OG unfurl** will not hit production until deploy; use [opengraph.xyz](https://www.opengraph.xyz/) only after push.

## Mail (Proton / client) — not auto-deployed

| Use | File (attach or host) |
|-----|------------------------|
| Header / banner | `C:\Grok\tcf-site\assets\images\tcf-three-doors-banner-v1.jpg` |
| Signature mark (square) | `C:\Grok\tcf-site\assets\images\tcf-mark-void-electric-v1.jpg` |

Suggested HTML header fragment (paste into campaign or signature block if your client allows):

```html
<img src="https://thecognitionfactory.com/assets/images/tcf-three-doors-banner-v1.jpg?v=img1"
     alt="The Cognition Factory — map, practice, save place"
     width="600" style="max-width:100%;height:auto;border:0;display:block;" />
```

Until deploy, attach the local JPEG or use a temporary host; do not invent a CDN path.

## LinkedIn

| Post type | Asset |
|-----------|--------|
| Square / profile-adjacent | `tcf-mark-void-electric-v1.jpg` |
| Landscape post | `tcf-three-doors-banner-v1.jpg` |

Copy: `docs/NARRATIVE_PACK_v1.md` (posts A–C). No private pedigree on airwaves.

## Explicit non-wire

- Product UI screenshots — scrub scripts only  
- Hero video swap — not this pass (still available as optional later)  
- Favicon — left on existing HAL-E2A mark  
