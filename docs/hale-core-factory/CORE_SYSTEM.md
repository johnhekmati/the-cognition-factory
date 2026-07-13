# CORE_SYSTEM — HAL-E / AAE Constitution

> Non-negotiable. Every Core, cartridge, CSS artifact, and CMS route inherits these rules.  
> If a suggestion conflicts with this document, this document wins.

## 1. Brand and product essence

| Element | Definition |
|---------|------------|
| **HAL-E** | Hyper Accelerated Learning Engine — depth engine; schema-first learning partner |
| **AAE** | Adaptive Assessment Engine — exam fidelity; measures genuine competency |
| **Promise** | Build durable mental models; spar until understanding sticks |
| **Enemy** | More content without architecture; fake mastery; tool sprawl |
| **Primary line** | Not more content. Better architecture. |
| **Dual engines** | HAL-E for depth · AAE for exam fidelity |

**Voice:** Confident, clean, technical-literacy friendly. Short declarations. Respect intelligence. No mascot-cute. No “AI tutor,” “guaranteed pass,” or “easy.”

**Audiences**

- Solo high-agency learners who want ownership, not more content.
- Institutions (colleges, nonprofits, firms) that need capability transfer, not seat time.

## 2. Runtime requirement

**HAL-E and AAE require a capable LLM core.**

- Local (e.g. Ollama with a strong model) or cloud (frontier models).
- Cartridge craft without model depth collapses into thin teach-back and repetitive mock exams.
- Engines supply architecture; the model supplies judgment under pressure.

## 3. Artifact types

| Artifact | Role | Lifetime |
|----------|------|----------|
| **HAL-E Core** | Living domain architecture; single source of truth (SSOT) | Long-term, versioned, continuously improved |
| **AAE cartridge** | Built-to-spec assessment / competency pack for a defined end-user outcome | Spec-bound; may be rebuilt when objectives change |
| **CSS** | Cognitive Save States — re-entry / continuity for learners and models | Session- and version-oriented cold storage |
| **CMS** | Cognitive Mapping System — orientation, offramps, bridges, crosswalks | Indexing and routing over Core metadata |

**Rules**

1. AAE cartridges **draw from** a HAL-E Core. They do not invent a parallel truth.
2. Cores are not disposable chat transcripts.
3. Multiple AAE carts may sample one Core (e.g. exam-aligned packs off an Accounting Core).
4. Institutions and solo learners share engines; they differ in cartridge specs and ramp goals.

## 4. Knowledge layers (mandatory hierarchy)

| Layer | Name | Role | Analogy |
|------:|------|------|---------|
| **L0** | Invariants | Atomic techniques of the domain | Techniques (kicks, punches) |
| **L1** | Core concepts | Combinations built on invariants | Combos |
| **L2** | Schema maps | Structured forms — how pieces move together | Kata / forms |
| **L3** | Knowledge graph | Curricular spine across the Core | Full style / curriculum |

**Examples (Accounting — illustrative, not exhaustive)**

- L0: atomic principles and techniques that recur across many topics.
- L1: CVP, break-even analysis, COGS, etc. — **core concepts**, not invariants.
- L2: maps showing how concepts and invariants relate under scenarios.
- L3: path / coverage spine for the domain (and links used by CMS).

See `LAYER_CLASSIFICATION.md` for decision tests.

## 5. CSS (Cognitive Save States) — constitution level

**Purpose:** Reduce re-entry tax when sessions hit token ceilings, lossy compression, context switches, or flow interruption.

**What CSS is for**

- Restore points for deep HAL-E work or dialed-in AAE runs.
- Intentional resume (depth vs drill vs handoff) rather than full cold boot of context.
- Tight version history so human + LLM reload only what the next hour needs.

**What CSS is not**

- Surveillance product.
- A substitute for a Core.
- Permission to keep unbounded raw logs as the SSOT.

**Naming (recommended pattern)**

```text
YYYY-MM-DD-HAL-E-<CoreName>-<Focus>-Session-N.md
```

Example: `2026-07-03-HAL-E-Accounting-Core-CVP-Session-2.md`

Operational detail: `CSS_CMS_OPS.md`.

## 6. CMS (Cognitive Mapping System) — constitution level

**Purpose:** Orientation and routing across the stack.

| Route type | Meaning |
|------------|---------|
| **HAL-E → AAE offramp** | Leave depth work into a built-to-spec cart when the objective is exam fidelity |
| **In-domain bridge** | Move concept A → concept B without losing the map |
| **Core crosswalk** | Links between Cores (e.g. Accounting × SCM × Functional Consulting) for multi-skill ramp |

**What CMS is not**

- A second LMS shelf of content.
- A free-form chatbot memory.

CMS relies on **metadata** on Core objects (and session artifacts where appropriate) for indexing — manually for expert solo users, or assisted indexing for orgs. Keep implementation details private if needed; public language stays high-level.

## 7. Quality bar

A Core is healthy when:

1. L0–L3 are consistent (no orphan concepts; no map nodes without homes).
2. Uncertain classifications are tagged for human review, not silently guessed forever.
3. An expert + preferred LLM can load the Core and spar with structure.
4. An AAE cart can be derived for a named outcome without inventing new L0/L1 under the table.
5. CSS can checkpoint and resume without rebuilding the architecture from chat history.

## 8. Agent operating rules

When building or editing Cores:

1. Prefer **files on disk** over long chat dumps.
2. **Never** demote a Core to a single undifferentiated markdown blob.
3. Propose layer labels with **confidence** and flag low-confidence items.
4. Run adversarial checks: “Why is this L1 not L0?”
5. After one Core is solid, **template it** before freehanding the next domain.
6. Do not invent exam carts until Core layers are consistent unless the user explicitly prioritizes a cart prototype.

## 9. Dual taglines (messaging)

- For the solo learner who wants ownership, not more content.
- For institutions that need capability transfer, not seat time.
