#!/usr/bin/env python3
"""Print the in-game HELP_DATA records that mention Transcendence, verbatim.

Source: analysis/VSFan/Extracted Assets (2026)/1441 (APK)/UI_CSV/*.json
This is FIRST-PARTY in-game help text from the 1.4.4.1 APK. Read-only.
"""
import json
import os
import re
import sys

BASE = r"analysis\VSFan\Extracted Assets (2026)\1441 (APK)\UI_CSV"


def records(path):
    raw = open(path, encoding="utf-8").read()
    # The project notes these files are NOT strict JSON; records are split on
    # the "id": "CONTENTS..." key. Do the same, do not reformat.
    out = []
    idxs = [m.start() for m in re.finditer(r'"id"\s*:\s*"CONTENTS', raw)]
    for i, s in enumerate(idxs):
        e = idxs[i + 1] if i + 1 < len(idxs) else len(raw)
        out.append(raw[s:e])
    return out


def main():
    for fn in sorted(os.listdir(BASE)):
        p = os.path.join(BASE, fn)
        recs = records(p)
        hits = [r for r in recs if re.search(r"transcend", r, re.I)]
        print(f"\n##### {fn}: {len(recs)} CONTENTS records, {len(hits)} mention 'transcend'")
        for r in hits:
            # keep the record id and the human text fields
            m = re.search(r'"id"\s*:\s*"(CONTENTS[\w_]*)"', r)
            print(f"\n--- {m.group(1) if m else '?'} ---")
            # print all key/value string pairs, unescaped
            for km in re.finditer(r'"([^"]+)"\s*:\s*"((?:[^"\\]|\\.)*)"', r):
                k, v = km.group(1), km.group(2)
                try:
                    v = json.loads('"' + v + '"')
                except Exception:
                    pass
                if len(v) > 400:
                    v = v[:400] + f" ...[{len(v)} chars total]"
                print(f"   {k}: {v}")


if __name__ == "__main__":
    main()
