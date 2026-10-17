#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OCR already-extracted frames in frames/<vid>/ (no ffmpeg step).
Usage: scan_existing.py <video_id>
Same scoring/sidecar logic as scan.py.
"""
import os, sys, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan import score
import ocr as O

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HITS = os.path.join(BASE, "hits")

def main():
    vid = sys.argv[1]
    outdir = os.path.join(BASE, "frames", vid)
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
                log.write("%s\t%s\t%d\tERR\t0\t0\tFalse\t%s\n" % (vid, f, i * 3, e)); continue
            s, toks, nums, trio = score(txt)
            snip = " | ".join(l.strip() for l in txt.splitlines() if l.strip())[:300].replace("\t", " ")
            log.write("%s\t%s\t%d\t%d\t%d\t%d\t%s\t%s\n" % (vid, f, i * 3, s, toks, nums, trio, snip))
            log.flush()
            if s >= 9 or trio:
                dst = os.path.join(HITS, "%s_%s" % (vid, f))
                shutil.copy(p, dst)
                with open(dst + ".txt", "w", encoding="utf-8") as h:
                    h.write("URL: https://www.youtube.com/watch?v=%s&t=%ds\nframe: %s\nscore: %d toks=%d nums=%d trio=%s\n---\n%s" % (vid, i * 3, f, s, toks, nums, trio, txt))
                print("HIT %s %s score=%d trio=%s" % (vid, f, s, trio), flush=True)
    print("DONE %s frames=%d" % (vid, len(frames)))

if __name__ == "__main__":
    main()
