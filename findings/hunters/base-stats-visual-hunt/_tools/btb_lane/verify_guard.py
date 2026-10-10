# -*- coding: utf-8 -*-
"""Guard compliance check on the deliverable.

Verifies: U+FFFD == 0, CRLF == 0, and reports Hangul / CJK / em-dash counts.
Also checks the folder for a silent CRLF flip (guard rule 14) and confirms the
protected files were NOT touched.
"""
import io
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

TARGET = "analysis/research/base-stats-visual-hunt/sister-game-stat-conventions-2026-10-09.md"

t = io.open(TARGET, encoding="utf-8", newline="").read()
print("=== DELIVERABLE HEALTH ===")
print("file            :", TARGET)
print("bytes           :", os.path.getsize(TARGET))
print("chars           :", len(t))
print("U+FFFD          :", t.count("\ufffd"), "(must be 0)")
print("CRLF            :", t.count("\r\n"), "(must be 0)")
print("bare CR         :", t.count("\r"), "(must be 0)")
print("em-dash U+2014  :", t.count("\u2014"))
print("Hangul AC00-D7A3:", len(re.findall(r"[\uac00-\uD7a3]", t)))
print("CJK 4E00-9FFF   :", len(re.findall(r"[\u4e00-\u9fff]", t)))
print("Kana            :", len(re.findall(r"[\u3040-\u30ff]", t)))
print("mojibake 'Ã'    :", t.count("\u00c3"), "(must be 0)")
print("lines           :", t.count("\n") + 1)

print()
print("=== FOLDER CR CHECK (guard rule 14: silent CRLF flips) ===")
base = "analysis/research/base-stats-visual-hunt"
bad = []
for root, dirs, files in os.walk(base):
    if "_tools" in root and "btb_lane" not in root:
        continue
    for f in files:
        if not f.endswith((".md", ".txt", ".tsv", ".json", ".py")):
            continue
        p = os.path.join(root, f)
        try:
            b = io.open(p, "rb").read()
        except OSError:
            continue
        if b"\r\n" in b:
            bad.append(p)
if bad:
    print("files containing CRLF (%d):" % len(bad))
    for p in bad[:20]:
        print("   ", p)
else:
    print("no CRLF found in the research folder (excluding _tools/btb_lane)")

print()
print("=== PROTECTED FILES UNTOUCHED ===")
try:
    out = subprocess.run(
        ["git", "status", "--porcelain", "--",
         "analysis/research/base-stats-visual-hunt/coverage.md",
         "analysis/research/base-stats-visual-hunt/polluted-observations.md",
         "analysis/research/base-stats-visual-hunt/archived-hunter-database-2019.tsv",
         "analysis/research/base-stats-visual-hunt/vsfan-wiki-2026-10-05.md",
         "server-ts"],
        capture_output=True, text=True, timeout=60,
    )
    print(out.stdout.strip() or "(clean - no modifications)")
except Exception as e:  # noqa: BLE001
    print("git unavailable:", e)