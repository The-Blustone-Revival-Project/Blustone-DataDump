#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""GUARD Rule 2/3/4 health check for a written note: verify the FILE, not the
console dump. Read bytes with explicit UTF-8, count U+FFFD / CRLF / mojibake /
Hangul / CJK, and confirm the Korean terms survived."""
import io
import re
import sys

p = sys.argv[1]
b = open(p, "rb").read()
t = b.decode("utf-8")           # raises if not valid UTF-8
print("file      :", p)
print("bytes     :", len(b))
print("chars     :", len(t))
print("U+FFFD    :", t.count("\ufffd"), "  (must be 0)")
print("CRLF      :", t.count("\r\n"), "  (must be 0)")
print("lone CR   :", t.count("\r"), "  (must be 0)")
print("mojibake  :", t.count("\u00c3"), t.count("\ufffd"), "(A-tilde count, must be 0)")
print("Hangul    :", len(re.findall(r"[\uAC00-\uD7A3]", t)), "  (must be > 0)")
print("CJK       :", len(re.findall(r"[\u4E00-\u9FFF]", t)))
print("em-dash   :", t.count("\u2014"))
print("nbsp      :", t.count("\u00a0"))
# the Korean gear names must be present byte-exact
need = [x for x in sys.argv[2:]]
for n in need:
    print("contains %-14s : %s" % (n, n in t))