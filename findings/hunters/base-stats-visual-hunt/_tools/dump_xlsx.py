#!/usr/bin/env python3
"""Dump every sheet of an .xlsx using only the stdlib (xlsx is a ZIP + XML).

Used because openpyxl is not installed in this workspace. Read-only: the input
file is never opened for writing.
"""
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

NS_MAIN = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
NS_REL = "{http://schemas.openxmlformats.org/package/2006/relationships}"
NS_DOCREL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"


def col_to_index(ref: str) -> int:
    m = re.match(r"([A-Z]+)", ref or "")
    if not m:
        return -1
    n = 0
    for ch in m.group(1):
        n = n * 26 + (ord(ch) - 64)
    return n - 1


def shared_strings(z):
    out = []
    try:
        raw = z.read("xl/sharedStrings.xml")
    except KeyError:
        return out
    root = ET.fromstring(raw)
    for si in root.findall(f"{NS_MAIN}si"):
        parts = [t.text or "" for t in si.iter(f"{NS_MAIN}t")]
        out.append("".join(parts))
    return out


def sheet_names(z):
    """Return [(sheet display name, worksheet xml path)] in workbook order."""
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    target = {}
    for r in rels.findall(f"{NS_REL}Relationship"):
        t = r.get("Target") or ""
        if t.startswith("/"):
            t = t[1:]
        elif not t.startswith("xl/"):
            t = "xl/" + t
        target[r.get("Id")] = t
    out = []
    for sh in wb.iter(f"{NS_MAIN}sheet"):
        rid = sh.get(f"{NS_DOCREL}id")
        path = target.get(rid)
        if path:
            out.append((sh.get("name") or "?", path))
    return out


def dump_sheet(z, path, sst):
    root = ET.fromstring(z.read(path))
    rows = []
    for row in root.iter(f"{NS_MAIN}row"):
        cells = {}
        for c in row.findall(f"{NS_MAIN}c"):
            ref = c.get("r") or ""
            idx = col_to_index(ref)
            t = c.get("t")
            if t == "s":
                v = c.find(f"{NS_MAIN}v")
                val = sst[int(v.text)] if v is not None and v.text else ""
            elif t == "inlineStr":
                is_el = c.find(f"{NS_MAIN}is")
                val = "".join(x.text or "" for x in is_el.iter(f"{NS_MAIN}t")) if is_el is not None else ""
            else:
                v = c.find(f"{NS_MAIN}v")
                val = v.text if v is not None and v.text is not None else ""
            if val not in ("", None):
                cells[idx] = val
        if cells:
            rows.append((row.get("r"), cells))
    return rows


def main(path):
    with zipfile.ZipFile(path) as z:
        sst = shared_strings(z)
        print(f"### FILE: {path}")
        print(f"### sharedStrings: {len(sst)}")
        for name, spath in sheet_names(z):
            print(f"\n=== SHEET: {name}  ({spath}) ===")
            for rnum, cells in dump_sheet(z, spath, sst):
                parts = []
                for idx in sorted(cells):
                    parts.append(f"c{idx}={cells[idx]!r}")
                print(f"  r{rnum}: " + " | ".join(parts))


if __name__ == "__main__":
    for p in sys.argv[1:]:
        main(p)
        print()
