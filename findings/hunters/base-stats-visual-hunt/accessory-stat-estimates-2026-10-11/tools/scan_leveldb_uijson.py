"""Enumerate every key and value key-path in the recovered LevelDB table dump,
looking for per-item equipment / accessory / jewel stat rows.

Read-only: parses sources/client-tables/recovered-data/leveldb-tables/all-tables.json
in memory and writes a summary under this lane.
"""

from __future__ import annotations

import io
import json
import os
import re
from collections import Counter

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))), "sources", "client-tables",
    "recovered-data", "leveldb-tables", "all-tables.json")

STAT_TOKEN = re.compile(r"(?i)\b(hp|atk|def|acc|accessory|equip|item|jewel|crystal|gem|stat|attack|defense|maxhp|power|grade|tier)\b")


def key_paths(value, prefix="", depth=0, limit=6):
    if depth > limit:
        return
    if isinstance(value, dict):
        for key, sub in value.items():
            yield prefix + "/" + str(key), sub
            yield from key_paths(sub, prefix + "/" + str(key), depth + 1, limit)
    elif isinstance(value, list):
        if value:
            yield prefix + "/[]", value[0]
            yield from key_paths(value[0], prefix + "/[]", depth + 1, limit)


def main() -> None:
    doc = json.loads(io.open(SRC, encoding="utf-8-sig").read())
    tables = doc["tables"]
    report = []
    report.append("tables: %s" % ", ".join("%s(%d)" % (k, len(v)) for k, v in sorted(tables.items())))

    for name, entries in sorted(tables.items()):
        if not isinstance(entries, (list, dict)):
            report.append("%s: unsupported shape %s" % (name, type(entries)))
            continue
        items = entries.items() if isinstance(entries, dict) else enumerate(entries)
        prefix_counter = Counter()
        token_counter = Counter()
        sample = {}
        for key, value in items:
            text_key = str(key)
            top = text_key.split("|")[0]
            prefix_counter[top] += 1
            paths = list(key_paths(value))
            for path, sub in paths:
                if isinstance(sub, (dict, list)):
                    continue
                if STAT_TOKEN.search(path):
                    token_counter[path] += 1
                    sample.setdefault(path, (text_key, sub))
        report.append("")
        report.append("=== %s ===" % name)
        report.append("key top-level prefixes (first 25): %s"
                      % ", ".join("%s=%d" % kv for kv in prefix_counter.most_common(25)))
        report.append("distinct key tops: %d" % len(prefix_counter))
        report.append("stat-like value key-paths: %d" % len(token_counter))
        for path, count in token_counter.most_common(40):
            text_key, sub = sample[path]
            report.append("   %-58s n=%-6d e.g. %s -> %r" % (path, count, text_key[:40], str(sub)[:60]))

    dest = os.path.join(LANE, "leveldb-uijson-key-scan.txt")
    with io.open(dest, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(report) + "\n")
    print("wrote", dest)


if __name__ == "__main__":
    main()
