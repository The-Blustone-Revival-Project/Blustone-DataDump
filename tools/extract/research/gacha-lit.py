#!/usr/bin/env python3
"""Resolve Thumb `ldr [pc,#imm]` + `add r, pc` string literals inside one function.

Validated against analysis/ghidra-setstage-exact.txt:
    target = (address of the `add r, pc` instruction) + 4 + literal_word

Ghidra's decompiler prints the unresolved pool word as `_DAT_<slot> + <imm>`.
Only <imm> is useful here.  For each <imm> in program order we search for the
string address T such that T - <imm> - 4 is a plausible `add` address inside the
function.  Because the reference expressions appear in program order and are
spaced ~0x20 bytes apart, a greedy left-to-right walk with a minimum spacing
resolves them uniquely; anything still ambiguous is reported as such.

Usage:
  gacha-lit.py SEQ <lo> <hi> <min_step> <imm> [<imm> ...]
  gacha-lit.py ALL <lo> <hi> <min_step> <imm> [<imm> ...]   # every candidate
"""
import sys
import bisect

TSV = 'sources/native/strings/native-all-strings.tsv'


def load_strings():
    addrs, strs = [], {}
    with open(TSV, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            sep = line.find("\t")
            if sep < 0:
                continue
            try:
                a = int(line[:sep], 16)
            except ValueError:
                continue
            addrs.append(a)
            strs[a] = line[sep + 1:].rstrip("\n")
    addrs.sort()
    return addrs, strs


def candidates(addrs, strs, lo, hi, imm):
    out = []
    for addaddr in range(lo, hi, 2):
        t = addaddr + 4 + imm
        i = bisect.bisect_left(addrs, t)
        if i < len(addrs) and addrs[i] == t:
            out.append((addaddr, t, strs[t]))
    return out


def main():
    mode = sys.argv[1]
    lo = int(sys.argv[2], 16)
    hi = int(sys.argv[3], 16)
    step = int(sys.argv[4], 0)
    imms = [int(x, 16) for x in sys.argv[5:]]
    addrs, strs = load_strings()

    if mode == "ALL":
        for imm in imms:
            c = candidates(addrs, strs, lo, hi, imm)
            if not c:
                print(f"imm=0x{imm:x}  -> NO MATCH")
            for addaddr, t, s in c:
                print(f"imm=0x{imm:x}  add@0x{addaddr:x} -> 0x{t:x}  {s!r}")
        return

    cursor = lo
    for imm in imms:
        c = [x for x in candidates(addrs, strs, cursor, hi, imm)]
        if not c:
            print(f"imm=0x{imm:x}  -> NO MATCH (cursor=0x{cursor:x})")
            continue
        addaddr, t, s = c[0]
        amb = len(c) > 1
        print(f"imm=0x{imm:<9x} add@0x{addaddr:x} -> 0x{t:x}  {s!r}"
              + ("   [AMBIGUOUS: " + ", ".join(f"0x{a:x}={v!r}" for a, _, v in c[1:6]) + "]" if amb else ""))
        cursor = addaddr + max(step, 2)


if __name__ == "__main__":
    main()