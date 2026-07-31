# -*- coding: utf-8 -*-
"""Wrap slug depth door-copy-body in white mark-bordered panels (Learn/Practice/Save/Gym|Dojo)."""
from pathlib import Path
import re

BORDER = {
    "map": "card-border-map",
    "aae": "card-border-practice",
    "platform": "card-border-save",
    "gym": "card-border-dojo",
    "dojo": "card-border-dojo",
}

PANEL_CSS = """
    /* Depth narrative body — white plate + mark rim (Learn/Practice/Save/Dojo|Gym) */
    .slug-depth .depth-panel {
      background: #ffffff;
      border-radius: 0.85rem;
      border-style: solid;
      border-width: 2px;
      padding: 1.5rem 1.5rem 1.75rem;
      box-shadow:
        0 8px 28px rgba(45, 50, 60, 0.08),
        0 2px 8px rgba(45, 50, 60, 0.04);
    }
    @media (min-width: 768px) {
      .slug-depth .depth-panel {
        padding: 2rem 2rem 2.25rem;
      }
    }
    .slug-depth .depth-panel.card-border-map {
      border-color: #c9a227;
    }
    .slug-depth .depth-panel.card-border-practice {
      border-color: #3d8c5a;
    }
    .slug-depth .depth-panel.card-border-save {
      border-color: #b03030;
    }
    .slug-depth .depth-panel.card-border-dojo {
      border-color: #2b5f9e;
    }
"""


def wrap_depth_panels(html: str) -> str:
    """Wrap each door-copy-body inside slug-depth with a depth-panel + mark border."""

    def replacer(m: re.Match) -> str:
        section_id = m.group(1)
        before = m.group(2)  # content between section open and door-copy-body
        body_inner = m.group(3)
        after = m.group(4)  # after body close through section end - not used in replace of full match carefully

        border = BORDER.get(section_id)
        if not border:
            return m.group(0)

        # Avoid double-wrap
        if "depth-panel" in body_inner:
            return m.group(0)

        wrapped = (
            f'<section id="{section_id}"{m.group("attrs")}>'
            f"{before}"
            f'<div class="door-copy-body mt-6" data-reveal>\n'
            f'            <div class="depth-panel {border}">\n'
            f"{body_inner}"
            f"            </div>\n"
            f"          </div>"
            f"{after}"
        )
        return wrapped

    # Match each depth section that has door-copy-body
    pattern = re.compile(
        r'<section id="(?P<id>map|aae|platform|gym|dojo)"(?P<attrs>[^>]*)>'
        r"(?P<before>.*?)"
        r'<div class="door-copy-body mt-6" data-reveal>\s*'
        r"(?P<body>.*?)"
        r"</div>\s*"
        r"(?P<after></div>\s*</div>\s*</section>)",
        re.S,
    )

    def repl(m: re.Match) -> str:
        section_id = m.group("id")
        border = BORDER.get(section_id)
        if not border or "depth-panel" in m.group("body"):
            return m.group(0)
        body = m.group("body")
        # indent body one level if needed — keep as-is
        return (
            f'<section id="{section_id}"{m.group("attrs")}>'
            f'{m.group("before")}'
            f'<div class="door-copy-body mt-6" data-reveal>\n'
            f'            <div class="depth-panel {border}">\n'
            f"{body}"
            f"            </div>\n"
            f"          </div>\n"
            f'{m.group("after")}'
        )

    new, n = pattern.subn(repl, html)
    return new, n


def ensure_css(html: str) -> str:
    if ".slug-depth .depth-panel" in html:
        return html
    # inject before product platform or after pathway-hero-copy block
    needle = "    /* Product platform readiness — icon row, not prose */"
    if needle in html:
        return html.replace(needle, PANEL_CSS + "\n" + needle, 1)
    # fallback: before </style> first head style
    return html.replace("</style>", PANEL_CSS + "\n  </style>", 1)


def process(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = ensure_css(text)
    text, n = wrap_depth_panels(text)
    path.write_text(text, encoding="utf-8")
    print(f"{path.name}: wrapped {n} depth panels")


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    for name in ("enterprise", "solo"):
        p = root / name / "index.html"
        if p.exists():
            process(p)
        else:
            print(f"skip missing {p}")
