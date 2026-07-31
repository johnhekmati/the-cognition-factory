---
title: Dual-Lane Homepage IA — Solo · Enterprise
status: Working on-disk — **no ship** · Principal locks 2026-07-30
date: 2026-07-30
updated: 2026-07-30
owner: Phillip John Hekmati
product: The Cognition Factory
related:
  - docs/ADULT_LANE_CONTENT_GYM_SSOT.md
  - docs/strategy/tcf-productization-mentorship-ssot.md
  - docs/LIABILITY_RISK_REGISTER.md
  - Adult-Lane-Content-Practice-Model (Grok-Build-Review)
  - thecognitionfactory.com index.html (current one-scroll spine)
notes_for_grok_build: |
  Design-only. Do not implement routes or cut homepage until Principal greenlights a build brick.
  LOCKED: triad Option A · Dojo enterprise-only · Gym solo-only (symmetric) · partners = motion ·
  product gallery stays with handsome hooks into doors · slugs /solo/ and /enterprise/.
---

# Dual-Lane Homepage IA

**Status:** Working · **local demo built** · **no prod ship**  
**Date:** 30 July 2026 · **Principal locks:** same day  

### Local demo (2026-07-30)

| Path | Role |
|------|------|
| `/` `index.html` | Dual doors + triad A; long Learn/Practice/Dojo/Save/Who removed |
| `/solo/` `solo/index.html` | Solo door · Gym · productized |
| `/enterprise/` `enterprise/index.html` | Enterprise door · Dojo · partners motion |
| Preview | `npm run preview -- -l 4173` → http://localhost:4173 |

Scripts: `scripts/build_dual_lane_home.py`, `scripts/build_dual_lane_doors.py` · partial: `partials/home-pathways-triad.html`  

This note locks the *shape* of the dual-lane homepage pivot before any code.  
Copy and section *types* stay; commercial hinge becomes **Solo** vs **Enterprise**.

---

## 1. Intent

| Layer | Job |
|-------|-----|
| **Home** | Sell **one factory, two pathways**. Short enough that mobile + Heavy + Kristi stop saying “too long.” |
| **Solo door** (`/solo/`) | Same body cloned; dialed for Adult SaaS, productized cores/carts, **Gym**. |
| **Enterprise door** (`/enterprise/`) | Same body cloned; dialed for high-touch, custom cores/carts, **Dojo**, teams (+ partners as motion). |

**Not two products.** One loop: Learn → Practice → Save place.  
**Two configurations:** commercial model, practice surface, content ownership.

### Symmetric pressure floors (locked)

| Lane | Practice depth surface | On home? |
|------|------------------------|----------|
| **Solo** | **Gym** only | No full Gym tour — depth on `/solo/` |
| **Enterprise** | **Dojo** only | No full Dojo tour — depth on `/enterprise/` |

Neither Gym nor Dojo gets a full mid-page essay on home. Triad stays Learn · Practice · Save; lane-specific floors live behind doors and **match each other in weight** (handsome, intentional, not cosplay on the wrong lane).

---

## 2. Enterprise clarity — Teams vs Partners

### Locked: one Enterprise door · Partners = motion

**One Enterprise door**, not a three-door home (Solo / Teams / Partners as equal).

| Inside Enterprise | Role |
|-------------------|------|
| **Teams (primary)** | The paying / briefing customer: ramp, cross-skill, standards, hypercare path. |
| **Partners (motion, not theater)** | Secondary narrative: *if* maps and scenario libraries are built from **their own engagement reality**, they can get (and give) **honest reads of real-world thought and action** under Dojo pressure — not “white-label partner program” cosplay, not logo wall, not affiliate theater. |

### Why drop equal “Partner” theater on the home fork

1. **Home already overcrowds** — a third commercial door competes with Adult vs Enterprise.  
2. **Partner value is true but narrow** — screening / co-delivery *via engagement libraries* is a *capability of Dojo + custom packs*, not a separate LOB identity.  
3. **Claim risk** — “partners” without a signed program looks like affiliation cosplay; claim rails already ban logo badges.  
4. **Reach-style partner boxes** (01 Partners / 02 Customers) are the generic pattern TCF should *not* ape.

### How Partners still appear (honest)

| Surface | Language |
|---------|----------|
| Enterprise door | Short rung: “Teams & those who screen for delivery” |
| Dojo section (Enterprise dial) | Scenario packs from **your** engagement library → structured view of judgment under pressure — not a hire credential |
| Contact offer ladder | Institution / team briefing; optional “partner packet” request stays as *request*, not home hero |
| Guides | Keep request-only partner materials gated |

**Hard line:** Partners do not get a third homepage mark equal to Adult.  
**Soft edge:** Partners may be a sub-head or second CTA on the Enterprise page only.

### Alternative (if Principal insists on two Enterprise doors)

```
Home
  ├── Adult Learners
  └── Enterprise
        ├── Teams
        └── Partners
```

