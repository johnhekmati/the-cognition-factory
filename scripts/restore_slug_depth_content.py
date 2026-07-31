"""
Restore full Learn / Practice / Gym|Dojo / Save copy into slug #content zones.
No brand door marks (strip door-split-mark / door-intro-mark / platform-mark images).
Keep small icon-tiles in 'What it does' lists.
"""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]


def strip_marks(html: str) -> str:
    # Remove door-split-mark columns
    html = re.sub(
        r'\s*<div class="door-split-mark[^"]*"[^>]*>.*?</div>\s*(?=<div class="door-split-body"|</div>\s*</div>\s*</div>)',
        "\n",
        html,
        flags=re.S,
    )
    # Remove door-intro-mark blocks
    html = re.sub(
        r'\s*<div class="door-intro-mark[^"]*"[^>]*>.*?</div>\s*',
        "\n",
        html,
        flags=re.S,
    )
    # Remove platform-mark image wrappers (brand marks)
    html = re.sub(
        r'\s*<div class="platform-mark[^"]*"[^>]*>\s*<img[^>]+>\s*</div>\s*',
        "\n",
        html,
        flags=re.S,
    )
    # Flatten door-split to single column flow
    html = html.replace('class="door-split door-split--mark-end"', 'class="max-w-3xl mx-auto"')
    html = html.replace('class="door-split door-split--mark-start"', 'class="max-w-3xl mx-auto"')
    html = html.replace('class="door-split-head"', 'class="door-copy-head"')
    html = html.replace('class="door-split-body"', 'class="door-copy-body mt-6"')
    # door-intro without mark column — keep head/body stack
    html = html.replace(
        'class="door-intro door-intro--dojo text-center max-w-3xl mx-auto mb-10 md:mb-12"',
        'class="door-intro text-center max-w-3xl mx-auto mb-10 md:mb-12"',
    )
    html = html.replace(
        'class="door-intro door-intro--save text-center max-w-3xl mx-auto mb-12 md:mb-16"',
        'class="door-intro text-center max-w-3xl mx-auto mb-12 md:mb-16"',
    )
    # Intro body spacing after head (no mark between)
    html = html.replace(
        'class="door-intro-body"',
        'class="door-intro-body mt-6"',
    )
    return html


map_html = strip_marks((root / "partials/_ext_map.html").read_text(encoding="utf-8"))
aae_html = strip_marks((root / "partials/_ext_aae.html").read_text(encoding="utf-8"))
dojo_html = strip_marks((root / "partials/_ext_dojo.html").read_text(encoding="utf-8"))
platform_html = strip_marks((root / "partials/_ext_platform.html").read_text(encoding="utf-8"))

# Ensure sections close
for name, h in [("map", map_html), ("aae", aae_html), ("dojo", dojo_html), ("platform", platform_html)]:
    if "</section>" not in h:
        print("WARN no close", name)

# --- Solo dials ---
aae_solo = aae_html.replace(
    """            <a href="#dojo" class="inline-flex items-center gap-1 text-sm font-medium mt-5 hover:gap-2 transition-all" style="color:#145032">
              Then step into the Dojo
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </a>""",
    """            <a href="#gym" class="inline-flex items-center gap-1 text-sm font-medium mt-5 hover:gap-2 transition-all" style="color:#145032">
              Then step into the Gym
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </a>""",
)

gym_html = dojo_html
gym_html = gym_html.replace('id="dojo"', 'id="gym"')
gym_html = gym_html.replace("The Dojo · Scenario practice", "The Gym · Training wheels")
gym_html = gym_html.replace("Deliver it when it’s messy", "Like the real thing for muscle memory")
gym_html = gym_html.replace("Real scenarios · not another quiz", "Training wheels · not Planet Fitness")
gym_html = gym_html.replace(
    """              Practice checks what you know. The <span class="text-ink-soft">Dojo</span> puts that skill into
              messy, timed scenarios — half-finished work, something at stake — so you can see how the call
              holds under pressure. Structured observation, not a hiring decision or certification.""",
    """              Practice checks what you know. The <span class="text-ink-soft">Gym</span> is where a vertical
              gets intentional thin environments when it needs them — martial-arts-studio tools, not a machine warehouse.
              Kristi filter: training wheels, no mockery, no injury. Neutral off-ramps when you’re ready for the real tool.
              <strong class="text-ink">Not the Dojo</strong> — Dojo is the Enterprise pressure floor.""",
)
gym_html = gym_html.replace("The Dojo asks for", "The Gym trains for")
gym_html = gym_html.replace("Delivering it", "Using it safely")
gym_html = gym_html.replace(
    """            so the Dojo tests what you actually built. No trick questions from nowhere.
          </p>
          <p class="mt-6 font-mono text-xs uppercase tracking-[0.2em] text-[#12355c]">
            Practice asks “do you know it?” · The Dojo asks “can you work the messy case?”
          </p>
          <a href="#who" class="btn-secondary mt-8 inline-flex">See who trains here →</a>""",
    """            so the Gym only appears when the vertical needs it. No cosplay floor for every subject.
          </p>
          <p class="mt-6 font-mono text-xs uppercase tracking-[0.2em] text-[#12355c]">
            Practice asks “do you know it?” · The Gym asks “can you try it with training wheels?”
          </p>
          <a href="#platform" class="btn-secondary mt-8 inline-flex">How save place works →</a>""",
)
# Solo scenarios: keep as flavor of pressure practice, retitle slightly
gym_html = gym_html.replace(
    "From real scenario packs — the flavor, not the answer key",
    "From real-world shaped drills — the flavor, not the answer key",
)
gym_html = gym_html.replace(
    'aria-label="From recognizing to delivering"',
    'aria-label="From recognizing to using it safely"',
)

