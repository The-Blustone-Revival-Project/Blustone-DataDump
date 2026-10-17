"""Search the recovered LevelDB key/value dump for any entry whose KEY looks
like a per-item equipment / accessory / jewel identifier, and report the value
key-paths present for those groups.

Read-only.
"""

from __future__ import annotations

import io
import json
import os
import re
from collections import Counter, defaultdict

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))), "sources", "client-tables",
    "recovered-data", "leveldb-tables", "all-tables.json")

ITEM_KEY = re.compile(
    r"(?i)(accessor|acce|equip|weapon|armor|armour|jewel|crystal|gem|item|acc_)")
STAT_KEY = re.compile(r"(?i)(hp|atk|def|acc|stat|attack|defense|power|grade|tier|level|value)")


def main() -> None:
    doc = json.loads(io.open(SRC, encoding="utf-8-sig").read())
    tables = doc["tables"]
    out = []
    for name in sorted(tables):
        entries = tables[name]
        if not isinstance(entries, list):
            continue
        matched = [e for e in entries if isinstance(e, dict) and ITEM_KEY.search(str(e.get("key", "")))]
        out.append("%-16s entries=%-6d item-like-keys=%d" % (name, len(entries), len(matched)))
        if not matched:
            continue
        paths = Counter()
        samples = {}
        for entry in matched:
            value = entry.get("json")
            if isinstance(value, dict):
                for key in value:
                    paths[key] += 1
                    samples.setdefault(key, (entry.get("key"), value.get(key)))
        for path, count in paths.most_common(60):
            out.append("    %-24s n=%-6d e.g. %s -> %s"
                       % (path, count, str(samples[path][0])[:48], str(samples[path][1])[:70]))
        # Also brute-force: any key anywhere that looked item-ish
        tops = Counter(str(e.get("key", "")).split("|")[0] for e in matched)
        out.append("    distinct key tops: %d; sample: %s"
                   % (len(tops), ", ".join(list(tops)[:20])))

    # brute-force scan of every value for stat-looking field names
    out.append("")
    out.append("=== brute-force value key scan over ALL tables ===")
    field_counter = Counter()
    field_samples = {}
    for name in sorted(tables):
        entries = tables[name]
        if not isinstance(entries, list):
            continue
        for entry in entries:
            value = entry.get("json") if isinstance(entry, dict) else None
            if not isinstance(value, dict):
                continue
            for key in value:
                if STAT_KEY.search(str(key)) and not re.match(r"(?i)(FONT|SIZE|ALIGN|COLOR|LSPACE|TSPACE|B_RECT|B_SIZE|B_ALIGN|TEXT|LANG|ORI_TXT|ID)", str(key)):
                    field_counter["%s:%s" % (name, key)] += 1
                    field_samples.setdefault("%s:%s" % (name, key), (entry.get("key"), value.get(key)))
    for key, count in field_counter.most_common(80):
        out.append("   %-40s n=%-6d e.g. %s -> %s"
                   % (key, count, str(field_samples[key][0])[:40], str(field_samples[key][1])[:60]))

    dest = os.path.join(LANE, "leveldb-keyed-item-scan.txt")
    with io.open(dest, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(out) + "\n")
    print("wrote", dest)


if __name__ == "__main__":
    main()
