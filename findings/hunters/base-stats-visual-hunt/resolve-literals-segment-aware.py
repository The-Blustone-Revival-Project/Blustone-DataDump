#!/usr/bin/env python3
"""Segment-aware Thumb literal-pool resolver.

HARDENED replacement for ``tools/resolve-literals-offline.py``, which accepts any
target whose bytes happen to be printable ASCII. That acceptance test is not
sufficient: a ``ldr <Rt>,[pc,#imm]`` + ``add <Rn>,pc`` pair can equally compute
the ADDRESS OF A GLOBAL OBJECT rather than the address of a string. The known
instance is Ghidra ``0x00f589e6`` (ELF ``0x00e589e6``) in
``CSRSyncCard::RequestGroupRankUp``, which the old tool reported as the string
``'X'``; it is really the address of a ``.got`` word.

FIXED DEFECTS (each is a real, reproduced failure of the old tool)

  D1  NO SEGMENT CHECK. The resolved target must live in a file-backed PT_LOAD
      whose ``p_flags`` have PF_W clear. Every genuine literal in this library
      is in ``.rodata``, inside the R-X segment. A target in the RW- segment
      (``.data.rel.ro`` / ``.got`` / ``.data``) or in BSS is data, not a string.
      -> kills the ``'X'`` false positive.
  D2  UNIFORM ``addr - 0x10000`` FILE MAPPING. That is only correct for the first
      PT_LOAD, where ``p_vaddr == p_offset``. For the RW- segment here
      ``p_offset == p_vaddr - 0x1000``, so the old mapping read 0x1000 bytes too
      low and manufactured a printable byte out of a pointer table. Mapping now
      goes through the program headers.
  D3  COORDINATE CONVENTION SILENTLY ASSUMED. Ghidra == ELF + 0x10000 here, and
      the two ``analysis/ghidra-*.txt`` dumps are in Ghidra coordinates while
      ``gem-popup-bindings-2026-10-05.md`` documents its ``.rodata`` addresses as
      ELF VA. Every input and output address now carries an explicit convention
      and the tool prints which one it used. Canonical internal space is ELF VA.
  D4  NO SELF-TEST. ``--expect`` existed on the old tool but was a NO-OP for
      ``--from-dump`` (it printed "NOTE: --expect is only meaningful for
      --function scans" and asserted nothing). This tool refuses to produce any
      result unless its self-test passes.
  D5  GAP-2/4-ONLY PAIRING. ``iter_thumb_ldr_addpc`` in the old tool walks back
      only 2 or 4 bytes from the ``add``. Measured against the 20 known-good
      sites in the two ground-truth dumps, that recovers 15/20 = 75%; the real
      gap distribution is 2,4,4,...,6,10 and the 5 sites at gap 6 and gap 10 are
      MISSED. ``--window`` (default 12) covers all 20.

TWO GUARDED RECALL FIXES

  R1  1-byte literals are legal. ``" "`` (a real ``GetSetEffectDesc`` literal) was
      rejected by a ``len >= 2`` guard in an earlier private version.
  R2  Non-ASCII bytes are legal. Korean/CJK UI literals are real strings here and
      the old all-printable-ASCII test discarded them (false negative).

SELF-TEST

  23 assertions, all derived from TWO INDEPENDENT known-good ground truths, run
  automatically before any other work:

    20  positive   -- re-resolve every site in analysis/ghidra-wave-keys.txt (7)
                      and analysis/ghidra-gem-inventory-keys.txt (13) and require
                      BOTH the recomputed target address AND the resolved string
                      to equal what the dump recorded. The dump's own ``w=`` and
                      ``target`` columns are ignored; only the on-disk slot word is
                      read, so this is a genuine re-derivation, not an echo.
     2  integrity  -- the two files must still yield exactly 7 and 13 sites, so a
                      truncated or edited dump fails the gate instead of silently
                      shrinking it.
     1  negative   -- the documented ``'X'`` site must be REJECTED by D1.

  Any mismatch exits 3 and prints nothing else. Exit codes: 0 ok, 2 usage/IO,
  3 self-test failure, 4 nothing resolved.

Usage
-----
    python resolve-literals-segment-aware.py --self-test
    python resolve-literals-segment-aware.py --list-segments
    python resolve-literals-segment-aware.py --function 0xf586e4:0xf58da0
    python resolve-literals-segment-aware.py --from-dump analysis/ghidra-wave-keys.txt
    python resolve-literals-segment-aware.py --function 0xf58da0:0xf59380 --allow-rw

Addresses are Ghidra on the command line by default (``--addr-convention``);
add ``--addr-convention elf`` to switch. Output follows ``--out-convention``.
"""
from __future__ import annotations

