#!/usr/bin/env python3
"""Driver: resolve the JSON/route literals of every function whose mangled name
matches a regex, using next-symbol boundaries from native-evidence.tsv."""
import re
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE))
import gacha_strings as G  # noqa: E402

EVID = 'sources/native/symbols/native-evidence.tsv'


def load_symbols():
    syms = []
    with open(EVID, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if line.startswith("[") or "\t" not in line:
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) < 2:
                continue
            try:
                a = int(p[0], 16)
            except ValueError:
                continue
            syms.append((a, p[1]))
    syms.sort()
    return syms


def main():
    pattern = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 9
    rx = re.compile(pattern)
    syms = load_symbols()
    segs, data = G.load_elf()
    saddrs, strs = G.load_strings()
    addrs = [a for a, _ in syms]
    n = 0
    for i, (a, name) in enumerate(syms):
        if not rx.search(name):
            continue
        j = i + 1
        while j < len(syms) and syms[j][0] == a:
            j += 1
        hi = syms[j][0] if j < len(syms) else a + 0x2000
        res = G.scan(segs, data, saddrs, strs, a, hi)
        print(f"===== 0x{a:08x}..0x{hi:08x}  {name[:150]}")
        for ad, ldr, t, s in res:
            print(f"   add@0x{ad:<9x} -> 0x{t:<9x} {s!r}")
        if not res:
            print("   (no string literals resolved)")
        n += 1
        if n >= limit:
            break


if __name__ == "__main__":
    main()