Only if both have distinct CTAs, pricing, and sales motions. Until then: **one Enterprise URL**, two rungs.

---

## 3. Learn · Practice · Save on home (truncated, still handsome)

### Principle

> **Name and show the triad on home. Explain in depth through the dual doors (with lane dials).**

Home keeps the **ritual identity** (gold / green / red, chiasmus, ticker).  
Home does **not** keep three full long-form door chapters stacked mid-page.

### Truncated home presence — options to ideate (pick later)

#### Option A — “Ritual strip + one line each” (shortest)

| Element | Home |
|---------|------|
| Label | How it works |
| Title | Learn · Practice · Save your place |
| Body | One sentence for the shared loop |
| Triad | Three surface cards (mark border): **Learn** / **Practice** / **Save** — title + one line each |
| CTA | “See how this fits Adult →” · “See how this fits Enterprise →” |

Depth: full copy moves to Adult / Enterprise pages (cloned + dialed).

#### Option B — “Schema lab mini” (current schema-lab, compressed)

Keep the two-pane Learn | Practice + Save connector, but:

- Cap body to ~2 sentences per pane  
- Kill long feature lists on home  
- Link “Full Learn path →” into doors (or a shared `/loop/` if ever needed)

#### Option C — “Mark row + progressive disclosure”

Horizontal row of four marks (Learn · Practice · Save · Dojo-as-Enterprise-only chip):

- Adult path chips: Learn, Practice (Gym), Save  
- Enterprise adds Dojo chip (not on Adult row)  
- Tap/click expands *in place* on desktop; on mobile, routes to door page

Risk: accordion complexity; prefer A or B for v1.

### Locked for first build: **Option A**

- Clearest dual-lane sell  
- Strongest attack on mobile length  
- Marks stay visible (handsome) without three essay sections  

### What moves off home (into doors)

| Current home block | Solo door (`/solo/`) | Enterprise door (`/enterprise/`) |
|--------------------|----------------------|----------------------------------|
| Full Learn section (`#map`) | Clone + solo examples + productized cores | Clone + custom maps |
| Full Practice section (`#aae`) | **Gym** full dial (conditional on-ramps, off-ramps) | Practice packs + **Dojo** (not Gym) |
| Full Dojo section (`#dojo`) | **Absent** (or one line: “Enterprise pressure floor →”) | **Full Dojo** (scenarios, claim-safe language) |
| Full Gym surface | **Full Gym** | **Absent** as Adult cosplay (may mention enterprise doesn’t use Gym) |
| Full Save place (`#platform`) | Clone + household / interruptible | Clone + cohort handoff / hypercare continuity |
| Stay oriented / lattice | Light mention or Guides only | Same |

### Shared one-liner bank (home triad)

| Mark | Home one-liner (shared) |
|------|-------------------------|
| **Learn** | Build the map of a subject — one idea until it clicks. |
| **Practice** | Check what you know under honest pressure — gaps named, not guessed. |
| **Save** | Leave a clean handoff when life interrupts — not re-scroll the chat. |

Lane-specific second lines live **only** behind doors:

| Mark | Solo second line | Enterprise second line |
|------|------------------|------------------------|
| Learn | Productized dense cores you can start from | Maps fitted to your standards and roles |
| Practice | **Gym** when the vertical needs training wheels | Packs + **Dojo** scenarios from your real work |
| Save | Short sessions that still count | Continuity across cohort and calendar |

### Product gallery (locked)

- **Stays** on the factory surface (home and/or door pages — see matrix).  
- Not a third commercial door.  
- **Handsome hooks** from both `/solo/` and `/enterprise/` into the gallery (and from home triad/doors into gallery where natural).  
- Gallery remains proof-of-loop / product chrome — claim-gated captions; no outcome guarantees.  
- Optional later path: `/product/` only if home lightens further; default is keep `#product` (or equivalent) with clear entry hooks, not a orphan slug.

---

## 4. Content objects — productized vs custom

| | Solo (`/solo/`) | Enterprise (`/enterprise/`) |
|--|-----------------|----------------------------|
| Cores | Productized starter set (Accounting, SCM, …) | Custom or adapted cores |
| Carts | Derived measurement carts from productized cores | Carts/scenarios for role, exam, or engagement standard |
| Practice surface | **Gym** (conditional, Markdown/YAML, thin tools) | **Dojo** (scenario packs, pressure) |
| Off-ramps | Neutral links to real tools | Internal graduation / desk tools as client defines |
| Claims | Alignment + retention support only | SOW-scoped readiness observation; no hire credential |

---

## 5. Section matrix (current home → dual-lane)

Legend: **Keep** · **Truncate** · **Move to door** · **New** · **Cut / demote**

