"""Dump every UI_JSON_RO / UI_TEXT_RO key group whose key names equipment,
accessories, jewels or substats, plus the full SR_EQUIP / SR_GEM UI_XML_RO
layout records, so per-item stat rows can be ruled in or out.

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

GROUP = re.compile(r"(?i)(accessor|acce|equip|weapon|armor|armour|jewel|crystal|gem|"
                   r"item|acc_|보조스탯|보석|장비|스탯|강화|등급|레벨)")


def main() -> None:
    doc = json.loads(io.open(SRC, encoding="utf-8-sig").read())
    tables = doc["tables"]
    out = []

    ui_json = tables["UI_JSON_RO"]
    matched = [e for e in ui_json if GROUP.search(str(e.get("key", "")))]
    out.append("UI_JSON_RO item/stat-like keys: %d / %d" % (len(matched), len(ui_json)))
    groups = defaultdict(list)
    for entry in matched:
        key = str(entry["key"])
        top = key.split("|")[0]
        groups[top].append(entry)
    out.append("distinct key tops: %d" % len(groups))
    for top in sorted(groups):
        entries = groups[top]
        locales = Counter()
        texts = {}
        for entry in entries:
            parts = str(entry["key"]).split("|")
            locale = parts[-1] if len(parts) >= 2 else ""
            locales[locale] += 1
            if locale == "EN":
                texts[str(entry["key"])] = entry.get("json", {}).get("TEXT")
        out.append("")
        out.append("### %s  (n=%d, locales=%s)" % (top, len(entries), dict(locales)))
        for key, text in list(texts.items())[:20]:
            out.append("    %-60s EN=%r" % (key[:60], text))

    ui_text = tables["UI_TEXT_RO"]
    matched_text = [e for e in ui_text if GROUP.search(str(e.get("key", "")))]
    out.append("")
    out.append("UI_TEXT_RO item/stat-like keys: %d / %d" % (len(matched_text), len(ui_text)))
    for entry in matched_text[:60]:
        out.append("    %-60s %r" % (str(entry.get("key"))[:60],
                                     json.dumps(entry.get("json"), ensure_ascii=False)[:160]))

    ui_xml = tables["UI_XML_RO"]
    out.append("")
    out.append("UI_XML_RO keys (all %d):" % len(ui_xml))
    for entry in ui_xml:
        out.append("    %s" % entry.get("key"))

    dest = os.path.join(LANE, "leveldb-ui-item-groups.txt")
    with io.open(dest, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(out) + "\n")
    print("wrote", dest, "lines", len(out))


if __name__ == "__main__":
    main()
