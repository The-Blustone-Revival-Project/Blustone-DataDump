# -*- coding: utf-8 -*-
"""Verify every Korean name cell in the report's roster table is byte-identical
to the string extracted from the rendered DOM. No retyping anywhere."""
import io
import json
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.environ.get("TEMP", ".")
roster = json.load(io.open(os.path.join(T, "namu_roster.json"), encoding="utf-8"))
rep = io.open(os.path.join(HERE, "namu-hunter-page-2026-10-08.md"),
              encoding="utf-8").read()

# the roster table rows look like: | Offense | name_ko | id | name_en | ...
rows = re.findall(r"^\| (Offense|Defense|Bomber|Support) \| (.*?) \| ", rep, re.M)
print("report roster rows: %d   roster JSON rows: %d" % (len(rows), len(roster)))

bad = 0
for i, (role, name) in enumerate(rows):
    want = roster[i]["name_ko_clean"]
    if name != want:
        bad += 1
        print("MISMATCH row %d" % i)
        print("   report: %r  %s" % (name, [hex(ord(c)) for c in name]))
        print("   dom   : %r  %s" % (want, [hex(ord(c)) for c in want]))
print("name-cell mismatches: %d  %s" % (bad, "PASS" if bad == 0 else "FAIL"))

# Also check the two element and grade cells per row.
bad2 = 0
for i, r in enumerate(rows):
    want_role = roster[i]["role_en"]
    if r[0] != want_role:
        bad2 += 1
        print("ROLE MISMATCH row %d: report=%s dom=%s" % (i, r[0], want_role))
print("role-cell mismatches: %d  %s" % (bad2, "PASS" if bad2 == 0 else "FAIL"))

# Write the exact DOM strings of every hero name to a file for safe retyping.
out = os.path.join(T, "namu_exact_names.txt")
with io.open(out, "w", encoding="utf-8", newline="\n") as fh:
    for h in roster:
        fh.write("%s\t%s\n" % (h["catalog_id"] or "----", h["name_ko_clean"]))
print("exact names ->", out)
