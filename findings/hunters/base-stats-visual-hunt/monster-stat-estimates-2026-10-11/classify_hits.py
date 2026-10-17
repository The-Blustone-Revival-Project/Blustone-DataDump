#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
classify_hits.py -- separate DATA-ROW hits (a monster ID bound to a value, e.g.
`"res_id": "M001"`) from PROSE/filename mentions, per catalog monster id.

Reads monster-id-workspace-census.json (produced by search_monster_ids.py) and
writes monster-id-hit-classification.tsv. Read-only w.r.t. everything outside
the output folder.
"""
import io, json, os, re, collections

ROOT = r"C:\Users\shaha\Documents\GitHub\Blustone-DataDump"
OUT = os.path.join(ROOT, "findings", "hunters", "base-stats-visual-hunt",
                   "monster-stat-estimates-2026-10-11")
CATALOG = ["M%03d" % i for i in range(1, 22)] + ["M100"]

# a "data row" = the id appears adjacent to a key name, or as a JSON value of a
# recognised field, or with a numeric stat nearby
DATA_RE = [
    re.compile(r'"(?:res_id|ref_id|monster_id|id|actor_id|thumb|card_id|monster)"\s*:\s*"?' + "M", re.I),
    re.compile(r'"M\d{3}"\s*:'),
    re.compile(r'\bM\d{3}\s*[=:]\s*\d'),
    re.compile(r'"(?:hp|atk|def)"\s*:\s*"?\d'),
    re.compile(r'\bM\d{3}\b[^\n]{0,40}\b(?:hp|atk|def|HP|ATK|DEF)\b[^\n]{0,40}\d'),
    re.compile(r'M\d{3}\.jet'),
    re.compile(r'M\d{3}[\w.]*'),   # loose: any attachment like M001.something
]
PROSE_MARK = re.compile(
    r'`M\d{3}`|\bM\d{3}\b(?=[^\n]{0,60}(?:penguin|monster|Unknown|UNKNOWN|enemy|catalog|stat))',
    re.I)


def main():
    d = json.load(io.open(os.path.join(OUT, "monster-id-workspace-census.json"),
                          encoding="utf-8"))
    hits = d["hits"]
    rows = []
    for mid in CATALOG:
        hs = hits.get(mid, [])
        by_file = collections.defaultdict(list)
        for f, ln, ctx in hs:
            by_file[f].append((ln, ctx))
        data_files, prose_files = [], []
        for f in sorted(by_file):
            n_data = 0
            for ln, ctx in by_file[f]:
                if any(r.search(ctx) for r in DATA_RE):
                    n_data += 1
            if n_data:
                data_files.append((f, n_data, len(by_file[f])))
            else:
                prose_files.append((f, len(by_file[f])))
        rows.append((mid, len(hs), data_files, prose_files))

    with io.open(os.path.join(OUT, "monster-id-hit-classification.tsv"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write("monster_id\ttotal_hits\tfiles_total\tfiles_with_data_row\thits_in_data_rows\t"
                "data_files\tprose_only_files\n")
        for mid, n, df, pf in rows:
            f.write("%s\t%d\t%d\t%d\t%d\t%s\t%s\n"
                    % (mid, n, len(df) + len(pf), len(df),
                       sum(x[1] for x in df),
                       " ; ".join("%s(%d/%d)" % x for x in df[:12]),
                       " ; ".join("%s(%d)" % x for x in pf[:12])))

    for mid, n, df, pf in rows:
        print("\n=== %s  hits=%d  data-row files=%d  prose-only files=%d"
              % (mid, n, len(df), len(pf)))
        for f, nd, nt in df[:14]:
            print("   DATA  %-70s %d/%d lines" % (f, nd, nt))
        for f, nt in pf[:8]:
            print("   prose %-70s %d lines" % (f, nt))
    print("\nwrote monster-id-hit-classification.tsv")


if __name__ == "__main__":
    main()
