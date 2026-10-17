"""Scoped locator: search findings/, datasets/, catalog/, sources/ (all file types,
skipping the multi-GB media directories) for the 100 distinct accessory names and
report every hit with a context window, so any per-item numeric row can be judged.

Read-only.
"""

from __future__ import annotations

import io
import os
import re

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

BASES = ("findings", "datasets", "catalog", "exports", "schemas", "manifests")
SKIP_DIRS = {".git", "__pycache__"}
SKIP_MEDIA = (".png", ".jpg", ".jpeg", ".mp4", ".mp3", ".wav", ".ogg", ".webp", ".gif")


def names() -> list:
    found = set()
    path = os.path.join(REPO, "catalog", "legacy-catalogue-data", "card-catalogue.tsv")
    rows = [l.split("\t") for l in io.open(path, encoding="utf-8").read().split("\n") if l.strip()]
    header = rows[0]
    idx = header.index("accessory")
    for row in rows[1:]:
        if row[idx].strip():
            found.add(row[idx].strip())
    charstr = os.path.join(REPO, "findings", "hunters", "base-stats-visual-hunt",
                           "charstr-items-2026-10-06.tsv")
    crows = [l.split("\t") for l in io.open(charstr, encoding="utf-8").read().split("\n") if l.strip()]
    for row in crows[1:]:
        for cell in row[3:8]:
            if cell.strip():
                found.add(cell.strip())
    for extra in ("Damaged Union Epaulet", "Heat Resistant Railgun Gloves", "Union Epaulet"):
        found.add(extra)
    return sorted(found, key=len, reverse=True)


def main() -> None:
    patterns = [(n, re.compile(re.escape(n).encode("utf-8"), re.I)) for n in names()]
    out = ["distinct search strings: %d" % len(patterns)]
    hits = {}
    scanned = 0
    for base in BASES:
        root = os.path.join(REPO, base)
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for filename in filenames:
                if filename.lower().endswith(SKIP_MEDIA):
                    continue
                path = os.path.join(dirpath, filename)
                try:
                    with open(path, "rb") as handle:
                        data = handle.read()
                except OSError:
                    continue
                scanned += 1
                local = []
                for name, pattern in patterns:
                    for match in pattern.finditer(data):
                        start = max(0, match.start() - 130)
                        end = min(len(data), match.end() + 130)
                        local.append((name, match.start(), data[start:end]))
                if local:
                    hits[os.path.relpath(path, REPO)] = local
    out.append("files scanned: %d" % scanned)
    out.append("files with hits: %d" % len(hits))
    for path in sorted(hits):
        entries = hits[path]
        names_hit = sorted({n for n, _, _ in entries})
        out.append("")
        out.append("=== %s  (%d hits; %d names: %s)"
                   % (path, len(entries), len(names_hit), ", ".join(names_hit[:10])))
        numeric = [e for e in entries if re.search(rb"\d", e[2])]
        out.append("    hits whose +-130 byte window contains a digit: %d" % len(numeric))
        for name, offset, context in numeric[:10]:
            out.append("    +%d %s" % (offset, name))
            out.append("      ctx: %r" % context[:280])
    dest = os.path.join(LANE, "scoped-accessory-name-locator.txt")
    with io.open(dest, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(out) + "\n")
    print("wrote", dest)


if __name__ == "__main__":
    main()
