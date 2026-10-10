# -*- coding: utf-8 -*-
"""Extract text from the locally-archived VisualShower .docx files.

These are first-party BTB / White Island documents that ship inside the
workspace (analysis/VSFan/Research). A .docx is a zip; we read
word/document.xml and convert the WordprocessingML runs to plain text while
preserving paragraph and table-cell boundaries.
"""
import io
import os
import re
import sys
import zipfile

sys.stdout.reconfigure(encoding="utf-8")

BASE = "analysis/VSFan/Research"
OUTDIR = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/docx"

TARGETS = [
    "Beyond the Bounds/BTB Characters.docx",
    "Beyond the Bounds/BTB Walkthrough.docx",
    "Beyond the Bounds/BTB Locations.docx",
    "Beyond the Bounds/BTB Credits.docx",
    "White Island/Overview.docx",
    "White Island/White Island Credits.docx",
    "VisualShower/Sources.docx",
]

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def para_text(pxml):
    """Concatenate all runs in one <w:p>, honouring <w:tab/> and <w:br/>.

    Input is the raw XML string of one <w:p> element (regex extraction), so we
    scan tags in document order rather than using an lxml iterator.
    """
    out = []
    for m in re.finditer(r"<w:t(?:\s[^>]*)?>(.*?)</w:t>|<w:tab\s*/>|<w:br\s*/>|<w:cr\s*/>", pxml, re.S):
        tok = m.group(0)
        if tok.startswith("<w:t"):
            out.append(m.group(1) or "")
        elif "tab" in tok:
            out.append("\t")
        else:
            out.append("\n")
    return unescape("".join(out))


def unescape(s):
    return (
        s.replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", '"')
        .replace("&apos;", "'")
        .replace("&#91;", "[")
        .replace("&#93;", "]")
        .replace("&amp;", "&")
    )


def docx_text(path):
    z = zipfile.ZipFile(path)
    names = z.namelist()
    xml = z.read("word/document.xml").decode("utf-8", "replace")
    # Split into block-level elements so table rows become their own lines.
    body = re.search(r"<w:body>(.*)</w:body>", xml, re.S)
    body = body.group(1) if body else xml
    lines = []
    # iterate paragraphs and table rows in document order
    for m in re.finditer(r"<w:p\b.*?</w:p>|<w:tbl>.*?</w:tbl>", body, re.S):
        chunk = m.group(0)
        if chunk.startswith("<w:tbl"):
            for rm in re.finditer(r"<w:tr\b.*?</w:tr>", chunk, re.S):
                cells = []
                for cm in re.finditer(r"<w:tc\b.*?</w:tc>", rm.group(0), re.S):
                    cells.append(
                        " ".join(
                            para_text(p.group(0)).strip()
                            for p in re.finditer(r"<w:p\b.*?</w:p>", cm.group(0), re.S)
                        ).strip()
                    )
                lines.append("\t|\t".join(cells))
        else:
            lines.append(para_text(chunk))
    return lines, names


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    index = []
    for rel in TARGETS:
        p = os.path.join(BASE, rel)
        if not os.path.exists(p):
            index.append((rel, "MISSING"))
            continue
        lines, names = docx_text(p)
        tag = re.sub(r"[^A-Za-z0-9]+", "_", rel).strip("_")
        outp = os.path.join(OUTDIR, tag + ".txt")
        txt = "\n".join(lines)
        io.open(outp, "w", encoding="utf-8", newline="\n").write(txt)
        tables = sum(1 for ln in lines if "\t|\t" in ln)
        index.append((rel, "%d lines, %d table rows, %d chars" % (len(lines), tables, len(txt))))
        print("%-42s -> %s" % (rel, os.path.basename(outp)))
        print("      %d lines, %d table rows, %d chars" % (len(lines), tables, len(txt)))

    io.open(
        OUTDIR + "/_index.txt", "w", encoding="utf-8", newline="\n"
    ).write("\n".join("%s\t%s" % (a, b) for a, b in index))


if __name__ == "__main__":
    main()