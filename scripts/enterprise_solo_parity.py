# -*- coding: utf-8 -*-
"""Enterprise slug: solo-parity first pass (header/footer/hero cue/depth/contact)."""
from pathlib import Path
import re

path = Path(__file__).resolve().parents[1] / "enterprise" / "index.html"
text = path.read_text(encoding="utf-8")

# ── 1) Head CSS: replace pathway-hero-copy block with solo-style suite ──
old_css = """    .pathway-hero-copy {
      background: #e8eaee;
    }
    .pathway-hero-copy .section-label {
      display: inline-block;
    }

    /* Product platform readiness — icon row, not prose */"""

new_css = r"""    /* Copy band uses .band-charcoal (foot CSS) — same dark field as main/solo */
    .pathway-hero-copy {
      background: transparent;
    }
    .pathway-hero-copy .section-label {
      display: inline-block;
    }
    .pathway-hero-copy.band-charcoal {
      margin-top: 0;
    }

    /*
     * Enterprise nav — plain CSS gaps (Tailwind content scan historically
     * missed utilities only used on slug pages).
     */
    #main-nav .ent-nav-desktop {
      display: none;
      align-items: center;
      flex-wrap: nowrap;
      flex-shrink: 0;
      gap: 1.75rem;
    }
    @media (min-width: 1024px) {
      #main-nav .ent-nav-desktop {
        display: flex;
      }
    }
    @media (min-width: 1280px) {
      #main-nav .ent-nav-desktop {
        gap: 2rem;
      }
    }
    #main-nav .ent-nav-desktop .nav-link {
      white-space: nowrap;
      flex-shrink: 0;
    }
    #main-nav .ent-nav-desktop .btn-primary {
      flex-shrink: 0;
      white-space: nowrap;
    }
    #main-nav .brand-wordmark-full {
      display: none;
      font-family: "Space Grotesk", system-ui, sans-serif;
      font-weight: 600;
      font-size: 0.875rem;
      letter-spacing: -0.025em;
      color: #000;
      border-left: 1px solid rgba(0, 0, 0, 0.1);
      padding-left: 0.75rem;
      white-space: nowrap;
    }
    #main-nav .brand-wordmark-ent {
      display: none;
      font-family: "JetBrains Mono", ui-monospace, monospace;
      font-size: 0.65rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #555;
      border-left: 1px solid rgba(0, 0, 0, 0.1);
      padding-left: 0.75rem;
      white-space: nowrap;
      flex-shrink: 0;
    }
    @media (min-width: 640px) {
      #main-nav .brand-wordmark-ent {
        display: block;
      }
    }
    @media (min-width: 1280px) {
      #main-nav .brand-wordmark-full {
        display: block;
      }
      #main-nav .brand-wordmark-ent {
        display: none;
      }
    }

    /* Hero scroll cue — top-center of banner stage */
    .pathway-hero .hero-banner-plate {
      position: relative;
    }
    .hero-scroll-cue {
      position: absolute;
      left: 50%;
      top: 1rem;
      bottom: auto;
      z-index: 20;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 2.75rem;
      height: 2.75rem;
      margin: 0;
      padding: 0;
      border: 1.5px solid rgba(255, 255, 255, 0.65);
      border-radius: 999px;
      background: rgba(25, 28, 34, 0.72);
      color: #ffffff;
      box-shadow:
        0 0 0 1px rgba(0, 0, 0, 0.25),
        0 8px 24px rgba(0, 0, 0, 0.35),
        0 0 28px rgba(43, 95, 158, 0.35);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      transform: translateX(-50%);
      transition: opacity 0.35s ease, visibility 0.35s ease, background 0.2s ease;
      animation: hero-scroll-cue-bob 1.9s ease-in-out infinite;
    }
    .hero-scroll-cue:hover,
    .hero-scroll-cue:focus-visible {
      background: rgba(25, 28, 34, 0.9);
      border-color: #ffffff;
      color: #ffffff;
      outline: none;
    }
    .hero-scroll-cue:focus-visible {
      box-shadow: 0 0 0 2px #e8eaee, 0 0 0 4px #2b5f9e;
    }
    .hero-scroll-cue svg {
      width: 1.35rem;
      height: 1.35rem;
      display: block;
    }
    .hero-scroll-cue.is-hidden {
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      animation: none;
    }
    @keyframes hero-scroll-cue-bob {
      0%, 100% { transform: translateX(-50%) translateY(0); opacity: 0.9; }
      50% { transform: translateX(-50%) translateY(0.4rem); opacity: 1; }
    }
    @media (prefers-reduced-motion: reduce) {
      .hero-scroll-cue {
        animation: none;
        opacity: 0.95;
      }
    }
    @media (max-width: 767px) {
      .hero-scroll-cue {
        top: 0.75rem;
        width: 2.5rem;
        height: 2.5rem;
      }
    }

    /* Product platform readiness — icon row, not prose */"""

