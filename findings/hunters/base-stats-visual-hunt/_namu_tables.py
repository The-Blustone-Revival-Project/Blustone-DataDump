# -*- coding: utf-8 -*-
"""Parse the rendered namu 헌터 DOM dump into full table grids.

Walks table.rows equivalent structure: builds a real 2-D grid honouring
rowspan/colspan, and records cell text plus any <img alt> text (namu renders
most hunter entries as image cards whose alt carries the name).

Reads only a local rendered HTML dump. Writes only temp output.
"""
import io
import json
import re
import sys
from html.parser import HTMLParser

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

CELL_TAGS = {"td", "th"}
SKIP_TAGS = {"script", "style", "noscript", "svg", "template"}


class TableParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables = []            # list of dicts
        self._tstack = []           # nested table stack
        self._row = None            # current <tr> being built
        self._cell = None           # current cell being built
        self._skipdepth = 0
        self._imgalt = []           # alt texts seen inside the current cell

    # -- helpers
    @staticmethod
    def _attrs_int(d, key, default=1):
        v = d.get(key)
        if v is None:
            return default
        m = re.match(r"\s*(\d+)", str(v))
        return int(m.group(1)) if m else default

    def _finish_cell(self):
        if self._cell is None:
            return
        txt = self._cell["parts"]
        cell = {
            "text": " ".join(" ".join(txt).split()),
            "alts": list(self._cell["alts"]),
            "rowspan": self._cell["rowspan"],
            "colspan": self._cell["colspan"],
            "header": self._cell["header"],
            "html_len": self._cell["html_len"],
        }
        self._cell = None
        self._row["cells"].append(cell)

    def _finish_row(self):
        if self._row is None:
            return
        self._finish_cell()
        self._tstack[-1]["raw"].append(self._row["cells"])
        self._row = None

    def _finish_table(self):
        self._finish_row()
        t = self._tstack.pop()
        rows = t["raw"]
        # expand into a rectangular grid honouring rowspan/colspan
        grid = []
        occupied = {}   # (r,c) -> cell dict already placed
        for r, cells in enumerate(rows):
            grid.append([])
            c = 0
            for cell in cells:
                while (r, c) in occupied:
                    grid[r].append(occupied[(r, c)])
                    c += 1
                for dr in range(cell["rowspan"]):
                    for dc in range(cell["colspan"]):
                        occ_r, occ_c = r + dr, c + dc
                        while len(grid) <= occ_r:
                            grid.append([])
                        while len(grid[occ_r]) <= occ_c:
                            grid[occ_r].append(None)
                        if dr == 0 and dc == 0:
                            grid[occ_r][occ_c] = cell
                        else:
                            grid[occ_r][occ_c] = {"text": "", "alts": [],
                                                  "rowspan": 0, "colspan": 0,
                                                  "header": False, "html_len": 0,
                                                  "spanned": True}
                for dr in range(cell["rowspan"]):
                    for dc in range(cell["colspan"]):
                        occupied[(r + dr, c + dc)] = grid[r + dr][c + dc] if (dr == 0 and dc == 0) else {"text": "", "alts": [], "rowspan": 0, "colspan": 0, "header": False, "html_len": 0, "spanned": True}
                c += cell["colspan"]
        width = max((len(x) for x in grid), default=0)
        for row in grid:
            while len(row) < width:
                row.append({"text": "", "alts": [], "rowspan": 0, "colspan": 0,
                            "header": False, "html_len": 0, "blank": True})
        self.tables.append({
            "index": len(self.tables),
            "raw_row_count": len(rows),
            "grid_width": width,
            "row_count": len(grid),
            "header_row_count": sum(1 for r in grid
                                    if any(c["header"] for c in r)),
            "grid": grid,
        })

    # -- HTMLParser hooks
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in SKIP_TAGS:
            if tag != "svg" or self._skipdepth == 0:
                self._skipdepth += 1
            return
        if self._skipdepth:
            return
        if tag == "table":
            self._finish_row()
            self._tstack.append({"raw": []})
            return
        if not self._tstack:
            return
        if tag == "tr":
            self._finish_row()
            self._row = {"cells": []}
            return
        if tag in CELL_TAGS and self._row is not None:
            self._finish_cell()
            self._cell = {
                "parts": [], "alts": [],
                "rowspan": self._attrs_int(a, "rowspan", 1),
                "colspan": self._attrs_int(a, "colspan", 1),
                "header": tag == "th",
                "html_len": 0,
            }
            return
        if self._cell is not None:
            if tag == "br":
                self._cell["parts"].append(" ")
            if tag == "img":
                alt = a.get("alt")
                if alt:
                    self._cell["alts"].append(alt)
                    self._cell["parts"].append(" [img:%s] " % alt)

    def handle_startendtag(self, tag, attrs):
        a = dict(attrs)
        if tag in SKIP_TAGS or self._skipdepth:
            return
        if tag == "img" and self._cell is not None:
            alt = a.get("alt")
            if alt:
                self._cell["alts"].append(alt)
                self._cell["parts"].append(" [img:%s] " % alt)

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS:
            if self._skipdepth:
                self._skipdepth -= 1
            return
        if self._skipdepth:
            return
        if tag in CELL_TAGS and self._cell is not None:
            self._finish_cell()
            return
        if tag == "tr":
            self._finish_row()
            return
        if tag == "table" and self._tstack:
            self._finish_table()
            return

    def handle_data(self, data):
        if self._skipdepth or self._cell is None:
            return
        self._cell["parts"].append(data)


def cell_repr(c):
    if c is None:
        return ""
    t = c.get("text", "")
    if c.get("spanned") or c.get("blank"):
        return "" if not t else t
    alts = c.get("alts") or []
    if not t and alts:
        return " [img:%s] " % " | ".join(alts)
    return t


def main():
    src = sys.argv[1]
    html = io.open(src, encoding="utf-8").read()
    p = TableParser()
    p.feed(html)
    out = []
    for t in p.tables:
        g = [[cell_repr(c) for c in row] for row in t["grid"]]
        out.append({
            "index": t["index"],
            "row_count": t["row_count"],
            "raw_row_count": t["raw_row_count"],
            "grid_width": t["grid_width"],
            "header_row_count": t["header_row_count"],
            "rows": g,
        })
    dest = sys.argv[2] if len(sys.argv) > 2 else None
    blob = json.dumps(out, ensure_ascii=False, indent=1)
    if dest:
        io.open(dest, "w", encoding="utf-8", newline="\n").write(blob)
    print("tables=%d" % len(out))
    for t in out:
        print("T%-2d rows=%-4d width=%-3d headrows=%d first=%s"
              % (t["index"], t["row_count"], t["grid_width"],
                 t["header_row_count"],
                 (t["rows"][0][0] if t["rows"] and t["rows"][0] else "")[:60]))


if __name__ == "__main__":
    main()
