"""Probe 2: extract the readable body + reply prose of 422653 (and 421776).

The tables alone cannot say what the 4,208 pool IS. The prose is the
authority on that. Read-only.
"""
import html
import re
import sys


def prose(path, limit=9000):
    b = open(path, "rb").read()
    t = b.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", t)
    # the document div used by this template
    m = re.search(r'(?is)<div[^>]*class="[^"]*xe_content[^"]*"[^>]*>(.*)', t)
    body = m.group(1) if m else t
    # cut at the trailing list/board furniture
    for stop in ("<!--#ecBoard-->", "ec_board", 'class="boardList', "Subject+Content"):
        i = body.find(stop)
        if i > 2000:
            body = body[:i]
    body = re.sub(r"(?is)<br\s*/?>", "\n", body)
    body = re.sub(r"(?is)</(p|div|li|h[1-6]|tr)>", "\n", body)
    body = re.sub(r"(?is)<table\b.*?</table\s*>", "\n[TABLE OMITTED]\n", body)
    body = re.sub(r"(?s)<[^>]*>", " ", body)
    body = html.unescape(body)
    body = re.sub(r"[ \t\xa0]+", " ", body)
    body = re.sub(r"\n\s*\n\s*\n+", "\n\n", body)
    return body.strip()[:limit]


OUT = r"analysis/research/base-stats-visual-hunt/_trace_cost_prose.txt"
buf = []
for p in sys.argv[1:]:
    buf.append("\n" + "=" * 78 + "\n%s\n" % p + "=" * 78 + "\n")
    buf.append(prose(p) + "\n")
open(OUT, "w", encoding="utf-8", newline="\n").write("".join(buf))
sys.stdout.write("wrote %s\n" % OUT)