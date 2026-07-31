"""Splice dual-lane pathways + triad into index.html (local demo). No deploy."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
lines = (root / "index.html").read_text(encoding="utf-8").splitlines(keepends=True)

# keep through solution (1-based line 424 → index 424 exclusive = 0:424)
head = lines[0:424]
mid = (root / "partials/home-pathways-triad.html").read_text(encoding="utf-8")
if not mid.endswith("\n"):
    mid += "\n"
# from product comment (1-based 1070 → index 1069)
tail = lines[1069:]

head_txt = "".join(head)
head_txt = head_txt.replace(
    'href="#loop" class="btn-secondary inline-flex">See how it works →</a>',
    'href="#pathways" class="btn-secondary inline-flex">Choose a pathway →</a>',
)

nav_old = """          <div class="hidden lg:flex items-center gap-6 shrink-0">
            <a href="#enemy" class="nav-link" data-nav>Problem</a>
            <a href="#loop" class="nav-link" data-nav>How it works</a>
            <a href="#product" class="nav-link" data-nav>Product</a>
            <a href="#proof" class="nav-link" data-nav>Proof</a>
            <a href="#resources" class="nav-link" data-nav>Guides</a>
            <a href="#promise" class="nav-link" data-nav>Why</a>
            <a href="#contact" class="btn-primary text-xs !px-5 !py-2.5">Talk with us</a>
          </div>"""
nav_new = """          <div class="hidden lg:flex items-center gap-6 shrink-0">
            <a href="#pathways" class="nav-link" data-nav>Pathways</a>
            <a href="/solo/" class="nav-link">Solo</a>
            <a href="/enterprise/" class="nav-link">Enterprise</a>
            <a href="#product" class="nav-link" data-nav>Product</a>
            <a href="#resources" class="nav-link" data-nav>Guides</a>
            <a href="#contact" class="btn-primary text-xs !px-5 !py-2.5">Talk with us</a>
          </div>"""
if nav_old not in head_txt:
    raise SystemExit("nav block not found")
head_txt = head_txt.replace(nav_old, nav_new)

mobile_old = """          <div class="site-chrome-inner py-6 flex flex-col gap-4">
            <a href="#enemy" class="nav-link py-2" data-nav>Problem</a>
            <a href="#loop" class="nav-link py-2" data-nav>How it works</a>
            <a href="#product" class="nav-link py-2" data-nav>Product</a>
            <a href="#proof" class="nav-link py-2" data-nav>Proof</a>
            <a href="#resources" class="nav-link py-2" data-nav>Guides</a>
            <a href="#promise" class="nav-link py-2" data-nav>Why</a>
            <a href="#contact" class="btn-primary text-center mt-2">Talk with us</a>
            <a href="#contact" class="text-center text-sm text-ink-muted hover:text-electric transition-colors">Teams &amp; institutions</a>
          </div>"""
mobile_new = """          <div class="site-chrome-inner py-6 flex flex-col gap-4">
            <a href="#pathways" class="nav-link py-2" data-nav>Pathways</a>
            <a href="/solo/" class="nav-link py-2">Solo</a>
            <a href="/enterprise/" class="nav-link py-2">Enterprise</a>
            <a href="#product" class="nav-link py-2" data-nav>Product</a>
            <a href="#resources" class="nav-link py-2" data-nav>Guides</a>
            <a href="#contact" class="btn-primary text-center mt-2">Talk with us</a>
          </div>"""
if mobile_old not in head_txt:
    raise SystemExit("mobile nav not found")
head_txt = head_txt.replace(mobile_old, mobile_new)
head_txt = head_txt.replace(
    'href="#hero" class="flex items-center gap-3 group min-w-0"',
    'href="/" class="flex items-center gap-3 group min-w-0"',
    1,
)

out = head_txt + mid + "".join(tail)

footer_old = """          <div class="flex flex-wrap items-center justify-center gap-6" aria-label="Site map">
            <a href="#enemy" class="text-ink-muted hover:text-electric text-sm transition-colors">Problem</a>
            <a href="#loop" class="text-ink-muted hover:text-electric text-sm transition-colors">How it works</a>
            <a href="#product" class="text-ink-muted hover:text-electric text-sm transition-colors">Product</a>
            <a href="#proof" class="text-ink-muted hover:text-electric text-sm transition-colors">Proof</a>
            <a href="#resources" class="text-ink-muted hover:text-electric text-sm transition-colors">Guides</a>
            <a href="#promise" class="text-ink-muted hover:text-electric text-sm transition-colors">Why</a>
            <a href="#contact" class="text-ink-muted hover:text-electric text-sm transition-colors">Contact</a>
          </div>"""
footer_new = """          <div class="flex flex-wrap items-center justify-center gap-6" aria-label="Site map">
            <a href="#pathways" class="text-ink-muted hover:text-electric text-sm transition-colors">Pathways</a>
            <a href="/solo/" class="text-ink-muted hover:text-electric text-sm transition-colors">Solo</a>
            <a href="/enterprise/" class="text-ink-muted hover:text-electric text-sm transition-colors">Enterprise</a>
            <a href="#product" class="text-ink-muted hover:text-electric text-sm transition-colors">Product</a>
            <a href="#resources" class="text-ink-muted hover:text-electric text-sm transition-colors">Guides</a>
            <a href="#contact" class="text-ink-muted hover:text-electric text-sm transition-colors">Contact</a>
          </div>"""
if footer_old in out:
    out = out.replace(footer_old, footer_new)

hook = """
        <div class="flex flex-col sm:flex-row items-center justify-center gap-3 mb-10 md:mb-12" data-reveal>
          <a href="/solo/#product" class="btn-secondary text-xs !px-4 !py-2">Solo · product →</a>
          <a href="/enterprise/#product" class="btn-secondary text-xs !px-4 !py-2">Enterprise · product →</a>
        </div>
"""
pi = out.find('<section id="product"')
if pi == -1:
    raise SystemExit("no product section")
sub = out.find("section-subtitle", pi)
end_p = out.find("</p>", sub)
pos = end_p
for _ in range(3):
    pos = out.find("</div>", pos + 1)
insert_at = pos + len("</div>")
out = out[:insert_at] + "\n" + hook + out[insert_at:]

(root / "index.html").write_text(out, encoding="utf-8")
print("home dual-lane splice ok", len(out))
