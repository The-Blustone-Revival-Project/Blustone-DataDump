# -*- coding: utf-8 -*-
"""GUARD rule 2/3 health check: verify the FILE, not the console."""
import io, os, sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass
HERE = os.path.dirname(os.path.abspath(__file__))
for name in ["vsfan-wiki-expansion-2026-10-05.md"]:
    p = os.path.join(HERE, name)
    b = io.open(p, "rb").read()
    t = b.decode("utf-8", "strict")          # strict: raises if not valid UTF-8
    print("== %s" % name)
    print("   bytes            : %d" % len(b))
    print("   chars            : %d" % len(t))
    print("   decodes as UTF-8 : YES (strict)")
    print("   U+FFFD           : %d" % t.count("\ufffd"))
    print("   CRLF             : %d" % t.count("\r\n"))
    print("   bare CR          : %d" % t.count("\r"))
    print("   em-dash U+2014   : %d" % t.count("\u2014"))
    print("   CJK U+4E00-9FFF  : %d" % sum(1 for c in t if "\u4e00" <= c <= "\u9fff"))
    print("   Hangul AC00-D7A3 : %d" % sum(1 for c in t if "\uac00" <= c <= "\ud7a3"))
    print("   mojibake 'Ã'     : %d" % t.count("\u00c3"))
    print("   star U+2605      : %d" % t.count("\u2605"))
    print("   BOM              : %s" % ("YES" if b.startswith(b"\xef\xbb\xbf") else "no"))
    print("   first 90 chars   : %r" % t[:90])