if old_css not in text:
    raise SystemExit("head CSS marker not found")
text = text.replace(old_css, new_css, 1)

# Footer CSS
if "footer .footer-sitemap" not in text:
    text = text.replace(
        "    footer {\n      background: #ffffff;\n    }",
        """    footer {
      background: #ffffff;
    }
    footer .footer-sitemap {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;
      column-gap: 1.25rem;
      row-gap: 0.5rem;
    }
    footer .footer-sitemap a {
      color: #555555;
      font-size: 0.875rem;
      line-height: 1.25rem;
      white-space: nowrap;
      transition: color 0.15s ease;
    }
    footer .footer-sitemap a:hover {
      color: #3b6f9e;
    }""",
        1,
    )

# Surface cards on charcoal (for contact)
if ".band-charcoal .surface-card .text-ink" not in text:
    mark = (
        "    .band-charcoal a.text-electric:hover {\n"
        "      color: #c5daf0 !important;\n"
        "    }"
    )
    surface = """
    .band-charcoal .surface-card {
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.28);
    }
    .band-charcoal .surface-card .text-ink,
    .band-charcoal .surface-card .text-ink-muted,
    .band-charcoal .surface-card .text-ink-soft {
      color: #000000 !important;
    }
    .band-charcoal a.accent-map {
      color: #d4b06a !important;
    }
    .band-charcoal a.accent-map:hover {
      color: #e8c97a !important;
    }
    .band-charcoal a.text-ink:hover {
      color: #9ec0e0 !important;
    }
"""
    if mark in text:
        text = text.replace(mark, mark + "\n" + surface, 1)

# ── 2) Header HTML ──
old_header = """          <a href="/" class="flex items-center gap-3 group min-w-0" aria-label="The Cognition Factory — Home">
            <img src="/assets/images/brand/tcf-mark-cf-charcoal-light.jpg?v=brand-exp19" alt="" class="brand-nav-mark shrink-0" width="40" height="40" />
            <span class="font-display font-semibold text-ink text-sm md:text-base tracking-tight hidden sm:block border-l border-ink/10 pl-3 truncate">The Cognition Factory</span>
          </a>
          <div class="hidden lg:flex items-center gap-6 shrink-0">
            <a href="/#pathways" class="nav-link">Pathways</a>
            <a href="/solo/" class="nav-link">Solo</a>
            <a href="/enterprise/" class="nav-link text-electric">Enterprise</a>
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
  </header>"""

new_header = """          <a href="/" class="flex items-center gap-3 group min-w-0" aria-label="The Cognition Factory — Home">
            <img src="/assets/images/brand/tcf-mark-cf-charcoal-light.jpg?v=brand-exp19" alt="" class="brand-nav-mark shrink-0" width="40" height="40" />
            <span class="brand-wordmark-full">The Cognition Factory</span>
            <span class="brand-wordmark-ent">Enterprise</span>
          </a>
          <div class="ent-nav-desktop" data-nav-context="enterprise">
            <a href="#enemy" class="nav-link" data-nav>Problem</a>
            <a href="#loop" class="nav-link" data-nav>How</a>
            <a href="#product" class="nav-link" data-nav>Product</a>
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
          <div class="site-chrome-inner py-6 flex flex-col gap-4" data-nav-context="enterprise">
            <p class="font-mono text-[0.65rem] uppercase tracking-[0.2em] text-ink-muted">Enterprise pathway</p>
            <a href="#enemy" class="nav-link py-2" data-nav>Problem</a>
            <a href="#loop" class="nav-link py-2" data-nav>How it works</a>
            <a href="#product" class="nav-link py-2" data-nav>Product</a>
            <a href="#contact" class="btn-primary text-center mt-2">Talk with us</a>
            <div class="border-t border-ink/10 pt-4 mt-2 flex flex-col gap-3">
              <a href="/" class="nav-link py-1" style="opacity:0.72">Home · pathways</a>
              <a href="/solo/" class="nav-link py-1" style="opacity:0.72">Solo path →</a>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </header>"""

