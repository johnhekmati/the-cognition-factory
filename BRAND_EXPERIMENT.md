# Brand experiment — stamp, don’t stream

**Branch:** `experiment/brand-copy`  
**Tree:** `C:\Grok\tcf-site-fork` only — **not** prod `C:\Grok\tcf-site`  
**Push / deploy:** **do not** (upstream push disabled; no live site)

## Mindset

> Same factory. Different room. Stamp, don’t stream.

Public site should invite John Q Consultant and busy parents — not read as a cyberpunk stream overlay.

## Face mark

| Asset | Path |
|-------|------|
| Mark | `assets/images/brand/tcf-mark-cf-charcoal-light.jpg` |

## Public language

- **Above the fold / primary nav:** human product language only  
- **HAL-E · AAE · CSS · CMS:** gate behind **technical whitepapers / deep docs** — they are the lattice, not the lobby  
- Product loop names: map · practice · save place  

## Color system (locked)

**Thesis:** mostly **white / light gray** canvas (+ charcoal bands). **Primary color only for engines and lattices** — thematically cohesive with the four door marks.

| Role | Hex | Use |
|------|-----|-----|
| **Map** | `#c9a227` gold | Map door, M tile, layer 1, solo path accents |
| **Practice** | `#3d8c5a` green | Practice door, P tile, layer 2, teams accents |
| **Save** | `#b03030` red | Save place, A tile, layer 3 |
| **Dojo** | `#2b5f9e` blue | Dojo door, Y tile, layer 4, partners / workflow floor |
| **Lattice** | `#c94a40` coral | Orient / lattice (secondary) |
| **Chrome** | ink muted / quiet steel | Nav, section labels, primary CTA — not competing with marks |

**Rule:** multi-item rows rotate gold → green → red → blue. Named engines use their color. Generic UI stays quiet.

Helpers: `.accent-map|practice|save|dojo|lattice`, `.card-border-*`, `.surface-card--*`, `.layer-chip--*`, `.icon-tile-*`.

## Rails

- Work only under this fork path  
- Local commits on `experiment/brand-copy` OK  
- Live thecognitionfactory.com = prod only; no accidental deploy from this tree  

## Related

App fork: `C:\Grok\tcf-app-fork` · same experiment  

## Dojo / partners (operator alignment — not public copy)
Dojo is where partners can pressure-test real delivery (sniff out bullshido) via scenarios — keep that intent off the marketing face; site language stays professional (screen for delivery, scenarios under pressure).
