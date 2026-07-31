"""Build /solo/ and /enterprise/ door pages for local dual-lane demo."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]

# Shared chrome CSS is inlined via reading styles block from current index
index = (root / "index.html").read_text(encoding="utf-8")
# Extract head first-paint + link tags through </head>
head_end = index.find("</head>")
head = index[:head_end]
# Drop hero preload clutter slightly OK keep
# Replace title later per page

# Extract style block from footer area (site-chrome etc.) — full page styles after <style>
style_start = index.find("  <style>\n    /*")
if style_start == -1:
    style_start = index.find("<style>")
style_end = index.find("</style>", style_start) + len("</style>")
styles = index[style_start:style_end]

script = '<script src="/js/main.js?v=hero-paint1" defer></script>\n'


def nav(active: str) -> str:
    solo_cls = "nav-link text-electric" if active == "solo" else "nav-link"
    ent_cls = "nav-link text-electric" if active == "enterprise" else "nav-link"
    return f"""  <header>
    <nav id="main-nav" class="fixed top-0 left-0 right-0 z-50 transition-all duration-300 border-b border-ink/10 bg-white" aria-label="Main navigation">
      <div class="site-chrome">
        <div class="site-chrome-inner flex items-center justify-between h-16 md:h-20">
          <a href="/" class="flex items-center gap-3 group min-w-0" aria-label="The Cognition Factory — Home">
            <img src="/assets/images/brand/tcf-mark-cf-charcoal-light.jpg?v=brand-exp19" alt="" class="brand-nav-mark shrink-0" width="40" height="40" />
            <span class="font-display font-semibold text-ink text-sm md:text-base tracking-tight hidden sm:block border-l border-ink/10 pl-3 truncate">The Cognition Factory</span>
          </a>
          <div class="hidden lg:flex items-center gap-6 shrink-0">
            <a href="/#pathways" class="nav-link">Pathways</a>
            <a href="/solo/" class="{solo_cls}">Solo</a>
            <a href="/enterprise/" class="{ent_cls}">Enterprise</a>
            <a href="#product" class="nav-link" data-nav>Product</a>
            <a href="/#resources" class="nav-link">Guides</a>
            <a href="#contact" class="btn-primary text-xs !px-5 !py-2.5">Talk with us</a>
          </div>
          <button id="menu-toggle" class="lg:hidden p-2 text-ink-muted hover:text-electric transition-colors shrink-0" aria-expanded="false" aria-controls="mobile-menu" aria-label="Toggle menu">
            <svg id="icon-open" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 6h16M4 12h16M4 18h16" /></svg>
            <svg id="icon-close" class="w-6 h-6 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>
      </div>
      <div id="mobile-menu" class="hidden lg:hidden border-t border-ink/10 bg-white">
        <div class="site-chrome">
          <div class="site-chrome-inner py-6 flex flex-col gap-4">
            <a href="/#pathways" class="nav-link py-2">Pathways</a>
            <a href="/solo/" class="nav-link py-2">Solo</a>
            <a href="/enterprise/" class="nav-link py-2">Enterprise</a>
            <a href="#product" class="nav-link py-2" data-nav>Product</a>
            <a href="/#resources" class="nav-link py-2">Guides</a>
            <a href="#contact" class="btn-primary text-center mt-2">Talk with us</a>
          </div>
        </div>
      </div>
    </nav>
  </header>
"""


footer = """  <footer class="border-t border-ink/10 bg-white">
    <div class="site-chrome">
      <div class="site-chrome-inner py-12">
        <div class="flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="flex items-center gap-3 min-w-0">
            <img src="/assets/images/brand/tcf-mark-cf-charcoal-light.jpg?v=brand-exp19" alt="The Cognition Factory" class="brand-nav-mark shrink-0" width="32" height="32" />
            <span class="text-ink-muted text-sm">&copy; 2026 The Cognition Factory. All rights reserved.</span>
          </div>
          <div class="flex flex-wrap items-center justify-center gap-6" aria-label="Site map">
            <a href="/" class="text-ink-muted hover:text-electric text-sm transition-colors">Home</a>
            <a href="/solo/" class="text-ink-muted hover:text-electric text-sm transition-colors">Solo</a>
            <a href="/enterprise/" class="text-ink-muted hover:text-electric text-sm transition-colors">Enterprise</a>
            <a href="#product" class="text-ink-muted hover:text-electric text-sm transition-colors">Product</a>
            <a href="/#resources" class="text-ink-muted hover:text-electric text-sm transition-colors">Guides</a>
            <a href="#contact" class="text-ink-muted hover:text-electric text-sm transition-colors">Contact</a>
          </div>
        </div>
      </div>
    </div>
  </footer>
