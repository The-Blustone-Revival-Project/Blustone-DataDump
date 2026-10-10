import re
import sys

p = sys.argv[1]
rows = [l for l in open(p, encoding="utf-8") if l.strip()]
rows = rows[1:] if rows and rows[0].startswith("net,") else rows
print("total rows:", len(rows))
seen = set()
for r in rows:
    f = r.rstrip("\n").split(" ")
    if len(f) < 7:
        continue
    ts, url, mime, status, length = f[1], f[2], f[3], f[4], f[6]
    if "/wiki/" not in url:
        continue
    slug = url.split("/wiki/", 1)[1]
    key = slug
    if key in seen:
        continue
    seen.add(key)
    print(f"{ts}  {status:4s} {mime:12s} len={length:>7s}  {url}")
print("\ndistinct /wiki/ slugs:", len(seen))
