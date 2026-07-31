"""
- Marks only inside the 4 bordered glass cards (loop grid)
- Strip marks from centered text sections
- Solo hero: adult-learners still (not video)
- Enterprise hero: 16s loop of team + partner banners
- Refresh home pathways partial (no marks on pathway/systems)
"""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]

# --- Home partial swap ---
index = (root / "index.html").read_text(encoding="utf-8")
partial = (root / "partials/home-pathways-triad.html").read_text(encoding="utf-8")
if not partial.endswith("\n"):
    partial += "\n"
start = index.find("PATHWAYS")
if start == -1:
    raise SystemExit("PATHWAYS missing")
start = index.rfind("<!--", 0, start)
marker = index.find("See the product gallery", start)
end = index.find("</section>", marker) + len("</section>")
while end < len(index) and index[end] in "\r\n":
    end += 1
index = index[:start] + partial + index[end:]
(root / "index.html").write_text(index, encoding="utf-8")
print("home partial refreshed")

HERO_CSS = """
    /* Door page pathway heroes */
    .pathway-hero {
      position: relative;
      padding-top: 4rem;
      background: #e8eaee;
    }
    @media (min-width: 768px) {
      .pathway-hero { padding-top: 5rem; }
    }
    .pathway-hero-media {
      position: relative;
      width: 100%;
      overflow: hidden;
      background: #e8eaee;
      border-bottom: 1px solid rgba(0,0,0,0.06);
    }
    .pathway-hero-media img,
    .pathway-hero-media video {
      display: block;
      width: 100%;
      height: auto;
      max-height: min(70vh, 36rem);
      object-fit: contain;
      object-position: center center;
      background: #e8eaee;
      margin: 0 auto;
    }
    .pathway-hero-copy {
      max-width: 48rem;
      margin: 0 auto;
      text-align: center;
      padding: 2.5rem 1.5rem 3rem;
    }
    @media (min-width: 768px) {
      .pathway-hero-copy { padding: 3rem 1.5rem 3.5rem; }
    }
"""

THUMB = {
    "map": "/assets/images/brand/tcf-door-map.jpg?v=marks3",
    "practice": "/assets/images/brand/tcf-door-practice-v3.jpg?v=marks4",
    "save": "/assets/images/brand/tcf-door-save-v2.jpg?v=marks4",
    "dojo": "/assets/images/brand/tcf-door-dojo.jpg?v=marks3",
}


def thumb(kind: str) -> str:
    return f"""            <div class="door-mark-thumb door-mark-thumb--{kind} mx-auto mb-4">
              <img src="{THUMB[kind]}" alt="" width="512" height="512" loading="lazy" decoding="async" />
            </div>
"""


def strip_orphan_thumbs(html: str) -> str:
    """Remove door-mark-thumb blocks that are NOT inside a glass-card article."""
    # Simpler: remove all thumbs, then re-add only into articles
    html = re.sub(
        r'\s*<div class="door-mark-thumb[^"]*"[^>]*>\s*<img[^>]+/>\s*</div>\s*',
        "\n",
        html,
        flags=re.I,
    )
    return html


def ensure_css(html: str) -> str:
    if "pathway-hero-media" not in html:
        if "/* Dual-lane brand marks" in html:
            html = html.replace(
                "    /* Dual-lane brand marks",
                HERO_CSS + "\n    /* Dual-lane brand marks",
                1,
            )
        elif "/* Flat charcoal CF" in html:
            html = html.replace(
                "    /* Flat charcoal CF",
                HERO_CSS + "\n    /* Flat charcoal CF",
                1,
            )
        else:
            html = html.replace("  </style>", HERO_CSS + "\n  </style>", 1)
    return html


def add_thumbs_to_loop_cards(html: str, kinds: list[str]) -> str:
    """
    After strip, each glass-card in #loop grid should get a thumb.
    kinds order matches article order.
    """
    # Find loop section grid articles
    loop_i = html.find('id="loop"')
    if loop_i == -1:
        return html
    grid_i = html.find("grid md:grid-cols-2", loop_i)
    if grid_i == -1:
        return html
    # Process each <article class="glass-card in loop until end of grid section
    pos = grid_i
    for kind in kinds:
        art = html.find("<article", pos)
        if art == -1:
            break
        # insert thumb after opening article tag
        gt = html.find(">", art)
        insert = gt + 1
        html = html[:insert] + "\n" + thumb(kind) + html[insert:]
        pos = insert + 80
    return html


