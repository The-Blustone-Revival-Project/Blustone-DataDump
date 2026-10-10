#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Extract HTML tables cell-by-cell (mirrors the prior lane's method) and print
their headers + first rows, so nothing is inferred from lossy text rendering."""
import os
import re
import sys
import html as htmlmod
from html.parser import HTMLParser

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")


class T(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables = []
        self.stack = []
        self.cur = None
        self.cell = None
        self.row = None

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.stack.append(self.cur)
            self.cur = {"rows": [], "attrs": dict(attrs)}
        elif self.cur is not None and tag == "tr":
            self.row = []
        elif self.cur is not None and tag in ("td", "th"):
            self.cell = {"tag": tag, "attrs": dict(attrs), "text": "",
                         "img": [], "span_classes": []}

    def handle_endtag(self, tag):
        if tag == "table" and self.cur is not None:
            self.tables.append(self.cur)
            self.cur = self.stack.pop() if self.stack else None
        elif self.cur is not None and tag == "tr" and self.row is not None:
            if any(c["text"].strip() or c["img"] for c in self.row):
                self.cur["rows"].append(self.row)
            self.row = None
        elif self.cur is not None and tag in ("td", "th") and self.cell is not None:
            if self.row is not None:
                self.row.append(self.cell)
            self.cell = None

    def handle_data(self, data):
        if self.cell is not None:
            self.cell["text"] += data

    def handle_startendtag(self, tag, attrs):
        if self.cell is not None and tag == "img":
            self.cell["img"].append(dict(attrs).get("src", ""))

    def handle_starttag_img(self):
        pass


def main():
    tag = sys.argv[1]
    filt = sys.argv[2] if len(sys.argv) > 2 else None
    src = os.path.join(RAW, tag + ".utf8.txt")
    with open(src, "r", encoding="utf-8") as fh:
        doc = fh.read()
    p = T()
    p.feed(doc)
    print("TAG", tag, "tables:", len(p.tables))
    for ti, tb in enumerate(p.tables):
        rows = tb["rows"]
        if not rows:
            continue
        flat = " ".join(
            " ".join(c["text"].split()) for r in rows for c in r)
        if filt and filt not in flat:
            continue
        print("\n=== TABLE %d  rows=%d attrs=%s" % (ti, len(rows), tb["attrs"]))
        for r in rows[:14]:
            cells = []
            for c in r:
                t = " ".join(c["text"].split())
                if c["img"]:
                    t += " [IMG:%d]" % len(c["img"])
                cells.append(t[:120])
            print("   | " + " | ".join(cells))


if __name__ == "__main__":
    main()