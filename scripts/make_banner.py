#!/usr/bin/env python3
"""Generate assets/banner.png (README hero) and assets/social-preview.png (1280x640). Text only, no third-party logos."""
import json, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter
root = pathlib.Path(__file__).resolve().parent.parent
n = len(json.loads((root / "data/entries.json").read_text(encoding="utf-8")))
W, H = 1280, 640
F = "/usr/share/fonts/truetype/noto/NotoSans-%s.ttf"
def font(w, s): return ImageFont.truetype(F % w, s)
img = Image.new("RGB", (W, H), (9, 10, 20))
# soft glow blobs
glow = Image.new("RGB", (W, H), (0, 0, 0)); g = ImageDraw.Draw(glow)
g.ellipse((-150, -200, 600, 400), fill=(70, 50, 200)); g.ellipse((700, 250, 1450, 850), fill=(0, 140, 170)); g.ellipse((500, -250, 1000, 150), fill=(150, 50, 160))
glow = glow.filter(ImageFilter.GaussianBlur(160))
img = Image.blend(img, Image.eval(glow, lambda v: v), 0.55)
d = ImageDraw.Draw(img, "RGBA")
# grid
for x in range(0, W, 40): d.line([(x, 0), (x, H)], fill=(255, 255, 255, 10))
for y in range(0, H, 40): d.line([(0, y), (W, y)], fill=(255, 255, 255, 10))
def glass(box, r=22, fill=(255, 255, 255, 22), line=(255, 255, 255, 60)):
    d.rounded_rectangle(box, r, fill=fill, outline=line, width=2)
glass((60, 60, 1220, 580), 34, (255, 255, 255, 14))
d.text((110, 105), "AWESOME LIST", font=font("Bold", 22), fill=(150, 200, 255, 255))
d.text((110, 145), "AI Search", font=font("Bold", 84), fill=(255, 255, 255, 255))
d.text((110, 240), "Optimization", font=font("Bold", 84), fill=(255, 255, 255, 255))
d.text((112, 355), "Open-source GitHub tools for AI SEO, AEO and GEO.", font=font("Regular", 30), fill=(210, 215, 235, 255))
d.text((112, 400), "Get found and cited when people ask AI instead of Google.", font=font("Regular", 24), fill=(160, 168, 195, 255))
# stat pills
x = 112
for t in [f"{n} checked repos", "8 categories", "Weekly health check"]:
    f = font("SemiBold" if False else "Bold", 22); w = d.textlength(t, font=f) + 44
    glass((x, 460, x + w, 512), 26, (255, 255, 255, 30)); d.text((x + 22, 473), t, font=f, fill=(255, 255, 255, 255)); x += w + 16
# engines column
d.text((860, 105), "BUILT FOR VISIBILITY IN", font=font("Bold", 18), fill=(150, 200, 255, 255))
engines = ["ChatGPT", "Perplexity", "Claude", "Gemini", "Google AI Overviews", "Copilot", "Grok"]
y = 140
for e in engines:
    f = font("Bold", 22); w = d.textlength(e, font=f) + 40
    glass((860, y, 860 + w, y + 44), 22, (255, 255, 255, 26)); d.text((880, y + 8), e, font=f, fill=(255, 255, 255, 255)); y += 54
d.text((860, 530), "Names shown as text only. Not affiliated.", font=font("Regular", 15), fill=(140, 148, 175, 255))
(root / "assets").mkdir(exist_ok=True)
img.save(root / "assets/banner.png", optimize=True); img.save(root / "assets/social-preview.png", optimize=True)
print("ok")
