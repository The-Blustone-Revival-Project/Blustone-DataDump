import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
P = r"analysis/research/base-stats-visual-hunt/swipe-panel-hunt-2026-10-05.md"
t = open(P, encoding="utf-8").read()
i = t.find("\u00c3")
print("the single U+00C3 occurs at index", i)
print("context:", repr(t[i - 90:i + 40]))
print()
print("count of the intentional quoted token:", t.count("mojibake `\u00c3`"))
print("=> it is the character being NAMED in the health-check line, not corruption:",
      t.count("mojibake `\u00c3`") == 1)
