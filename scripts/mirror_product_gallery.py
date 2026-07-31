"""Mirror product gallery to /solo and /enterprise with audience-specific blurbs."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
index = (root / "index.html").read_text(encoding="utf-8")

# Extract product section
start = index.find('id="product"')
start = index.rfind("<section", 0, start)
depth = 0
i = start
end = -1
while i < len(index):
    if index.startswith("<section", i):
        depth += 1
        i = index.find(">", i) + 1
        continue
    if index.startswith("</section>", i):
        depth -= 1
        if depth == 0:
            end = i + len("</section>")
            break
        i += len("</section>")
        continue
    i += 1
gallery = index[start:end]

# Extract lightbox
lb_start = index.find('id="product-lightbox"')
lb_start = index.rfind("<div", 0, lb_start)
lb_end = index.find("</div>\n  </div>\n\n  <script", lb_start)
# more reliable: from comment
lb_c = index.find("<!-- Product gallery lightbox -->")
lb_end = index.find("<script src=", lb_c)
lightbox = index[lb_c:lb_end].strip() + "\n"

# Remove dual pathway buttons from mirrored galleries (already on pathway)
gallery = re.sub(
    r"\s*<!-- Pathway hooks sit ABOVE the gallery grid \(not under a mockup\) -->.*?</div>\s*",
    "\n",
    gallery,
    count=1,
    flags=re.S,
)


def apply_blurbs(html: str, audience: str) -> str:
    """Replace intro + aio-copy blurbs for solo or enterprise."""
    if audience == "solo":
        subs = [
            (
                """            <h3 class="font-display text-2xl font-semibold text-ink">The household desk</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Learn · practice · save place on a full screen — plus a thin workflow floor
              when the skill needs a form and a stage.
            </p>""",
                """            <h3 class="font-display text-2xl font-semibold text-ink">Your desk, your calendar</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Full-screen Learn · Practice · Save place for interruptible weeks —
              plus a thin workflow floor only when the skill actually needs a form and a stage.
            </p>""",
            ),
            (
                """              <h3 class="font-display text-xl font-semibold text-ink">Build the map</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                Libraries, topics, and side chat when it earns its keep.
                One idea until it clicks — calm chrome, mark color where it earns its keep.
              </p>""",
                """              <h3 class="font-display text-xl font-semibold text-ink">Build the map</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                Productized cores you can start from. One idea until it clicks —
                side chat only when it earns its keep under a loud week.
              </p>""",
            ),
            (
                """              <h3 class="font-display text-xl font-semibold text-ink">Prove the gaps</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                Closed-notes style: mark correct or incorrect as you go, name what went wrong,
                keep teaching and testing on the same story.
              </p>""",
                """              <h3 class="font-display text-xl font-semibold text-ink">Prove the gaps</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                Honest closed-notes packs from <em>your</em> map — name what went wrong,
                drill the gap, not the whole playlist. Gym when a vertical needs training wheels.
              </p>""",
            ),
            (
                """              <h3 class="font-display text-xl font-semibold text-ink">Park clean when life hits</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                Where you left off, what to do next, and a short park note —
                so the next sitting starts without thrash.
              </p>""",
                """              <h3 class="font-display text-xl font-semibold text-ink">Park clean when life hits</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                Kids, work, noise — leave a clear next step so the next short sitting
                starts without re-scrolling chat.
              </p>""",
            ),
            (
                """              <h3 class="font-display text-xl font-semibold text-ink">Hands on a process</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                After the map and the quiz, some skills need a form and a stage.
                Thin, Dynamics-shaped practice — not a Microsoft product, not full ERP theater.
                Cohorts without volumetric enterprise seats use the same floor until the click order is boring.
              </p>""",
                """              <h3 class="font-display text-xl font-semibold text-ink">Hands on a process</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                When a solo subject needs a form and a stage, the thin workflow floor is there —
                not a second product to babysit, and not a promise of hire-day software.
              </p>""",
            ),
            (
                """                <h3 class="font-display text-xl font-semibold text-ink">Plain house tools</h3>
                <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                  A 60-second recipe with no factory jargon, support dump when admin is away,
                  and the quieter doors under More — Settings, Help, Telemetry.
                </p>""",
                """                <h3 class="font-display text-xl font-semibold text-ink">Plain house tools</h3>
                <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                  A 60-second recipe with no factory jargon — settings and help when you need them,
                  without turning the household install into an IT project.
                </p>""",
            ),
            (
                """            <h3 class="font-display text-2xl font-semibold text-ink">Same loop in your pocket</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Learn, Practice, Save place — and the side chat when it earns its keep.
              Not a thinner product; the same doors on a phone.
            </p>""",
                """            <h3 class="font-display text-2xl font-semibold text-ink">Same loop in your pocket</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Short sittings between everything else — Learn, Practice, Save place on Android.
              Same doors as the desk, sized for real life.
            </p>""",
            ),
            (
                """        <p class="max-w-2xl mx-auto text-center text-ink-muted text-sm mt-10 md:mt-12 leading-relaxed" data-reveal>
          Windows and Android first; macOS and iOS when the same loop is solid there.
          Canvas stays light — gold · green · red · blue only for the engines they name.
          The workflow floor stays light and dense on purpose — so moving onto a real tool is less
          of a cold start, with explicit neutral off-ramps when you are ready for the real thing.
        </p>""",
                """        <p class="max-w-2xl mx-auto text-center text-ink-muted text-sm mt-10 md:mt-12 leading-relaxed" data-reveal>
          Windows and Android first. When you’re ready for the real tool in a subject,
          Gym and off-ramps stay neutral — no vendor logo theater.
        </p>""",
            ),
        ]
    else:
        subs = [
            (
                """            <h3 class="font-display text-2xl font-semibold text-ink">The household desk</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Learn · practice · save place on a full screen — plus a thin workflow floor
              when the skill needs a form and a stage.
            </p>""",
                """            <h3 class="font-display text-2xl font-semibold text-ink">The team desk</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Same loop on a full screen — maps and packs on <em>your</em> standards,
              plus a thin workflow floor when the role needs a form and a stage.
            </p>""",
            ),
            (
                """              <h3 class="font-display text-xl font-semibold text-ink">Build the map</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                Libraries, topics, and side chat when it earns its keep.
                One idea until it clicks — calm chrome, mark color where it earns its keep.
              </p>""",
                """              <h3 class="font-display text-xl font-semibold text-ink">Build the map</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                Shared maps fitted to roles and curricula you define —
                one story for the team, not a pile of personal chat threads.
              </p>""",
            ),
            (
                """              <h3 class="font-display text-xl font-semibold text-ink">Prove the gaps</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                Closed-notes style: mark correct or incorrect as you go, name what went wrong,
                keep teaching and testing on the same story.
              </p>""",
                """              <h3 class="font-display text-xl font-semibold text-ink">Prove the gaps</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                Closed-notes packs against team standards — name the gap, aim the next run.
                Dojo is the pressure floor when the work gets messy (not a hire credential).
              </p>""",
            ),
            (
                """              <h3 class="font-display text-xl font-semibold text-ink">Park clean when life hits</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                Where you left off, what to do next, and a short park note —
                so the next sitting starts without thrash.
              </p>""",
                """              <h3 class="font-display text-xl font-semibold text-ink">Handoff across calendars</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                Cohort ramps and real calendars — leave a clear next step so continuity
                survives meetings, travel, and handoffs.
              </p>""",
            ),
            (
                """              <h3 class="font-display text-xl font-semibold text-ink">Hands on a process</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                After the map and the quiz, some skills need a form and a stage.
                Thin, Dynamics-shaped practice — not a Microsoft product, not full ERP theater.
                Cohorts without volumetric enterprise seats use the same floor until the click order is boring.
              </p>""",
                """              <h3 class="font-display text-xl font-semibold text-ink">Hands on a process</h3>
              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                Thin, Dynamics-shaped practice floor for process muscle —
                not a Microsoft product, not full ERP theater. Useful when seats are scarce
                and the click order still has to become boring.
              </p>""",
            ),
            (
                """                <h3 class="font-display text-xl font-semibold text-ink">Plain house tools</h3>
                <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                  A 60-second recipe with no factory jargon, support dump when admin is away,
                  and the quieter doors under More — Settings, Help, Telemetry.
                </p>""",
                """                <h3 class="font-display text-xl font-semibold text-ink">Plain house tools</h3>
                <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                  Same calm chrome for learners and admins — support dump when needed,
                  quieter doors under More without turning delivery into IT theater.
                </p>""",
            ),
            (
                """            <h3 class="font-display text-2xl font-semibold text-ink">Same loop in your pocket</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Learn, Practice, Save place — and the side chat when it earns its keep.
              Not a thinner product; the same doors on a phone.
            </p>""",
                """            <h3 class="font-display text-2xl font-semibold text-ink">Same loop between meetings</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Field and hallway sittings — Learn, Practice, Save place on Android.
              Same doors as the desk, for teams that don’t live at one monitor.
            </p>""",
            ),
            (
                """        <p class="max-w-2xl mx-auto text-center text-ink-muted text-sm mt-10 md:mt-12 leading-relaxed" data-reveal>
          Windows and Android first; macOS and iOS when the same loop is solid there.
          Canvas stays light — gold · green · red · blue only for the engines they name.
          The workflow floor stays light and dense on purpose — so moving onto a real tool is less
          of a cold start, with explicit neutral off-ramps when you are ready for the real thing.
        </p>""",
                """        <p class="max-w-2xl mx-auto text-center text-ink-muted text-sm mt-10 md:mt-12 leading-relaxed" data-reveal>
          Windows and Android first. Scenario packs and the workflow floor stay tied to
          <em>your</em> standards — observation under pressure, not a placement guarantee.
        </p>""",
            ),
        ]

    for old, new in subs:
        if old not in html:
            print("WARN missing blurb chunk for", audience)
        else:
            html = html.replace(old, new, 1)
    return html


def swap_product(page: Path, audience: str) -> None:
    html = page.read_text(encoding="utf-8")
    g = apply_blurbs(gallery, audience)
    # find product section
    i = html.find('id="product"')
    if i < 0:
        raise SystemExit(f"no product in {page}")
    s = html.rfind("<section", 0, i)
    depth = 0
    j = s
    end = -1
    while j < len(html):
        if html.startswith("<section", j):
            depth += 1
            j = html.find(">", j) + 1
            continue
        if html.startswith("</section>", j):
            depth -= 1
            if depth == 0:
                end = j + len("</section>")
                break
            j += len("</section>")
            continue
        j += 1
    html = html[:s] + g + html[end:]

    # lightbox once before script
    if "product-lightbox" not in html:
        html = html.replace(
            '<script src="/js/main.js',
            lightbox + '\n  <script src="/js/main.js',
            1,
        )

    # ensure platform-status CSS if missing
    if ".platform-status" not in html:
        # copy from index if present
        m = re.search(
            r"/\* Product platform readiness.*?(?=/\* Manifesto|\.prose-panel)",
            index,
            flags=re.S,
        )
        if m:
            html = html.replace("  </style>", m.group(0) + "\n  </style>", 1)

    # product-aio-grid css - in styles.css via npm build, should be fine
    page.write_text(html, encoding="utf-8")
    print("gallery →", page, "lightbox" in html)


swap_product(root / "solo" / "index.html", "solo")
swap_product(root / "enterprise" / "index.html", "enterprise")
print("done")