if old_header not in text:
    raise SystemExit("header HTML not found")
text = text.replace(old_header, new_header, 1)

# ── 3) Hero: scroll cue + charcoal copy ──
old_hero_end = """          </div>

      </div>

      <div class="pathway-hero-copy section-padding !pt-12 md:!pt-16 !pb-14 md:!pb-16">
        <div class="max-w-3xl mx-auto text-center" data-reveal>
          <span class="section-label !text-[#12355c]">Enterprise pathway</span>"""

# Find marquee close more flexibly
hero_cue = """
            <!-- On-stage scroll nudge -->
            <a
              href="#enterprise-intro"
              class="hero-scroll-cue"
              data-hero-scroll-cue
              aria-label="Scroll down past the banner"
            >
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M6 9l6 6 6-6" />
              </svg>
            </a>
          </div>
        </div>

          <div class="hero-marquee" aria-hidden="true">"""

# Insert cue inside stage after video figure closes - look for stage structure
# Enterprise has: banner-plate > stage > slides > figure video
# After slides closing, before stage close - insert cue

stage_insert_marker = """              </figure>
            </div>
          </div>
        </div>

          <div class="hero-marquee" aria-hidden="true">"""

stage_with_cue = """              </figure>
            </div>
            <a
              href="#enterprise-intro"
              class="hero-scroll-cue"
              data-hero-scroll-cue
              aria-label="Scroll down past the banner"
            >
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M6 9l6 6 6-6" />
              </svg>
            </a>
          </div>
        </div>

          <div class="hero-marquee" aria-hidden="true">"""

if stage_insert_marker not in text:
    raise SystemExit("hero stage marker not found for scroll cue")
text = text.replace(stage_insert_marker, stage_with_cue, 1)

text = text.replace(
    '<div class="pathway-hero-copy section-padding !pt-12 md:!pt-16 !pb-14 md:!pb-16">',
    '<div id="enterprise-intro" class="pathway-hero-copy band-charcoal section-padding !pt-12 md:!pt-16 !pb-14 md:!pb-16">',
    1,
)

# ── 4) Depth: reorder Save before Dojo + reformat both ──
depth_start = text.find(
    "    <!-- ═══════════════════════════════════════════════════════════\n"
    "         DEPTH — Learn · Practice · Dojo · Save"
)
if depth_start < 0:
    depth_start = text.find("DEPTH — Learn · Practice · Dojo · Save")
    depth_start = text.rfind("    <!--", 0, depth_start)

content_end = text.find('    </div><!-- /#content.slug-depth -->')
if depth_start < 0 or content_end < 0:
    raise SystemExit(f"depth bounds fail {depth_start} {content_end}")

# Keep map + aae from existing, rebuild save + dojo
# Extract map and aae by finding section ids
map_start = text.find('<section id="map"', depth_start)
aae_start = text.find('<section id="aae"', depth_start)
dojo_start = text.find('<section id="dojo"', depth_start)
platform_start = text.find('<section id="platform"', depth_start)

# end of aae is dojo_start
map_aae = text[map_start:dojo_start]

# Fix map chain CTA if missing - add after map ul close if needed
if 'href="#aae"' not in map_aae:
    map_aae = map_aae.replace(
        """            </ul>
          </div>
        </div>
      </div>
    </section>""",
        """            </ul>

            <p class="mt-8 font-mono text-xs uppercase tracking-[0.2em] text-ink-muted">
              Learn builds the map
            </p>
            <a href="#aae" class="inline-flex items-center gap-1 text-sm font-medium mt-5 hover:gap-2 transition-all" style="color:#5c4a0c">
              Then prove it in Practice
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </a>
          </div>
        </div>
      </div>
    </section>""",
        1,
    )

# Fix practice CTA: dojo → platform (save)
map_aae = map_aae.replace(
    """            <p class="mt-8 font-mono text-xs uppercase tracking-[0.2em] text-ink-muted">
              Learn builds the map · Practice proves
            </p>
            <a href="#dojo" class="inline-flex items-center gap-1 text-sm font-medium mt-5 hover:gap-2 transition-all" style="color:#145032">
              Then step into the Dojo
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </a>""",
    """            <p class="mt-8 font-mono text-xs uppercase tracking-[0.2em] text-ink-muted">
              Learn builds the map · Practice proves
            </p>
            <a href="#platform" class="inline-flex items-center gap-1 text-sm font-medium mt-5 hover:gap-2 transition-all" style="color:#145032">
              Then save your place
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </a>""",
    1,
)

