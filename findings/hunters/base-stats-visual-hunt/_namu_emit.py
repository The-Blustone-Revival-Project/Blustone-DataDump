# -*- coding: utf-8 -*-
"""Emit the namu roster as markdown rows plus provenance hashes."""
import hashlib
import io
import json
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

T = os.environ.get("TEMP", ".")
roster = json.load(io.open(os.path.join(T, "namu_roster.json"), encoding="utf-8"))

rows = []
for h in roster:
    cid = h["catalog_id"] or "—"
    ar = h["archive_element_en"] or "—"
    if not h["catalog_id"]:
        verdict = "n/a (unmapped)"
    elif not h["archive_present"]:
        verdict = "n/a (no archive row)"
    else:
        verdict = "AGREE" if h["element_agrees"] else "**DISAGREE**"
    rows.append("| %s | %s | %s | %s | %s | %s★ | %s | %s |" % (
        h["role_en"], h["name_ko_clean"], cid, h["name_en"] or "—",
        h["elem_ko"] + " / " + h["elem_en"], h["grade_stars"], ar, verdict))
md = "\n".join(rows)
io.open(os.path.join(T, "namu_roster.md"), "w", encoding="utf-8", newline="\n").write(md)

print("rows=%d md_chars=%d" % (len(rows), len(md)))
print("ROSTER_MD_SHA256=%s" % hashlib.sha256(md.encode("utf-8")).hexdigest())
print("ROSTER_JSON_SHA256=%s" % hashlib.sha256(
    io.open(os.path.join(T, "namu_roster.json"), "rb").read()).hexdigest())
for n in ("namu_hunter", "namu_offense", "namu_defense", "namu_bomber", "namu_support"):
    p = os.path.join(T, n + ".html")
    if os.path.exists(p):
        print("HTML_SHA256 %-14s %s  (%d bytes)" % (
            n, hashlib.sha256(io.open(p, "rb").read()).hexdigest(),
            os.path.getsize(p)))
    p = os.path.join(T, n + ".txt")
    if os.path.exists(p):
        print("TEXT_SHA256 %-14s %s  (%d chars)" % (
            n, hashlib.sha256(io.open(p, "rb").read()).hexdigest(),
            os.path.getsize(p)))
