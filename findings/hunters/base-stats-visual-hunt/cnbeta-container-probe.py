"""Ground-truth probe of an MP4 whose container advertises 1796 s but which
ffmpeg stops decoding at ~727 s. Answers: how much is ACTUALLY decodable,
and is the file truncated?

Read-only. No PowerShell text cmdlets.
"""
import json
import os
import struct
import subprocess
import sys

VID = os.path.expandvars(r"%TEMP%\opencode\zh\vids\av38052023_BV12t411v71Y.mp4")


def run(cmd, timeout=None):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=timeout)


def boxes(path):
    """Walk top-level (and 1-level nested) MP4 boxes with real offsets/sizes."""
    size_total = os.path.getsize(path)
    out = []
    with open(path, "rb") as fh:
        def walk(fh, start, end, depth):
            pos = start
            while pos + 8 <= end:
                fh.seek(pos)
                hdr = fh.read(8)
                if len(hdr) < 8:
                    break
                bsize, btype = struct.unpack(">I4s", hdr)
                hsize = 8
                if bsize == 1:
                    ext = fh.read(8)
                    if len(ext) < 8:
                        break
                    bsize = struct.unpack(">Q", ext)[0]
                    hsize = 16
                elif bsize == 0:
                    bsize = end - pos
                out.append((depth, pos, bsize, btype.decode("latin-1"), pos + bsize <= end))
                if btype in (b"moov", b"trak", b"mdia", b"minf", b"stbl", b"edts", b"udta"):
                    walk(fh, pos + hsize, min(pos + bsize, end), depth + 1)
                if bsize <= 0:
                    break
                pos += bsize
        walk(fh, 0, size_total, 0)
    return out, size_total


def count_decodable(path):
    """Count video frames actually emitted, ignoring the null muxer's dts check."""
    r = run(["ffmpeg", "-nostdin", "-v", "error", "-fflags", "+genpts+igndts",
             "-i", path, "-map", "0:v:0", "-vsync", "0", "-f", "rawvideo",
             "-y", os.devnull])
    return r.returncode, r.stderr[-1500:]


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "boxes":
        bx, total = boxes(VID)
        for depth, pos, size, name, complete in bx:
            print("%s%-6s off=%-12d size=%-12d end=%-12d complete=%s"
                  % ("  " * depth, name, pos, size, pos + size, complete))
        print("FILE SIZE =", total)
    elif mode == "rawcount":
        rc, err = count_decodable(VID)
        print("rawvideo rc =", rc)
        print("stderr tail:", err)
    elif mode == "showframes":
        r = run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                 "-show_entries", "packet=pts_time,flags,duration_time",
                 "-of", "json", "-read_intervals", "%s+%s" % (sys.argv[2], sys.argv[3]),
                 VID], timeout=300)
        data = json.loads(r.stdout or "{}")
        pk = data.get("packets", [])
        print("packets in interval:", len(pk))
        if pk:
            print("first:", pk[0], " last:", pk[-1])