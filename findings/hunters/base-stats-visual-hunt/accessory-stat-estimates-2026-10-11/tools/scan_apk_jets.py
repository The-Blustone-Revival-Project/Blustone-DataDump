"""Scan every .jet / .jt2 asset inside the recovered VSFan 1.4.4.1 APK for
text-bearing resources, and report any that look like item / equipment /
accessory stat tables.

Read-only: the APK is opened as a zip and entries are decoded in memory.
"""

from __future__ import annotations

import io
import os
import re
import sys
import zipfile

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.insert(0, os.path.join(REPO, "tools", "extract", "jet-viewer"))

from jet_decoder import extract_strings, inflate_jet_resources  # noqa: E402

APK = os.path.join(
    REPO, "sources", "community", "raw", "VSFan", "Extracted Assets (2026)",
    "com-vshower-prd-sr-1441-39567016-ef64fd3f499bd158a709f4c380d3c06d.apk",
)

# Stat-ish tokens that would indicate a per-item value table.
KEYS = [
    "HP", "ATK", "DEF", "ACC", "EQUIP", "ITEM", "ACCESSORY", "JEWEL",
    "CRYSTAL", "GEM", "STAT", "ABILITY", "GRADE", "RANK", "LEVEL",
    "UPGRADE", "STRENGTH", "ATTACK", "DEFENSE", "MAXHP", "POWER",
    "cost", "rupee", "money", "gold",
]
# Literal names from the shipped CHAR_STR table (all locales) to cross-check.
NAME_HINTS = [
    "Judecca", "Tribe", "Mandarin", "Crossbody", "Cerberus", "Iron Bag",
    "Pendant", "Bracelet", "Epaulet", "Gauntlet", "Hair Tie", "Lucky Coin",
    "Grenade", "Strap", "Knot", "Patch", "Fanny", "Cannon", "Necklace",
    "Chocolate", "Messenger", "Choker", "Clip", "Necklace", "Headband",
]


def interest(text: str) -> list[str]:
    hits = []
    for key in KEYS:
        for match in re.finditer(r"(?<![A-Za-z])" + re.escape(key) + r"(?![A-Za-z])", text):
            hits.append(key)
            break
    for name in NAME_HINTS:
        if name in text:
            hits.append("NAME:" + name)
    return hits


def main() -> None:
    out = []
    with zipfile.ZipFile(APK) as archive:
        entries = [n for n in archive.namelist() if n.lower().endswith((".jet", ".jt2"))]
        for name in sorted(entries):
            data = archive.read(name)
            logical = inflate_jet_resources(data)
            out.append("%-34s %9d B  %d logical resources" % (name, len(data), len(logical)))
            for offset, payload, chunks in logical:
                printable = sum(1 for b in payload[:4096] if 9 <= b <= 13 or 32 <= b <= 126)
                ratio = printable / min(len(payload), 4096) if payload else 0
                head = payload[:24]
                strings = extract_strings(payload) if ratio > 0.72 else []
                text = "\n".join(strings)
                hits = interest(text) if text else []
                if strings and (hits or head.startswith((b"RW", b"RWM"))):
                    out.append("    +%08x %8d B  x%d  head=%r  strings=%d  hits=%s"
                               % (offset, len(payload), chunks, head, len(strings), sorted(set(hits))[:12]))
                    # Print a short window of the first few stat-relevant strings.
                    shown = [s for s in strings if any(k in s for k in KEYS)][:12]
                    for s in shown:
                        out.append("        | " + s[:200])
    report = "\n".join(out)
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "apk-jet-scan.txt")
    with io.open(dest, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(report + "\n")
    print("wrote", dest, len(report), "chars")


if __name__ == "__main__":
    main()
