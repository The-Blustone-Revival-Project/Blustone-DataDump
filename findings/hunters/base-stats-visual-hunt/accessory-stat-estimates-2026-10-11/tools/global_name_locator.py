"""Global locator search: does ANY local file contain an item/equipment/accessory
identifier paired with a numeric stat? Searches the whole workspace (skipping
.git and __pycache__) for the 100 distinct accessory names in all five locales
and reports every file with a hit, plus a ±120-character context window so any
adjacent numerals can be judged.

Read-only.
"""

from __future__ import annotations

import io
import os
import re
import sys

WORKSPACE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

SKIP_DIRS = {".git", "__pycache__", "node_modules"}
# Only text-plausible containers get decoded; binaries are still searched raw.
TEXT_EXT = {
    ".json", ".tsv", ".csv", ".txt", ".md", ".py", ".rw", ".bin", ".xml",
    ".properties", ".yaml", ".yml", ".log", ".ts", ".js", ".html",
}


def load_accessory_names() -> dict:
    """EN/JA/KO/SC/TC names for the 100 distinct accessories (card catalogue)."""
    path = os.path.join(WORKSPACE, "catalog", "legacy-catalogue-data", "card-catalogue.tsv")
    rows = [line.split("\t") for line in
            io.open(path, encoding="utf-8").read().split("\n") if line.strip()]
    header = rows[0]
    idx = {name: i for i, name in enumerate(header)}
    names = {}
    for row in rows[1:]:
        name = row[idx["accessory"]].strip()
        if name:
            names[name] = name
    # charstr fallback for the three awakened-form names absent from the catalogue
    extra = {"Damaged Union Epaulet", "Heat Resistant Railgun Gloves", "Union Epaulet"}
    for name in extra:
        names.setdefault(name, name)
    charstr = os.path.join(WORKSPACE, "findings", "hunters", "base-stats-visual-hunt",
                           "charstr-items-2026-10-06.tsv")
    crows = [line.split("\t") for line in
             io.open(charstr, encoding="utf-8").read().split("\n") if line.strip()]
    for row in crows[1:]:
        if len(row) > 7:
            for cell in row[3:8]:
                cell = cell.strip()
                if cell:
                    names.setdefault(cell, cell)
    return names


def main() -> None:
    names = sorted(set(load_accessory_names().values()), key=len, reverse=True)
    patterns = [(name, re.compile(re.escape(name).encode("utf-8"), re.I)) for name in names]
    out = []
    out.append("distinct search strings: %d" % len(patterns))
    hits = {}
    scanned = 0
    for dirpath, dirnames, filenames in os.walk(WORKSPACE):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for filename in filenames:
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
                    start = max(0, match.start() - 120)
                    end = min(len(data), match.end() + 120)
                    local.append((name, match.start(), data[start:end]))
            if local:
                hits[os.path.relpath(path, WORKSPACE)] = local
    out.append("files scanned: %d" % scanned)
    out.append("files with accessory-name hits: %d" % len(hits))
    for path in sorted(hits):
        entries = hits[path]
        names_hit = sorted({n for n, _, _ in entries})
        out.append("")
        out.append("=== %s  (%d hits; names: %s)"
                   % (path, len(entries), ", ".join(names_hit[:8])))
        for name, offset, context in entries[:6]:
            out.append("    +%d %s" % (offset, name))
            out.append("      ctx: %r" % context[:260])
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "..", "global-accessory-name-locator.txt")
    with io.open(dest, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(out) + "\n")
    print("wrote", os.path.normpath(dest), "hits", len(hits))


if __name__ == "__main__":
    main()
