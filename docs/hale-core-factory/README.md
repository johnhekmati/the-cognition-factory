# HAL-E Core Factory — Project Kit

**Purpose:** Portable constitution, SOPs, checklists, and templates so a new Grok Build session can create, iterate, and maintain HAL-E subject Cores (Accounting, SCM, Functional Consulting, etc.) with CSS / CMS scaffolding — without re-explaining the system from scratch.

**How to use**

1. Create (or open) your Core project directory.
2. Copy this entire folder into that project, e.g.:

   ```text
   your-project/
     docs/hale-core-factory/   ← this kit (or paste files at repo root)
     cores/
     cold-storage/
     templates/
   ```

3. Point Grok Build at the project root.
4. Open `SESSION_STARTER.md`, paste the first-message block (fill in paths), attach master lists.
5. Follow `CORE_BUILD_SOP.md`. Do not improvise hierarchy.

**Read order (humans and agents)**

| Order | File | Role |
|------:|------|------|
| 1 | `CORE_SYSTEM.md` | Non-negotiable constitution |
| 2 | `LAYER_CLASSIFICATION.md` | L0–L3 decision tests |
| 3 | `CORE_BUILD_SOP.md` | Phased build workflow |
| 4 | `CSS_CMS_OPS.md` | Save states + mapping (ops, not secret sauce) |
| 5 | `NEW_CORE_CHECKLIST.md` | Gate before a Core is “done” |
| 6 | `SESSION_STARTER.md` | First prompt for a new agent session |
| 7 | `templates/hale-core/` | Empty Core skeleton to stamp |

**Design intent**

- One Core fully (Accounting) → freeze template → stamp SCM / Consulting / next domains.
- HAL-E Core = living single source of truth.
- AAE cartridge = built-to-spec from Core; never forks truth.
- Prefer durable files over chat-only artifacts.
- Flag uncertain L0 vs L1 classifications for human review.

**Related public brand site**

The Cognition Factory marketing site describes engines and platform at a high level. This kit is the **working system** for Core authors. Do not paste implementation secret sauce into public docs.
