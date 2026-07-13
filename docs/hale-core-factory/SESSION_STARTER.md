# Session Starter — Paste Into a New Grok Build Session

Use this when the project directory already contains this kit (and preferably empty `cores/`, `cold-storage/`, `templates/`).

Replace bracketed placeholders. Attach or path the master lists.

---

## First message (copy everything below the line)

---

**Project: HAL-E Core Factory (CSS + CMS scaffolding)**

You are building and maintaining **HAL-E subject Cores** as long-lived single sources of truth.  
**AAE cartridges** are built-to-spec **from** Cores — they never fork the truth.

### Mandatory hierarchy

| Layer | Name |
|------:|------|
| L0 | Invariants (techniques) |
| L1 | Core concepts (combos) |
| L2 | Schema maps (forms) |
| L3 | Knowledge graph (curricular spine) |

Analogy: technique → combo → form → curriculum.

### Runtime

HAL-E and AAE require a **capable LLM core** (local or cloud). Architecture without model depth is insufficient.

### Constitution (read first)

Read and obey:

1. `docs/hale-core-factory/CORE_SYSTEM.md`
2. `docs/hale-core-factory/LAYER_CLASSIFICATION.md`
3. `docs/hale-core-factory/CORE_BUILD_SOP.md`
4. `docs/hale-core-factory/CSS_CMS_OPS.md`
5. `docs/hale-core-factory/NEW_CORE_CHECKLIST.md`

If anything conflicts with chat improvisation, **files win**.

### First milestone

**Accounting Core** from these masters:

- Invariants: `[PATH OR ATTACH — Invariant master list]`
- Financial Accounting concepts: `[PATH — Financial Accounting core concept master list]`
- Managerial Accounting concepts: `[PATH — Managerial Accounting core concept master list]`
- Schema map: `[PATH — Schema Map]`

### Deliverables (in order)

1. Confirm/create repo layout: `cores/`, `cold-storage/`, `templates/hale-core/`, `cartridges/` (optional).
2. Normalize **Accounting Core** into layered files with stable IDs + metadata (CMS-ready).
3. Apply CSS naming + cold-storage conventions; add one example session artifact schema.
4. Document CMS offramp/bridge stubs for Accounting.
5. Freeze/update **`templates/hale-core/`** from the Accounting shape.
6. Produce a short plan to stamp **SCM Core** and **Functional Consulting Core** from the template (do not freehand a new hierarchy).

### Constraints

- Prefer durable files over chat-only artifacts.
- Flag uncertain L0 vs L1 with `needs_human_review` — do not silently guess forever.
- Do **not** invent full AAE carts until Core layers are consistent (unless I override).
- Keep proprietary stitching algorithms out of public docs; implement interfaces + examples.
- Voice: precise, non-mascot; no “AI tutor” framing.

### Capability

- Use faster passes for scaffolds and bulk structure.
- Use higher judgment for layer boundaries, schema integrity, and crosswalks.

### Success criteria

- Expert + LLM can load Accounting Core and spar with structure.
- A fresh session can continue from files alone.
- Template is ready so SCM / Consulting are isomorphic stamps.

**Start by reading the constitution files, then propose the Accounting Core folder tree before writing large content.**

---

## Optional follow-ups (later messages)

**Stamp SCM**

> Using `templates/hale-core/`, create `cores/SCM-Core/`. Ingest [masters]. Run `NEW_CORE_CHECKLIST.md`. Same L0–L3 rules. No new hierarchy.

**Stamp Functional Consulting**

> Same as SCM for `cores/Functional-Consulting-Core/`. Add crosswalk stubs to Accounting and SCM where multi-skill ramp matters.

**AAE cart**

> Build AAE cart `[name]` for outcome `[exam/role]`, drawing only from Core IDs in `[core]`. Do not invent L0/L1.

**Maintenance**

> Run coverage/orphan pass on `[core]`. Open a human review queue file for low-confidence layers.
