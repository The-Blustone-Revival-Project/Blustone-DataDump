#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Enumerate namu FILE pages linked from the fetched gear pages, and fetch each
file description page (filenames/descriptions are text; only pixels need the
image host)."""
import os
import re
import sys
import urllib.parse

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")


def rd(tag):
    p = os.path.join(RAW, tag + ".utf8.txt")
    return open(p, encoding="utf-8").read()


def main():
    tags = sys.argv[1:]
    out = []
    for tag in tags:
        d = rd(tag)
        for m in re.finditer(r"href=[\"']([^\"']*?/w/([^\"'#?]+))[\"']", d):
            path = urllib.parse.unquote(m.group(2))
            if not path.startswith("\ud30c\uc77c:"):     # '파일:'
                continue
            if path not in out:
                out.append(path)
    print("file pages:", len(out))
    with open(os.path.join(RAW, "_filepages.txt"), "w",
              encoding="utf-8", newline="\n") as fh:
        for p in out:
            fh.write(p + "\n")
    for p in out:
        print(p)


if __name__ == "__main__":
    main()