| Current block | Home (target) | Solo `/solo/` | Enterprise `/enterprise/` |
|---------------|---------------|---------------|---------------------------|
| Hero + ticker | **Keep** (dual-lane subhead OK) | Optional short hero | Optional short hero |
| Thesis (Learn. Practice. Save.) | **Keep** | Clone short | Clone short |
| Problem | **Keep** (shared) | Clone | Clone |
| Solution bridge | **Truncate** | Clone | Clone |
| How it works / schema lab | **Truncate** → **Option A triad** | Full clone + **Gym** | Full clone + **Dojo** |
| Learn long (`#map`) | **Move** (via doors) | **Keep full** + productized | **Keep full** + custom |
| Practice long (`#aae`) | **Move** | Full + **Gym** | Full + packs; **Dojo** is the floor |
| Dojo long (`#dojo`) | **Cut from home** | Absent (link out only) | **Keep full** |
| Gym surface | **Cut from home** | **Keep full** | Absent as Solo cosplay |
| Save place long (`#platform`) | **Truncate** to triad line | Full + household | Full + team continuity |
| Who trains (3 equal cards) | **Replace** with **Solo \| Enterprise** doors | n/a | Teams primary; Partners motion |
| What you work with (cores/carts) | **Truncate** or one sentence | Productized cores/carts | Custom cores/carts |
| Product gallery | **Keep** + **handsome hooks** from doors | Hook into gallery (solo-relevant shots) | Hook into gallery (team/enterprise shots) |
| Proof | **Keep** short | Clone | Clone |
| Guides | **Keep** | Solo emphasis | Exec/SOP emphasis |
| Why / claim rails | **Keep** | Clone | Clone + SOW non-reliance pointer |
| Connect | **Keep**; dual CTA | Solo/household default | Team/institution default |

---

## 6. URL sketch (paths, not subdomains)

No implement until greenlight.

| URL | Purpose |
|-----|---------|
| `/` | Dual-lane home (triad A + Solo \| Enterprise doors) |
| **`/solo/`** | Solo / Adult Learners door — full body, **Gym** dial, productized cores/carts |
| **`/enterprise/`** | Enterprise door — full body, **Dojo** dial, Teams primary, Partners motion |
| Optional later | `/enterprise/partners/` only if motion earns its own page |
| Optional later | `/product/` only if gallery leaves home; default = in-page gallery + hooks |

Guides stay under `/assets/docs/` or future `/guides/`.

---

## 7. Clone discipline (so two doors don’t drift)

1. **Shared markdown/HTML partials** (or one content SSOT) for Problem, Loop, Save, Claims.  
2. **Dial blocks** only for: Gym vs Dojo, productized vs custom, CTAs, ICP examples.  
3. Any copy change to shared spine updates **both** doors in one commit.  
4. Claim-language gate applies to home and both doors.  
5. **Symmetry:** Gym on Solo and Dojo on Enterprise are peer surfaces — same craft weight, opposite lanes.

---

## 8. Principal locks (2026-07-30) — closed

| # | Question | Lock |
|---|----------|------|
| Q1 | Home triad | **Option A** — three mark cards + one line each + dual CTAs |
| Q2 | Dojo on home | **No** — Dojo **Enterprise only** (`/enterprise/`) |
| Q2b | Gym symmetry | **Gym Solo only** (`/solo/`) — matches Dojo weight, wrong-lane cosplay forbidden |
| Q3 | Partners | **Motion** under Enterprise — honest reads via engagement libraries; not equal home door |
| Q4 | Product gallery | **Keep** with **handsome hooks** from home/doors into gallery |
| Q5 | Slugs | **`/solo/`** and **`/enterprise/`** |

---

## 9. Explicit non-goals (this doc)

- No visual redesign of marks / chiasmus  
- No Reach-style 01/02 partner theater on home  
- No third homepage LOB for Partners  
- No Gym on Enterprise page as primary floor; no Dojo on Solo page as primary floor  
- No ship / no deploy from this document alone  
- No new public prices or package claims  

---

## 10. Suggested next bricks (when greenlit)

1. **Wireframe pass** — home: dual doors + triad A + gallery hooks.  
2. **Door outline** — `/solo/` and `/enterprise/` section lists (clone map + Gym/Dojo dial).  
3. **Copy pass** — shared one-liners + dial second lines (claim gate).  
4. **Implement** — routes + cut home long sections (ship when Principal says).  

---

## 11. Decision log

| Decision | Status |
|----------|--------|
| Dual-lane home fork | **Locked** — Solo \| Enterprise |
| Clone body + dial Gym/Dojo and productized/custom | **Locked** |
| Learn/Practice/Save = triad Option A on home; depth in doors | **Locked** |
| Dojo = Enterprise only; Gym = Solo only (symmetric) | **Locked** |
| Partners = motion under Enterprise | **Locked** |
| Product gallery stays + handsome hooks | **Locked** |
| Slugs `/solo/` + `/enterprise/` | **Locked** |
| On-disk only, no ship | **Active** |

---

*Working IA. Principal locks Q1–Q5 closed 2026-07-30. Pair with Adult Lane Gym SSOT and Productization Mentorship Map. Implement only on greenlight.*
