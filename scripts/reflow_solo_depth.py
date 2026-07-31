# -*- coding: utf-8 -*-
"""Reorder solo depth Learn→Practice→Save→Gym; reformat Save/Gym like Learn/Practice."""
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "solo" / "index.html"
text = path.read_text(encoding="utf-8")

start_marker = "    <!-- ═══════════════════════════════════════════════════════════\n         DEPTH —"
end_marker = "    </div><!-- /#content.slug-depth -->"
start = text.find(start_marker)
end = text.find(end_marker)
if start < 0 or end < 0:
    raise SystemExit(f"markers not found start={start} end={end}")
end = end + len(end_marker)

new = r'''    <!-- ═══════════════════════════════════════════════════════════
         DEPTH — Learn · Practice · Save · Gym (no brand door marks)
         ═══════════════════════════════════════════════════════════ -->
    <div id="content" class="slug-depth">
    <section id="map" class="section-padding relative section-charcoal">
      <div class="absolute inset-0 bg-gradient-to-b from-transparent via-electric/[0.02] to-transparent pointer-events-none" aria-hidden="true"></div>

      <div class="max-w-7xl mx-auto relative">
        <div class="max-w-3xl mx-auto">
          <div class="door-copy-head" data-reveal>
            <span class="section-label !text-[#5c4a0c]">Learn</span>
            <h2 class="section-title">One idea until it clicks</h2>
            <p class="font-mono text-sm mt-2 text-[#d4b06a]">Build the map · not binge the playlist</p>
          </div>
          <div class="door-copy-body mt-6" data-reveal>
            <p class="text-ink font-medium text-lg">
              For subjects you need to <em>think through</em> — not just finish.
            </p>
            <p class="mt-4 text-ink-muted leading-relaxed">
              Not a chatbot tutor. Not a content firehose.
              <span class="text-ink-soft">Learn</span> is where you build the map: write down what the subject is made of,
              what always holds true, and how pieces connect — then challenge the fuzzy spots until understanding sticks.
              You keep a living picture of the subject.
              When you are ready to prove it, <span class="text-ink-soft">Practice</span> uses that same map
              so teaching and testing stay on the same story.
            </p>

            <p class="text-xs font-mono uppercase tracking-wider text-ink-muted mt-10 mb-4">What it does</p>
            <ul class="space-y-4">
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-map">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Clear maps</h3>
                  <p class="text-ink-muted text-sm mt-1">A picture of the ideas and how they link — structure you can keep and reuse.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-map">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">What always holds</h3>
                  <p class="text-ink-muted text-sm mt-1">Core principles that stay true — not just for one lesson.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-map">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Until you can use it without notes</h3>
                  <p class="text-ink-muted text-sm mt-1">Challenge fuzzy explanations until understanding sticks — not until a progress bar fills.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-map">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Skill that still works next month</h3>
                  <p class="text-ink-muted text-sm mt-1">Easy restarts so skill doesn’t quietly fade after a busy week.</p>
                </div>
              </li>
            </ul>

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
    </section>


    <section id="aae" class="section-padding relative section-charcoal">
      <div class="max-w-7xl mx-auto">
        <div class="max-w-3xl mx-auto">
          <div class="door-copy-head" data-reveal>
            <span class="section-label !text-[#145032]">Practice</span>
            <h2 class="section-title">Check what you know — honestly</h2>
            <p class="font-mono text-sm mt-2 text-[#145032]">Closed notes when it counts · not cruise the open book</p>
          </div>
          <div class="door-copy-body mt-6" data-reveal>
            <p class="text-ink font-medium text-lg">
              For goals you need to <em>prove</em> — not just re-read.
            </p>
            <p class="mt-4 text-ink-muted leading-relaxed">
              Not a comfort scoreboard. Not a random drill dump.
              <span class="text-ink-soft">Practice</span> shows the gap between recognizing material and being able to use it —
              then names what went wrong and aims the next run at those gaps until the skill holds.
              Practice packs are built for a clear goal — an exam, a job skill, a team standard —
              and always draw from the same map you built in <span class="text-ink-soft">Learn</span>.
              Same map; harder questions when it counts. One map can feed many packs.
            </p>

            <p class="text-xs font-mono uppercase tracking-wider text-ink-muted mt-10 mb-4">What it does</p>
            <ul class="space-y-4">
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-practice">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Closed-notes practice</h3>
                  <p class="text-ink-muted text-sm mt-1">Test yourself without hints or guessing from how the question looks.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-practice">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Name what went wrong</h3>
                  <p class="text-ink-muted text-sm mt-1">Missing idea, wrong method, or “couldn’t put the pieces together” — then fix the right thing.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-practice">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Drills from real gaps</h3>
                  <p class="text-ink-muted text-sm mt-1">Practice aimed at what you missed — not random coverage of everything.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-practice">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Track over time</h3>
                  <p class="text-ink-muted text-sm mt-1">Skill that still works next month — not one lucky good day.</p>
                </div>
              </li>
            </ul>

            <p class="mt-8 font-mono text-xs uppercase tracking-[0.2em] text-ink-muted">
              Learn builds the map · Practice proves
            </p>
            <a href="#platform" class="inline-flex items-center gap-1 text-sm font-medium mt-5 hover:gap-2 transition-all" style="color:#145032">
              Then save your place
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </a>
          </div>
        </div>
      </div>
    </section>


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
              For weeks that <em>interrupt</em> — not perfect study streaks.
            </p>
            <p class="mt-4 text-ink-muted leading-relaxed">
              Not a chat archive. Not another app to babysit.
              <span class="text-ink-soft">Save place</span> is how you leave a clean handoff for tomorrow —
              whether you were in Learn or mid Practice.
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
                  <p class="text-ink-muted text-sm mt-1">Capture where you were and what still feels fuzzy — enough that restarting is intentional.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-save">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Name the next step</h3>
                  <p class="text-ink-muted text-sm mt-1">Deeper map work, more practice, or a real check — so tomorrow’s you is not guessing.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-save">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Short sessions that still count</h3>
                  <p class="text-ink-muted text-sm mt-1">Open only what the next sitting needs — kids, work, and loud weeks do not erase the loop.</p>
                </div>
              </li>
              <li class="flex items-start gap-4">
                <div class="icon-tile icon-tile-orient">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" /></svg>
                </div>
                <div>
                  <h3 class="text-ink font-semibold">Stay oriented</h3>
                  <p class="text-ink-muted text-sm mt-1">Quiet layer under save place: where you are on the map, when open study should become honest practice — not another portal to buy.</p>
                </div>
              </li>
            </ul>

            <p class="mt-8 font-mono text-xs uppercase tracking-[0.2em] text-ink-muted">
              Learn builds the map · Practice proves · Save place keeps the loop
            </p>
            <a href="#gym" class="inline-flex items-center gap-1 text-sm font-medium mt-5 hover:gap-2 transition-all" style="color:#6e1818">
              When a vertical needs it — the Gym
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </a>
          </div>
        </div>
      </div>
    </section>


    <section id="gym" class="section-padding relative section-charcoal">
      <div class="absolute inset-0 pointer-events-none" style="background: linear-gradient(to bottom, transparent, rgba(43,95,158,0.06), transparent)" aria-hidden="true"></div>
      <div class="max-w-7xl mx-auto relative">
        <div class="max-w-3xl mx-auto">
          <div class="door-copy-head" data-reveal>
            <span class="section-label !text-[#12355c]">Gym · Solo only</span>
            <h2 class="section-title">Like the real thing for muscle memory</h2>
            <p class="font-mono text-sm mt-2 text-[#12355c]">Training wheels · not Planet Fitness</p>
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
            </p>
            <a href="#product" class="inline-flex items-center gap-1 text-sm font-medium mt-5 hover:gap-2 transition-all" style="color:#12355c">
              Where the loop runs
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </a>
          </div>
        </div>
      </div>
    </section>

    </div><!-- /#content.slug-depth -->'''

path.write_text(text[:start] + new + text[end:], encoding="utf-8")
print("ok", path, "start", start, "replaced", end - start, "chars")
