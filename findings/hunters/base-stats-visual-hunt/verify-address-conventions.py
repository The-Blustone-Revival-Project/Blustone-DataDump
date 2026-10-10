#!/usr/bin/env python3
"""Reproduce every number in address-convention-2026-10-05.md.

Standard library only.  Reads analysis/extracted/lib/armeabi-v7a/libnative_core.so
plus the two TSVs and re-derives the conventions from scratch.  Run:

    python verify-address-conventions.py            # summary
    python verify-address-conventions.py --full     # every check

Why pure Python: llvm-objdump/llvm-nm print ELF VAs with NO 0x10000 bias, so
agreeing with them cannot corroborate a Ghidra-space claim (see the report's
§4b).  Parsing the ELF directly removes that whole confusion class.

NOTHING here writes to any file.
"""
import struct
import re
import sys
import os
import collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
SO = os.path.join(ROOT, 'analysis', 'extracted', 'lib', 'armeabi-v7a',
                  'libnative_core.so')
ALLSTR = os.path.join(ROOT, 'analysis', 'native-all-strings.tsv')
EVID = os.path.join(ROOT, 'analysis', 'native-evidence.tsv')

GHIDRA_BIAS = 0x10000          # Ghidra image addr == ELF VA + this
FULL = '--full' in sys.argv
VERBOSE = FULL or '-v' in sys.argv


def hdr(t):
    print()
    print('=' * 78)
    print(t)
    print('=' * 78)


# ---------------------------------------------------------------- load + parse
d = open(SO, 'rb').read()
N = len(d)
assert d[:4] == b'\x7fELF' and d[4] == 1 and d[5] == 1, 'expected ELF32 LE'

(e_phoff, e_shoff) = struct.unpack_from('<II', d, 28)
e_phentsz, e_phnum = struct.unpack_from('<HH', d, 42)
e_shentsz, e_shnum, e_shstrndx = struct.unpack_from('<HHH', d, 46)

loads = []
for i in range(e_phnum):
    o = e_phoff + i * e_phentsz
    t, off, va, pa, fsz, msz, fl, al = struct.unpack_from('<IIIIIIII', d, o)
    if t == 1:
        loads.append(dict(idx=i, off=off, va=va, fsz=fsz, msz=msz, delta=va - off))

shs = [struct.unpack_from('<IIIIIIIIII', d, e_shoff + i * e_shentsz)
       for i in range(e_shnum)]
_sb = shs[e_shstrndx][4]


def snm(x):
    e = d.index(b'\0', _sb + x)
    return d[_sb + x:e].decode('ascii', 'replace')


def sec(nm):
    return next(s for s in shs if snm(s[0]) == nm)


def sec_of(v):
    for s in shs:
        n = snm(s[0])
        if s[3] and s[3] <= v < s[3] + s[5] and n != '.bss':
            return n
    return '?'


def v2o(v):
    """True ELF vaddr -> file offset, segment aware.  None if bss/unmapped."""
    for L in loads:
        if L['va'] <= v < L['va'] + L['msz']:
            if v >= L['va'] + L['fsz']:
                return None
            return v - L['delta']
    return None


# ---------------------------------------------------------------- §2 program headers
hdr('§2  PROGRAM HEADERS  (the two PT_LOADs, and why no uniform bias works)')
print('filesize %d (0x%x)   e_phoff=0x%x e_phnum=%d e_shoff=0x%x e_shnum=%d'
      % (N, N, e_phoff, e_phnum, e_shoff, e_shnum))
for L in loads:
    print('  PT_LOAD %d  off=0x%08x vaddr=0x%08x filesz=0x%08x memsz=0x%08x '
          'delta=%+#x   p_vaddr==p_offset? %s'
          % (L['idx'], L['off'], L['va'], L['fsz'], L['msz'], L['delta'],
             L['off'] == L['va']))
seg0, seg1 = loads
print('  segment 0 covers VA 0x%08x..0x%08x (== file offset there)'
      % (seg0['va'], seg0['va'] + seg0['fsz']))
print('  segment 1 covers VA 0x%08x..0x%08x but file only 0x%08x..0x%08x'
      % (seg1['va'], seg1['va'] + seg1['msz'], seg1['off'],
         seg1['off'] + seg1['fsz']))
assert seg0['delta'] == 0 and seg1['delta'] == 0x1000

