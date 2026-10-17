#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scan a downloaded video: ffmpeg 1fps -> OCR (jpn+kor+eng) -> stat-token scoring.
Usage: scan.py <video_id> [fps] [max_frames]
Appends to frame-results.tsv; copies hit frames to hits/ with .txt sidecar.
"""
import os, sys, re, subprocess, shutil, time

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
DL = os.path.join(BASE, "dl")
FR = os.path.join(BASE, "frames")
HITS = os.path.join(BASE, "hits")
FFMPEG = r"C:\Users\shaha\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe"
sys.path.insert(0, HERE)
import ocr as O

TOKENS = ["HP", "ATK", "DEF", "Strength", "Power", "STR",
          "체력", "공격", "방어", "전투력", "스탯", "장비", "각성", "헌터",
          "ステータス", "攻撃", "体力", "防御", "戦闘力", "装備", "覚醒", "ハンター",
          "攻击", "防御", "生命", "战斗力", "装备", "觉醒", "猎人",
          "Lv", "MAX", "Rank", "Grade", "Critical", "Speed", "Regen"]
NUMRE = re.compile(r"\d[\d,]*\.?\d*")

def score(text):
    flat = text.replace(" ", "").replace(",", "")
    toks = sum(1 for t in TOKENS if t in text or t.replace(" ", "") in flat)
    nums = len(NUMRE.findall(text))
    has_trio = ("HP" in text and "ATK" in text and "DEF" in text)
    s = toks + min(nums, 6) + (6 if has_trio else 0)
    return s, toks, nums, has_trio

def main():
    vid = sys.argv[1]
    fps = sys.argv[2] if len(sys.argv) > 2 else "1"
    src = None
    for f in os.listdir(DL):
        if f.startswith(vid):
            src = os.path.join(DL, f)
            break
    if not src:
        print("NO-SRC %s" % vid); return 1
    outdir = os.path.join(FR, vid)
    os.makedirs(outdir, exist_ok=True)
    if not os.listdir(outdir):
        cmd = [FFMPEG, "-y", "-i", src, "-vf", "fps=%s,scale=1280:-1" % fps, os.path.join(outdir, "f%05d.jpg")]
        r = subprocess.run(cmd, capture_output=True, timeout=1200)
        if r.returncode != 0:
            print("FFMPEG-ERR " + r.stderr.decode("utf-8", "replace")[-500:]); return 1
    frames = sorted(f for f in os.listdir(outdir) if f.endswith(".jpg"))
    res_path = os.path.join(BASE, "frame-results.tsv")
    new_file = not os.path.exists(res_path)
    with open(res_path, "a", encoding="utf-8") as log:
        if new_file:
            log.write("video_id\tframe\tapprox_sec\tscore\ttokens\tnumerals\ttrio\ttext_snippet\n")
        for i, f in enumerate(frames):
            p = os.path.join(outdir, f)
            try:
                txt = O.ocr(p)
            except Exception as e:
                log.write("%s\t%s\t%d\tERR\t0\t0\tFalse\t%s\n" % (vid, f, i, e)); continue
            s, toks, nums, trio = score(txt)
            snip = " | ".join(l.strip() for l in txt.splitlines() if l.strip())[:300].replace("\t", " ")
            log.write("%s\t%s\t%d\t%d\t%d\t%d\t%s\t%s\n" % (vid, f, i, s, toks, nums, trio, snip))
            log.flush()
            if s >= 9 or trio:
                ts = i  # approx seconds at 1fps
                dst = os.path.join(HITS, "%s_%s" % (vid, f))
                shutil.copy(p, dst)
                with open(dst + ".txt", "w", encoding="utf-8") as h:
                    h.write("URL: https://www.youtube.com/watch?v=%s&t=%ds\nframe: %s\nscore: %d toks=%d nums=%d trio=%s\n---\n%s" % (vid, ts, f, s, toks, nums, trio, txt))
                print("HIT %s %s score=%d trio=%s" % (vid, f, s, trio))
    print("DONE %s frames=%d" % (vid, len(frames)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
