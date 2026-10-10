#!/usr/bin/env python3
'List every PC-relative string literal referenced by a native function range.\n\nNo Ghidra required.  The extracted libnative_core.so keeps a plaintext .text and\nplaintext literal pools (only .rodata is encrypted at rest; the decrypted strings\nare already dumped to sources/native/strings/native-all-strings.tsv), and Ghidra addresses are\nfile vaddr + IMAGE_BASE (0x10000, from sources/native/symbols/native-evidence.tsv).\n\nRecognised idioms\n  ldr   rN, [pc, #imm8]        ; Thumb T1     0100 1 Rt imm8\n  ldr.w rN, [pc, #imm12]       ; Thumb T2     1111 1000 U 1011 1111 | Rt imm12\n  add   rN, pc                 ; Thumb T1     0100 0100 011 1111 Rd\n  add.w rD, pc, #imm           ; Thumb T3     1111 0i00 0100 1111 | 0imm3 Rd imm8\n  ->  target = address_of_add + 4 + pool_word\n\nStrings are reported in address order (== program order for these functions).\n\nUsage: gacha-strings.py <lo> <hi> [<lo> <hi> ...]      # Ghidra addresses\n'
import struct
import sys
import bisect

IMAGE_BASE = 0x10000
ELF = 'local/inputs/extracted/lib/armeabi-v7a/libnative_core.so'
TSV = 'sources/native/strings/native-all-strings.tsv'


def load_elf(path=ELF):
    with open(path, "rb") as fh:
        data = fh.read()
    e_phoff = struct.unpack_from("<I", data, 0x1C)[0]
    e_phentsize = struct.unpack_from("<H", data, 0x2A)[0]
    e_phnum = struct.unpack_from("<H", data, 0x2C)[0]
    segs = []
    for i in range(e_phnum):
        p_type, p_offset, p_vaddr, _p, p_filesz = struct.unpack_from(
            "<IIIII", data, e_phoff + i * e_phentsize)
        if p_type == 1:
            segs.append((p_vaddr, p_filesz, p_offset))
    return segs, data


def v2o(segs, vaddr):
    for pv, pf, po in segs:
        if pv <= vaddr < pv + pf:
            return po + (vaddr - pv)
    return None


def w16(data, segs, va):
    o = v2o(segs, va - IMAGE_BASE)
    return None if o is None or o + 2 > len(data) else struct.unpack_from("<H", data, o)[0]


def w32(data, segs, va):
    o = v2o(segs, va - IMAGE_BASE)
    return None if o is None or o + 4 > len(data) else struct.unpack_from("<I", data, o)[0]


def ldr_pools(segs, data, at, span=26):
    """Every (ldr_addr, pool_word) for pc-relative literal loads in [at-span, at)."""
    out = []
    for back in range(at - span, at, 2):
        lo = w16(data, segs, back)
        if lo is None:
            continue
        if (lo & 0xF800) == 0x4800:            # ldr Rt, [pc, #imm8]  (imm8 * 4)
            pool = ((back + 4) & ~3) + (lo & 0xFF) * 4
            w = w32(data, segs, pool)
            if w is not None:
                out.append((back, w))
            continue
        if (lo & 0x0FF0) == 0x0850 and (lo & 0x000F) == 0x000F:   # ldr.w Rt,[pc,#imm12]
            hi = w16(data, segs, back + 2)
            if hi is None:
                continue
            u = (lo >> 7) & 1
            off = hi & 0xFFF
            base = (back + 4) & ~3
            pool = base + off if u else base - off
            w = w32(data, segs, pool)
            if w is not None:
                out.append((back, w))
    return out


def is_add_rdn_pc(w):
    return (w & 0xFFF8) == 0x4478


def is_add_w_rd_pc(w, w2):
    """32-bit Thumb T3 `add.w rd, pc, #imm`: hw1 = 1111 0i0 0100 0 1111."""
    return (w & 0xFBF0) in (0xF480, 0xF880) and (w & 0x000F) == 0x000F \
        and (w & 0x0010) == 0 and (w2 & 0x8000) == 0


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


def scan(segs, data, saddrs, strs, lo, hi):
    """Brute-force every even address; no instruction-stream walking needed.

    For each `add rdn, pc` we try every pc-relative literal load in the preceding
    window and keep the ones whose implied target is a known string address.
    """
    out = []
    for a in range(lo, hi, 2):
        w = w16(data, segs, a)
        if w is None:
            continue
        if not (is_add_rdn_pc(w) or is_add_w_rd_pc(w, w16(data, segs, a + 2) or 0)):
            continue
        for ldr, word in ldr_pools(segs, data, a):
            t = a + 4 + word
            i = bisect.bisect_left(saddrs, t)
            if i < len(saddrs) and saddrs[i] == t:
                out.append((a, ldr, t, strs[t]))
                break
    return out


def refs(segs, data, target, lo=0, hi=0x2100000):
    """Every `add rdn, pc` in the range whose resolved target == `target`."""
    out = []
    for a in range(lo, hi, 2):
        w = w16(data, segs, a)
        if w is None:
            continue
        if not (is_add_rdn_pc(w) or is_add_w_rd_pc(w, w16(data, segs, a + 2) or 0)):
            continue
        for ldr, word in ldr_pools(segs, data, a):
            if a + 4 + word == target:
                out.append((a, ldr))
                break
    return out


def main():
    args = sys.argv[1:]
    so = ELF
    if args and args[0].endswith(".so"):
        so = args.pop(0)
    segs, data = load_elf(so)
    saddrs, strs = load_strings()
    if args and args[0] == "--refs":
        for t in args[1:]:
            a = int(t, 0)
            hits = refs(segs, data, a)
            print(f"target 0x{a:x} {strs.get(a, '?')!r}: {len(hits)} refs")
            for ad, ldr in hits:
                print(f"    add@0x{ad:<9x} ldr@0x{ldr:x}")
        return
    pairs = [(int(args[i], 0), int(args[i + 1], 0)) for i in range(0, len(args) - 1, 2)]
    for lo, hi in pairs:
        print(f"===== 0x{lo:x}..0x{hi:x} =====")
        for a, ldr, t, s in scan(segs, data, saddrs, strs, lo, hi):
            print(f"add@0x{a:<9x} ldr@0x{ldr:<9x} -> 0x{t:<9x} {s!r}")


if __name__ == "__main__":
    main()