"""Extract every equipment / accessory / jewel / slot context window from the
corpus's own estimate and revival documents, so the derivation model can quote
its anchors verbatim.

Read-only.
"""

from __future__ import annotations

import io
import os
import re

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

TARGETS = [
    r"findings\hunters\base-stats-visual-hunt\STATS-ESTIMATE-2026-10-08.md",
]

# extra pattern sets, searched recursively over findings/ and datasets/
PATTERNS = [
    r"accessor", r"jewel", r"gem\b", r"equipment", r"slot",
    r"HP\s*260", r"134", r"102",
]
KEY = re.compile(r"(?i)accessor|jewel|\bgem\b|equipment| slots? |accessory")


def snippets(text: str, pattern: re.Pattern, width: int = 400):
    out = []
    for match in pattern.finditer(text):
        start = max(0, match.start() - width)
        end = min(len(text), match.end() + width)
        out.append(text[start:end].replace("\n", " "))
    return out


def main() -> None:
    out = []
    for rel in TARGETS:
        path = os.path.join(REPO, rel)
        text = io.open(path, encoding="utf-8").read()
        pattern = re.compile(r"(?i)accessor|jewel|\bgem\b|equipment")
        found = snippets(text, pattern)
        out.append("=== %s: %d hits" % (rel, len(found)))
        for item in found:
            out.append("  ... %s ..." % item)
    # Broad sweep of findings/ + datasets/ for accessory numbers
    hits_total = 0
    out.append("")
    out.append("=== recursive sweep of findings/ and datasets/ ===")
    for base in ("findings", "datasets"):
        root = os.path.join(REPO, base)
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
            for filename in filenames:
                if not filename.lower().endswith((".md", ".tsv", ".csv", ".txt")):
                    continue
                path = os.path.join(dirpath, filename)
                try:
                    text = io.open(path, encoding="utf-8", errors="replace").read()
                except OSError:
                    continue
                for match in KEY.finditer(text):
                    hits_total += 1
    out.append("keyword hits across findings/ + datasets/ text files: %d" % hits_total)
    dest = os.path.join(LANE, "corpus-accessory-context.txt")
    with io.open(dest, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(out) + "\n")
    print("wrote", dest)


if __name__ == "__main__":
    main()