# Fix door-copy-body indent on aae if messy
map_aae = map_aae.replace(
    "</div>\n<div class=\"door-copy-body mt-6\" data-reveal>",
    '</div>\n          <div class="door-copy-body mt-6" data-reveal>',
)

save_section = r'''
    <section id="platform" class="section-padding relative section-charcoal">
      <div class="absolute inset-0 bg-gradient-to-b from-transparent via-electric/[0.02] to-transparent pointer-events-none" aria-hidden="true"></div>
      <div class="max-w-7xl mx-auto relative">
        <div class="max-w-3xl mx-auto">
          <div class="door-copy-head" data-reveal>
            <span class="section-label !text-[#6e1818]">Save</span>
            <h2 class="section-title">Pick up where you left off</h2>
            <p class="font-mono text-sm mt-2 text-[#c45a5a]">Clean handoff · not re-scroll the chat</p>
          </div>
          <div class="door-copy-body mt-6" data-reveal>
            <p class="text-ink font-medium text-lg">
              For calendars that <em>interrupt</em> — not perfect study streaks.
            </p>
            <p class="mt-4 text-ink-muted leading-relaxed">
              Not a chat archive. Not another app to babysit.
              <span class="text-ink-soft">Save place</span> is how you leave a clean handoff for tomorrow —
              whether a learner was in Learn, mid Practice, or between cohort sessions.
              Long sessions break. Apps forget. People get called away.
              If your notes die when the chat ends, you do not have a system — you have a mood.
              The loop still holds: a named next step, not a scroll hunt.
            </p>

            <p class="text-xs font-mono uppercase tracking-wider text-ink-muted mt-10 mb-4">What it does</p>
            <ul class="space-y-4">
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-save">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Leave a clean stop</h3>
                  <p class="text-ink-muted text-sm mt-1">Capture where the cohort was and what still feels fuzzy — enough that restarting is intentional.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-save">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Name the next step</h3>
                  <p class="text-ink-muted text-sm mt-1">Deeper map work, more practice, or a real check — so the next sitting is not a guess.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-save">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Continuity across calendars</h3>
                  <p class="text-ink-muted text-sm mt-1">Cohort and calendar interruptibility — ramps do not die in chat history.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-orient">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Stay oriented</h3>
                  <p class="text-ink-muted text-sm mt-1">Quiet layer under save place: where the team is on the map, when open study should become honest practice — not another portal.</p>
                </div>
              </li>
            </ul>

            <p class="mt-8 font-mono text-xs uppercase tracking-[0.2em] text-ink-muted">
              Learn builds the map · Practice proves · Save place keeps the loop
            </p>
            <a href="#dojo" class="inline-flex items-center gap-1 text-sm font-medium mt-5 hover:gap-2 transition-all" style="color:#6e1818">
              When pressure is real — the Dojo
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </a>
          </div>
        </div>
      </div>
    </section>


    <section id="dojo" class="section-padding relative section-charcoal">
      <div class="absolute inset-0 pointer-events-none" style="background: linear-gradient(to bottom, transparent, rgba(43,95,158,0.06), transparent)" aria-hidden="true"></div>
      <div class="max-w-7xl mx-auto relative">
        <div class="max-w-3xl mx-auto">
          <div class="door-copy-head" data-reveal>
            <span class="section-label !text-[#12355c]">Dojo · Enterprise only</span>
            <h2 class="section-title">Deliver it when it’s messy</h2>
            <p class="font-mono text-sm mt-2 text-[#12355c]">Real scenarios · not another quiz</p>
          </div>
          <div class="door-copy-body mt-6" data-reveal>
            <p class="text-ink font-medium text-lg">
              For skills you need to <em>use</em> — not just pass.
            </p>
            <p class="mt-4 text-ink-muted leading-relaxed">
              Practice checks what you know. The <span class="text-ink-soft">Dojo</span> puts that skill into
              messy, timed scenarios — half-finished work, something at stake — so you can see how the call
              holds under pressure. Structured observation of judgment, not a hiring decision or certification.
              Same factory as Learn and Practice — the Dojo tests what you actually built.
              <strong class="text-ink">Not the Gym</strong> — Gym is the Solo training-wheels floor.
            </p>

            <p class="text-xs font-mono uppercase tracking-wider text-ink-muted mt-10 mb-4">What it does</p>
            <ul class="space-y-4">
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-dojo">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Messy cases on a clock</h3>
                  <p class="text-ink-muted text-sm mt-1">Half-finished work, something at stake — pressure that looks like the job, not a quiz timer.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-dojo">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Structured observation</h3>
                  <p class="text-ink-muted text-sm mt-1">See how the call holds — not a placement guarantee, pass credential, or client-ready stamp.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-dojo">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Packs from real work</h3>
                  <p class="text-ink-muted text-sm mt-1">Late invoice, three docs that disagree, a dump that must become a plan — flavor of the messy case, not the answer key.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-dojo">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Same map underneath</h3>
                  <p class="text-ink-muted text-sm mt-1">Scenario packs built from the same map as Learn and Practice — no trick questions from nowhere.</p>
                </div>
              </li>
            </ul>

            <p class="mt-8 font-mono text-xs uppercase tracking-[0.2em] text-[#12355c]">
              Practice asks “do you know it?” · The Dojo asks “can you work the messy case?”
            </p>
            <a href="#partners" class="inline-flex items-center gap-1 text-sm font-medium mt-5 hover:gap-2 transition-all" style="color:#12355c">
              Partners as motion
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </a>
          </div>
        </div>
      </div>
    </section>

'''

