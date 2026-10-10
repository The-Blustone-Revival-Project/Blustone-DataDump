"""Probe: extract the raw 422653 tables from the archived capture.

Read-only. Prints structure so the note's transcription can be checked
against the actual archived bytes rather than trusted.
"""
import hashlib
import html
import re
import sys

P = r"recovered-assets/forum-en-2026-10-05/pass2/body/422653.html"

b = open(P, "rb").read()
sys.stdout.write("bytes  %d\n" % len(b))
sys.stdout.write("sha256 %s\n" % hashlib.sha256(b).hexdigest())
t = b.decode("utf-8", "replace")
sys.stdout.write("U+FFFD %d\n" % t.count("\ufffd"))

# strip script/style so embedded JS <table> strings do not pollute the count
t2 = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", t)
opens = len(re.findall(r"(?i)<table\b", t2))
closes = len(re.findall(r"(?i)</table\s*>", t2))
sys.stdout.write("tables after script/style strip: open=%d close=%d\n" % (opens, closes))


def rows_of(tbl):
    out = []
    for tr in re.findall(r"(?is)<tr\b.*?</tr>", tbl):
        cells = []
        for m in re.finditer(r"(?is)<t[dh]\b([^>]*)>(.*?)</t[dh]\s*>", tr):
            attr, inner = m.group(1), m.group(2)
            txt = re.sub(r"(?is)<[^>]*>", " ", inner)
            txt = html.unescape(txt)
            txt = re.sub(r"\s+", " ", txt).strip()
            span = re.search(r"(?i)(?:colspan|rowspan)\s*=\s*\"?(\d+)", attr)
            cells.append((txt, int(span.group(1)) if span else 1))
        out.append(cells)
    return out


for i, m in enumerate(re.finditer(r"(?is)<table\b.*?</table\s*>", t2)):
    tbl = m.group(0)
    rs = rows_of(tbl)
    sys.stdout.write("\n=== TABLE %d : %d rows, %d cells total ===\n" % (i, len(rs), sum(len(r) for r in rs)))
    for r in rs:
        sys.stdout.write(" | ".join(c[0] for c in r) + "\n")