import argparse
import re
import struct
import sys
from pathlib import Path

DEFAULT_SO = Path("analysis/extracted/lib/armeabi-v7a/libnative_core.so")
GT_WAVE = Path("analysis/ghidra-wave-keys.txt")
GT_GEM = Path("analysis/ghidra-gem-inventory-keys.txt")

# Ghidra loads this library at 0x10000, so Ghidra image address == ELF VA + this.
GHIDRA_BIAS = 0x10000

PT_LOAD = 1
PF_X, PF_W, PF_R = 1, 2, 4

# Ground-truth site counts. Pinned so an edited/truncated dump fails the gate.
GT_EXPECTED = {GT_WAVE.name: 7, GT_GEM.name: 13}
GT_FILES = (GT_WAVE, GT_GEM)

# Documented false positive that MUST be rejected.  Ghidra 0x00f589e6 inside
# CSRSyncCard::RequestGroupRankUp (ELF 0x00f486e4 .. 0x00f48da0 per llvm-nm -D).
FP_SITE_ELF = 0x00F489E6
FP_SITE_GHIDRA = FP_SITE_ELF + GHIDRA_BIAS


# --------------------------------------------------------------------------
# ELF view with PROGRAM-HEADER-accurate VA -> file mapping (D2)
# --------------------------------------------------------------------------
def flags_str(f):
    return "%s%s%s" % ("R" if f & PF_R else "-",
                       "W" if f & PF_W else "-",
                       "X" if f & PF_X else "-")


class Segment:
    __slots__ = ("vaddr", "offset", "filesz", "memsz", "flags", "name")

    def __init__(self, vaddr, offset, filesz, memsz, flags):
        self.vaddr, self.offset = vaddr, offset
        self.filesz, self.memsz = filesz, memsz
        self.flags = flags
        self.name = flags_str(flags)

    @property
    def has_w(self):
        return bool(self.flags & PF_W)

    def contains(self, va):
        return self.vaddr <= va < self.vaddr + self.memsz

    def file_backed(self, va):
        return self.vaddr <= va < self.vaddr + self.filesz


