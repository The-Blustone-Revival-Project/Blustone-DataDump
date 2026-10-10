#!/usr/bin/env python3
'Resolve the Thumb `ldr [pc,#imm]` + `add rdn,pc` string literals that Ghidra\nprints as `_DAT_<slot> + <imm>` in the existing decomp dumps.\n\nWhy this exists\n---------------\n`analysis/ghidra-scripts/ResolvePcRelativeStrings.java` needs the Ghidra project\n(which is owned exclusively by the parent agent and must stay closed).  But the\ninformation it produces is fully recoverable offline, because:\n\n  * the extracted `libnative_core.so` has a *plaintext* .text (only .rodata is\n    encrypted at rest -- the decrypted strings are already dumped into\n    `sources/native/strings/native-all-strings.tsv`);\n  * Ghidra addresses == file vaddr + IMAGE_BASE, IMAGE_BASE == 0x10000\n    (`sources/native/symbols/native-evidence.tsv` line 2: `IMAGE_BASE 00010000`).\n\nThe idiom (validated against analysis/ghidra-setstage-exact.txt and reproduced\nindependently with llvm-objdump --triple=thumbv7-linux-gnueabihf) is\n\n    ldr  rN, [pc, #imm]      ; Thumb T1 literal load, pool at Align(pc+4,4)+imm\n    add  rN, pc              ; Thumb T1, opcode 0100 0100 011 Rm Rd\n    ->  target = (address of the `add`) + 4 + <pool word>\n\nThe <imm> values that Ghidra prints ARE the pre-relocation pool words, so given\nthe pool word and the function range the target is simply\n`add_addr + 4 + pool_word`.  Searching for the right `add` is unambiguous once\nthe ELF bytes are used as the filter: a candidate must be a real\n`add rdn, pc` (halfword `0x4478|rdn`) or `add.w rd, pc, #imm`\n(hw1 `0xF18F`/`0xF08F` with Rn == 15), preceded within 12 bytes by a real\n`ldr rX, [pc, #imm]` (`0x4800` mask).\n\nUsage\n-----\n  gacha-lit2.py <so> <lo> <hi> <imm> [<imm> ...]     # all candidates\n  gacha-lit2.py <so> --seq <lo> <hi> <imm> [...]      # greedy, program order\n\nAll addresses are Ghidra addresses (add 0x10000 for the file offset).\n'
import struct
import sys
import bisect

IMAGE_BASE = 0x10000
ELF = 'local/inputs/extracted/lib/armeabi-v7a/libnative_core.so'
TSV = 'sources/native/strings/native-all-strings.tsv'


def load_elf(path=ELF):
    with open(path, "rb") as fh:
        data = fh.read()
    if data[:4] != b"\x7fELF":
        raise SystemExit("not an ELF: " + path)
    e_phoff = struct.unpack_from("<I", data, 0x1C)[0]
    e_phentsize = struct.unpack_from("<H", data, 0x2A)[0]
    e_phnum = struct.unpack_from("<H", data, 0x2C)[0]
    segs = []
    for i in range(e_phnum):
        p_type, p_offset, p_vaddr, _p_paddr, p_filesz = struct.unpack_from(
            "<IIIII", data, e_phoff + i * e_phentsize)
        if p_type == 1:
            segs.append((p_vaddr, p_filesz, p_offset))
    return segs, data


def v2o(segs, vaddr):
    for p_vaddr, p_filesz, p_offset in segs:
        if p_vaddr <= vaddr < p_vaddr + p_filesz:
            return p_offset + (vaddr - p_vaddr)
    return None


def hw16(data, segs, vaddr):
    off = v2o(segs, vaddr - IMAGE_BASE)
    if off is None or off + 2 > len(data):
        return None
    return struct.unpack_from("<H", data, off)[0]


def is_add_rdn_pc(lo, hi):
    """16-bit Thumb T1 `add rdn, pc`  (0100 0100 011 Rm=1111 Rd)."""
    return (lo & 0xFFF8) == 0x4478


def is_add_w_rd_pc(lo, hi):
    """32-bit Thumb T3 `add.w rd, pc, #imm` (Rn == 15, opcode 0100, S == 0)."""
    return (lo & 0xFBF0) == 0xF100 and (lo & 0x000F) == 0x000F and (hi & 0x8000) == 0


def is_ldr_literal(lo):
    return (lo & 0xF800) == 0x4800


def has_ldr_before(data, segs, addaddr, span=12):
    for back in range(addaddr - span, addaddr, 2):
        w = hw16(data, segs, back)
        if w is not None and is_ldr_literal(w):
            return back
    return None


def load_strings(path=TSV):
    addrs, strs = [], {}
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
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


def find(segs, data, saddrs, strs, lo, hi, imm):
    out = []
    for addaddr in range(lo, hi, 2):
        w = hw16(data, segs, addaddr)
        if w is None:
            continue
        w2 = hw16(data, segs, addaddr + 2) or 0
        if not (is_add_rdn_pc(w, 0) or is_add_w_rd_pc(w, w2)):
            continue
        ldr = has_ldr_before(data, segs, addaddr)
        if ldr is None:
            continue
        t = addaddr + 4 + imm
        i = bisect.bisect_left(saddrs, t)
        if i < len(saddrs) and saddrs[i] == t:
            out.append((addaddr, ldr, t, strs[t]))
    return out


def main():
    a = sys.argv[1:]
    seq = False
    if a and a[0] == "--seq":
        seq = True
        a = a[1:]
    so, lo, hi = a[0], int(a[1], 0), int(a[2], 0)
    imms = [int(x, 0) for x in a[3:]]
    segs, data = load_elf(so)
    saddrs, strs = load_strings()

    if not seq:
        for imm in imms:
            c = find(segs, data, saddrs, strs, lo, hi, imm)
            if not c:
                print(f"imm=0x{imm:x}  -> NO MATCH")
            for addaddr, ldr, t, s in c:
                print(f"imm=0x{imm:x}  ldr@0x{ldr:x} add@0x{addaddr:x} "
                      f"-> 0x{t:x}  {s!r}")
        return

    cursor = lo
    for imm in imms:
        c = find(segs, data, saddrs, strs, cursor, hi, imm)
        if not c:
            print(f"imm=0x{imm:<10x} -> NO MATCH (cursor=0x{cursor:x})")
            continue
        addaddr, ldr, t, s = c[0]
        extra = ""
        if len(c) > 1:
            extra = "   [AMBIGUOUS: " + ", ".join(f"0x{o:x}={v!r}" for o, _, _, v in c[1:4]) + "]"
        print(f"imm=0x{imm:<10x} ldr@0x{ldr:x} add@0x{addaddr:x} -> 0x{t:x}  {s!r}{extra}")
        cursor = addaddr + 2


if __name__ == "__main__":
    main()