"""Render social share cards (1200x630) and site icons with headless Chrome.

Run: python3 scripts/build-share-images.py
Outputs: assets/share/*.jpg, favicon.ico, favicon.svg, favicon-48.png,
apple-touch-icon.png, icon-192.png, icon-512.png
Requires Google Chrome and macOS `sips`.
"""
from pathlib import Path
import struct
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
A = (ROOT / "assets").as_uri()

ICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#f43229"/><g fill="#fff" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"><path d="M32.2 10 44.2 34.3H20.2Z"/><path d="M19.2 37.1 27.3 43.4 11.4 53.6Z"/><path d="M28 37.1H45.6L52.6 54Z"/></g></svg>"""

AR_STYLE = dict(lang="ar", dir="rtl", pad="62px 64px 52px 40px", side="right", deg="90deg", lh="1.28", ls="0")
EN_STYLE = dict(lang="en", dir="ltr", pad="62px 40px 52px 64px", side="left", deg="270deg", lh="1.08", ls="-.02em")

# slug -> (eyebrow, title lines, subtitle, image)
CARDS = {
    "home": ("مساكن أسبار", ["راحتهم مسؤوليتنا", "وثقتك <em>أولويتنا</em>"],
             "سكن العمالة · النقل · الإعاشة · إدارة المرافق", "room-red-bedding.jpg"),
    "worker-accommodation": ("خدماتنا", ["سكن العمالة", "<em>للشركات</em>"],
                             "غرف مجهزة ومفروشة وتشغيل منظم من جهة واحدة", "room-red-bedding.jpg"),
    "worker-transport": ("خدماتنا", ["نقل العمالة", "بين السكن <em>والعمل</em>"],
                         "رحلات منظمة تناسب مواعيد الورديات", "team.jpg"),
    "worker-catering": ("خدماتنا", ["إعاشة العمالة", "<em>وتنظيم الوجبات</em>"],
                        "وجبات يومية متنوعة حسب طبيعة العمل", "kitchen.jpg"),
    "facilities-management": ("خدماتنا", ["إدارة مرافق", "<em>سكن العمالة</em>"],
                              "النظافة والصيانة والأمن والإشراف الميداني", "facilities-management.png"),
    "choosing-worker-accommodation": ("دليل للشركات", ["كيف تختار سكن", "العمالة <em>لشركتك؟</em>"],
                                      "قائمة عملية لمقارنة عروض السكن", "room-red-bedding.jpg"),
}

EN_CARDS = {
    "home": ("Aspar Residences", ["Their comfort,", "our <em>responsibility.</em>"],
             "Housing · Transport · Catering · Facilities", "room-red-bedding.jpg"),
    "worker-accommodation": ("Our services", ["Worker", "accommodation <em>for companies</em>"],
                             "Furnished rooms and organized operations, one partner", "room-red-bedding.jpg"),
    "worker-transport": ("Our services", ["Worker transport", "from housing <em>to site</em>"],
                         "Organized trips aligned with your shifts", "team.jpg"),
    "worker-catering": ("Our services", ["Worker catering", "<em>and meal planning</em>"],
                        "Varied daily meals around your working day", "kitchen.jpg"),
    "facilities-management": ("Our services", ["Facilities", "<em>management</em>"],
                              "Cleaning, maintenance, security and supervision", "facilities-management.png"),
    "choosing-worker-accommodation": ("Guide for companies", ["How to choose", "worker <em>accommodation</em>"],
                                      "A practical checklist for comparing offers", "room-red-bedding.jpg"),
}

