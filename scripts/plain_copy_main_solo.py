# -*- coding: utf-8 -*-
"""Plain business English copy pass — main + solo (not enterprise)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════
main = (ROOT / "index.html").read_text(encoding="utf-8")

main_swaps = [
    (
        'content="Skill that sticks when life is loud. Learn. Practice. Save your place. For busy adults and teams — not seat-time theater."',
        'content="Skill that sticks when life is loud. Learn. Practice. Save your place. For busy adults and teams — not hours logged for show."',
    ),
    (
        """            <p class="text-ink font-semibold mt-2 text-center group-hover:underline">Productized cores &amp; carts</p>
            <p class="text-ink-muted text-sm mt-2 text-center">Hosted starter set — Accounting, SCM, and more as they ship.</p>""",
        """            <p class="text-ink font-semibold mt-2 text-center group-hover:underline">Ready-to-start courses</p>
            <p class="text-ink-muted text-sm mt-2 text-center">A clear starter set — Accounting, supply chain, and more as they ship.</p>""",
    ),
    (
        'aria-label="Solo pathway — productized cores and carts"',
        'aria-label="Solo pathway — ready-to-start courses"',
    ),
    (
        """            <p class="text-ink font-semibold mt-2 text-center group-hover:underline">Custom maps &amp; scenarios</p>
            <p class="text-ink-muted text-sm mt-2 text-center">Fitted to your roles, standards, and engagement libraries.</p>""",
        """            <p class="text-ink font-semibold mt-2 text-center group-hover:underline">Maps built for your work</p>
            <p class="text-ink-muted text-sm mt-2 text-center">Built around your roles, your standards, and the real work your people do.</p>""",
    ),
    (
        """            <p class="text-ink-muted text-sm mt-4 leading-relaxed flex-1">
              Productized dense cores and practice packs. <span class="text-ink-soft">Gym</span> when a vertical needs training wheels —
              interruptible weeks, clean save place, you own the outcome.
            </p>
            <ul class="mt-6 space-y-2 text-sm text-ink-muted">
              <li class="flex gap-2"><span class="accent-map shrink-0" aria-hidden="true">·</span><span>Hosted cores &amp; carts</span></li>
              <li class="flex gap-2"><span class="accent-map shrink-0" aria-hidden="true">·</span><span>Gym (conditional) · not Dojo</span></li>
              <li class="flex gap-2"><span class="accent-map shrink-0" aria-hidden="true">·</span><span>Low-touch SaaS path</span></li>
            </ul>""",
        """            <p class="text-ink-muted text-sm mt-4 leading-relaxed flex-1">
              Ready courses and honest practice you can start from. When a subject needs a safe place to try the real tool,
              the <span class="text-ink-soft">Gym</span> is there — for weeks that get interrupted, with a clear place to stop and pick up.
              You own the result.
            </p>""",
    ),
    (
        """            <p class="text-ink-muted text-sm mt-4 leading-relaxed flex-1">
              Custom maps and packs on <em>your</em> standards. <span class="text-ink-soft">Dojo</span> for pressure scenarios —
              teams primary; partners as a motion for honest reads from engagement libraries.
            </p>
            <ul class="mt-6 space-y-2 text-sm text-ink-muted">
              <li class="flex gap-2"><span class="accent-dojo shrink-0" aria-hidden="true">·</span><span>Custom cores &amp; scenarios</span></li>
              <li class="flex gap-2"><span class="accent-dojo shrink-0" aria-hidden="true">·</span><span>Dojo · not Gym cosplay</span></li>
              <li class="flex gap-2"><span class="accent-dojo shrink-0" aria-hidden="true">·</span><span>Implementation · hypercare path</span></li>
            </ul>""",
        """            <p class="text-ink-muted text-sm mt-4 leading-relaxed flex-1">
              Maps and practice packs built on <em>your</em> standards. The <span class="text-ink-soft">Dojo</span> is for messy, timed cases —
              for teams first. Partners may join when real work under pressure needs an honest read, not a logo on the wall.
            </p>""",
    ),
    (
        """            <h3 class="font-display text-xl font-semibold text-ink mt-2">Clean handoff</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed flex-1">
              Leave a clear next step when life interrupts — not re-scroll the chat.
            </p>""",
        """            <h3 class="font-display text-xl font-semibold text-ink mt-2">Leave a clear stop</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed flex-1">
              When life interrupts, leave a clear next step — not an hour of re-scrolling old chat.
            </p>""",
    ),
    (
        """        <p class="max-w-2xl mx-auto text-center text-ink-muted text-sm mt-10 leading-relaxed" data-reveal>
          <span class="text-ink-soft">Solo</span> adds <span class="text-ink-soft">Gym</span> when a vertical needs training wheels.
          <span class="text-ink-soft">Enterprise</span> adds <span class="text-ink-soft">Dojo</span> for messy, timed scenarios —
          same factory, different floor.
        </p>""",
        """        <p class="max-w-2xl mx-auto text-center text-ink-muted text-sm mt-10 leading-relaxed" data-reveal>
          <span class="text-ink-soft">Solo</span> adds the <span class="text-ink-soft">Gym</span> when a subject needs a safe place to try the real work.
          <span class="text-ink-soft">Enterprise</span> adds the <span class="text-ink-soft">Dojo</span> for messy, timed cases —
          same system, different floor.
        </p>""",
    ),
    (
        """              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                After the map and the quiz, some skills need a form and a stage.
                Thin, Dynamics-shaped practice — not a Microsoft product, not full ERP theater.
                Cohorts without volumetric enterprise seats use the same floor until the click order is boring.
              </p>""",
        """              <p class="text-ink-muted text-sm mt-3 leading-relaxed">
                After the map and the quiz, some skills need a form and a stage.
                Practice that looks like the real process — without pretending to be the full enterprise system.
                Teams use the same floor until the click path is familiar and calm.
              </p>""",
    ),
    (
        """            and a clean handoff when life interrupts. One loop for busy adults and teams
            who need skill that sticks under real life, not short-term scores.""",
        """            and a clear place to stop when life interrupts. One loop for busy adults and teams
            who need skill that still works under real life, not short-term scores.""",
    ),
    (
        """              <ul class="space-y-2.5 text-sm text-ink-muted leading-relaxed list-none">
                <li class="flex gap-2"><span class="accent-map shrink-0" aria-hidden="true">·</span><span>Give structure: Learn (build the map), honest practice, a clean place to park when life interrupts.</span></li>
                <li class="flex gap-2"><span class="accent-practice shrink-0" aria-hidden="true">·</span><span>Align study lanes to public pathways and published skill lists — so the work stays legible.</span></li>
                <li class="flex gap-2"><span class="accent-save shrink-0" aria-hidden="true">·</span><span>Say when we are not a fit, instead of stretching the offer.</span></li>
                <li class="flex gap-2"><span class="accent-dojo shrink-0" aria-hidden="true">·</span><span>Leave dedication and results with you. We build the runway; you own the run.</span></li>
              </ul>""",
        """              <div class="space-y-3 text-sm text-ink-muted leading-relaxed">
                <p>We give structure: Learn to build the map, honest practice, and a clean place to park when life interrupts.</p>
                <p>We keep study paths clear and public where we can, so the work stays easy to follow.</p>
                <p>We say when we are not a fit, instead of stretching the offer.</p>
                <p>Dedication and results stay with you. We build the runway; you own the run.</p>
              </div>""",
    ),
    (
        """              <ul class="space-y-2.5 text-sm text-ink-muted leading-relaxed list-none">
                <li class="flex gap-2"><span class="text-ink-muted shrink-0" aria-hidden="true">·</span><span>Sell seat-time, completion theater, or a wall of badges as if that were skill.</span></li>
                <li class="flex gap-2"><span class="text-ink-muted shrink-0" aria-hidden="true">·</span><span>Play superhero: we won’t “fix” a career, a team, or a go-live from the outside.</span></li>
                <li class="flex gap-2"><span class="text-ink-muted shrink-0" aria-hidden="true">·</span><span>Promise a specific exam score, pass, job, or business result. Outcomes stay yours.</span></li>
                <li class="flex gap-2"><span class="text-ink-muted shrink-0" aria-hidden="true">·</span><span>Claim endorsement, partnership, or affiliation with any brand or logo. Path alignment is not a partnership badge.</span></li>
              </ul>""",
        """              <div class="space-y-3 text-sm text-ink-muted leading-relaxed">
                <p>We do not sell hours logged, completion badges, or a wall of certificates as if that were skill.</p>
                <p>We do not play superhero. We will not “fix” a career, a team, or a go-live from the outside.</p>
                <p>We do not promise a specific exam score, job, or business result. Outcomes stay yours.</p>
                <p>We do not claim endorsement or partnership with any brand or logo. Aligning to a public path is not a partnership badge.</p>
              </div>""",
    ),
    (
        """                <p class="text-sm text-ink leading-relaxed">Shared skill under real calendars — not seat-time LMS theater. Say the role and the constraint.</p>""",
        """                <p class="text-sm text-ink leading-relaxed">Shared skill under real calendars — not hours logged for show. Say the role and the constraint.</p>""",
    ),
    (
        """                <p class="text-sm text-ink leading-relaxed">Passive content binge, completion badges only, guaranteed-outcome shopping, or “AI tutor with no structure.” We will say no rather than cosplay — and we never sell someone else’s logo as our badge.</p>""",
        """                <p class="text-sm text-ink leading-relaxed">Passive content binge, badges only, guaranteed-result shopping, or an “AI tutor” with no structure. We will say no rather than stretch the offer — and we never sell someone else’s logo as our badge.</p>""",
    ),
    (
        """              <strong class="text-ink-muted">Support ritual:</strong> we take serious inquiries.
              Expect a reply within a few days when it is a fit — not 24/7 chat.
              App users: Help → Contact support for a private dump +""",
        """              <strong class="text-ink-muted">How we answer:</strong> we take serious inquiries.
              Expect a reply within a few days when it is a fit — not 24/7 chat.
              App users: Help → Contact support for a private dump +""",
    ),
    (
        """          of a cold start, with explicit neutral off-ramps when you are ready for the real thing.""",
        """          of a cold start, with a clean exit when you are ready for the real tool.""",
    ),
    (
        """            <p class="text-ink-soft text-sm leading-relaxed">Check yourself under honest pressure. Right or wrong is recorded without cosplay.</p>""",
        """            <p class="text-ink-soft text-sm leading-relaxed">Check yourself under honest pressure. Right or wrong is recorded without soft grading.</p>""",
    ),
    (
        """          Product screens on this site show the shell; your household run produces the real handoff.""",
        """          Product screens on this site show the shell; your own run produces the real next step when you stop and start again.""",
    ),
    (
        """            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Learn · practice · save place on a full screen — plus a thin workflow floor""",
        """            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Learn, practice, and save your place on a full screen — plus a simple practice floor""",
    ),
]

for a, b in main_swaps:
    if a not in main:
        print("MAIN MISS:", a[:80].replace("\n", " "))
    else:
        main = main.replace(a, b, 1)
        print("main ok:", a[:50].replace("\n", " "))

(ROOT / "index.html").write_text(main, encoding="utf-8")

# ═══════════════════════════════════════════════════════════════
# SOLO
# ═══════════════════════════════════════════════════════════════
solo = (ROOT / "solo" / "index.html").read_text(encoding="utf-8")

solo_swaps = [
    (
        'content="Adult learners: productized cores, Gym when needed, Learn · Practice · Save place. You own the outcome."',
        'content="Adult learners: ready courses, Gym when needed, Learn · Practice · Save place. You own the outcome."',
    ),
    (
        'content="Skill that sticks when life is loud. Learn. Practice. Save your place. For busy adults and teams — not seat-time theater."',
        'content="Skill that sticks when life is loud. Learn. Practice. Save your place. For busy adults — not hours logged for show."',
    ),
    (
        """            Productized cores and carts. <span class="text-ink-soft">Gym</span> when a vertical needs training wheels.
            Same factory as Enterprise — dialed for interruptible real life. You own the outcome.""",
        """            Ready courses you can start from. <span class="text-ink-soft">Gym</span> when a subject needs a safe place to try the real work.
            Same system as Enterprise — built for weeks that get interrupted. You own the outcome.""",
    ),
    (
        """              Dense micro-cores shaped like typical regionally accredited sequences — not affiliation claims.
              One idea until it clicks; productized starter set you can start from.""",
        """              Dense short courses shaped like common college sequences — not a claim of school endorsement.
              One idea until it clicks; a clear starter set you can begin from.""",
    ),
    (
        """            <h3 class="font-display text-xl font-semibold text-ink mt-3">Clean handoff</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Short sessions that still count. Leave where you were and what is next —
              not re-scroll the chat after kids, work, or a loud week.
            </p>""",
        """            <h3 class="font-display text-xl font-semibold text-ink mt-3">Leave a clear stop</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Short sessions that still count. Leave where you were and what is next —
              not an hour of re-scrolling chat after kids, work, or a loud week.
            </p>""",
    ),
    (
        """            <h3 class="font-display text-xl font-semibold text-ink mt-3">Training wheels, not Planet Fitness</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              Conditional thin environments when a vertical needs them — martial-arts-studio intentional tools,
              Kristi filter (no mockery, no injury), neutral off-ramps to real tools.
              <strong class="text-ink">Not the Dojo.</strong> Dojo is the Enterprise pressure floor.
            </p>""",
        """            <h3 class="font-display text-xl font-semibold text-ink mt-3">A safe place to try the real work</h3>
            <p class="text-ink-muted text-sm mt-3 leading-relaxed">
              When a subject needs it, thin practice tools shaped like the real job — intentional, not a warehouse of gadgets.
              Safe enough to try, honest enough to learn, with a clean exit when you are ready for the real tool.
              <strong class="text-ink">Not the Dojo.</strong> Dojo is the Enterprise pressure floor.
            </p>""",
    ),
    (
        """              Not a chatbot tutor. Not a content firehose.
              <span class="text-ink-soft">Learn</span> is where you build the map: write down what the subject is made of,
              what always holds true, and how pieces connect — then challenge the fuzzy spots until understanding sticks.
              You keep a living picture of the subject.
              When you are ready to prove it, <span class="text-ink-soft">Practice</span> uses that same map
              so teaching and testing stay on the same story.""",
        """              Not a chatbot tutor. Not a pile of videos to binge.
              <span class="text-ink-soft">Learn</span> is where you build the map: write down what the subject is made of,
              what always holds true, and how pieces connect — then challenge the fuzzy spots until understanding sticks.
              You keep a living picture of the subject.
              When you are ready to prove it, <span class="text-ink-soft">Practice</span> uses that same map
              so teaching and testing stay on the same story.""",
    ),
    (
        """              Not a comfort scoreboard. Not a random drill dump.
              <span class="text-ink-soft">Practice</span> shows the gap between recognizing material and being able to use it —
              then names what went wrong and aims the next run at those gaps until the skill holds.
              Practice packs are built for a clear goal — an exam, a job skill, a team standard —
              and always draw from the same map you built in <span class="text-ink-soft">Learn</span>.
              Same map; harder questions when it counts. One map can feed many packs.""",
        """              Not a comfort scoreboard. Not random drills dumped on the desk.
              <span class="text-ink-soft">Practice</span> shows the gap between recognizing material and being able to use it —
              then names what went wrong and aims the next run at those gaps until the skill holds.
              Practice packs are built for a clear goal — an exam, a job skill, a team standard —
              and always draw from the same map you built in <span class="text-ink-soft">Learn</span>.
              Same map; harder questions when it counts. One map can feed many packs.""",
    ),
    (
        """            <p class="font-mono text-sm mt-2 text-[#c45a5a]">Clean handoff · not re-scroll the chat</p>""",
        """            <p class="font-mono text-sm mt-2 text-[#c45a5a]">Clear stop · not re-scroll the chat</p>""",
    ),
    (
        """              <span class="text-ink-soft">Save place</span> is how you leave a clean handoff for tomorrow —
              whether you were in Learn or mid Practice.
              Long sessions break. Apps forget. People get called away.
              If your notes die when the chat ends, you do not have a system — you have a mood.
              The loop still holds: a named next step, not a scroll hunt.""",
        """              <span class="text-ink-soft">Save place</span> is how you leave a clear stop for tomorrow —
              whether you were in Learn or mid Practice.
              Long sessions break. Apps forget. People get called away.
              If your notes die when the chat ends, you do not have a system — you have a mood.
              The loop still holds: a named next step, not a scroll hunt.""",
    ),
    (
        """              When a vertical needs it — the Gym""",
        """              When a subject needs it — the Gym""",
    ),
    (
        """            <p class="font-mono text-sm mt-2 text-[#12355c]">Training wheels · not Planet Fitness</p>
          </div>
          <div class="door-copy-body mt-6" data-reveal>
            <p class="text-ink font-medium text-lg">
              For skills you need to <em>use</em> — not just pass.
            </p>
            <p class="mt-4 text-ink-muted leading-relaxed">
              Practice checks what you know. The <span class="text-ink-soft">Gym</span> is where a vertical
              gets intentional thin environments when it needs them — martial-arts-studio tools, not a machine warehouse.
              Kristi filter: training wheels, no mockery, no injury. Neutral off-ramps when you’re ready for the real tool.
              Same factory as Learn and Practice — the Gym only appears when the vertical needs it.
              <strong class="text-ink">Not the Dojo</strong> — Dojo is the Enterprise pressure floor.
            </p>

            <p class="text-xs font-mono uppercase tracking-wider text-ink-muted mt-10 mb-4">What it does</p>
            <ul class="space-y-4">
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-dojo">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Thin environments on purpose</h3>
                  <p class="text-ink-muted text-sm mt-1">Intentional tools shaped like the real work — studio, not warehouse. Only when the vertical needs them.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-dojo">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Training wheels, Kristi filter</h3>
                  <p class="text-ink-muted text-sm mt-1">No mockery, no injury. Safe enough to try; honest enough to build muscle memory.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-dojo">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Real-world shaped drills</h3>
                  <p class="text-ink-muted text-sm mt-1">The flavor of the messy case — late invoice, three docs that disagree, a dump that must become a plan — not the answer key.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-dojo">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Neutral off-ramps</h3>
                  <p class="text-ink-muted text-sm mt-1">When you’re ready for the real tool, step off cleanly — no cosplay floor for every subject.</p>
                </div>
              </li>
            </ul>

            <p class="mt-8 font-mono text-xs uppercase tracking-[0.2em] text-[#12355c]">
              Practice asks “do you know it?” · The Gym asks “can you try it with training wheels?”
            </p>""",
        """            <p class="font-mono text-sm mt-2 text-[#12355c]">Safe practice · not a gadget warehouse</p>
          </div>
          <div class="door-copy-body mt-6" data-reveal>
            <p class="text-ink font-medium text-lg">
              For skills you need to <em>use</em> — not just pass.
            </p>
            <p class="mt-4 text-ink-muted leading-relaxed">
              Practice checks what you know. The <span class="text-ink-soft">Gym</span> is where a subject
              gets thin practice tools when it needs them — shaped like the real work, not a warehouse of toys.
              Safe enough to try, honest enough to learn. A clean exit when you are ready for the real tool.
              Same system as Learn and Practice — the Gym only appears when the subject needs it.
              <strong class="text-ink">Not the Dojo</strong> — Dojo is the Enterprise pressure floor.
            </p>

            <p class="text-xs font-mono uppercase tracking-wider text-ink-muted mt-10 mb-4">What it does</p>
            <ul class="space-y-4">
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-dojo">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Thin tools on purpose</h3>
                  <p class="text-ink-muted text-sm mt-1">Intentional tools shaped like the real work — studio, not warehouse. Only when the subject needs them.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-dojo">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Safe enough to try</h3>
                  <p class="text-ink-muted text-sm mt-1">No mockery, no injury. Honest enough to build real habit.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-dojo">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Drills shaped like real work</h3>
                  <p class="text-ink-muted text-sm mt-1">The flavor of the messy case — late invoice, three docs that disagree, a dump that must become a plan — not the answer key.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-dojo">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">A clean exit to the real tool</h3>
                  <p class="text-ink-muted text-sm mt-1">When you are ready for the real system, step off cleanly — no fake floor for every subject.</p>
                </div>
              </li>
            </ul>

            <p class="mt-8 font-mono text-xs uppercase tracking-[0.2em] text-[#12355c]">
              Practice asks “do you know it?” · The Gym asks “can you try it safely?”
            </p>""",
    ),
    (
        """                Productized cores you can start from. One idea until it clicks —""",
        """                Ready courses you can start from. One idea until it clicks —""",
    ),
    (
        """                drill the gap, not the whole playlist. Gym when a vertical needs training wheels.""",
        """                drill the gap, not the whole playlist. Gym when a subject needs a safe place to try.""",
    ),
    (
        """          Gym and off-ramps stay neutral — no vendor logo theater.""",
        """          Gym and exits stay neutral — no vendor logo on the wall as if that were skill.""",
    ),
    (
        """                <p class="text-sm text-ink leading-relaxed">Busy adult or small home install — learn · practice · park on your machine. We point you at the right starting path.</p>""",
        """                <p class="text-sm text-ink leading-relaxed">Busy adult or small home setup — learn, practice, and park on your machine. We point you at the right starting path.</p>""",
    ),
    (
        """                <p class="text-sm text-ink leading-relaxed">Passive content binge, completion badges only, guaranteed-outcome shopping, or “AI tutor with no structure.” We will say no rather than cosplay.</p>""",
        """                <p class="text-sm text-ink leading-relaxed">Passive content binge, badges only, guaranteed-result shopping, or an “AI tutor” with no structure. We will say no rather than stretch the offer.</p>""",
    ),
    (
        """              <strong class="text-ink-muted">Support ritual:</strong> we take serious inquiries.
              Expect a reply within a few days when it is a fit — not 24/7 chat.""",
        """              <strong class="text-ink-muted">How we answer:</strong> we take serious inquiries.
              Expect a reply within a few days when it is a fit — not 24/7 chat.""",
    ),
]

for a, b in solo_swaps:
    if a not in solo:
        print("SOLO MISS:", a[:90].replace("\n", " "))
    else:
        solo = solo.replace(a, b, 1)
        print("solo ok:", a[:50].replace("\n", " "))

(ROOT / "solo" / "index.html").write_text(solo, encoding="utf-8")
print("done")
