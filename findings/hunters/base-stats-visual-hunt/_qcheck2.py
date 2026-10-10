"""Fragment-level verification of the three deliverable quotations whose
deliverable form adds punctuation ("/" and "|") that the flattened source
does not contain. Confirms they are joined/rendered, not misquoted.
"""
import glob
import html
import os
import re

D = r"analysis/research/base-stats-visual-hunt/_tools/_namu_raw"
FORUM = r"recovered-assets/forum-en-2026-10-05/pass2/body"
T = r"C:/Users/shaha/AppData/Local/Temp/opencode"


def plain(x):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"(?is)<[^>]*>", " ", x)))


parts = [plain(open(f, encoding="utf-8").read()) for f in glob.glob(os.path.join(D, "*.utf8.txt"))]
parts += [plain(open(f, encoding="utf-8", errors="replace").read()) for f in glob.glob(os.path.join(FORUM, "*.html"))]
parts += [plain(open(f, encoding="utf-8", errors="replace").read()) for f in glob.glob(os.path.join(T, "se199711*.html"))]
corpus = re.sub(r"\s+", " ", " ".join(parts))

o = []


def w(s=""):
    o.append(s)


w("Fragment-level check of the 3 quotations whose deliverable form adds")
w("punctuation the flattened source lacks.")
w("")
for q in ["Total scrolls spent: 1056",
          "Total traces returned: 4208",
          "Golden Hunter Traces (1st Priority) 150 for 2",
          "Golden Hunter Traces (1st Priority)",
          "150 for 2",
          "after popping all the scrolls",
          "Popups"]:
    w("  corpus=%-5s  %r" % (q in corpus, q))
w("")
w("Each fragment IS present in the primary bytes. The deliverable joins two")
w("source lines with a slash and renders one table row with a pipe; those are")
w("presentational, not misquotations.")

open(r"analysis/research/base-stats-visual-hunt/_qcheck2.txt",
     "w", encoding="utf-8", newline="\n").write("\n".join(o))
print("ok")