class Image:
    def __init__(self, path: Path):
        self.path = path
        self.data = path.read_bytes()
        self.size = len(self.data)
        if self.data[:4] != b"\x7fELF":
            raise ValueError("%s is not an ELF file" % path)
        if self.data[4] != 1:
            raise ValueError("%s is not ELF32" % path)
        e = "<" if self.data[5] == 1 else ">"
        phoff, = struct.unpack_from(e + "I", self.data, 0x1C)
        phentsize, phnum = struct.unpack_from(e + "HH", self.data, 0x2A)
        self.segments = []
        for i in range(phnum):
            o = phoff + i * phentsize
            p_type, p_off, p_vaddr, _pa, p_filesz, p_memsz, p_flags, _al = \
                struct.unpack_from(e + "IIIIIIII", self.data, o)
            if p_type == PT_LOAD:
                self.segments.append(
                    Segment(p_vaddr, p_off, p_filesz, p_memsz, p_flags))
        if not self.segments:
            raise ValueError("%s has no PT_LOAD segments" % path)
        self.segments.sort(key=lambda s: s.vaddr)
        shoff, = struct.unpack_from(e + "I", self.data, 0x20)
        shentsize, shnum, shstrndx = struct.unpack_from(e + "HHH", self.data, 0x2E)
        raw = []
        for i in range(shnum):
            o = shoff + i * shentsize
            sh_name, _t, _fl, sh_addr, sh_off, sh_size = \
                struct.unpack_from(e + "IIIIII", self.data, o)
            raw.append((sh_name, sh_addr, sh_size, sh_off))
        # .shstrtab is NON-ALLOC, so its sh_addr is 0. The name table must be
        # located by sh_offset; reading sh_addr here silently yields garbage
        # names (it lands in the ELF header).
        strtab = raw[shstrndx][3]
        self.sections = []
        for sh_name, sh_addr, sh_size, _off in raw:
            end = self.data.index(b"\x00", strtab + sh_name)
            nm = self.data[strtab + sh_name:end].decode("ascii", "replace")
            if nm and sh_addr:
                self.sections.append((nm, sh_addr, sh_size))

    def segment(self, va):
        for s in self.segments:
            if s.contains(va):
                return s
        return None

    def file_off(self, va):
        """VA -> file offset, or None if unmapped / BSS (no file bytes).

        This is D2. A single uniform bias is wrong here: segment 0 has
        p_vaddr == p_offset, segment 1 has p_offset == p_vaddr - 0x1000.
        """
        s = self.segment(va)
        if s is None or not s.file_backed(va):
            return None
        return s.offset + (va - s.vaddr)

    def section_of(self, va):
        for nm, addr, size in self.sections:
            if addr <= va < addr + size:
                return nm
        return None

    def u16(self, va):
        off = self.file_off(va)
        if off is None or off + 2 > self.size:
            raise ValueError("u16 unmapped at VA %#x" % va)
        return struct.unpack_from("<H", self.data, off)[0]

    def u32(self, va):
        off = self.file_off(va)
        if off is None or off + 4 > self.size:
            raise ValueError("u32 unmapped at VA %#x" % va)
        return struct.unpack_from("<I", self.data, off)[0]

    def string_at(self, va, limit=512):
        """(text, segment) for a NUL-terminated C string at VA, else (None, seg).

        The terminator must lie inside the SAME segment, so a read can never run
        off the end of a mapping.
        """
        off = self.file_off(va)
        seg = self.segment(va)
        if off is None or seg is None:
            return None, seg
        hard = min(off + limit, seg.offset + seg.filesz, self.size)
        end = self.data.find(b"\x00", off, hard)
        if end < 0:
            return None, seg
        try:
            return self.data[off:end].decode("utf-8"), seg
        except UnicodeDecodeError:
            return None, seg


def is_plausible_literal(text):
    """len >= 1 (R1), no C0/C1 control characters, no DEL. Bytes >= 0xA0 are
    allowed so Korean/CJK UI literals survive (R2)."""
    if not text:
        return False
    for ch in text:
        o = ord(ch)
        if o < 0x20 or o == 0x7F or 0x80 <= o <= 0x9F:
            return False
    return True


# --------------------------------------------------------------------------
# Thumb decoding
# --------------------------------------------------------------------------
def decode_ldr_pc_imm(img, ldr_va):
    """If a PC-relative literal load starts at ldr_va return (rt, imm, width).

    T1 ``LDR (literal)``: ``01001 Rt imm8`` -- the 3-bit field is the DESTINATION
    register Rt and the base is *implicitly* PC. There is no Rn field to test, so
    the opcode class alone guarantees a literal-pool load. (An earlier draft of
    this file wrongly required Rn == 15 here and rejected every T1 site.)

    T2 ``LDR.W (literal)``: ``1111 1000 1101 1111 imm12 Rt`` -- here Rn IS a real
    4-bit field (bits[6:3] of hw1) and must be 0b1111. Masking 0xF8DF enforces
    that; masking 0xF8D0, as the old tool did, also matched ``ldr.w r0,[r1,#imm]``.
    """
    try:
        hw1 = img.u16(ldr_va)
    except ValueError:
        return None
    if (hw1 & 0xF800) == 0x4800:
        return hw1 & 0x7, (hw1 & 0xFF) * 4, 2
    if (hw1 & 0xFF00) == 0xF8DF:
        try:
            hw2 = img.u16(ldr_va + 2)
        except ValueError:
            return None
        if (hw2 & 0xF000) != 0xF000:
            return None
        return hw2 & 0xF, ((hw1 & 0xF) << 8) | hw2, 4
    return None


