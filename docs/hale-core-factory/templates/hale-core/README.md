# HAL-E Core Template

Copy this directory to:

```text
cores/<Domain>-Core/
```

Example: `cores/Accounting-Core/`, `cores/SCM-Core/`, `cores/Functional-Consulting-Core/`.

Then replace placeholders and fill layer files. **Do not change the hierarchy.**

## Directory layout

```text
hale-core/                          # rename to <Domain>-Core
  README.md                         # this file → become Core overview
  CHECKLIST.md                      # copy from NEW_CORE_CHECKLIST.md
  meta/
    core.yaml                       # Core identity + version
  L0-invariants/
    README.md
    _index.yaml                     # list of invariant IDs
    # INV-....md
  L1-core-concepts/
    README.md
    _index.yaml
    # CONCEPT-....md
  L2-schema-maps/
    README.md
    _index.yaml
    # MAP-....md (or .mmd / images referenced here)
  L3-knowledge-graph/
    README.md
    spine.yaml                      # curricular spine / graph stubs
  cms/
    offramps.yaml                   # HAL-E → AAE
    bridges.yaml                    # in-domain
    crosswalks.yaml                 # to other Cores
  aae/
    README.md                       # carts live under repo cartridges/ preferred
  CHANGELOG.md
```

## Fill order

1. `meta/core.yaml`
2. L0 from masters  
3. L1 from masters (link L0)  
4. L2 maps  
5. L3 spine  
6. CMS stubs  
7. Checklist sign-off  

## ID conventions (recommended)

| Layer | Pattern | Example |
|-------|---------|---------|
| L0 | `INV-<SHORT>` | `INV-COST-BEHAVIOR` |
| L1 | `CONCEPT-<SHORT>` | `CONCEPT-CVP` |
| L2 | `MAP-<SHORT>` | `MAP-MANAGERIAL-CORE` |
| L3 | `SPINE-<CORE>` | `SPINE-ACCOUNTING` |

Keep IDs stable once referenced by CSS/CMS/AAE.