depth_header = """    <!-- ═══════════════════════════════════════════════════════════
         DEPTH — Learn · Practice · Save · Dojo (no brand door marks)
         ═══════════════════════════════════════════════════════════ -->
    <div id="content" class="slug-depth">
"""

new_depth = depth_header + map_aae.rstrip() + "\n\n" + save_section + "\n    </div><!-- /#content.slug-depth -->"

text = text[:depth_start] + new_depth + text[content_end + len("    </div><!-- /#content.slug-depth -->") :]

# ── 5) Contact charcoal ──
text = text.replace(
    """    <section id="contact" class="section-padding relative">
      <div class="absolute inset-0 bg-gradient-to-t from-electric/[0.03] to-transparent pointer-events-none" aria-hidden="true"></div>""",
    """    <section id="contact" class="section-padding relative band-charcoal">
      <div class="absolute inset-0 pointer-events-none" aria-hidden="true"></div>""",
    1,
)

# ── 6) Footer ──
old_footer_links = None
# find footer site map
m = re.search(
    r'(<div class="flex flex-wrap items-center justify-center gap-6" aria-label="Site map">)(.*?)(</div>)',
    text,
    re.S,
)
if m:
    text = (
        text[: m.start()]
        + """          <div class="footer-sitemap" aria-label="Site map">
            <a href="#enemy">Problem</a>
            <a href="#loop">How it works</a>
            <a href="#product">Product</a>
            <a href="#contact">Talk with us</a>
            <a href="/">Home</a>
            <a href="/solo/">Solo</a>
          </div>"""
        + text[m.end() :]
    )
else:
    # try simpler
    print("WARN: footer site map pattern not exact; trying alternate")
    if 'aria-label="Site map"' in text:
        # manual
        start = text.find('aria-label="Site map"')
        div_start = text.rfind("<div", 0, start)
        div_end = text.find("</div>", start) + len("</div>")
        text = (
            text[:div_start]
            + """          <div class="footer-sitemap" aria-label="Site map">
            <a href="#enemy">Problem</a>
            <a href="#loop">How it works</a>
            <a href="#product">Product</a>
            <a href="#contact">Talk with us</a>
            <a href="/">Home</a>
            <a href="/solo/">Solo</a>
          </div>"""
            + text[div_end:]
        )
    else:
        raise SystemExit("footer site map not found")

# ── 7) main.js cache ──
text = text.replace(
    'src="/js/main.js?v=contact-slugs1"',
    'src="/js/main.js?v=main-nav1"',
    1,
)

path.write_text(text, encoding="utf-8")

# Verify
ids = re.findall(r'<section id="([^"]+)"', path.read_text(encoding="utf-8"))
print("sections:", ids)
assert "dojo" in ids and "platform" in ids
# order: platform before dojo in depth
plat = text.find('id="platform"')
doj = text.find('id="dojo"')
assert plat < doj, "Save should precede Dojo"
assert 'band-charcoal' in text and 'data-hero-scroll-cue' in text
assert "ent-nav-desktop" in text
assert 'id="contact" class="section-padding relative band-charcoal"' in text
print("ok enterprise solo parity")
