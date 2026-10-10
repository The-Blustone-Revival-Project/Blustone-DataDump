import json
import os
import re

base = os.path.expandvars(r"%TEMP%\opencode\zh\vids")
for f in ("_dl.json", "_dl2.json"):
    p = os.path.join(base, f)
    d = json.load(open(p, encoding="utf-8"))
    print("=====", f, type(d).__name__)
    s = json.dumps(d, ensure_ascii=False, indent=1)
    hits = list(re.finditer(r".{0,500}av38052023.{0,500}", s))
    print("matches:", len(hits))
    for m in hits:
        print(m.group(0))
        print("-" * 60)