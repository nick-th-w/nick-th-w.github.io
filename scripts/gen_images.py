"""Generates og-image.png and favicon.png for the CV site from brand colors.
Run: python3 scripts/gen_images.py
"""
from PIL import Image, ImageDraw, ImageFont

INK = "#1c1c1c"
GREEN = "#234a3a"
GREEN_LIGHT = "#f4f3f1"
WHITE = "#ffffff"

ARIAL_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"

def og_image():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), GREEN)
    d = ImageDraw.Draw(img)

    # monogram circle
    r = 90
    cx, cy = 140, H // 2
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=WHITE)
    mono_font = ImageFont.truetype(ARIAL_BOLD, 64)
    bbox = d.textbbox((0, 0), "NW", font=mono_font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text((cx - tw / 2 - bbox[0], cy - th / 2 - bbox[1]), "NW", font=mono_font, fill=GREEN)

    # name
    name_font = ImageFont.truetype(ARIAL_BOLD, 76)
    d.text((280, 210), "Nick Wong", font=name_font, fill=WHITE)

    # role
    role_font = ImageFont.truetype(ARIAL_BOLD, 30)
    d.text((282, 310), "BUSINESS OPERATIONS & GROWTH", font=role_font, fill=GREEN_LIGHT)

    # lede
    lede_font = ImageFont.truetype(ARIAL, 26)
    d.text((282, 366), "15 years scaling marketplace and operating", font=lede_font, fill="#dfe8e4")
    d.text((282, 402), "functions at Grab, Uber, Zoomo, Momos & Veridooh", font=lede_font, fill="#dfe8e4")

    img.save("assets/og-image.png")
    print("wrote assets/og-image.png")

def favicon():
    for size in (16, 32, 48, 180, 192, 512):
        img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        d.ellipse([0, 0, size, size], fill=GREEN)
        font_size = int(size * 0.42)
        try:
            font = ImageFont.truetype(ARIAL_BOLD, font_size)
        except OSError:
            font = ImageFont.load_default()
        bbox = d.textbbox((0, 0), "NW", font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        d.text(((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1]), "NW", font=font, fill=WHITE)
        if size == 32:
            img.save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
            print("wrote favicon.ico")
        if size in (180, 192, 512):
            img.save(f"assets/icon-{size}.png")
            print(f"wrote assets/icon-{size}.png")

if __name__ == "__main__":
    og_image()
    favicon()
