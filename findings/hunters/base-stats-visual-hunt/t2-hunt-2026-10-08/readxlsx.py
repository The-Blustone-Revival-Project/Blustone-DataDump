import re
import sys
import xml.etree.ElementTree as ET
import zipfile

sys.stdout.reconfigure(encoding="utf-8")
NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
p = r"analysis/VSFan/Research/Blustone/Hunter Stats [BROKEN IGNORE].xlsx"
z = zipfile.ZipFile(p)
ss = []
try:
    r = ET.fromstring(z.read("xl/sharedStrings.xml"))
    for si in r.findall(NS + "si"):
        ss.append("".join(t.text or "" for t in si.iter(NS + "t")))
except KeyError:
    pass
wb = ET.fromstring(z.read("xl/workbook.xml"))
print([s.get("name") for s in wb.iter(NS + "sheet")])
for sh in ["xl/worksheets/sheet1.xml", "xl/worksheets/sheet2.xml"]:
    print("=" * 30, sh)
    r = ET.fromstring(z.read(sh))
    for row in r.iter(NS + "row"):
        cells = []
        for c in row.findall(NS + "c"):
            ref = c.get("r")
            t = c.get("t")
            v = c.find(NS + "v")
            isel = c.find(NS + "is")
            if isel is not None:
                val = "".join(x.text or "" for x in isel.iter(NS + "t"))
            elif v is None:
                val = ""
            elif t == "s":
                val = ss[int(v.text)]
            else:
                val = v.text
            cells.append(f"{ref}={val}")
        if cells:
            print(row.get("r"), " | ".join(cells))