"""


def page(title: str, desc: str, active: str, body: str) -> str:
    h = head
    # replace title and description if present
    import re

    h = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", h, count=1)
    h = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="{desc}"',
        h,
        count=1,
    )
    return f"""{h}
</head>
<body class="overflow-x-hidden">
  <a href="#main" class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-[100] focus:px-4 focus:py-2 focus:bg-void focus:text-electric focus:border focus:border-electric/40 focus:rounded-md">Skip to content</a>
{nav(active)}
  <main id="main">
{body}
  </main>
{footer}
{styles}
{script}
</body>
</html>
"""


SOLO_BODY = r'''
    <section class="relative pt-24 md:pt-28 section-padding section-charcoal">
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
    </section>

    <section id="enemy" class="section-padding relative">
      <div class="max-w-3xl mx-auto text-center" data-reveal>
        <span class="section-label">The problem</span>
        <h2 class="section-title">More content doesn’t mean more skill</h2>
        <p class="mt-6 text-ink-muted leading-relaxed">
          Certificates stack. Apps multiply. A hard week still shows fuzzy structure.
          Busy adults need a map, honest practice, and a clean place to stop — not another binge library.
        </p>
      </div>
    </section>

    <section id="loop" class="section-padding relative section-charcoal">
      <div class="max-w-5xl mx-auto">
        <div class="text-center max-w-3xl mx-auto mb-12" data-reveal>
          <span class="section-label">How it works</span>
          <h2 class="section-title">Learn · Practice · Save · Gym</h2>
        </div>
        <div class="grid md:grid-cols-2 gap-6" data-reveal>
          <article class="glass-card card-border-map p-6 md:p-8">
            <span class="font-mono text-xs uppercase tracking-[0.2em] text-[#5c4a0c]">Learn</span>
            <h3 class="font-display text-xl font-semibold text-ink mt-3">Build the map</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Dense micro-cores shaped like typical regionally accredited sequences — not affiliation claims.
              One idea until it clicks; productized starter set you can start from.
            </p>
          </article>
          <article class="glass-card card-border-practice p-6 md:p-8">
            <span class="font-mono text-xs uppercase tracking-[0.2em] text-[#145032]">Practice</span>
            <h3 class="font-display text-xl font-semibold text-ink mt-3">Honest packs</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Practice packs derived from the same map — closed notes when it counts.
              Gaps named; drills aimed at what you missed.
            </p>
          </article>
          <article class="glass-card card-border-save p-6 md:p-8">
            <span class="font-mono text-xs uppercase tracking-[0.2em] text-[#6e1818]">Save</span>
            <h3 class="font-display text-xl font-semibold text-ink mt-3">Clean handoff</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Short sessions that still count. Leave where you were and what is next —
              not re-scroll the chat after kids, work, or a loud week.
            </p>
          </article>
          <article id="gym" class="glass-card card-border-map p-6 md:p-8">
            <span class="font-mono text-xs uppercase tracking-[0.2em] accent-map">Gym · Solo only</span>
            <h3 class="font-display text-xl font-semibold text-ink mt-3">Training wheels, not Planet Fitness</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Conditional thin environments when a vertical needs them — martial-arts-studio intentional tools,
              Kristi filter (no mockery, no injury), neutral off-ramps to real tools.
              <strong class="text-ink">Not the Dojo.</strong> Dojo is the Enterprise pressure floor.
            </p>
          </article>
        </div>
      </div>
    </section>

    <section id="content" class="section-padding relative">
      <div class="max-w-3xl mx-auto text-center" data-reveal>
        <span class="section-label">Content</span>
        <h2 class="section-title">Productized cores &amp; carts</h2>
        <p class="section-subtitle mx-auto">
          Hosted dense cores and measurement carts — Accounting and SCM first, then Mathematics and the starter set.
          Factory process: Scaffolding → L0–L3 → carts. No heavy proprietary dSKUs for Solo v1.
        </p>
        <ul class="text-left max-w-md mx-auto mt-8 space-y-2 text-sm text-ink-muted">
          <li class="flex gap-2"><span class="accent-map">·</span><span>Productized, not custom-built per household</span></li>
          <li class="flex gap-2"><span class="accent-map">·</span><span>Markdown/YAML + Postgres posture</span></li>
          <li class="flex gap-2"><span class="accent-map">·</span><span>Claim gate: shaped like / informed by — never accredited-as</span></li>
        </ul>
      </div>
    </section>

    <section id="product" class="section-padding relative border-t border-ink/10">
      <div class="max-w-3xl mx-auto text-center" data-reveal>
        <span class="section-label">Product</span>
        <h2 class="section-title">Where the loop runs</h2>
        <p class="section-subtitle mx-auto">
          Windows and Android thin clients — same Learn · Practice · Save place loop.
        </p>
        <a href="/#product" class="btn-secondary mt-6 inline-flex">Open full product gallery on home →</a>
      </div>
    </section>

    <section id="contact" class="section-padding relative">
      <div class="max-w-xl mx-auto text-center" data-reveal>
        <span class="section-label">Connect</span>
        <h2 class="section-title">Start as solo / household</h2>
        <p class="section-subtitle mx-auto">
          Tell us the subject, your constraints, and what good looks like. No outcome guarantees — we build the runway; you own the run.
        </p>
        <a href="/#contact" class="btn-primary mt-6 inline-flex">Talk with us on the main site →</a>
        <p class="mt-6 text-sm text-ink-muted"><a href="/enterprise/" class="accent-dojo hover:underline">Looking for teams / Dojo? Enterprise path →</a></p>
      </div>
    </section>
'''

ENT_BODY = r'''
    <section class="relative pt-24 md:pt-28 section-padding section-charcoal">
      <div class="max-w-3xl mx-auto text-center" data-reveal>
        <span class="section-label !text-[#12355c]">Enterprise pathway</span>
        <h1 class="section-title">Teams &amp; institutions · pressure that stays honest</h1>
        <p class="section-subtitle mx-auto">
          Custom maps and scenarios on <em>your</em> standards. <span class="text-ink-soft">Dojo</span> for messy, timed work —
          not Gym cosplay. Teams primary; partners as a motion for honest reads from engagement libraries.
        </p>
        <div class="flex flex-col sm:flex-row gap-3 justify-center mt-8">
          <a href="#dojo" class="btn-primary">See the Dojo</a>
          <a href="/solo/" class="btn-secondary">Solo path →</a>
        </div>
      </div>
    </section>

    <section id="enemy" class="section-padding relative">
      <div class="max-w-3xl mx-auto text-center" data-reveal>
        <span class="section-label">The problem</span>
        <h2 class="section-title">Seat-time theater isn’t readiness</h2>
        <p class="mt-6 text-ink-muted leading-relaxed">
          A wall of certificates says what someone finished — not how they handle half-finished work on a clock.
          Teams need maps on real standards, packs that match the map, and scenarios from real engagement pressure.
        </p>
      </div>
    </section>

    <section id="loop" class="section-padding relative section-charcoal">
      <div class="max-w-5xl mx-auto">
        <div class="text-center max-w-3xl mx-auto mb-12" data-reveal>
          <span class="section-label">How it works</span>
          <h2 class="section-title">Learn · Practice · Save · Dojo</h2>
        </div>
        <div class="grid md:grid-cols-2 gap-6" data-reveal>
          <article class="glass-card card-border-map p-6 md:p-8">
            <span class="font-mono text-xs uppercase tracking-[0.2em] text-[#5c4a0c]">Learn</span>
            <h3 class="font-display text-xl font-semibold text-ink mt-3">Maps on your standards</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Custom or adapted dense maps for roles and curricula you define —
              same Learn discipline, not a catalog dump.
            </p>
          </article>
          <article class="glass-card card-border-practice p-6 md:p-8">
            <span class="font-mono text-xs uppercase tracking-[0.2em] text-[#145032]">Practice</span>
            <h3 class="font-display text-xl font-semibold text-ink mt-3">Packs from the same map</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Honest closed-notes work aimed at team standards and real gaps —
              one map, many packs.
            </p>
          </article>
          <article class="glass-card card-border-save p-6 md:p-8">
            <span class="font-mono text-xs uppercase tracking-[0.2em] text-[#6e1818]">Save</span>
            <h3 class="font-display text-xl font-semibold text-ink mt-3">Continuity across calendars</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Cohort and calendar interruptibility — clean handoffs so ramps don’t die in chat history.
            </p>
          </article>
          <article id="dojo" class="glass-card card-border-dojo p-6 md:p-8">
            <span class="font-mono text-xs uppercase tracking-[0.2em] accent-dojo">Dojo · Enterprise only</span>
            <h3 class="font-display text-xl font-semibold text-ink mt-3">Deliver it when it’s messy</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Scenario packs from real work — half-finished, on a clock, something at stake.
              Structured observation of judgment under pressure —
              <strong class="text-ink">not</strong> a hiring decision, pass credential, or client-ready guarantee.
              <strong class="text-ink">Not the Gym.</strong> Gym is the Solo training-wheels floor.
            </p>
          </article>
        </div>
      </div>
    </section>

    <section id="content" class="section-padding relative">
      <div class="max-w-3xl mx-auto text-center" data-reveal>
        <span class="section-label">Content</span>
        <h2 class="section-title">Custom maps &amp; scenarios</h2>
        <p class="section-subtitle mx-auto">
          Built against your roles, SOPs, and engagement libraries — SOW-scoped, client-owned success criteria.
        </p>
      </div>
    </section>

    <section id="partners" class="section-padding relative section-charcoal">
      <div class="max-w-3xl mx-auto text-center" data-reveal>
        <span class="section-label !text-[#12355c]">Partners · motion</span>
        <h2 class="section-title">Honest reads — not partner theater</h2>
        <p class="section-subtitle mx-auto">
          If scenario libraries are built from <em>your</em> real engagement work, Dojo can give (and you can give)
          a structured view of thought and action under pressure.
          Not a white-label logo program. Not affiliation cosplay. Not equal to the Solo home door.
        </p>
      </div>
    </section>

    <section id="product" class="section-padding relative border-t border-ink/10">
      <div class="max-w-3xl mx-auto text-center" data-reveal>
        <span class="section-label">Product</span>
        <h2 class="section-title">Where the loop runs</h2>
        <p class="section-subtitle mx-auto">Same loop surfaces — configured for team and institution delivery.</p>
        <a href="/#product" class="btn-secondary mt-6 inline-flex">Open full product gallery on home →</a>
      </div>
    </section>

    <section id="contact" class="section-padding relative">
      <div class="max-w-xl mx-auto text-center" data-reveal>
        <span class="section-label">Connect</span>
        <h2 class="section-title">Request a team / institution briefing</h2>
        <p class="section-subtitle mx-auto">
          Outcomes and employment decisions stay yours. We structure maps, packs, and Dojo observation inside a written SOW.
        </p>
        <a href="/#contact" class="btn-primary mt-6 inline-flex">Talk with us on the main site →</a>
        <p class="mt-6 text-sm text-ink-muted"><a href="/solo/" class="accent-map hover:underline">Looking for solo / Gym? Solo path →</a></p>
      </div>
    </section>
'''

(root / "solo").mkdir(exist_ok=True)
(root / "enterprise").mkdir(exist_ok=True)
(root / "solo" / "index.html").write_text(
    page(
        "Solo pathway — The Cognition Factory",
        "Adult learners: productized cores, Gym when needed, Learn · Practice · Save place. You own the outcome.",
        "solo",
        SOLO_BODY,
    ),
    encoding="utf-8",
)
(root / "enterprise" / "index.html").write_text(
    page(
        "Enterprise pathway — The Cognition Factory",
        "Teams and institutions: custom maps, Dojo scenarios, Learn · Practice · Save place. Partners as motion.",
        "enterprise",
        ENT_BODY,
    ),
    encoding="utf-8",
)
print("wrote solo/index.html and enterprise/index.html")
