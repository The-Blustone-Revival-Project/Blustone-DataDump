"""Health check for the new note, per GUARD-encoding-and-archive-traps.md:
verify the FILE (not the console dump) for U+FFFD, CRLF, mojibake, and that the
Hangul we transcribed survived."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

P = r"analysis/research/base-stats-visual-hunt/swipe-panel-hunt-2026-10-05.md"
raw = open(P, "rb").read()
t = raw.decode("utf-8")

print("bytes            : %d" % len(raw))
print("chars            : %d" % len(t))
print("U+FFFD (must be 0): %d" % t.count("\ufffd"))
print("CRLF (expect 0)  : %d" % t.count("\r\n"))
print("bare CR (exp 0)  : %d" % t.count("\r"))
print("mojibake 'Ã'     : %d" % t.count("\u00c3"))
print("mojibake 'â€'    : %d" % t.count("\u00e2\u20ac"))
print("em-dash U+2014   : %d" % t.count("\u2014"))
print("hangul AC00-D7A3 : %d" % len(re.findall(r"[\uac00-\ud7a3]", t)))
print("CJK 4E00-9FFF    : %d" % len(re.findall(r"[\u4e00-\u9fff]", t)))

need = ["\uc804\ud234\ub825", "\uc0dd\uba85\ub825", "\uacf5\uaca9\ub825",
        "\ubc29\uc5b4\ub825", "\uacf5\uaca9 \uc18d\ub3c4",
        "\uc138\ud2b8 \uc801\uc6a9", "\uc7a5\ube44 \uac15\ud654"]
print("\nrequired Hangul strings (from faq_09 transcription):")
for s in need:
    print("  %-16s %s" % (s, "PRESENT" if s in t else "*** MISSING ***"))

# headline numbers must all be present
for s in ["24068", "+6291", "30359", "23847", "18244", "61815", "4980",
          "2634", "1992", "134", "102", "260", "2069", "2275", "1047",
          "1.169", "1.274", "1.300"]:
    if s not in t:
        print("*** MISSING NUMERAL: %s" % s)
print("\nnumeral presence check done")
