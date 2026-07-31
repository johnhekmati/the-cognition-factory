"""Refresh dual-lane home partial + inject door-mark CSS. Rebuild door pages with marks."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
index_path = root / "index.html"
index = index_path.read_text(encoding="utf-8")
partial = (root / "partials/home-pathways-triad.html").read_text(encoding="utf-8")
if not partial.endswith("\n"):
    partial += "\n"

start = index.find("PATHWAYS")
if start == -1:
    raise SystemExit("PATHWAYS not found")
start = index.rfind("<!--", 0, start)
marker_end = index.find("See the product gallery", start)
if marker_end == -1:
    raise SystemExit("gallery hook not found")
end = index.find("</section>", marker_end) + len("</section>")
while end < len(index) and index[end] in "\r\n":
    end += 1

new = index[:start] + partial + index[end:]

css = """
    /* Dual-lane brand marks (map / practice / save / dojo / lattice) */
    .door-mark-thumb {
      width: 6.5rem;
      height: 6.5rem;
      border-radius: 0.85rem;
      overflow: hidden;
      background: #ffffff;
      border: 2px solid rgba(0, 0, 0, 0.08);
      box-shadow: 0 8px 24px rgba(45, 50, 60, 0.08);
    }
    .door-mark-thumb img {
      display: block;
      width: 100%;
      height: 100%;
      object-fit: contain;
      background: #ffffff;
    }
    .door-mark-thumb--sm {
      width: 3.25rem;
      height: 3.25rem;
      border-radius: 0.55rem;
      border-width: 1.5px;
    }
    .door-mark-thumb--map { border-color: rgba(201, 162, 39, 0.55); }
    .door-mark-thumb--practice { border-color: rgba(61, 140, 90, 0.5); }
    .door-mark-thumb--save { border-color: rgba(176, 48, 48, 0.5); }
    .door-mark-thumb--dojo { border-color: rgba(43, 95, 158, 0.55); }
    .door-mark-thumb--lattice { border-color: rgba(201, 74, 64, 0.45); }
    @media (min-width: 768px) {
      .door-mark-thumb:not(.door-mark-thumb--sm) {
        width: 7.5rem;
        height: 7.5rem;
      }
    }