SOLO_HERO = """
    <section class="pathway-hero" aria-label="Solo pathway">
      <div class="pathway-hero-media">
        <img
          src="/assets/images/hero-slides/adult-learners.jpg?v=marks2"
          alt="Adult learners: upskill in the moments that matter"
          width="1920"
          height="1071"
          fetchpriority="high"
          decoding="async"
        />
      </div>
      <div class="pathway-hero-copy" data-reveal>
        <span class="section-label !text-[#5c4a0c]">Solo pathway</span>
        <h1 class="section-title">Adult learners · structure that holds when life is loud</h1>
        <p class="section-subtitle mx-auto">
          Productized cores and carts. <span class="text-ink-soft">Gym</span> when a vertical needs training wheels.
          Same factory as Enterprise — dialed for interruptible real life. You own the outcome.
        </p>
        <div class="flex flex-col sm:flex-row gap-3 justify-center mt-8">
          <a href="#gym" class="btn-primary">See the Gym</a>
          <a href="/enterprise/" class="btn-secondary">Enterprise path →</a>
        </div>
      </div>
    </section>
"""

ENT_HERO = """
    <section class="pathway-hero" aria-label="Enterprise pathway">
      <div class="pathway-hero-media">
        <video
          class="pathway-hero-video"
          autoplay
          muted
          loop
          playsinline
          preload="metadata"
          poster="/assets/images/hero-slides/team-cross-skilling.jpg?v=marks2"
          aria-label="Enterprise audience: teams cross-skilling and partners under pressure — 16 second loop"
        >
          <source src="/assets/videos/enterprise-hero-loop.mp4?v=ent1" type="video/mp4" />
        </video>
      </div>
      <div class="pathway-hero-copy" data-reveal>
        <span class="section-label !text-[#12355c]">Enterprise pathway</span>
        <h1 class="section-title">Teams &amp; institutions · pressure that stays honest</h1>
        <p class="section-subtitle mx-auto">
          Custom maps and scenarios on <em>your</em> standards. <span class="text-ink-soft">Dojo</span> for messy, timed work —
          teams primary; partners as a motion for honest reads from engagement libraries.
        </p>
        <div class="flex flex-col sm:flex-row gap-3 justify-center mt-8">
          <a href="#dojo" class="btn-primary">See the Dojo</a>
          <a href="/solo/" class="btn-secondary">Solo path →</a>
        </div>
      </div>
    </section>
"""


def replace_first_section(html: str, new_hero: str) -> str:
    """Replace first <section ...> ... </section> inside <main>."""
    main = html.find("<main")
    s = html.find("<section", main)
    if s == -1:
        raise SystemExit("no first section")
    depth = 0
    i = s
    end = -1
    while i < len(html):
        if html.startswith("<section", i):
            depth += 1
            i = html.find(">", i) + 1
            continue
        if html.startswith("</section>", i):
            depth -= 1
            if depth == 0:
                end = i + len("</section>")
                break
            i += len("</section>")
            continue
        i += 1
    if end == -1:
        raise SystemExit("unclosed first section")
    return html[:s] + new_hero + html[end:]


def polish_door(path: Path, hero: str, kinds: list[str]) -> None:
    html = path.read_text(encoding="utf-8")
    html = strip_orphan_thumbs(html)
    html = replace_first_section(html, hero)
    html = strip_orphan_thumbs(html)  # in case hero had none
    # remove any thumbs that reappeared outside articles — strip all then readd to loop
    html = strip_orphan_thumbs(html)
    html = add_thumbs_to_loop_cards(html, kinds)
    html = ensure_css(html)
    # text-center on cards for mark alignment
    html = html.replace(
        'class="glass-card card-border-map p-6 md:p-8"',
        'class="glass-card card-border-map p-6 md:p-8 text-center"',
    )
    html = html.replace(
        'class="glass-card card-border-practice p-6 md:p-8"',
        'class="glass-card card-border-practice p-6 md:p-8 text-center"',
    )
    html = html.replace(
        'class="glass-card card-border-save p-6 md:p-8"',
        'class="glass-card card-border-save p-6 md:p-8 text-center"',
    )
    html = html.replace(
        'class="glass-card card-border-dojo p-6 md:p-8"',
        'class="glass-card card-border-dojo p-6 md:p-8 text-center"',
    )
    # Gym uses map border
    html = html.replace(
        'id="gym" class="glass-card card-border-map p-6 md:p-8 text-center text-center"',
        'id="gym" class="glass-card card-border-map p-6 md:p-8 text-center"',
    )
    path.write_text(html, encoding="utf-8")
    print("polished", path)


polish_door(
    root / "solo/index.html",
    SOLO_HERO,
    ["map", "practice", "save", "practice"],  # Gym uses practice/exam-book mark
)
polish_door(
    root / "enterprise/index.html",
    ENT_HERO,
    ["map", "practice", "save", "dojo"],
)
print("done")
