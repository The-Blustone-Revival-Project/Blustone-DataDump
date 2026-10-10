# -*- coding: utf-8 -*-
"""Re-verify every numeric claim at high zoom and emit a findings table.

Discipline: each reading is taken from a crop scaled>=5x, and the tool PRINTS
what it cropped so the crop can be eyeballed against the timestamp. Nothing is
recorded from a contact sheet.

Output: findings.tsv (machine-readable) + a zoom PNG per claim.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "cnbeta-frames-2026-10-09")
FRAMES = os.path.expandvars(r"%TEMP%\opencode\cnbeta\f1s")
L, T, R, B = [int(v) for v in open(os.path.join(D, "active-box.txt"), encoding="utf-8").read().split()]

# claim_id, t, x, y, w, h (ACTIVE-relative), scale, what it should show
CLAIMS = [
    ("C01-detail-power", 538, 220, 570, 200, 90, 5.0, "detail screen 战斗力 210"),
    ("C02-detail-lv", 538, 0, 620, 300, 100, 5.0, "detail screen Lv. 1"),
    ("C03-detail-name", 538, 0, 60, 420, 100, 4.5, "detail name 顶尖厨师/蒂希尔"),
    ("C04-recruit", 531, 0, 560, 818, 160, 4.0, "recruit result 蒂希尔"),
    ("C05-victory-heroes", 705, 0, 330, 300, 120, 7.0, "victory Lv.4=314 / Lv.1=210"),
    ("C06-victory-stars", 705, 20, 70, 380, 140, 5.0, "3 star conditions"),
    ("C07-victory-team", 705, 0, 260, 818, 90, 5.0, "team level 2"),
    ("C08-power-pre", 85, 0, 330, 360, 120, 5.0, "Lv.1 293"),
    ("C09-power-post", 87, 0, 330, 360, 120, 5.0, "Lv.2 300 +7"),
    ("C10-prep-vs", 716, 90, 425, 260, 40, 8.0, "我方队员 536 VS 预想敌军 860"),
    ("C11-prep-ap", 716, 240, 70, 340, 60, 6.0, "AP 97/61"),
    ("C12-prep-lv10", 716, 0, 140, 700, 200, 5.0, "enemy Lv.10"),
    ("C13-battle-hp", 665, 0, 0, 818, 130, 5.0, "enemy wave 562 x6 + counters"),
    ("C14-skillcut", 671, 0, 0, 818, 720, 1.2, "料理治愈法 skill cut-in"),
    ("C15-reward-day1", 449, 0, 380, 818, 240, 4.0, "login reward day1-3"),
    ("C16-skillcut2", 683, 0, 0, 818, 720, 1.2, "闪电击 skill cut-in"),
]


def main():
    rows = []
    try:
        font = ImageFont.truetype("arialbd.ttf", 22)
    except Exception:  # noqa: BLE001
        font = ImageFont.load_default()
    for cid, t, x, y, w, h, scale, note in CLAIMS:
        src = os.path.join(FRAMES, "f_%06d.jpg" % (t + 1))
        with Image.open(src) as im:
            im.load()
            full = im.convert("RGB")
            crop = full.crop((L + x, T + y, L + x + w, T + y + h))
        up = crop.resize((int(crop.width * scale), int(crop.height * scale)), Image.LANCZOS)
        lab = Image.new("RGB", (up.width, up.height + 30), (18, 18, 22))
        lab.paste(up, (0, 30))
        d = ImageDraw.Draw(lab)
        d.text((6, 4), "%s  t=%ds  active-rect=%s  x%.1f" % (cid, t, (x, y, w, h), scale),
               fill=(255, 230, 90), font=font)
        p = os.path.join(D, "claim-%s.png" % cid)
        lab.save(p)
        rows.append((cid, t, "%d,%d,%d,%d" % (x, y, w, h), scale, note,
                     os.path.basename(p), "%dx%d" % lab.size))
        print("%-20s t=%-4d rect=%-22s x%-4.1f -> %s  (%s)" % (cid, t, (x, y, w, h), scale,
                                                               os.path.basename(p), note))
    with open(os.path.join(D, "findings.tsv"), "w", encoding="utf-8", newline="") as fh:
        fh.write("claim_id\tt_s\tactive_rect\tscale\twhat\tshot\tshot_px\n")
        for r in rows:
            fh.write("\t".join(str(v) for v in r) + "\n")
    print("\nwrote findings.tsv with %d claims" % len(rows))


if __name__ == "__main__":
    main()