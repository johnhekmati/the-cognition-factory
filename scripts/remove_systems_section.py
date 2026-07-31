# -*- coding: utf-8 -*-
from pathlib import Path
import re

path = Path(__file__).resolve().parents[1] / "index.html"
text = path.read_text(encoding="utf-8")

start = text.find("WHAT YOU WORK WITH")
if start < 0:
    raise SystemExit("WHAT YOU WORK WITH not found")
start = text.rfind("    <!--", 0, start)

end = text.find("PRODUCT GALLERY")
if end < 0:
    raise SystemExit("PRODUCT GALLERY not found")
end = text.rfind("    <!--", 0, end)

if start < 0 or end <= start:
    raise SystemExit(f"bad bounds start={start} end={end}")

text2 = text[:start] + text[end:]
path.write_text(text2, encoding="utf-8")

ids = re.findall(r'<section id="([^"]+)"', path.read_text(encoding="utf-8"))
print("sections:", ids)
if "systems" in ids:
    raise SystemExit("systems still present")
if ids.index("pathways") + 1 != ids.index("loop"):
    raise SystemExit(f"expected pathways→loop, got {ids}")
print("ok: systems removed; pathways → loop intact")
