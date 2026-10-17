#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
jet_namespace_walk.py -- crosswalk the 22 catalog monster ART PACKAGES to the
episode monster res_ids that carry stat blocks in EPISODE_STAT_ACTORS.json.

Recovered JET format (verified below by positive control):
  * 24-byte outer header at offset 0: u32 uncompressed_size, u32 dup,
    u32 packed_size, u64 record_id, u16 pad, u16 kind ("I2" ...), then `packed`
    bytes of raw zlib.
  * subsequent records: identical 24-byte header + `packed` zlib bytes;
    record length = 24 + packed_size.
  * the record NAME is its u64 id rendered in base 38 over
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._".  (Anonymous I2 texture records
    hash to opaque token names like "NUIM6M"; the sprite/animation families
    S2/AT decode to live names such as M022_R01 / M022_SHADOW.)

Positive control (script exits without writing if it fails):
  walking M008.jet must end exactly at its file size AND produce the
  M022_R01..R04 / M022_H01..H15 / M022_DIE / M022_SHADOW / M022_S families
  documented in findings/episodes/episode-cb0102-m022-original-resources.md
  (33 M022-prefixed records).

Output: jet-monster-namespaces.tsv (one row per catalog package, with every
decoded Mxxx namespace it hosts) and jet-monster-namespaces.json.
"""
import io, os, struct, zlib, sys, json, collections, re

ROOT = r"C:\Users\shaha\Documents\GitHub\Blustone-DataDump"
OUT = os.path.join(ROOT, "findings", "hunters", "base-stats-visual-hunt",
                   "monster-stat-estimates-2026-10-11")

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._"
JET_DIRS = [
    r"local\archive\analysis\jadx\resources\assets",
    r"local\inputs\extracted\assets",
    r"local\private\recovered-assets\phone-2026-09-18\extracted\split_PADResource\assets",
]
HDR = 24


def b38(n):
    if n == 0:
        return "0"
    out = []
    while n:
        n, r = divmod(n, 38)
        out.append(ALPHABET[r])
    return "".join(reversed(out))


def walk(data):
    """Yield (offset, kind, record_id, name, packed, payload).

    Raises ValueError if the chain does not consume the file exactly.
    """
    n = len(data)
    pos = 0
    while pos + HDR <= n:
        size, dup, packed, rid = struct.unpack_from("<IIIQ", data, pos)
        kind = data[pos + 22:pos + 24]
        if size == 0 or packed == 0:
            raise ValueError("zero size/packed at %d" % pos)
        if pos + HDR + packed > n:
            raise ValueError("record overruns file at %d" % pos)
        body = data[pos + HDR:pos + HDR + packed]
        yield pos, kind.decode("latin-1"), rid, b38(rid), packed, body
        pos += HDR + packed
    if pos != n:
        raise ValueError("walk ended at %d, file is %d" % (pos, n))


def ns_of(name):
    """Monster namespace token of a decoded name: M022_R01 -> M022."""
    m = re.match(r"^(M\d{3})_", name)
    return m.group(1) if m else None


def main():
    base = None
    for d in JET_DIRS:
        if os.path.isdir(os.path.join(ROOT, d)):
            base = os.path.join(ROOT, d)
            break
    if base is None:
        sys.exit("no JET asset directory found")
    print("JET asset dir: %s" % os.path.relpath(base, ROOT))

    # ---------------- positive control --------------------------------------
    p8 = os.path.join(base, "M008.jet")
    d8 = open(p8, "rb").read()
    try:
        recs = list(walk(d8))
    except ValueError as e:
        sys.exit("POSCTL FAILED (%s)" % e)
    names = [r[3] for r in recs]
    m022 = sorted({ns_of(n) for n in names if ns_of(n) == "M022"} |
                  {n for n in names if n.startswith("M022_")})
    exp = {"M022_R01", "M022_R02", "M022_R03", "M022_R04", "M022_DIE",
           "M022_SHADOW", "M022_S", "M022_TH"}
    got = {n for n in names if n.startswith("M022_")}
    ok = (all(n in got for n in exp)
          and len([n for n in names if n.startswith("M022_")]) == 33)
    print("POSCTL M008.jet: %d records, exact EOF, %d M022_* names; "
          "expected families present: %s -> %s"
          % (len(recs), len(got), sorted(exp), "OK" if ok else "FAIL"))
    if not ok:
        sys.exit("POSCTL FAILED: M022 families not reproduced")

    # ---------------- full crosswalk ----------------------------------------
    rows = []
    jsonrows = []
    for i in list(range(1, 22)) + [100]:
        pkg = "M%03d" % i
        p = os.path.join(base, pkg + ".jet")
        if not os.path.exists(p):
            rows.append((pkg, "MISSING", "", "", ""))
            continue
        data = open(p, "rb").read()
        try:
            recs = list(walk(data))
        except ValueError as e:
            rows.append((pkg, "WALK-FAILED: %s" % e, "", "", ""))
            continue
        names = [r[3] for r in recs]
        nss = collections.Counter()
        fams = collections.defaultdict(set)
        for nm in names:
            ns = ns_of(nm)
            if ns:
                nss[ns] += 1
                fams[ns].add(nm)
        # does the package also host its own literal id namespace?
        own = pkg in nss
        rows.append((pkg,
                     "OK exact-EOF %d recs" % len(recs),
                     "yes" if own else "no",
                     ";".join("%s(%d)" % (k, v) for k, v in sorted(nss.items())),
                     ";".join("%s: %s" % (k, ",".join(sorted(fams[k])))
                              for k in sorted(nss))))
        jsonrows.append({
            "package": pkg, "bytes": len(data), "records": len(recs),
            "own_namespace_present": own,
            "namespaces": {k: {"count": v, "families": sorted(fams[k])}
                           for k, v in sorted(nss.items())},
        })

    with io.open(os.path.join(OUT, "jet-monster-namespaces.tsv"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write("package\twalk\towns_own_namespace\thosted_Mxxx_namespaces(count)\n")
        for a, b, c, d, e in rows:
            f.write("%s\t%s\t%s\t%s\n" % (a, b, c, d))
    with io.open(os.path.join(OUT, "jet-monster-namespaces.json"), "w",
                 encoding="utf-8", newline="\n") as f:
        json.dump(jsonrows, f, ensure_ascii=False, indent=1)

    print("\n%-6s %-26s %-6s %s" % ("pkg", "walk", "own", "hosted namespaces"))
    for a, b, c, d, e in rows:
        print("%-6s %-26s %-6s %s" % (a, b, c, d))
    print("\nwrote jet-monster-namespaces.tsv / .json")


if __name__ == "__main__":
    main()