def is_add_pc(hw):
    """True for ``ADD <Rdn>, PC`` (01000100 0 Rm=111 Rdn).

    Rdn is deliberately unconstrained: the ground-truth pair at ELF 0x009fd1b0 /
    0x009fd1b4 loads into r2 but adds into r0, so requiring Rdn == Rt is wrong.
    """
    return (hw & 0xFF00) == 0x4400 and ((hw >> 3) & 0x7) == 7


def _top5(img, va):
    """bits[15:11] of the halfword at va, or None if unmapped."""
    try:
        return (img.u16(va) >> 11) & 0x1F
    except ValueError:
        return None


def is_32bit_branch(img, va):
    """True only for a 32-bit Thumb-2 BL/BLX.

    hw1 alone is NOT enough: ``11110 S 0`` also encodes 32-bit data processing,
    so ``add.w r0,r4,#0x60`` (0xF104 0x0060) and ``bl`` (0xF169 0xD64C) share
    hw1's class. The discriminator is in hw2: bits[15:14] == 11 and bit[12] == 1,
    i.e. ``(hw2 & 0xD000) == 0xD000``.

    Getting this wrong costs a real ground-truth key: the ``otp`` literal in
    CSRSyncCard::RequestGroupRankUp is
        0x00f487ba  ldr  r1,[pc,#0x2f0]
        0x00f487bc  add.w r0, r4, #0x60      <-- 32-bit, NOT a branch
        0x00f487c0  add  r1, pc
    so treating it as a branch makes the walk abandon the pair.

    The mask must also be 0x1F, not 3: ``((hw >> 11) & 3) == 2`` additionally
    matches ordinary 16-bit instructions whose top bits are 100xx, e.g.
    ``str r0,[sp,#0x18]`` (0x9006).
    """
    try:
        hw1 = img.u16(va)
        hw2 = img.u16(va + 2)
    except ValueError:
        return False
    return (((hw1 >> 11) & 0x1F) == 0x1E
            and ((hw1 >> 10) & 1) == 0
            and (hw2 & 0xD000) == 0xD000)


def insn_width(img, va):
    """2 or 4, by the standard Thumb rule.

    top5 == 0b11101 (0xE8..0xEF, load/store multiple + dual), 0b11110
    (0xF0..0xF7, branches and misc) or 0b11111 (0xF8..0xFF) means 32 bits.
    Everything else is 16 bits. Must be the GENERAL test, not the BL/BLX test:
    the ground truth contains ``ldr@0x00a0d33e / add@0x00a0d342`` with a
    16-bit ``str`` between them, and ``ldr@0x00a5c0a6 / add@0x00a5c0ac`` with a
    16-bit ``str`` plus a 16-bit ``mov``.
    """
    t = _top5(img, va)
    if t is None:
        return None
    return 4 if t in (0x1D, 0x1E, 0x1F) else 2


def find_add_pc(img, ldr_va, width, window):
    """First ``ADD <Rn>,PC`` after the load, within `window` bytes (D5).

    Real gaps in the ground truth are 2, 4, 6 and 10 bytes -- the load and its
    add are frequently NOT adjacent.  Walks instruction-by-instruction, stepping
    4 over 32-bit instructions.  A 32-bit BL/BLX immediately before the add is
    rejected outright: that is the phantom-``_id`` defence from AGENTS.md 16.7,
    where a ``bl`` was paired with an unrelated later ``add r1,sp,#8``.
    """
    va = ldr_va + width
    limit = ldr_va + window
    while va <= limit:
        try:
            hw = img.u16(va)
        except ValueError:
            return None
        if is_32bit_branch(img, va):
            return None
        if is_add_pc(hw):
            return va
        nxt = insn_width(img, va)
        if nxt is None:
            return None
        va += nxt
    return None


