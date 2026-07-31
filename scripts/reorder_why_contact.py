# -*- coding: utf-8 -*-
"""Move Why above knowledge base (soft gray); charcoal Connect like solo."""
from pathlib import Path
import re

path = Path(__file__).resolve().parents[1] / "index.html"
text = path.read_text(encoding="utf-8")

def find_comment_block_start(text: str, title_snip: str) -> int:
    idx = text.find(title_snip)
    if idx < 0:
        raise SystemExit(f"missing marker: {title_snip}")
    return text.rfind("    <!--", 0, idx)


res_start = find_comment_block_start(text, "RESEARCH / K-BASE")
prom_start = find_comment_block_start(text, "PROMISE —")
contact_start = find_comment_block_start(text, "CONTACT —")

resources = text[res_start:prom_start]
promise = text[prom_start:contact_start]

# Soft-gray Why (not charcoal)
promise = promise.replace(
    '<section id="promise" class="section-padding relative band-charcoal">',
    '<section id="promise" class="section-padding relative section-soft-gray">',
    1,
)
promise = promise.replace(
    "PROMISE — charcoal closer (chiasmus mirror of hero charcoal; founder on johnhekmati.com)",
    "PROMISE — Why it exists (soft-gray field; founder on johnhekmati.com)",
    1,
)

# Resources comment
resources = resources.replace(
    "RESEARCH / K-BASE — before Why (hinge of page; charcoal Why follows)",
    "RESEARCH / K-BASE — after Why it exists",
    1,
)

new_mid = promise.rstrip() + "\n\n\n" + resources.lstrip()
if not new_mid.endswith("\n"):
    new_mid += "\n"
new_mid = new_mid.rstrip() + "\n\n"

text = text[:res_start] + new_mid + text[contact_start:]

# Contact charcoal like solo
old_contact = (
    '    <section id="contact" class="section-padding relative">\n'
    '      <div class="absolute inset-0 bg-gradient-to-t from-electric/[0.03] to-transparent pointer-events-none" aria-hidden="true"></div>'
)
new_contact = (
    '    <section id="contact" class="section-padding relative band-charcoal">\n'
    '      <div class="absolute inset-0 pointer-events-none" aria-hidden="true"></div>'
)
if old_contact not in text:
    raise SystemExit("contact open not found")
text = text.replace(old_contact, new_contact, 1)

# Soft-gray CSS in head
soft_css = """
    /* Soft-gray field for Why it exists (not charcoal) */
    .section-soft-gray {
      width: 100%;
      background: #e8eaee;
      border-top: 1px solid rgba(0, 0, 0, 0.06);
      border-bottom: 1px solid rgba(0, 0, 0, 0.06);
    }
"""
if "section-soft-gray" not in text:
    needle = (
        "    #main-nav .main-nav-desktop .btn-primary {\n"
        "      flex-shrink: 0;\n"
        "      white-space: nowrap;\n"
        "    }\n"
        "  </style>"
    )
    if needle not in text:
        raise SystemExit("head style end not found for soft-gray CSS")
    text = text.replace(
        needle,
        "    #main-nav .main-nav-desktop .btn-primary {\n"
        "      flex-shrink: 0;\n"
        "      white-space: nowrap;\n"
        "    }\n"
        + soft_css
        + "  </style>",
        1,
    )

# Surface / field link restores on charcoal (connect offer rungs)
surface_fix = """
    /* Offer rungs / surface cards on charcoal — white plate, dark type */
    .band-charcoal .surface-card {
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.28);
    }
    .band-charcoal .surface-card .text-ink,
    .band-charcoal .surface-card .text-ink-muted,
    .band-charcoal .surface-card .text-ink-soft {
      color: #000000 !important;
    }
    .band-charcoal a.text-ink:hover {
      color: #9ec0e0 !important;
    }
"""
if ".band-charcoal .surface-card .text-ink" not in text:
    mark = (
        "    .band-charcoal a.text-electric:hover {\n"
        "      color: #c5daf0 !important;\n"
        "    }"
    )
    if mark not in text:
        raise SystemExit("charcoal electric hover not found for surface restore")
    text = text.replace(mark, mark + "\n" + surface_fix, 1)

path.write_text(text, encoding="utf-8")
ids = re.findall(r'<section id="([^"]+)"', path.read_text(encoding="utf-8"))
print("ok sections:", ids)
assert ids.index("promise") < ids.index("resources"), "Why must precede knowledge base"
assert 'id="promise" class="section-padding relative section-soft-gray"' in path.read_text(
    encoding="utf-8"
)
assert 'id="contact" class="section-padding relative band-charcoal"' in path.read_text(
    encoding="utf-8"
)
print("checks passed")