CARD_HTML = """<!doctype html><html lang="{lang}" dir="{dir}"><head><meta charset="utf-8"><style>
@font-face{{font-family:L;src:url({A}/fonts/lyon-arabic-display-black.otf)}}
@font-face{{font-family:M;src:url({A}/fonts/lyon-arabic-display-medium.otf)}}
*{{margin:0;box-sizing:border-box}}html,body{{width:1200px;height:630px;overflow:hidden}}
body{{display:flex;background:#131722;color:#fff;font-family:M}}
.copy{{width:640px;padding:{pad};display:flex;flex-direction:column;position:relative}}
.copy:before{{content:'';position:absolute;{side}:0;top:62px;width:10px;height:250px;background:#c8dc2a}}
.logo{{width:120px;height:120px;object-fit:contain;filter:brightness(0) invert(1);margin-bottom:22px}}
.eyebrow{{color:#c8dc2a;font-size:30px;margin-bottom:6px}}
h1{{font-family:L;font-size:{size}px;line-height:{lh};letter-spacing:{ls};font-weight:900}}h1 em{{font-style:normal;color:#f43229}}
p{{font-size:27px;color:#d6d8de;margin-top:20px}}
.url{{margin-top:auto;font-family:Arial,sans-serif;font-size:24px;letter-spacing:.5px;color:#fff;direction:ltr;text-align:{side}}}
.url b{{color:#f43229}}
.photo{{flex:1;background:url({A}/{img}) center/cover;position:relative}}
.photo:after{{content:'';position:absolute;inset:0;background:linear-gradient({deg},rgba(19,23,34,0) 70%,#131722)}}
</style></head><body><div class="copy"><img class="logo" src="{A}/logo-transparent.png" alt="">
<div class="eyebrow">{eyebrow}</div><h1>{title}</h1><p>{sub}</p><div class="url">msakinasbar<b>.</b>com</div></div>
<div class="photo"></div></body></html>"""

ICON_HTML = """<!doctype html><html><head><style>*{{margin:0}}html,body{{width:{s}px;height:{s}px;overflow:hidden;background:{bg}}}
img{{width:{s}px;height:{s}px;display:block}}</style></head><body><img src="data:image/svg+xml;utf8,{svg}"></body></html>"""


def shoot(html, out_png, w, h, tmp):
    src = Path(tmp) / (out_png.stem + ".html")
    src.write_text(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--default-background-color=00000000", "--allow-file-access-from-files",
                    "--force-device-scale-factor=1", f"--window-size={w},{h}", "--virtual-time-budget=3000",
                    f"--screenshot={out_png}", src.as_uri()], check=True, capture_output=True)


def ico_from_png(png_path, ico_path, size):
    data = png_path.read_bytes()
    header = struct.pack("<HHH", 0, 1, 1)
    entry = struct.pack("<BBBBHHII", size % 256, size % 256, 0, 0, 1, 32, len(data), 6 + 16)
    ico_path.write_bytes(header + entry + data)


def main():
    share = ROOT / "assets" / "share"
    share.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for slug, (eyebrow, lines, sub, img) in CARDS.items():
            size = 74 if max(len(l) for l in lines) < 20 else 66
            html = CARD_HTML.format(A=A, img=img, eyebrow=eyebrow, title="<br>".join(lines), sub=sub, size=size, **AR_STYLE)
            png = Path(tmp) / f"{slug}.png"
            shoot(html, png, 1200, 630, tmp)
            out = share / f"{slug}.jpg"
            subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "84", str(png), "--out", str(out)],
                           check=True, capture_output=True)
        for slug, (eyebrow, lines, sub, img) in EN_CARDS.items():
            html = CARD_HTML.format(A=A, img=img, eyebrow=eyebrow, title="<br>".join(lines), sub=sub, size=64, **EN_STYLE)
            png = Path(tmp) / f"en-{slug}.png"
            shoot(html, png, 1200, 630, tmp)
            subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "84", str(png), "--out", str(share / f"en-{slug}.jpg")],
                           check=True, capture_output=True)
        (ROOT / "favicon.svg").write_text(ICON_SVG)
        svg_q = ICON_SVG.replace("#", "%23").replace('"', "'")
        for name, s, bg in [("favicon-48.png", 48, "transparent"), ("apple-touch-icon.png", 180, "#f43229"),
                            ("icon-192.png", 192, "transparent"), ("icon-512.png", 512, "transparent")]:
            # apple-touch-icon must be full-bleed: iOS adds its own rounded mask.
            svg = svg_q.replace("rx='14'", "rx='0'") if name == "apple-touch-icon.png" else svg_q
            shoot(ICON_HTML.format(s=s, bg=bg, svg=svg), ROOT / name, s, s, tmp)
        ico_from_png(ROOT / "favicon-48.png", ROOT / "favicon.ico", 48)
    print("Generated", len(CARDS), "share cards and site icons.")


if __name__ == "__main__":
    main()
