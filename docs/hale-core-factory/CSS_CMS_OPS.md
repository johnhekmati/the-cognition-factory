# CSS & CMS — Operational Notes (High Level)

This document is **operations and interfaces**, not a full disclosure of proprietary implementation. Enough for agents and operators to build the right folder structure and metadata; not a recipe to reverse-engineer secret sauce.

---

## CSS — Cognitive Save States

### Problem CSS solves

| Friction | Effect |
|----------|--------|
| Token ceilings in long sessions | Context drops mid-architecture |
| Lossy compression | Subtle schema errors on resume |
| Context-switching Cores / carts | Cognitive + model thrash |
| Flow interruption | High re-entry tax next day |

### Operator goals

1. Capture enough **session substance** to resume intentionally.
2. Tag **session intent** (`depth` | `drill` | `assessment` | `crosswalk` | custom).
3. Keep **tight version history**; avoid infinite undifferentiated logs as SSOT.
4. Leave raw bulk in **cold storage**; resume with stitched, intent-scoped context.

### Recommended layout

```text
cold-storage/
  <CoreName>/
    YYYY/
      MM/
        YYYY-MM-DD-HAL-E-<CoreName>-<Focus>-Session-N.md
        YYYY-MM-DD-AAE-<CartName>-Session-N.md   # if applicable
  _index/                    # optional manifest of sessions
```

### Recommended filename pattern

```text
YYYY-MM-DD-HAL-E-<CoreName>-<Focus>-Session-N.md
```

### Front matter (illustrative schema)

Agents should use a consistent YAML block. Field names may evolve; keep semantics stable.

```yaml
---
artifact_type: css_session
engine: HAL-E          # or AAE
core_id: accounting
focus: CVP
session_number: 2
session_intent: depth  # depth | drill | assessment | crosswalk
date: 2026-07-03
llm_core: "operator-chosen"
related_layer_ids:
  - L1-CVP
  - L0-...
resume_hints:
  - "Continue spar on contribution margin edge cases"
needs_human_review: false
---
```

### Resume contract (what “good” looks like)

- Operator states intent for the next hour.
- System (or human) selects cold artifacts + Core slices by metadata.
- Model receives **Core SSOT + scoped CSS**, not the entire cold archive.

### Anti-patterns

- Treating CSS files as the Core.
- Untitled dumps (`notes.md`, `session final FINAL.md`).
- Resume with full raw logs every time “just in case.”

---

## CMS — Cognitive Mapping System

### Problem CMS solves

Learners and models get lost across layers, carts, and multi-domain ramps. CMS provides **routes**, not more content shelves.

### Route types

| Type | Description | Example |
|------|-------------|---------|
| **Offramp** | HAL-E depth → AAE cart for exam fidelity | Accounting Core → D196-style cart (illustrative) |
| **Bridge** | In-domain concept-to-concept | L1-A → L1-B with shared L0 set |
| **Crosswalk** | Between Cores | Accounting × SCM × Functional Consulting |

### Metadata CMS expects on Core objects

Minimum useful fields (extend as needed):

```yaml
id: L1-CVP
layer: L1
title: "Cost-Volume-Profit"
core_id: accounting
prerequisites: [L0-..., L1-...]
schema_map_refs: [MAP-...]
tags: [managerial, analysis]
aae_eligible: true
crosswalk:
  scm: []
  functional_consulting: []
```

### Offramp rules (policy level)

Document when to leave depth for assessment, e.g.:

- Target outcome is exam / certification fidelity.
- Error classes need blind sampling rather than open spar.
- Cart weighting exists and is approved.

Offramp **reads** Core IDs; it does not redefine them.

### Crosswalk rules (policy level)

- Only link nodes that are intentionally multi-domain (not vague “related”).
- Prefer shared skill outcomes for org ramp (e.g. consultant needs accounting + SCM + cert path).
- Crosswalks are CMS concerns; they do not merge Cores into one blob.

### Anti-patterns

- CMS as a second copy of Core prose.
- Orphan routes with no Core IDs.
- Auto-linking everything with embedding similarity and no human policy.

---

## Interoperability picture (public-safe)

```text
LLM core (local or cloud)
        │
        ▼
┌───────────────────┐     offramp      ┌──────────────────┐
│   HAL-E Core      │ ───────────────► │  AAE cartridge   │
│  L0 L1 L2 L3      │ ◄── diagnostics  │  built-to-spec   │
└───────────────────┘                  └──────────────────┘
        │                                      │
        │         CSS (save / resume)          │
        └──────────────────┬───────────────────┘
                           │
                    cold-storage/
                           │
                    CMS (routes / index)
```

---

## Agent instructions

When implementing CSS/CMS in a project:

1. Create folders and schemas first.
2. Enforce IDs and front matter on new files.
3. Refuse to “just chat” architecture that should live in Core files.
4. Keep proprietary stitching / MoE routing details out of public READMEs unless the owner requests them in a private doc.
