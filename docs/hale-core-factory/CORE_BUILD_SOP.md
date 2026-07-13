# CORE_BUILD_SOP — Create, Iterate, Maintain HAL-E Cores

Phased workflow for humans and agents. Complete phases in order unless the user explicitly reprioritizes.

## Phase 0 — Project bootstrap

**Goal:** Repo is loadable by Grok Build with constitution on disk.

**Actions**

1. Ensure this kit lives under the project (e.g. `docs/hale-core-factory/`).
2. Create top-level dirs if missing:

   ```text
   cores/
   cold-storage/
   cartridges/          # optional until first AAE cart
   templates/hale-core/ # copy from this kit if not present
   ```

3. Agent reads `CORE_SYSTEM.md` + `LAYER_CLASSIFICATION.md` before editing content.
4. Confirm LLM runtime assumption is documented for operators (local or cloud).

**Exit criteria**

- [ ] Constitution files present
- [ ] Empty or existing `cores/` tree known
- [ ] Cold-storage root exists

---

## Phase A — Normalize first Core (recommended: Accounting)

**Goal:** One complete, consistent Core from master lists.

**Inputs (example)**

- Invariant master list
- Financial Accounting core concept master list
- Managerial Accounting core concept master list
- Schema map

**Actions**

1. Ingest masters → propose L0 / L1 assignments with confidence.
2. Adversarial pass: challenge every boundary case.
3. Align L2 schema map nodes to L0/L1 IDs (no orphans either way).
4. Draft L3 spine (coverage path / graph skeleton).
5. Attach metadata suitable for CMS indexing (IDs, layers, tags, prerequisites).
6. Human review queue: `needs_human_review: true` items.

**Exit criteria**

- [ ] L0 set published under Core
- [ ] L1 set published under Core
- [ ] L2 maps linked to IDs
- [ ] L3 spine draft exists
- [ ] Review queue empty or explicitly deferred with owners

**Do not** build full AAE carts until this exit is met (unless user overrides).

---

## Phase B — CSS cold-storage conventions

**Goal:** Re-entry without amnesia; versioned session artifacts.

**Actions**

1. Adopt naming pattern from `CORE_SYSTEM.md`.
2. Define cold-storage layout (see `CSS_CMS_OPS.md`).
3. Define session intent vocabulary (e.g. `depth` | `drill` | `assessment` | `crosswalk`).
4. Document what is stitched on resume vs left cold (high-level; no need to expose proprietary stitching logic in public notes).

**Exit criteria**

- [ ] Operators can name and file a session artifact correctly
- [ ] Resume parameters are documented
- [ ] Cores remain SSOT; cold storage is not a second Core

---

## Phase C — CMS routes

**Goal:** Orientation without a second LMS.

**Actions**

1. Define HAL-E → AAE offramp conditions (when depth yields to exam fidelity).
2. Define in-domain bridges (concept A → B) using Core IDs.
3. After ≥2 Cores: define crosswalk fields (Accounting × SCM × Consulting, etc.).
4. Ensure metadata fields required for indexing exist on Core objects.

**Exit criteria**

- [ ] Offramp rules written
- [ ] Bridge examples exist for first Core
- [ ] Crosswalk schema ready even if second Core not filled yet

---

## Phase D — Freeze Core template

**Goal:** Next domains are stamps, not inventions.

**Actions**

1. Copy successful Accounting structure into `templates/hale-core/`.
2. Strip domain-specific content; keep folders, metadata schemas, checklists.
3. Write “fill these files” notes in template README.
4. Link template from this SOP.

**Exit criteria**

- [ ] Empty Core can be generated in <1 agent turn from template
- [ ] Hierarchy identical to Accounting

---

## Phase E — Stamp next Cores (SCM, Functional Consulting, …)

**Goal:** Isomorphic Cores from scratch or from partial notes.

**Actions**

1. `cp -R templates/hale-core cores/<Domain>-Core` (or agent equivalent).
2. Ingest domain masters (or generate first-pass masters with human review).
3. Run same L0→L1→L2→L3 pipeline and checklists.
4. Only then consider domain AAE carts.

**Exit criteria**

- [ ] `NEW_CORE_CHECKLIST.md` fully checked for the domain
- [ ] Crosswalk stubs to Accounting (or other Cores) if multi-skill ramp is in scope

---

## Phase F — Maintain and iterate

**Cadence suggestions**

| Trigger | Action |
|---------|--------|
| New invariant discovered in sparring | Propose L0; link to affected L1/L2 |
| Exam outline changes | Update AAE cart weights; Core L0/L1 only if truth changed |
| Cross-skill engagement | CMS crosswalk update |
| Session friction / re-entry pain | CSS naming or stitch parameters |

**Always**

- Version Cores deliberately.
- Prefer small PRs / commits per layer or per concept cluster.
- Re-run orphan checks after edits.

---

## Multi-pass “MoE-style” quality loop (any phase)

Run as sequential agent passes (or subagents):

1. **Classifier** — propose layers + confidence  
2. **Adversary** — attack mis-layers  
3. **Coverage** — map ↔ masters orphans  
4. **AAE readiness** — which L1s need error classes / weights  
5. **Crosswalk** — only after ≥2 Cores  

Record outcomes in files, not only in chat.

---

## Capability settings (Grok / agent)

| Work | Prefer |
|------|--------|
| Scaffolds, renames, bulk structure, YAML shapes | Faster / lower |
| L0 vs L1 fights, schema integrity, crosswalks, exam fidelity | Higher judgment |
| Secret stitching algorithms | Keep private; give interfaces + examples |

---

## Definition of done (project-level)

The Core Factory is operational when:

1. Accounting Core is consistent and reviewable.
2. Template exists and has been used once successfully on a second domain (or a dry-run stamp).
3. CSS and CMS conventions are documented and used in at least one real session cycle.
4. A new contributor (or new Grok session) can start from `SESSION_STARTER.md` without tribal knowledge.