def resolve_at(img, ldr_va, window=12, require_readonly=True):
    """Resolve the literal consumed by the ``add <Rn>,pc`` following ldr_va.

    Canonical ELF arithmetic, convention-independent by construction:

        slot_elf   = ((ldr_elf & ~3) + 4 + imm) & ~3
        target_elf = u32(slot_elf) + (add_elf + 4)

    Returns a record dict always (so callers can report *why* something was
    rejected); ``"reject"`` is absent on success.
    """
    got = decode_ldr_pc_imm(img, ldr_va)
    if got is None:
        return None
    rt, imm, width = got
    add_va = find_add_pc(img, ldr_va, width, window)
    if add_va is None:
        return None
    slot_elf = ((ldr_elf := ldr_va) & ~3) + 4 + imm
    slot_elf &= ~3
    try:
        w = img.u32(slot_elf)
    except ValueError:
        return None
    target_elf = w + (add_va + 4)
    text, seg = img.string_at(target_elf)
    rec = {
        "ldr_elf": ldr_va, "rt": rt, "slot_elf": slot_elf, "w": w,
        "add_elf": add_va, "gap": add_va - ldr_va, "target_elf": target_elf,
        "section": img.section_of(target_elf), "segment": seg, "text": text,
    }
    # ---- D1: the acceptance test the old tool was missing --------------------
    if require_readonly:
        if seg is None:
            rec["reject"] = "D1 target in no PT_LOAD segment"
            return rec
        if seg.has_w:
            rec["reject"] = ("D1 target in %s segment (%s) -- not read-only, "
                             "so it is data, not a literal"
                             % (seg.name, rec["section"]))
            return rec
    if text is None:
        rec["reject"] = "no NUL-terminated string at target"
        return rec
    if not is_plausible_literal(text):
        rec["reject"] = "implausible literal (control byte or empty)"
        return rec
    return rec


def scan(img, lo_elf, hi_elf, window=12, require_readonly=True):
    """Scan [lo,hi) ELF VA. Anchored on ``ADD <Rn>,PC``, walking BACK up to
    `window` bytes for the load, because the load may be a 4-byte ``ldr.w`` and
    may be separated from its add."""
    out = []
    seen = set()
    va = lo_elf & ~1
    while va < hi_elf:
        try:
            hw = img.u16(va)
        except ValueError:
            va += 2
            continue
        if not is_add_pc(hw):
            va += 2
            continue
        for back in range(2, window + 1, 2):
            cand = va - back
            if cand < lo_elf:
                break
            if is_32bit_branch(img, cand):
                break
            if decode_ldr_pc_imm(img, cand) is None:
                continue
            rec = resolve_at(img, cand, window, require_readonly)
            if rec is not None and "reject" not in rec and cand not in seen:
                seen.add(cand)
                out.append(rec)
            break
        va += 2
    return out


# --------------------------------------------------------------------------
# ground truth (D4)
# --------------------------------------------------------------------------
DUMP_LINE = re.compile(
    r"ldr@(0x)?([0-9a-fA-F]+)\s+slot=(0x)?([0-9a-fA-F]+)\s+"
    r"w=(0x)?([0-9a-fA-F]+)\s+add@(0x)?([0-9a-fA-F]+)\s*->\s*"
    r"(0x)?([0-9a-fA-F]+)\s+(.*)$")


def load_ground_truth(path, bias):
    """Parse a dump into (ldr_elf, expected_target_elf, expected_text) rows.

    `bias` converts the dump's Ghidra coordinates to ELF VA.
    """
    rows = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = DUMP_LINE.search(raw)
        if not m:
            continue
        # the dumps write the text as a quoted Python repr, e.g. "_id" or " "
        txt = m.group(11).strip()
        if len(txt) >= 2 and txt[0] == '"' and txt[-1] == '"':
            txt = txt[1:-1]
        rows.append((int(m.group(2), 16) - bias,
                     int(m.group(10), 16) - bias,
                     txt))
    return rows


