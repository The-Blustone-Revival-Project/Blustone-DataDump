"""Locate which PDF pages mention Blustone / Korean title so only the relevant
images need viewing."""
import os
import sys

import pymupdf

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
VS = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", "analysis", "VSFan"))
PDFS = []
for root, d, files in os.walk(os.path.join(VS, "Research")):
    for f in sorted(files):
        if f.lower().endswith(".pdf"):
            PDFS.append(os.path.join(root, f))

KEYS = ["blustone", "블루스톤", "bruise", "vsfan", "visualshower"]
for src in sorted(PDFS):
    doc = pymupdf.open(src)
    hits = []
    for pno in range(doc.page_count):
        t = doc[pno].get_text().lower()
        found = [k for k in KEYS if k in t]
        if found:
            imgs = [i for i in doc[pno].get_images(full=True)]
            hits.append((pno + 1, found, len(imgs)))
    print("%-62s pages=%3d hits=%s" % (os.path.basename(src)[:62],
                                       doc.page_count,
                                       hits if hits else "none"))
    doc.close()
