#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""POSITIVE CONTROL: render known numerals + English stat labels, OCR with the
exact tesseract pipeline, and assert the numbers come back. A stat-signature
batch is only trusted if this control passes.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image, ImageDraw, ImageFont
import ocr as O

def make_control(path):
    W, H = 900, 560
    img = Image.new("RGB", (W, H), (24, 28, 40))
    d = ImageDraw.Draw(img)
    def font(sz):
        for p in ["arial.ttf", "DejaVuSans.ttf"]:
            try:
                return ImageFont.truetype(p, sz)
            except Exception:
                continue
        return ImageFont.load_default()
    f_big = font(46); f_row = font(34); f_lbl = font(30)
    gold = (254, 196, 60); white = (235, 238, 245); green = (84, 214, 110)
    y = 20
    d.text((30, y), "Upgrade Equipment", fill=(120,180,255), font=f_lbl); y += 60
    d.text((30, y), "Strength", fill=white, font=f_lbl)
    d.text((420, y-6), "24068", fill=gold, font=f_big)
    d.text((700, y), "+6291", fill=green, font=f_row); y += 70
    for lbl, val, delta in [("HP","2879","+437"),("ATK","1471","+317"),
                            ("DEF","1149","+154"),
                            ("Attacking Speed","8.00","+1.72")]:
        d.text((30, y), lbl, fill=white, font=f_lbl)
        d.text((420, y), val, fill=gold, font=f_row)
        d.text((700, y), delta, fill=green, font=f_row); y += 54
    d.text((30, y), "Critical Attack Chance", fill=white, font=f_lbl)
    d.text((420, y), "33.00", fill=gold, font=f_row); y += 54
    d.text((30, y), "Regeneration", fill=white, font=f_lbl)
    d.text((420, y), "42.00", fill=gold, font=f_row)
    img.save(path)
    return path

def main():
    tmp = os.environ.get("PANELHUNT_TMP", r"C:\Users\shaha\AppData\Local\Temp\opencode\panelhunt")
    os.makedirs(tmp, exist_ok=True)
    path = os.path.join(tmp, "_control_panel.png")
    make_control(path)
    txt = O.ocr(path, lang="eng")
    sys.stdout.buffer.write(b"=== RAW OCR (eng) ===\n")
    sys.stdout.buffer.write(txt.encode("utf-8", errors="replace"))
    checks = ["24068", "6291", "2879", "1471", "1149", "8.00", "33.00", "42.00"]
    flat = txt.replace(" ", "").replace(",", "")
    hits = [c for c in checks if c in flat]
    sys.stdout.buffer.write(("\n=== MATCH %d/%d: %s ===\n" % (len(hits), len(checks), hits)).encode())
    ok = len(hits) >= 6
    sys.stdout.buffer.write(("CONTROL: %s\n" % ("PASS" if ok else "FAIL")).encode())
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
