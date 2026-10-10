# -*- coding: utf-8 -*-
"""Emit a readable text rendering of the namu 헌터 article.

Tables are emitted row-by-row from the parsed grid (so they survive), prose is
emitted in DOM order between them. Also writes a SHA-256 of the extracted text
for provenance, and a table-only digest for cross-page comparison.
"""
import hashlib
import io
import json
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

sys.path.insert(0, __file__.rsplit("\\", 1)[0].rsplit("/", 1)[0])
from _namu_tables import TableParser, cell_repr  # noqa: E402


def main():
    src, dst = sys.argv[1], sys.argv[2]
    html = io.open(src, encoding="utf-8").read()
    p = TableParser()
    p.feed(html)

    # Walk the DOM in order, emitting tables inline with prose.
    out = []
    # Re-walk with a second parser that records document order.
    class Ordered(TableParser):
        def __init__(self):
            super().__init__()
            self.stream = []   # ('text', s) | ('table', idx)

        def handle_starttag(self, tag, attrs):
            super().handle_starttag(tag, attrs)
            if tag == "table":
                # remember a placeholder position
                self.stream.append(("tablemark", len(self._tstack) - 1))
                self.stream.append(("pendtab", None))
            elif not self._skipdepth and tag in ("p", "div", "li", "h1", "h2", "h3", "h4", "br"):
                self.stream.append(("brk", None))

        def handle_data(self, data):
            if self._skipdepth:
                return
            self.stream.append(("text", data))

    op = Ordered()
    op.feed(html)

    # Rebuild: simple linear scan of raw HTML is more faithful for ordering.
    # Walk tokens of html, emitting text and tables in document order.
    chunks = []
    pos = 0
    tbl_pat = re.compile(r"<table\b.*?</table>", re.S | re.I)
    for m in tbl_pat.finditer(html):
        seg = html[pos:m.start()]
        chunks.append(("prose", seg))
        chunks.append(("table", m.group(0)))
        pos = m.end()
    chunks.append(("prose", html[pos:]))

    ti = 0
    for kind, payload in chunks:
        if kind == "table":
            out.append("\n\n===== TABLE %d =====\n" % ti)
            tp = TableParser()
            tp.feed(payload)
            if tp.tables:
                t = tp.tables[0]
                for r, row in enumerate(t["grid"]):
                    cells = [cell_repr(c) for c in row]
                    if not any(x.strip() for x in cells):
                        continue
                    out.append("r%02d | %s\n" % (r, " || ".join(x.strip() for x in cells)))
            ti += 1
        else:
            seg = re.sub(r"(?is)<(script|style|noscript|svg)\b.*?</\1>", " ", payload)
            seg = re.sub(r"(?is)<br\s*/?>", "\n", seg)
            seg = re.sub(r"(?is)</(p|div|li|h1|h2|h3|h4|tr)>", "\n", seg)
            seg = re.sub(r"(?is)<img[^>]*alt=[\"']([^\"']*)[\"'][^>]*>", r" [img:\1] ", seg)
            seg = re.sub(r"(?s)<[^>]+>", " ", seg)
            seg = (seg.replace("&nbsp;", " ").replace("&amp;", "&")
                      .replace("&lt;", "<").replace("&gt;", ">")
                      .replace("&#39;", "'").replace("&quot;", '"')
                      .replace("&#x27;", "'").replace("&mdash;", "-"))
            seg = re.sub(r"[ \t\u00a0]+", " ", seg)
            seg = re.sub(r"\n\s*\n\s*\n+", "\n\n", seg)
            seg = seg.strip()
            if seg:
                out.append(seg + "\n")

    text = "".join(out)
    text = re.sub(r"\r\n?", "\n", text)
    io.open(dst, "w", encoding="utf-8", newline="\n").write(text)

    tnorm = "\n".join(
        " | ".join(cell_repr(c) for c in t["grid"][r])
        for t in p.tables for r in range(len(t["grid"]))
    )
    tnorm = re.sub(r"[ \t]+", " ", tnorm)
    print("chars=%d lines=%d" % (len(text), text.count("\n") + 1))
    print("TEXT_SHA256=%s" % hashlib.sha256(text.encode("utf-8")).hexdigest())
    print("TABLETEXT_SHA256=%s" % hashlib.sha256(tnorm.encode("utf-8")).hexdigest())
    print("tables=%d" % len(p.tables))
    print("U+FFFD=%d" % text.count("\ufffd"))


if __name__ == "__main__":
    main()
