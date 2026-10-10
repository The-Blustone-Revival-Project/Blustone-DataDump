"""Extract every embedded raster image from the VSFan PDFs, plus render pages, so
the Blustone-related brochures/press kits can be screened for in-game stat panels.
Read-only w.r.t. the PDFs.
"""
import hashlib
import os
import sys

import pymupdf

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "pdfimg")
VS = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", "analysis", "VSFan"))

PDFS = [
    "Research/VisualShower/2013 E3 Gameshow Korea Pavilion.pdf",
    "Research/VisualShower/2014 E3 Gameshow Korea Pavilion.pdf",
    "Research/VisualShower/Unknown E3 Korean Pavilion Brochure.pdf",
    "Research/VisualShower/Unknown E3 Korean Pavilion Company Descriptions.pdf",
    "Research/VisualShower/2014 China Digital Entertainment Expo _ Conference Post Show Report.pdf",
    "Research/VisualShower/2010 Dubai World Game Expo Report.pdf",
    "Research/LingoWinner/LingoWinner Company Introduction.pdf",
]


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for rel in PDFS:
        src = os.path.join(VS, rel.replace("/", os.sep))
        if not os.path.exists(src):
            print("MISSING %s" % rel)
            continue
        doc = pymupdf.open(src)
        tag = os.path.splitext(os.path.basename(rel))[0]
        tag = "".join(c if c.isalnum() else "_" for c in tag)[:28]
        n = 0
        for pno in range(doc.page_count):
            page = doc[pno]
            for img in page.get_images(full=True):
                xref = img[0]
                try:
                    d = doc.extract_image(xref)
                except Exception:
                    continue
                if not d:
                    continue
                b = d["image"]
                if len(b) < 12000:      # skip icons/logos/rules
                    continue
                w, h = d.get("width", 0), d.get("height", 0)
                if w < 240 or h < 240:
                    continue
                n += 1
                name = "%s_p%02d_%02d_%dx%d.%s" % (tag, pno + 1, n, w, h, d["ext"])
                with open(os.path.join(OUT, name), "wb") as f:
                    f.write(b)
                rows.append((rel, name, len(b), w, h))
        print("%-72s pages=%3d images>=240px=%d" % (os.path.basename(rel), doc.page_count, n))
        doc.close()
    print("\nTOTAL extracted: %d" % len(rows))
    with open(os.path.join(OUT, "_index.tsv"), "w", encoding="utf-8", newline="\n") as f:
        for rel, name, s, w, h in rows:
            f.write("%s\t%s\t%d\t%d\t%d\n" % (rel, name, s, w, h))


if __name__ == "__main__":
    main()