def self_test(img, root=Path("."), verbose=True):
    fails = []
    n = 0
    for rel in GT_FILES:
        name = rel.name
        p = root / rel
        if not p.exists():
            fails.append("ground truth %s not found (run from the workspace root)"
                         % rel)
            continue
        rows = load_ground_truth(p, GHIDRA_BIAS)
        # ---- integrity assertion -------------------------------------------
        n += 1
        want = GT_EXPECTED[name]
        if len(rows) != want:
            fails.append("%s: expected %d sites, found %d -- ground truth was "
                         "edited or truncated" % (name, want, len(rows)))
            continue
        if verbose:
            print("  ok   %-28s integrity: %d sites" % (name, len(rows)))
        for ldr_elf, want_tgt, want_txt in rows:
            n += 1
            rec = resolve_at(img, ldr_elf)
            if rec is None:
                fails.append("%s ldr@%#x: no literal pair resolved" % (name, ldr_elf))
                continue
            if "reject" in rec:
                fails.append("%s ldr@%#x: rejected (%s), expected %r"
                             % (name, ldr_elf, rec["reject"], want_txt))
                continue
            if rec["target_elf"] != want_tgt:
                fails.append("%s ldr@%#x: target %#x, dump says %#x"
                             % (name, ldr_elf, rec["target_elf"], want_tgt))
                continue
            if rec["text"] != want_txt:
                fails.append("%s ldr@%#x: string %r, dump says %r"
                             % (name, ldr_elf, rec["text"], want_txt))
                continue
            if verbose:
                print("  ok   %-28s %#010x gap=%-2d -> %#010x %-8s %r"
                      % (name, ldr_elf, rec["gap"], rec["target_elf"],
                         rec["section"], rec["text"]))
    # ---- negative regression guard -----------------------------------------
    n += 1
    rec = resolve_at(img, FP_SITE_ELF)
    if rec is None:
        fails.append("negative guard: FP site %#x produced no pair at all; the "
                     "decoder regressed" % FP_SITE_ELF)
    elif "reject" not in rec:
        fails.append("negative guard: FP site %#x NOT rejected (target=%#x, %s) "
                     "-- D1 is not working"
                     % (FP_SITE_ELF, rec["target_elf"], rec["section"]))
    elif verbose:
        print("  ok   %-28s %#010x REJECTED (%s) target=%#x section=%s seg=%s"
              % ("negative/D1-guard", FP_SITE_ELF, rec["reject"],
                 rec["target_elf"], rec["section"],
                 rec["segment"].name if rec["segment"] else None))
    if fails:
        print("SELF-TEST FAILED  %d/%d assertions" % (len(fails), n),
              file=sys.stderr)
        for f in fails:
            print("  FAIL " + f, file=sys.stderr)
        return 3, n
    if verbose:
        print("\nself-test: %d/%d PASS  (20 positive re-derivations from 2 "
              "ground-truth dumps + 2 file-integrity assertions + 1 D1 negative "
              "guard)" % (n, n))
    return 0, n


