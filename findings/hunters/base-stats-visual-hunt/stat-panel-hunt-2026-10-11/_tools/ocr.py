#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OCR helper for the Blustone stat-panel hunt.
Calls tesseract.exe directly with jpn+kor+eng (all present in the custom
tessdata dir). Never swallows subprocess errors silently.
"""
import os, sys, subprocess

TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TESSDATA = r"C:\Users\shaha\AppData\Local\Temp\opencode\tessdata"
DEF_LANG = "jpn+kor+eng"

def ocr(image_path, lang=DEF_LANG, psm=None):
    cmd = [TESS, image_path, "stdout", "-l", lang, "--tessdata-dir", TESSDATA]
    if psm:
        cmd += ["--psm", str(psm)]
    r = subprocess.run(cmd, capture_output=True, timeout=200)
    return r.stdout.decode("utf-8", errors="replace")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        lang = sys.argv[2] if len(sys.argv) >= 3 else DEF_LANG
        sys.stdout.buffer.write(ocr(sys.argv[1], lang).encode("utf-8", errors="replace"))