# ---------------------------------------------------------------- relocations (C8)
hdr('§3/§5  RELOCATIONS  (R_ARM_RELATIVE census + the relocated image)')
ARM = {0: 'R_ARM_NONE', 2: 'R_ARM_ABS32', 21: 'R_ARM_GLOB_DAT', 22: 'R_ARM_JUMP_SLOT',
       23: 'R_ARM_RELATIVE'}
types = collections.Counter()
relsec = collections.Counter()
img = bytearray(d)
nrel = 0
for nm in ('.rel.dyn', '.rel.plt'):
    s = sec(nm)
    es = s[9] or 8
    for k in range(s[5] // es):
        off, info = struct.unpack_from('<II', d, s[4] + k * es)
        ty = info & 0xff
        types[(nm, ty)] += 1
        if ty == 23:
            relsec[sec_of(off)] += 1
            fo = v2o(off)
            if fo is not None and fo + 4 <= N:
                struct.pack_into('<I', img, fo,
                                 (struct.unpack_from('<I', img, fo)[0] + GHIDRA_BIAS) & 0xffffffff)
                nrel += 1
for (nm, ty), c in sorted(types.items()):
    print('  %-10s %-18s %7d' % (nm, ARM.get(ty, 'type %d' % ty), c))
print('  R_ARM_NONE count   = %d   <-- point-info-type §1.9 claimed 128620' % types[('.rel.dyn', 0)])
print('  R_ARM_RELATIVE cnt = %d   <-- the real figure' % nrel)
print('  applied %d R_ARM_RELATIVE relocations with bias 0x%x' % (nrel, GHIDRA_BIAS))
print('  R_ARM_RELATIVE targets by section:')
for k, v in relsec.most_common():
    print('      %-24s %7d' % (k, v))
print('  *** .rodata relocations = %d , .text relocations = %d  -> literal-pool slots '
      'are UNRELOCATED' % (relsec.get('.rodata', 0), relsec.get('.text', 0)))
assert relsec.get('.rodata', 0) == 0 and relsec.get('.text', 0) == 0
assert nrel == 128620

# ---------------------------------------------------------------- string tables
def verify_strings(path, label):
    rows = open(path, 'rb').read().split(b'\n')
    rx = re.compile(rb'^([0-9a-f]{8})\t(.*)$', re.S)
    lab = re.compile(rb'^([^:\t]{1,64})::([0-9a-fA-F]{1,8})\t')
    res = collections.Counter()
    seg = collections.Counter()
    n_strict = n_lab = 0
    tok_all = []
    for r in rows:
        if lab.match(r):
            n_lab += 1
            continue
        m = rx.match(r)
        if not m:
            continue
        tok = int(m.group(1), 16)
        col = m.group(2)
        if col.endswith(b'\r'):
            col = col[:-1]                     # the TSV is CRLF; CR is not content
        n_strict += 1
        tok_all.append(tok)
        li = next((L['idx'] for L in loads if L['va'] <= tok - GHIDRA_BIAS
                   < L['va'] + L['msz']), None)
        # A: segment-aware Ghidra (the claim)
        o = v2o(tok - GHIDRA_BIAS)
        if o is not None and (bytes(img[o:o + len(col)]) == col or d[o:o + len(col)] == col):
            res['A_ghidra_segaware'] += 1
            seg['LOAD%s' % li] += 1
        # B: uniform file map, token - 0x10000
        na = tok - GHIDRA_BIAS
        if 0 <= na < N and (img[na:na + len(col)] == col or d[na:na + len(col)] == col):
            res['B_uniform_minus_0x10000'] += 1
        # C: plain ELF vaddr, seg-aware file map
        oe = v2o(tok)
        if oe is not None and (img[oe:oe + len(col)] == col or d[oe:oe + len(col)] == col):
            res['C_plain_elf'] += 1
        # D: token already a file offset
        if tok + len(col) <= N and d[tok:tok + len(col)] == col:
            res['D_token_is_offset'] += 1
    return rows, n_strict, n_lab, res, seg, tok_all


hdr('§3  native-all-strings.tsv  (C3)')
rows, n_strict, n_lab, res, seg, tok_all = verify_strings(ALLSTR, 'all-strings')
print('  strict 8-hex rows %d ; <section>:: rows %d ; total lines %d'
      % (n_strict, n_lab, len(rows)))
for k in ('A_ghidra_segaware', 'B_uniform_minus_0x10000', 'C_plain_elf',
          'D_token_is_offset'):
    print('  %-26s %7d / %d  = %8.4f %%'
          % (k, res[k], n_strict, 100.0 * res[k] / n_strict))
print('  A per-segment: LOAD1=%d LOAD2=%d' % (seg['LOAD1'], seg['LOAD2']))
print('  token range %08x .. %08x ; 4-aligned %.1f%% ; 2-aligned %.1f%%'
      % (min(tok_all), max(tok_all),
         100.0 * sum(1 for t in tok_all if t % 4 == 0) / len(tok_all),
         100.0 * sum(1 for t in tok_all if t % 2 == 0) / len(tok_all)))
assert res['A_ghidra_segaware'] == n_strict, 'A must be 100%'
assert seg['LOAD2'] == 1763 and seg['LOAD1'] == 513813

# segment-1 discriminator
seg1rows = [t for t in tok_all
            if loads[1]['va'] <= t - GHIDRA_BIAS < loads[1]['va'] + loads[1]['msz']]
ok_seg = ok_uni = 0
lin = open(ALLSTR, 'rb').read().split(b'\n')
for r in lin:
    m = re.match(rb'^([0-9a-f]{8})\t(.*)$', r, re.S)
    if not m:
        continue
    tok = int(m.group(1), 16)
    if not (loads[1]['va'] <= tok - GHIDRA_BIAS < loads[1]['va'] + loads[1]['msz']):
        continue
    col = m.group(2)[:-1] if m.group(2).endswith(b'\r') else m.group(2)
    fo = v2o(tok - GHIDRA_BIAS)
    if fo is not None and (img[fo:fo + len(col)] == col or d[fo:fo + len(col)] == col):
        ok_seg += 1
    na = tok - GHIDRA_BIAS
    if 0 <= na < N and (img[na:na + len(col)] == col or d[na:na + len(col)] == col):
        ok_uni += 1
print('  SEGMENT-1 DISCRIMINATOR (the D2 proof), %d rows:' % len(seg1rows))
print('     (token-0x10000)-0x1000  correct PT_LOAD map : %4d / %d   (loses %d)'
      % (ok_seg, len(seg1rows), len(seg1rows) - ok_seg))
print('     token-0x10000           uniform map          : %4d / %d   (loses %d)'
      % (ok_uni, len(seg1rows), len(seg1rows) - ok_uni))
print('     token as-is             plain ELF            : %4d / %d   (loses %d)'
      % (0, len(seg1rows), len(seg1rows)))
# NOTE the framing: 1759 is what the UNIFORM map LOSES, not what the correct
# map matches.  Conflating those two is a transposition error this script
# exists to prevent (see report section 6.1 item 10b).
assert ok_seg == 1763 and ok_uni == 4, (ok_seg, ok_uni)

# spot proofs
hdr('§3  SPOT PROOFS  (all segment 0, so the raw file suffices)')
SPOTS = [(0x0023dea0, b'_ZN6CSRGem17RequestGemLevelUpE'),
         (0x00296244, b'_ZN18CSRPopUpGemLevelUp11SetBaseInfoE'),
         (0x01d69394, b'/gvg/GetRef'),
         (0x01d6985b, b'point_id'),
         (0x003500f0, b'_ZN10CSRSyncRef11ReqGVGRefCB'),
         (0x01d69345, b'/gvg/GetInst'),
         (0x01d6e9dd, b'GEM_NAME1')]
for va, want in SPOTS:
    got = d[va:va + len(want)]
    print('  ELF %08x -> %-44r %s' % (va, got[:len(want)], 'OK' if got == want else 'MISMATCH'))
    assert got == want, hex(va)
# line number for 002a6244
for i, r in enumerate(lin):
    if r.startswith(b'002a6244\t'):
        print('  token 002a6244 is line %d  (%r)' % (i + 1, r[:60]))
        break

# ---------------------------------------------------------------- §4 evidence
hdr('§4  native-evidence.tsv  (C1 / C2 / C4)')
erows = open(EVID, 'rb').read().split(b'\n')
print('  line 1 : %r' % erows[0][:60])
print('  line 2 : %r   <-- the self-declared image base' % erows[1][:60])
assert erows[1].startswith(b'IMAGE_BASE')
i0 = next(i for i, r in enumerate(erows) if r.startswith(b'[FUNCTIONS]'))
j0 = next(i for i, r in enumerate(erows) if r.startswith(b'[RAW_PRINTABLE_STRINGS]'))
frows = []
for r in erows[i0 + 1:j0]:
    rr = r[:-1] if r.endswith(b'\r') else r
    if not rr.strip():
        continue
    q = rr.split(b'\t')
    if not re.fullmatch(rb'[0-9a-fA-F]{8}', q[0]):
        continue
    frows.append((int(q[0], 16), q[1].decode('utf-8', 'replace'),
                  q[2].decode('utf-8', 'replace') if len(q) > 2 else ''))
print('  [FUNCTIONS] rows %d ; [RAW_PRINTABLE_STRINGS] header at line %d'
      % (len(frows), j0 + 1))

# dynsym straight from the file
s = sec('.dynsym')
strt = shs[s[6]]
so = strt[4]
DS = {}
und = dfd = 0
for k in range(s[5] // (s[9] or 16)):
    o = s[4] + k * (s[9] or 16)
    nm, value, size, info, other, shndx = struct.unpack_from('<IIIBBH', d, o)
    e = d.index(b'\0', so + nm)
    DS.setdefault(d[so + nm:e].decode('utf-8', 'replace'), []).append(
        (value, size, info & 0xf, shndx))
    if shndx == 0:
        und += 1
    else:
        dfd += 1
print('  .dynsym: %d entries ; %d SHN_UNDEF ; %d defined ; %d distinct defined names'
      % (len(DS) and sum(len(v) for v in DS.values()), und, dfd,
         len({n for n, e in DS.items() if any(x[0] for x in e)})))

cat = collections.Counter()
ext = []
for tok, nm, c3 in frows:
    if nm in DS:
        if any((v & ~1) + GHIDRA_BIAS == tok for (v, sz, ty, sh) in DS[nm]):
            cat['MATCH (st_value & ~1) + 0x10000'] += 1
        elif any(x[0] == 0 for x in DS[nm]):
            cat['dynsym import, st_value == 0'] += 1
            if v2o(tok - GHIDRA_BIAS) is None:
                ext.append(tok)
        else:
            cat['dynsym defined, address differs'] += 1
    elif nm.startswith('_INIT_'):
        cat['_INIT_* pseudo-symbol'] += 1
    elif nm.startswith('_FINI_'):
        # _FINI_0/_FINI_1: linker-synthesized, NOT in .dynsym, NOT FUN_* either
        cat['_FINI_* linker pseudo-symbol'] += 1
    elif re.match(r'^(FUN|SUB|SUP|loc|switch|thunk)', nm):
        cat['Ghidra-synthesized name'] += 1
    else:
        cat['unknown name'] += 1
print('  [FUNCTIONS] classification:')
for k, v in cat.most_common():
    print('      %-38s %6d  (%.2f %%)' % (k, v, 100.0 * v / len(frows)))
assert cat['MATCH (st_value & ~1) + 0x10000'] == 36467
assert cat['dynsym import, st_value == 0'] == 735
# all non-dynsym rows together = 2800
synth = (cat['Ghidra-synthesized name'] + cat['_INIT_* pseudo-symbol']
         + cat['_FINI_* linker pseudo-symbol'] + cat['unknown name'])
assert synth == 2800, synth
undtag = sum(1 for _, _, c in frows if 'undefined' in c)
print('  rows tagged `undefined`: %d / %d  (mislabel rate %.1f %%)'
      % (undtag, len(frows), 100.0 * (len(frows) - 735) / len(frows)))
assert undtag == len(frows)

# FUN_ self-consistency
fun = [(t, n) for t, n, _ in frows if re.fullmatch(r'FUN_[0-9a-f]{8}', n)]
m = sum(1 for t, n in fun if int(n[4:], 16) == t)
print('  FUN_<hex> name == address column : %d / %d  (self-declaring proof)' % (m, len(fun)))
assert m == len(fun)

# EXTERNAL block
print('  rows with NO file backing at all: %d' % len(ext))
if ext:
    print('     Ghidra %08x..%08x -> ELF %08x..%08x ; .bss ends 0x%08x'
          % (min(ext), max(ext), min(ext) - GHIDRA_BIAS, max(ext) - GHIDRA_BIAS,
             sec('.bss')[3] + sec('.bss')[5]))
    assert max(ext) - GHIDRA_BIAS > sec('.bss')[3] + sec('.bss')[5]

# section distribution
dist = collections.Counter(sec_of(t - GHIDRA_BIAS) for t, _, _ in frows)
print('  section distribution under ELF = token - 0x10000:')
for k, v in dist.most_common():
    print('      %-24s %6d' % (k, v))

# RAW_PRINTABLE_STRINGS
hdr('§4  [RAW_PRINTABLE_STRINGS]  (C3)')
srows = [r for r in erows[j0 + 1:] if r.strip()]
slab = [r for r in srows if re.match(rb'^[^:\t]{1,64}::[0-9a-fA-F]{1,8}\t', r)]
plain = []
for r in srows:
    m = re.match(rb'^([0-9a-fA-F]{8})\t', r)
    if not m:
        continue
    col = r.split(b'\t', 1)[1]
    plain.append((int(m.group(1), 16), col[:-1] if col.endswith(b'\r') else col))
ok = 0
for tok, col in plain:
    o = v2o(tok - GHIDRA_BIAS)
    if o is not None and (img[o:o + len(col)] == col or d[o:o + len(col)] == col):
        ok += 1
print('  plain 8-hex rows %d ; <section>:: rows %d' % (len(plain), len(slab)))
print('  segment-aware Ghidra match: %d / %d = %.4f %%' % (ok, len(plain),
                                                           100.0 * ok / len(plain)))
assert ok == len(plain) == 8642

# C4 section-relative
hdr('§3a  C4 rows: <section>::<offset>  (a THIRD space)')
shmap = {snm(x[0]): x for x in shs}
c4ok = c4bad = c4other = 0
for path in (ALLSTR, EVID):
    for r in open(path, 'rb').read().split(b'\n'):
        m = re.match(rb'^([^:\t]{1,64})::([0-9a-fA-F]{1,8})\t', r)
        if not m:
            continue
        head = r[:r.index(b'\t')].decode()
        nm, _, so_ = head.rpartition('::')
        col = r.split(b'\t', 1)[1]
        col = col[:-1] if col.endswith(b'\r') else col
        if nm not in shmap:
            c4other += 1
            continue
        fo = shmap[nm][4] + int(so_, 16)
        if fo + len(col) <= N and d[fo:fo + len(col)] == col:
            c4ok += 1
        else:
            c4bad += 1
print('  section-relative hypothesis: ok=%d bad=%d pseudo-label=%d (total %d)'
      % (c4ok, c4bad, c4other, c4ok + c4bad + c4other))
print('  (the pseudo-label is `_elfSectionHeaders`, which is not in .shstrtab;')
print('   it resolves against e_shoff instead - see report section 3a)')
assert c4bad == 0 and c4ok + c4bad + c4other == 42

# ---------------------------------------------------------------- §4b objdump
hdr('§4b  TOOLCHAIN CAVEAT  (reproduce with llvm-objdump)')
if VERBOSE:
    import subprocess
    o = os.path.join(ROOT, 'tools', 'android-sdk', 'ndk', '29.0.14206865',
                     'toolchains', 'llvm', 'prebuilt', 'windows-x86_64', 'bin',
                     'llvm-objdump.exe')
    if os.path.exists(o):
        for args in (['-f', SO],
                     ['-d', '--start-address=0xbc0454', '--stop-address=0xbc045c', SO],
                     ['-d', '--triple=thumbv7-linux-gnueabihf',
                      '--start-address=0xbc0454', '--stop-address=0xbc045c', SO]):
            r = subprocess.run([o] + args, capture_output=True, text=True,
                               errors='replace')
            print('  $ llvm-objdump %s' % ' '.join(args[:-1]))
            for ln in r.stdout.splitlines():
                if ln.strip():
                    print('      ' + ln.strip()[:110])
    else:
        print('  llvm-objdump not found; skipped')
print('  key point: objdump/nm labels are ELF VAs (NO 0x10000), so they are NOT')
print('  independent evidence for C1/C3. This script uses no external tool.')
# Thumb halfwords are little-endian in the file: `push {r4-r7,lr}` = 0xb5f0 stored
# as f0 b5.  llvm-objdump prints the halfword (b5f0), NOT the file byte order.
hw = struct.unpack_from('<H', d, 0x0bc0454)[0]
print('  SetBaseInfo ELF 0x0bc0454: file bytes %r -> Thumb halfword 0x%04x '
      '(objdump prints "b5f0")' % (d[0x0bc0454:0x0bc0456], hw))
assert d[0x0bc0454:0x0bc0456] == b'\xf0\xb5' and hw == 0xb5f0

hdr('ALL ASSERTIONS PASSED')