"""

if "door-mark-thumb {" not in new:
    needle = "    /* Flat charcoal CF"
    if needle in new:
        new = new.replace(needle, css + "\n" + needle, 1)
    else:
        new = new.replace("  </style>", css + "\n  </style>", 1)

index_path.write_text(new, encoding="utf-8")
print("home marks injected")

# --- Rebuild door page bodies with marks (patch build script bodies via direct write) ---
# Import and re-run door builder after patching SOLO/ENT strings in that file is heavy;
# patch generated HTML instead.

MARK_CSS = css  # same rules for door pages


def inject_marks_css(html: str) -> str:
    if "door-mark-thumb {" in html:
        return html
    if "/* Flat charcoal CF" in html:
        return html.replace("    /* Flat charcoal CF", MARK_CSS + "\n    /* Flat charcoal CF", 1)
    return html.replace("  </style>", MARK_CSS + "\n  </style>", 1)


def thumb(kind: str, src: str, sm: bool = False) -> str:
    sm_cls = " door-mark-thumb--sm" if sm else ""
    return f'''            <div class="door-mark-thumb{sm_cls} door-mark-thumb--{kind} mx-auto mb-4">
              <img src="{src}" alt="" width="512" height="512" loading="lazy" decoding="async" />
            </div>
'''


solo = (root / "solo/index.html").read_text(encoding="utf-8")
# After solo pathway label / before h1 - add map mark in hero
if "door-mark-thumb--map" not in solo.split("Solo pathway")[1][:800]:
    solo = solo.replace(
        '<span class="section-label !text-[#5c4a0c]">Solo pathway</span>',
        thumb("map", "/assets/images/brand/tcf-door-map.jpg?v=marks3").replace(
            "mb-4", "mb-6"
        )
        + '        <span class="section-label !text-[#5c4a0c]">Solo pathway</span>',
        1,
    )

# Card marks for Learn / Practice / Save / Gym
replacements = [
    (
        '<span class="font-mono text-xs uppercase tracking-[0.2em] text-[#5c4a0c]">Learn</span>',
        thumb("map", "/assets/images/brand/tcf-door-map.jpg?v=marks3")
        + '            <span class="font-mono text-xs uppercase tracking-[0.2em] text-[#5c4a0c]">Learn</span>',
    ),
    (
        '<span class="font-mono text-xs uppercase tracking-[0.2em] text-[#145032]">Practice</span>',
        thumb("practice", "/assets/images/brand/tcf-door-practice-v3.jpg?v=marks4")
        + '            <span class="font-mono text-xs uppercase tracking-[0.2em] text-[#145032]">Practice</span>',
    ),
    (
        '<span class="font-mono text-xs uppercase tracking-[0.2em] text-[#6e1818]">Save</span>',
        thumb("save", "/assets/images/brand/tcf-door-save-v2.jpg?v=marks4")
        + '            <span class="font-mono text-xs uppercase tracking-[0.2em] text-[#6e1818]">Save</span>',
    ),
    (
        '<span class="font-mono text-xs uppercase tracking-[0.2em] accent-map">Gym · Solo only</span>',
        thumb("practice", "/assets/images/brand/tcf-door-practice-v3.jpg?v=marks4")
        + '            <span class="font-mono text-xs uppercase tracking-[0.2em] accent-map">Gym · Solo only</span>',
    ),
    (
        '<span class="section-label">Content</span>',
        thumb("lattice", "/assets/images/brand/tcf-door-lattice.jpg?v=brand-exp21").replace(
            "mb-4", "mb-5"
        )
        + '        <span class="section-label">Content</span>',
    ),
]
for old, new_s in replacements:
    if old in solo and "door-mark-thumb" not in solo[solo.find(old) - 200 : solo.find(old)]:
        solo = solo.replace(old, new_s, 1)

solo = inject_marks_css(solo)
(root / "solo/index.html").write_text(solo, encoding="utf-8")
print("solo marks ok")

ent = (root / "enterprise/index.html").read_text(encoding="utf-8")
if "door-mark-thumb--dojo" not in ent.split("Enterprise pathway")[1][:900]:
    ent = ent.replace(
        '<span class="section-label !text-[#12355c]">Enterprise pathway</span>',
        thumb("dojo", "/assets/images/brand/tcf-door-dojo.jpg?v=marks3").replace(
            "mb-4", "mb-6"
        )
        + '        <span class="section-label !text-[#12355c]">Enterprise pathway</span>',
        1,
    )

ent_reps = [
    (
        '<span class="font-mono text-xs uppercase tracking-[0.2em] text-[#5c4a0c]">Learn</span>',
        thumb("map", "/assets/images/brand/tcf-door-map.jpg?v=marks3")
        + '            <span class="font-mono text-xs uppercase tracking-[0.2em] text-[#5c4a0c]">Learn</span>',
    ),
    (
        '<span class="font-mono text-xs uppercase tracking-[0.2em] text-[#145032]">Practice</span>',
        thumb("practice", "/assets/images/brand/tcf-door-practice-v3.jpg?v=marks4")
        + '            <span class="font-mono text-xs uppercase tracking-[0.2em] text-[#145032]">Practice</span>',
    ),
    (
        '<span class="font-mono text-xs uppercase tracking-[0.2em] text-[#6e1818]">Save</span>',
        thumb("save", "/assets/images/brand/tcf-door-save-v2.jpg?v=marks4")
        + '            <span class="font-mono text-xs uppercase tracking-[0.2em] text-[#6e1818]">Save</span>',
    ),
    (
        '<span class="font-mono text-xs uppercase tracking-[0.2em] accent-dojo">Dojo · Enterprise only</span>',
        thumb("dojo", "/assets/images/brand/tcf-door-dojo.jpg?v=marks3")
        + '            <span class="font-mono text-xs uppercase tracking-[0.2em] accent-dojo">Dojo · Enterprise only</span>',
    ),
    (
        '<span class="section-label">Content</span>',
        thumb("lattice", "/assets/images/brand/tcf-door-lattice.jpg?v=brand-exp21").replace(
            "mb-4", "mb-5"
        )
        + '        <span class="section-label">Content</span>',
    ),
    (
        '<span class="section-label !text-[#12355c]">Partners · motion</span>',
        thumb("lattice", "/assets/images/brand/tcf-door-lattice.jpg?v=brand-exp21").replace(
            "mb-4", "mb-5"
        )
        + '        <span class="section-label !text-[#12355c]">Partners · motion</span>',
    ),
]
for old, new_s in ent_reps:
    pos = ent.find(old)
    if pos != -1 and "door-mark-thumb" not in ent[max(0, pos - 220) : pos]:
        ent = ent.replace(old, new_s, 1)

ent = inject_marks_css(ent)
(root / "enterprise/index.html").write_text(ent, encoding="utf-8")
print("enterprise marks ok")
