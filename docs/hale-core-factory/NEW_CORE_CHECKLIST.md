# New Core Checklist

Copy this section into `cores/<Domain>-Core/CHECKLIST.md` and tick as you go.

**Core name:** _______________  
**Owner:** _______________  
**Date started:** _______________  
**Template version:** _______________

---

## 0. Bootstrap

- [ ] Copied from `templates/hale-core/` (or equivalent)
- [ ] `CORE_SYSTEM.md` read by builder/agent
- [ ] `LAYER_CLASSIFICATION.md` applied
- [ ] LLM runtime noted for operators

## 1. Masters ingested

- [ ] L0 candidate source(s) identified
- [ ] L1 candidate source(s) identified
- [ ] Schema map source identified
- [ ] Source versions / dates recorded

## 2. Layers

- [ ] L0 list published with stable IDs
- [ ] L1 list published with stable IDs
- [ ] Every L1 lists supporting L0 (or marked TBD + review)
- [ ] L2 map(s) linked to IDs (no orphan map nodes)
- [ ] L0/L1 without map homes listed and resolved or deferred
- [ ] L3 spine draft exists
- [ ] Low-confidence layer labels in review queue

## 3. Metadata / CMS readiness

- [ ] Front matter / metadata schema applied to objects
- [ ] Prerequisites expressed where known
- [ ] Tags consistent with Core conventions
- [ ] AAE-eligible L1s marked (even if cart not built)
- [ ] Crosswalk stubs present if multi-Core ramp is in scope

## 4. CSS readiness

- [ ] Cold-storage path for this Core exists
- [ ] Session naming pattern documented for operators
- [ ] At least one example CSS artifact (can be synthetic)

## 5. Quality passes

- [ ] Classifier pass done
- [ ] Adversarial L0/L1 pass done
- [ ] Coverage / orphan pass done
- [ ] Human review of flagged items done or scheduled

## 6. AAE (optional until Core solid)

- [ ] Target outcome(s) named (exam, role, org competency)
- [ ] Cart draws only from Core IDs
- [ ] Weights / objectives documented
- [ ] Error classes sketched (conceptual / mechanical / integrative)

## 7. Definition of done

- [ ] Expert can load Core + LLM and spar with structure
- [ ] Second person (or fresh agent session) can navigate without tribal chat history
- [ ] Checklist committed with Core

**Sign-off:** _______________ **Date:** _______________