platform_solo = platform_html.replace(
    'href="#contact" class="btn-secondary mt-8 inline-flex">Ask how picking back up works day to day</a>',
    'href="#contact" class="btn-secondary mt-8 inline-flex">Ask how picking back up works day to day</a>',
)
# Stay oriented item 3 for solo can stay "later paths" or soften for household
platform_solo = platform_solo.replace(
    "Later: paths across skills</span> — for teams working more than one subject.",
    "Later: paths across skills</span> — when one subject is not enough.",
)

# --- Enterprise dials ---
aae_ent = aae_html  # already links to #dojo
dojo_ent = dojo_html.replace(
    '<a href="#who" class="btn-secondary mt-8 inline-flex">See who trains here →</a>',
    '<a href="#platform" class="btn-secondary mt-8 inline-flex">How save place works →</a>',
)
# Light enterprise learn dial in map body
map_ent = map_html.replace(
    "productized starter set you can start from.",
    "maps fitted to roles and curricula you define.",
)
# If that string only in list - also dial the long paragraph slightly
map_ent = map_ent.replace(
    "You keep a living picture of the subject.",
    "Teams keep a living picture of the subject on shared standards.",
)

platform_ent = platform_html.replace(
    "For weeks that <em>interrupt</em> — not perfect study streaks.",
    "For calendars that <em>interrupt</em> — not perfect study streaks.",
)
platform_ent = platform_ent.replace(
    "whether you were in Learn or mid Practice.",
    "whether a learner was in Learn, mid Practice, or between cohort sessions.",
)

CONTENT_SOLO = f"""
    <!-- ═══════════════════════════════════════════════════════════
         DEPTH — Learn · Practice · Gym · Save (no brand door marks)
         ═══════════════════════════════════════════════════════════ -->
    <div id="content" class="slug-depth">
{map_html}
{aae_solo}
{gym_html}
{platform_solo}
    </div>
"""

CONTENT_ENT = f"""
    <!-- ═══════════════════════════════════════════════════════════
         DEPTH — Learn · Practice · Dojo · Save (no brand door marks)
         ═══════════════════════════════════════════════════════════ -->
    <div id="content" class="slug-depth">
{map_ent}
{aae_ent}
{dojo_ent}
{platform_ent}
    </div>
"""


def replace_content_section(page: Path, block: str) -> None:
    html = page.read_text(encoding="utf-8")
    # Find short content section OR existing slug-depth
    if 'id="content"' in html:
        i = html.find('id="content"')
        # if content is a section
        s = html.rfind("<section", 0, i)
        if s == -1 or s < html.find("<main"):
            s = html.rfind("<div", 0, i)
        tag = "section" if html[s : s + 8] == "<section" else "div"
        # if id is on section
        open_tag = html.rfind("<", 0, i + 1)
        # walk from the opening tag that contains id=content
        open_tag = html.rfind("<", 0, i)
        # determine tag name
        m = re.match(r"<(section|div)\b", html[open_tag:])
        if not m:
            raise SystemExit(f"cannot find content open {page}")
        tag = m.group(1)
        depth = 0
        j = open_tag
        end = -1
        open_pat = f"<{tag}"
        close_pat = f"</{tag}>"
        while j < len(html):
            if html.startswith(open_pat, j) and (
                len(html) == j + len(open_pat)
                or html[j + len(open_pat)] in " \t\n\r>/"
            ):
                depth += 1
                j = html.find(">", j) + 1
                continue
            if html.startswith(close_pat, j):
                depth -= 1
                if depth == 0:
                    end = j + len(close_pat)
                    break
                j += len(close_pat)
                continue
            j += 1
        if end < 0:
            raise SystemExit(f"unclosed content {page}")
        html = html[:open_tag] + block + html[end:]
    else:
        # insert before product or contact
        ins = html.find('id="product"')
        if ins < 0:
            ins = html.find('id="contact"')
        ins = html.rfind("<section", 0, ins)
        html = html[:ins] + block + html[ins:]

    page.write_text(html, encoding="utf-8")
    print("depth content →", page)


replace_content_section(root / "solo" / "index.html", CONTENT_SOLO)
replace_content_section(root / "enterprise" / "index.html", CONTENT_ENT)

# Quick sanity: no door mark images in content depth
for p in [root / "solo" / "index.html", root / "enterprise" / "index.html"]:
    t = p.read_text(encoding="utf-8")
    # brand door images should not appear inside slug-depth (product gallery may not have them)
    depth = t[t.find('id="content"') : t.find('id="product"') if 'id="product"' in t else t.find('id="contact"')]
    bad = [x for x in ["tcf-door-map", "tcf-door-practice", "tcf-door-save", "tcf-door-dojo", "tcf-door-lattice"] if x in depth]
    print(p.name, "brand marks in depth:", bad or "none")
    print("  has #map", 'id="map"' in depth, " #aae", 'id="aae"' in depth, " #gym/#dojo", 'id="gym"' in depth or 'id="dojo"' in depth, " #platform", 'id="platform"' in depth)

print("done")
