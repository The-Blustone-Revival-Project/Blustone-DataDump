"""Decode every equipment / gem / item JET chunk in the recovered corpus and
report every logical resource, its shape, and any readable text.

Read-only. Uses the repository JET decoder (tools/extract/jet-viewer).
"""

from __future__ import annotations

import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(HERE)))))
sys.path.insert(0, os.path.join(REPO, "tools", "extract", "jet-viewer"))

from jet_decoder import extract_strings, inflate_jet_resources  # noqa: E402

JETS = [
    r"local\inputs\extracted\assets\EQUIP.jet",
    r"local\inputs\extracted\assets\E_GEM_DEFALT.jet",
    r"local\inputs\extracted\assets\GEM.jet",
    r"local\inputs\extracted\assets\GEM_CHA.jet",
    r"local\inputs\extracted\assets\GEM_EFT.jet",
    r"local\inputs\extracted\assets\GEM_SELECT.jet",
    r"local\inputs\extracted\assets\LEVELING.jet",
    r"local\inputs\extracted\assets\MP4_GEM.jet",
    r"local\inputs\extracted\assets\UI_GEM.jet",
    r"local\inputs\extracted\assets\UI_ITEM.jet",
    r"local\inputs\extracted\assets\UI_ITEM_CHA.jet",
    r"local\private\recovered-assets\phone-2026-09-18\extracted\split_PADResource\assets\UI_ITEM.jet",
]

TOKEN = re.compile(rb"(?i)[A-Za-z_]{2,}")


def printable_ratio(payload: bytes) -> float:
    if not payload:
        return 0.0
    sample = payload[:4096]
    return sum(1 for b in sample if 9 <= b <= 13 or 32 <= b <= 126) / len(sample)


def main() -> None:
    out = []
    for rel in JETS:
        path = os.path.join(REPO, rel)
        if not os.path.exists(path):
            out.append("MISSING %s" % rel)
            continue
        data = open(path, "rb").read()
        resources = inflate_jet_resources(data)
        out.append("")
        out.append("=== %s  (%d logical resources, %d raw bytes)" % (rel, len(resources), len(data)))
        for index, (offset, payload, chunks) in enumerate(resources):
            head = payload[:8]
            ratio = printable_ratio(payload)
            strings = extract_strings(payload) if ratio > 0.5 else []
            # count how many ASCII tokens carry digits nearby
            numeric = len(re.findall(rb"[A-Za-z_]{2,}[\"'\s:=|,>-]*\d", payload))
            out.append("  [%02d] +%08x %8d B x%d head=%r print=%.2f strings=%d numeric=%d"
                       % (index, offset, len(payload), chunks, head, ratio, len(strings), numeric))
            if strings:
                for value in strings[:40]:
                    out.append("        | %s" % value[:180])
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jet-equipment-corpus.txt")
    with io.open(dest, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(out) + "\n")
    print("wrote", dest)


if __name__ == "__main__":
    main()