# --------------------------------------------------------------------------
def main():
    # Windows consoles default to cp1252, which cannot encode Hangul/CJK literals
    # and crashes this tool on a legitimate non-ASCII literal. Reconfigure
    # explicitly instead of relying on the console codepage.
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8", errors="backslashreplace")
        except Exception:
            pass
    ap = argparse.ArgumentParser(
        description="Segment-aware Thumb literal-pool resolver (hardened).")
    ap.add_argument("--so", type=Path, default=DEFAULT_SO)
    ap.add_argument("--addr-convention", choices=("elf", "ghidra"), default="ghidra",
                    help="convention of addresses you PASS IN (default ghidra, "
                         "what every analysis/ghidra-*.txt dump uses)")
    ap.add_argument("--out-convention", choices=("elf", "ghidra"), default="ghidra",
                    help="convention of addresses printed (default ghidra)")
    ap.add_argument("--function", metavar="ADDR[:END]",
                    help="address range to scan structurally")
    ap.add_argument("--window", type=int, default=12,
                    help="max gap between a literal load and its ADD (default 12; "
                         "--window 4 reproduces the strict old tool)")
    ap.add_argument("--allow-rw", action="store_true",
                    help="D1 OFF: accept targets in a writable segment. Diagnostic "
                         "only -- this is the class that produced 'X'.")
    ap.add_argument("--from-dump", type=Path)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--skip-self-test", action="store_true",
                    help="UNSAFE: skip the self-test gate")
    ap.add_argument("--list-segments", action="store_true")
    args = ap.parse_args()

    if not args.so.exists():
        print("ERROR: %s not found (run from the workspace root)" % args.so,
              file=sys.stderr)
        return 2
    img = Image(args.so)
    in_bias = GHIDRA_BIAS if args.addr_convention == "ghidra" else 0
    out_bias = GHIDRA_BIAS if args.out_convention == "ghidra" else 0

    def O(elf_va):
        return elf_va + out_bias

    def I(a):
        return int(a, 16) - in_bias

    if args.list_segments:
        print("# %s  %d bytes" % (args.so, img.size))
        print("\nPT_LOAD (ELF VA):")
        for s in img.segments:
            print("  %#010x-%#010x filesz=%#010x memsz=%#010x %s off=%#010x "
                  "delta=%#x" % (s.vaddr, s.vaddr + s.memsz, s.filesz, s.memsz,
                                 s.name, s.offset, s.vaddr - s.offset))
        print("\nsections:")
        for nm, addr, size in img.sections:
            seg = img.segment(addr)
            print("  %-22s %#010x-%#010x  %s"
                  % (nm, addr, addr + size, seg.name if seg else "?"))
        return 0

    if args.self_test:
        rc, n = self_test(img)
        if rc == 0:
            print("\nSTATUS: VALIDATED for the two known-good ground-truth dumps "
                  "(20/20 re-derivations, targets and strings byte-identical).\n"
                  "The segment rule itself is a LOCAL HEURISTIC -- 'PF_W clear' -- "
                  "correct for this library, not proved universal.")
        return rc

    if not args.skip_self_test:
        rc, n = self_test(img, verbose=False)
        if rc != 0:
            print("self-test gate FAILED -- refusing to produce results "
                  "(re-run --self-test for detail)", file=sys.stderr)
            return rc
        print("# self-test %d/%d PASS -- D1 segment rule %s"
              % (n, n, "OFF (--allow-rw)" if args.allow_rw else "ACTIVE"))

    print("# %s  %d bytes" % (args.so, img.size))
    print("# in=%s out=%s window=%d\n" % (args.addr_convention,
                                          args.out_convention, args.window))
    ro = not args.allow_rw

    if args.from_dump:
        rows = load_ground_truth(args.from_dump, in_bias)
        ok = bad = 0
        for ldr_elf, want_tgt, want_txt in rows:
            rec = resolve_at(img, ldr_elf, args.window, ro)
            if rec is None or "reject" in rec:
                bad += 1
                print("  REJECT ldr@%#010x  %s"
                      % (O(ldr_elf), rec["reject"] if rec else "no pair"))
                continue
            flag = "OK    " if (rec["target_elf"] == want_tgt
                                and rec["text"] == want_txt) else "DIFFER"
            if flag == "OK    ":
                ok += 1
            else:
                bad += 1
            print("  %s ldr@%#010x slot=%#010x w=%#010x -> %#010x "
                  "(%s, %s) %r   [dump: %#010x %s]"
                  % (flag, O(ldr_elf), O(rec["slot_elf"]), rec["w"],
                     O(rec["target_elf"]), rec["section"],
                     rec["segment"].name, rec["text"], O(want_tgt), want_txt))
        print("\nmatched: %d   rejected-or-differing: %d   total: %d"
              % (ok, bad, len(rows)))
        return 0 if ok and not bad else 4

    if args.function:
        if ":" not in args.function:
            print("ERROR: --function wants ADDR[:END]", file=sys.stderr)
            return 2
        a, _, b = args.function.partition(":")
        lo, hi = I(a), (I(b) if b else I(a) + 0x400)
        recs = scan(img, lo, hi, args.window, ro)
        print("===== %#x..%#x   D1 %s   window=%d ====="
              % (O(lo), O(hi), "OFF" if not ro else "ON", args.window))
        for r in recs:
            print("ldr@%#010x r%-2d gap=%-2d slot=%#010x w=%#010x -> %#010x "
                  "(%s, %s) %r"
                  % (O(r["ldr_elf"]), r["rt"], r["gap"], O(r["slot_elf"]), r["w"],
                     O(r["target_elf"]), r["section"], r["segment"].name,
                     r["text"]))
        print("resolved: %d" % len(recs))
        return 0 if recs else 4

    ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())