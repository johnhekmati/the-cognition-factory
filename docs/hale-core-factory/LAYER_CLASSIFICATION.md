# Layer Classification Guide (L0–L3)

Use this when sorting master lists into a HAL-E Core. When uncertain, **flag for human review** — do not force a label to look complete.

## Quick table

| Layer | Name | Question that decides it |
|------:|------|---------------------------|
| L0 | Invariant | Is this an **atomic technique** reused across many concepts? |
| L1 | Core concept | Is this a **named combination / analysis package** built from invariants? |
| L2 | Schema map | Does this show **how objects move together** under structure or scenarios? |
| L3 | Knowledge graph | Does this define **path, coverage, or curricular spine** across the Core? |

## L0 — Invariants (techniques)

**Include when**

- Atomic: hard to decompose without losing the unit of practice.
- Recurs across multiple L1 concepts.
- Stable over curricula versions (exam outlines may weight it differently; the technique still exists).
- Can be sparred or drilled in isolation (“show me X”).

**Exclude when**

- It is really a multi-step analysis with its own named method (likely L1).
- It only makes sense as a chapter title or course module (may be L3 navigation, not L0).

**Review prompts**

- “Where else in the domain does this reappear?”
- “If I strip the scenario, does a pure technique remain?”

## L1 — Core concepts (combos)

**Include when**

- Named package used by practitioners (e.g. in Accounting: CVP, break-even, COGS — as **concepts**, not L0).
- Composes multiple L0 invariants (and sometimes other L1s).
- Supports teach-back: “Explain the model; where on the map?”
- Natural target for AAE sampling and error classification.

**Exclude when**

- It is only a synonym for an L0 technique.
- It is a full curriculum path (L3) or a multi-concept diagram (L2).

**Review prompts**

- “Which invariants does this stand on?”
- “Could an AAE cart weight this as a distinct outcome?”

## L2 — Schema maps (forms / kata)

**Include when**

- Explicit structure of relationships (maps, not prose essays).
- Shows sequencing, dependencies, or scenario frames.
- Helps the learner answer “where on the map?” during sparring.

**Exclude when**

- Wall-of-text explanation with no structural artifact.
- Mere table of contents (closer to L3).

**Review prompts**

- “What edges connect which nodes?”
- “What would break if this relationship were wrong?”

## L3 — Knowledge graph (curriculum spine)

**Include when**

- Ordered or graph-shaped coverage of the Core for learning paths.
- Links modules, maps, and concepts into a navigable whole.
- Supports CMS bridges and offramps (depth → exam cart).

**Exclude when**

- A single concept definition (L1).
- A single technique (L0).

## Conflict resolution

1. Prefer **smaller layer** when something is both “atomic” and “named package” only if it truly recurs as technique; otherwise L1.
2. Prefer **human review** over model overconfidence on boundary cases.
3. Record decisions in Core metadata:

   ```yaml
   layer: L1
   layer_confidence: medium
   layer_rationale: "Named analysis package; rests on L0 cost behavior + contribution"
   needs_human_review: false
   ```

## Domain transfer

The **same tests** apply to SCM, Functional Consulting, and future Cores. Only the content changes; hierarchy does not.

| Domain (example) | L0 flavor | L1 flavor |
|------------------|-----------|-----------|
| Accounting | Atomic measurement / recognition techniques | Named analyses (CVP, etc.) |
| SCM | Flow, buffer, constraint techniques | Named operating models / planning packages |
| Functional consulting | Engagement / diagnosis techniques | Named workstream or artifact packages |

Do not invent a new layer system per domain.
