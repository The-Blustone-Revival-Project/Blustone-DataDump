# -*- coding: utf-8 -*-
"""Verify the report: U+FFFD == 0, no CRLF, and the Korean survived intact."""
import io
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

P = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 "namu-hunter-page-2026-10-08.md")
b = io.open(P, "rb").read()
t = b.decode("utf-8", "strict")

print("bytes            : %d" % len(b))
print("chars            : %d" % len(t))
print("U+FFFD           : %d   %s" % (t.count("\ufffd"),
                                       "PASS" if t.count("\ufffd") == 0 else "FAIL"))
print("CR bytes         : %d   %s" % (b.count(b"\r"),
                                       "PASS" if b.count(b"\r") == 0 else "FAIL"))
print("CRLF pairs       : %d   %s" % (t.count("\r\n"),
                                       "PASS" if t.count("\r\n") == 0 else "FAIL"))
print("ends with LF     : %s" % ("PASS" if b.endswith(b"\n") else "FAIL"))

# Korean must be byte-identical to what the DOM gave us. Hero-name probes are
# DERIVED from the rendered DOM, never hand-typed, so this check cannot itself
# introduce the very mojibake it is looking for.
import json  # noqa: E402

_T = os.environ.get("TEMP", ".")
_roster = json.load(io.open(os.path.join(_T, "namu_roster.json"), encoding="utf-8"))
_by_id = {h["catalog_id"]: h for h in _roster if h["catalog_id"]}

KO_PROBES = {
    _by_id["033"]["name_ko_clean"]: 1,          # Patrone  (roster row only)
    _by_id["014"]["name_ko_clean"]: 1,          # Locke    (roster row only)
    _by_id["065"]["name_ko_clean"]: 2,          # Teresa   (roster + §6.3)
    _by_id["057"]["name_ko_clean"]: 2,          # Pansy    (roster + §6.2)
    _by_id["023"]["name_ko_clean"]: 1,          # Hermes
    _by_id["036"]["name_ko_clean"]: 1,          # Bear
    "등급에 상관없이 30레벨이 최대": 1,
    "타게임의 초월과 비슷한 개념": 1,
    "(2^n)×10개": 1,
    "냉기 > 화염 > 전격 > 냉기": 1,
    "0/3/1": 1,
    "火炎": 2,
    "冷気": 2,
}
# Substrings that must NOT appear: mojibake sentinels and a malformed grade cell.
NEG_PROBES = ["한자匠", "시키beda", "�", "☆☆ ☆☆ [53]"]
print("\nKorean/term integrity probes:")
bad = 0
for s, expect in KO_PROBES.items():
    n = t.count(s)
    ok = (n == expect)
    if not ok:
        bad += 1
    print("  %-34s count=%d expect=%d %s"
          % (s, n, expect, "ok" if ok else "MISMATCH"))
print("\nprobe mismatches: %d  %s" % (bad, "PASS" if bad == 0 else "FAIL"))
print("negative probes (must be absent):")
nb = 0
for s in NEG_PROBES:
    n = t.count(s)
    if n:
        nb += 1
    print("  %-20s count=%d %s" % (s, n, "ok" if n == 0 else "UNEXPECTED"))
print("negative-probe failures: %d  %s" % (nb, "PASS" if nb == 0 else "FAIL"))

# required content anchors
anchors = ["최근 수정 시각: 2026-10-03 11:15:24",
           "a53213d31d07b181f785573d8500b6bd8551e80379da680eb33ea2e7b9d33cde",
           "1/113", "1/100", "0/22",
           "Pansy", "DISAGREE", "positive control", "Positive control"]
print("\ncontent anchors:")
for a in anchors:
    print("  %-56s %s" % (a[:56], "ok" if a in t else "MISSING"))
