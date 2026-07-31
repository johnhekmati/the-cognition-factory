from pathlib import Path


def swap_contact(page_path: Path, partial_path: Path) -> None:
    html = page_path.read_text(encoding="utf-8")
    partial = partial_path.read_text(encoding="utf-8")
    if not partial.endswith("\n"):
        partial += "\n"
    needle = 'id="contact"'
    i = html.find(needle)
    if i < 0:
        raise SystemExit(f"no contact in {page_path}")
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
    if end < 0:
        raise SystemExit(f"unclosed contact in {page_path}")
    html = html[:s] + partial + html[end:]
    html = html.replace("main.js?v=hero-paint1", "main.js?v=contact-slugs1")
    html = html.replace("main.js?v=contact-slugs1", "main.js?v=contact-slugs1")
    page_path.write_text(html, encoding="utf-8")
    print("swapped", page_path)


root = Path(__file__).resolve().parents[1]
swap_contact(root / "solo" / "index.html", root / "partials" / "contact-solo.html")
swap_contact(
    root / "enterprise" / "index.html", root / "partials" / "contact-enterprise.html"
)
idx = root / "index.html"
text = idx.read_text(encoding="utf-8")
if "main.js?v=" in text:
    import re

    text2 = re.sub(r"main\.js\?v=[^\"']+", "main.js?v=contact-slugs1", text)
    if text2 != text:
        idx.write_text(text2, encoding="utf-8")
        print("home js cache bumped")
print("ok")
