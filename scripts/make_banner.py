#!/usr/bin/env python3
"""Generate assets/banner.png and assets/social-preview.png (1280x640). Original artwork, text only.
Usage: python scripts/make_banner.py  (reads data/banner.json)"""
import json, math, pathlib, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
root = pathlib.Path(__file__).resolve().parent.parent
cfg = json.loads((root / "data/banner.json").read_text(encoding="utf-8"))
W, H = 1280, 640
N = "/usr/share/fonts/truetype/noto/"
MONO = ImageFont.truetype(N + "NotoSansMono-Bold.ttf", 15)
def F(name, s): return ImageFont.truetype(N + name, s)
rnd = random.Random(7)
# 1) dense tiled-text texture, colored by a diagonal gradient
words = cfg["tile_words"]
tex = Image.new("RGB", (W, H), (8, 9, 12)); td = ImageDraw.Draw(tex)
c0, c1, c2 = [tuple(c) for c in cfg["gradient"]]   # left, middle, right colours
def grad(x, y):
    t = min(1, max(0, (x / W) * 0.8 + (y / H) * 0.2))
    a, b, u = (c0, c1, t * 2) if t < .5 else (c1, c2, (t - .5) * 2)
    return tuple(int(a[i] + (b[i] - a[i]) * u) for i in range(3))
y = -6
while y < H:
    x = -rnd.randint(0, 120)
    while x < W:
        w = rnd.choice(words)
        r, g, b = grad(x, y)
        k = 0.22 + 0.78 * (max(0, x) / W) ** 1.4          # stronger on the right
        if rnd.random() < 0.12: k = min(1, k * 1.8)
        td.text((x, y), w, font=MONO, fill=(int(r * k), int(g * k), int(b * k)))
        x += int(td.textlength(w, font=MONO)) + 12
    y += 19
# 2) left vignette so the title reads
shade = Image.new("L", (W, H), 0); sd = ImageDraw.Draw(shade)
for x in range(W):
    sd.line([(x, 0), (x, H)], fill=int(235 * max(0, 1 - x / 880) ** 0.8))
img = Image.composite(Image.new("RGB", (W, H), (7, 8, 11)), tex, shade)
d = ImageDraw.Draw(img, "RGBA")
# 3) glasses mark + "awesome" wordmark (original drawing)
gx, gy = 70, 66
col = (225, 228, 235, 255)
d.rounded_rectangle((gx, gy, gx + 66, gy + 40), 16, fill=col)
d.rounded_rectangle((gx + 80, gy, gx + 146, gy + 40), 16, fill=col)
d.arc((gx + 56, gy - 6, gx + 90, gy + 22), 200, 340, fill=col, width=6)
d.line([(gx, gy + 6), (gx - 12, gy - 6)], fill=col, width=6); d.line([(gx + 146, gy + 6), (gx + 158, gy - 6)], fill=col, width=6)
d.text((gx + 180, gy - 10), "awesome", font=F("NotoSansMono-Bold.ttf", 54), fill=(225, 228, 235, 255))
# 4) title
ser = F("NotoSerif-BoldItalic.ttf", 96)
for i, line in enumerate(cfg["title"]):
    d.text((66, 150 + i * 108), line, font=ser, fill=(255, 255, 255, 255))
# 5) CTA
cy = 420
d.text((70, cy), ">> " + cfg["cta1"], font=F("NotoSansMono-Bold.ttf", 33), fill=(255, 255, 255, 255))
d.text((70, cy + 52), cfg["cta2"], font=F("NotoSansMono-Bold.ttf", 33), fill=(255, 255, 255, 255))
bx = 70 + d.textlength(cfg["cta2"], font=F("NotoSansMono-Bold.ttf", 33)) + 18
bf = F("NotoSans-Bold.ttf", 34)
bw = d.textlength(cfg["brand"], font=bf)
d.rounded_rectangle((bx, cy + 44, bx + bw + 50, cy + 100), 14, fill=tuple(cfg["brand_color"]) + (255,))
d.text((bx + 25, cy + 50), cfg["brand"], font=bf, fill=(255, 255, 255, 255))
d.rounded_rectangle((60, 556, 60 + d.textlength(cfg["foot"], font=F("NotoSansMono-Bold.ttf", 17)) + 24, 596), 10, fill=(8, 9, 12, 200)); d.text((72, 566), cfg["foot"], font=F("NotoSansMono-Bold.ttf", 17), fill=(170, 176, 190, 255))
# 6) logo grid (official marks taken from each brand's own site; see assets/logos/README.md)
if cfg.get("logos"):
    T = 128; gap = 22; gx0 = 800; gy0 = 70
    d.rounded_rectangle((gx0 - 28, gy0 - 28, gx0 + 3 * T + 2 * gap + 28, gy0 + 2 * T + gap + 28 + 44), 30, fill=(8, 9, 12, 150), outline=(255, 255, 255, 70), width=2)
    for i, n in enumerate(cfg["logos"]):
        lg0 = Image.open(root / "assets/logos" / (n + ".png")).convert("RGBA").resize((T, T), Image.LANCZOS)
        lg = Image.new("RGB", (T, T), (255, 255, 255)); lg.paste(lg0, (0, 0), lg0)
        m = Image.new("L", (T, T), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, T - 1, T - 1), 28, fill=255)
        x0 = gx0 + (i % 3) * (T + gap); y0 = gy0 + (i // 3) * (T + gap)
        img.paste(lg, (x0, y0), m); d = ImageDraw.Draw(img, "RGBA")
    d.text((gx0, gy0 + 2 * T + gap + 12), cfg["logo_caption"], font=F("NotoSansMono-Bold.ttf", 15), fill=(200, 205, 220, 255))
(root / "assets").mkdir(exist_ok=True)
img.save(root / "assets/banner.png", optimize=True); img.save(root / "assets/social-preview.png", optimize=True)
print("ok")
