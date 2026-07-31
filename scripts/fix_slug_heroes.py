"""Align /solo and /enterprise heroes with main site stage size + gradient rails + marquee."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]

MARQUEE = """
          <div class="hero-marquee" aria-hidden="true">
            <div class="hero-marquee-track">
              <span>Learn</span><i>·</i><span>Map</span><i>·</i><span>Practice</span><i>·</i><span>Save your place</span><i>·</i><span>Upskill</span><i>·</i>
              <span>Learn</span><i>·</i><span>Map</span><i>·</i><span>Practice</span><i>·</i><span>Save your place</span><i>·</i><span>Upskill</span><i>·</i>
              <span>Learn</span><i>·</i><span>Map</span><i>·</i><span>Practice</span><i>·</i><span>Save your place</span><i>·</i><span>Upskill</span><i>·</i>
              <span>Learn</span><i>·</i><span>Map</span><i>·</i><span>Practice</span><i>·</i><span>Save your place</span><i>·</i><span>Upskill</span><i>·</i>
              <span>Learn</span><i>·</i><span>Map</span><i>·</i><span>Practice</span><i>·</i><span>Save your place</span><i>·</i><span>Upskill</span><i>·</i>
              <span>Learn</span><i>·</i><span>Map</span><i>·</i><span>Practice</span><i>·</i><span>Save your place</span><i>·</i><span>Upskill</span><i>·</i>
            </div>
          </div>
"""

SOLO_HERO = f"""
    <section class="pathway-hero" id="hero" aria-label="Solo pathway">
      <div class="hero-landing">
        <div class="hero-banner-plate">
          <div class="hero-slide-stage pathway-hero-stage">
            <div class="hero-slides">
              <figure class="hero-slide is-active" aria-hidden="false">
                <picture>
                  <source
                    media="(max-width: 767px)"
                    srcset="/assets/images/hero-slides/mobile/adult-learners.jpg?v=mhero1"
                  />
                  <img
                    src="/assets/images/hero-slides/adult-learners.jpg?v=marks2"
                    alt="Adult learners: upskill in the moments that matter"
                    width="1920"
                    height="1071"
                    decoding="async"
                    fetchpriority="high"
                  />
                </picture>
              </figure>
            </div>
          </div>
        </div>
{MARQUEE}
      </div>

      <div class="pathway-hero-copy section-padding !pt-12 md:!pt-16 !pb-14 md:!pb-16">
        <div class="max-w-3xl mx-auto text-center" data-reveal>
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
      </div>
    </section>
"""

ENT_HERO = f"""
    <section class="pathway-hero" id="hero" aria-label="Enterprise pathway">
      <div class="hero-landing">
        <div class="hero-banner-plate">
          <div class="hero-slide-stage pathway-hero-stage">
            <div class="hero-slides">
              <figure class="hero-slide is-active" aria-hidden="false">
                <video
                  class="pathway-hero-video"
                  autoplay
                  muted
                  loop
                  playsinline
                  preload="metadata"
                  poster="/assets/images/hero-slides/team-cross-skilling.jpg?v=marks2"
                  aria-label="Enterprise audience: teams and partners — 16 second loop"
                >
                  <source src="/assets/videos/enterprise-hero-loop.mp4?v=ent1" type="video/mp4" />
                </video>
              </figure>
            </div>
          </div>
        </div>
{MARQUEE}
      </div>

      <div class="pathway-hero-copy section-padding !pt-12 md:!pt-16 !pb-14 md:!pb-16">
        <div class="max-w-3xl mx-auto text-center" data-reveal>
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
      </div>
    </section>
"""

EXTRA_CSS = """
    /* Pathway slug heroes: same stage size + rails + marquee as main home */
    .pathway-hero {
      background: #e8eaee;
    }
    .pathway-hero .hero-landing {
      min-height: 0 !important;
    }
    .pathway-hero-stage .hero-slide {
      opacity: 1 !important;
      visibility: visible !important;
      z-index: 1;
      pointer-events: auto;
      transition: none !important;
    }
    .pathway-hero-video {
      display: block;
      width: 100%;
      height: 100%;
      object-fit: contain;
      object-position: center center;
      background: #e8eaee;
    }
    .pathway-hero-copy {
      background: #e8eaee;
    }
    .pathway-hero-copy .section-label {
      display: inline-block;
    }
"""


def replace_first_section(html: str, new_hero: str) -> str:
    main = html.find("<main")
    s = html.find("<section", main)
    if s == -1:
        raise SystemExit("no section")
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
    if end < 0:
        raise SystemExit("unclosed section")
    return html[:s] + new_hero + html[end:]


def ensure_css(html: str) -> str:
    # Drop old pathway-hero-media rules if present
    html = re.sub(
        r"\s*/\* Door page pathway heroes \*/.*?(?=/\*|  </style>)",
        "\n",
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r"\s*/\* Pathway slug heroes:.*?(?=/\*|  </style>)",
        "\n",
        html,
        count=1,
        flags=re.S,
    )
    if "pathway-hero-stage .hero-slide" not in html:
        html = html.replace("  </style>", EXTRA_CSS + "\n  </style>", 1)
    return html


def polish(path: Path, hero: str) -> None:
    html = path.read_text(encoding="utf-8")
    html = replace_first_section(html, hero)
    html = ensure_css(html)
    # Door pages need --hero-nav-h for stage height calc
    if "--hero-nav-h" not in html:
        html = html.replace(
            "<style>",
            "<style>\n    #hero, .pathway-hero { --hero-nav-h: 4rem; --hero-field: #e8eaee; }\n"
            "    @media (min-width: 768px) { #hero, .pathway-hero { --hero-nav-h: 5rem; } }\n",
            1,
        )
    path.write_text(html, encoding="utf-8")
    print("ok", path.name, "marquee" in html, "hero-slide-stage" in html)


polish(root / "solo" / "index.html", SOLO_HERO)
polish(root / "enterprise" / "index.html", ENT_HERO)
print("done")
