#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
search_monster_ids.py -- task 3: workspace-wide census of catalog monster IDs
M001..M021 and M100 (plus the wider episode roster M001..M069 that does appear in
EPISODE_STAT_ACTORS.json), reported with file + line + context.

Fast path: the whole file is read as BYTES and searched with a compiled bytes
regex; only lines that actually match are decoded. Nothing outside this output
folder is written.

Skipped-by-extension (pure media / disk-image / archive / native, where an
M0nn byte token carries no meaning and the read cost is the whole bottleneck):
.png .jpg .jpeg .gif .webp .bmp .ico .mp4 .mp3 .ogg .wav .m4a .webm .mkv .avi
.img .qcow2 .vmdk .vdi .apk .ipa .tar .tgz .gz .zip .7z .rar .so .dll .exe .oat
.odex .vdex .art .dex .jar .ldb .bin .dat .db .sqlite .pack .unity3d .asset
Every skipped file is counted and reported by extension so that a read limit is
never mistaken for a content negative.

Positive control: M100 and M001 must both be found in
sources/client-tables/reference/EPISODE_STAT_ACTORS.json.
"""
import io, os, re, sys, json, collections

ROOT = r"C:\Users\shaha\Documents\GitHub\Blustone-DataDump"
OUT = os.path.join(ROOT, "findings", "hunters", "base-stats-visual-hunt",
                   "monster-stat-estimates-2026-10-11")

CATALOG = ["M%03d" % i for i in range(1, 22)] + ["M100"]
WIDER = set("M%03d" % i for i in range(1, 70)) | {"M100"}
TOKEN = re.compile(rb"\bM\d{3}\b")
SKIP_DIRS = {".git", "__pycache__", "node_modules"}
MAXB = 32 * 1024 * 1024

SKIP_EXT = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".ico", ".tif", ".tiff",
    ".mp4", ".mp3", ".ogg", ".wav", ".m4a", ".webm", ".mkv", ".avi", ".mov", ".flac",
    ".img", ".qcow2", ".vmdk", ".vdi", ".vhd", ".iso", ".dmg",
    ".apk", ".ipa", ".tar", ".tgz", ".gz", ".bz2", ".xz", ".zip", ".7z", ".rar",
    ".so", ".dll", ".exe", ".oat", ".odex", ".vdex", ".art", ".dex", ".jar",
    ".ldb", ".log2", ".bin", ".dat", ".db", ".sqlite", ".sqlite3", ".pack",
    ".unity3d", ".asset", ".bundle", ".ttf", ".otf", ".woff", ".woff2", ".pdf",
    ".pcap", ".pcapng", ".har", ".prof", ".blob", ".spv", ".ktx", ".astc",
}


def iter_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            yield os.path.join(dirpath, fn)


def main():
    hits = collections.defaultdict(list)
    n_scan = n_skip_ext = n_too_big = n_readerr = 0
    skipped = collections.Counter()
    skipped_bytes = 0

    for p in iter_files():
        ext = os.path.splitext(p)[1].lower()
        if ext in SKIP_EXT:
            n_skip_ext += 1
            skipped[ext] += 1
            try:
                skipped_bytes += os.path.getsize(p)
            except OSError:
                pass
            continue
        try:
            if os.path.getsize(p) > MAXB:
                n_too_big += 1
                continue
            with open(p, "rb") as f:
                data = f.read()
        except OSError:
            n_readerr += 1
            continue
        n_scan += 1
        if not TOKEN.search(data):
            continue
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        for ln, raw in enumerate(data.split(b"\n"), 1):
            if not TOKEN.search(raw):
                continue
            try:
                line = raw.decode("utf-8")
            except UnicodeDecodeError:
                line = raw.decode("utf-8", "replace")
            for m in re.finditer(r"\bM(\d{3})\b", line):
                mid = "M" + m.group(1)
                if mid in WIDER:
                    hits[mid].append((rel, ln, line.strip()[:400]))

    print("content-scanned %d files; skipped by ext %d (%.1f GB); >32MB %d; read-error %d"
          % (n_scan, n_skip_ext, skipped_bytes / 2**30, n_too_big, n_readerr))
    print("skipped extensions: %s"
          % ", ".join("%s=%d" % kv for kv in sorted(skipped.items())))

    actors_rel = "sources/client-tables/reference/EPISODE_STAT_ACTORS.json"
    for ctl in ("M100", "M001"):
        ok = any(h[0] == actors_rel for h in hits.get(ctl, []))
        print("POSCTL %s present in %s -> %s" % (ctl, actors_rel, "OK" if ok else "FAIL"))
        if not ok:
            sys.exit("POSITIVE CONTROL FAILED - scan broken, nothing written")

    order = ["M%03d" % i for i in range(1, 70)] + ["M100"]
    with io.open(os.path.join(OUT, "monster-id-workspace-census.tsv"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write("monster_id\tin_catalog_22\ttoken_hits\tdistinct_files\t"
                "first_file\tfirst_line\tsample_context\n")
        for mid in order:
            hs = hits.get(mid, [])
            files = sorted({h[0] for h in hs})
            if hs:
                a, b, c = hs[0]
                sample = " || ".join("%s:%d" % (x, y) for x, y, _ in hs[:4])
            else:
                a = b = c = sample = ""
            f.write("%s\t%s\t%d\t%d\t%s\t%s\t%s\n"
                    % (mid, "yes" if mid in CATALOG else "no", len(hs),
                       len(files), a, b, sample))

    with io.open(os.path.join(OUT, "monster-id-workspace-census.json"), "w",
                 encoding="utf-8", newline="\n") as f:
        json.dump({"scanned_files": n_scan,
                   "skipped_by_ext": n_skip_ext,
                   "skipped_ext_detail": dict(skipped),
                   "too_large": n_too_big, "read_errors": n_readerr,
                   "hits": {k: v for k, v in sorted(hits.items())}},
                  f, ensure_ascii=False, indent=1)

    print("\n%-6s %-6s %-7s %s" % ("id", "cat22", "hits", "files"))
    for mid in order:
        hs = hits.get(mid, [])
        if not hs:
            continue
        print("%-6s %-6s %-7d %d" % (mid, "yes" if mid in CATALOG else "no",
                                     len(hs), len({h[0] for h in hs})))
    zero = [m for m in CATALOG if not hits.get(m)]
    print("\nCATALOG IDS WITH ZERO CONTENT HITS: %s" % (", ".join(zero) or "none"))
    print("wrote monster-id-workspace-census.tsv / .json")


if __name__ == "__main__":
    main()
