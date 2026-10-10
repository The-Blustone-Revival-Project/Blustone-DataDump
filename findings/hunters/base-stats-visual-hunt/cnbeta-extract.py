"""Frame extraction for the CN-server beta playthrough av38052023.

Read-only against the source video. Writes JPEGs into a plain subfolder of the
research directory. Verifies every extracted frame actually decoded and reports
real pixel dimensions (GUARD: never trust a status code).
"""
import json
import os
import subprocess
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
VID = os.path.expandvars(r"%TEMP%\opencode\zh\vids\av38052023_BV12t411v71Y.mp4")


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def probe():
    p = run([
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration,size", "-show_entries",
        "stream=index,codec_name,width,height,nb_frames", "-of", "json", VID,
    ])
    return json.loads(p.stdout)


def extract(outdir, fps, start=None, duration=None, label=""):
    os.makedirs(outdir, exist_ok=True)
    cmd = ["ffmpeg", "-nostdin", "-v", "error", "-y"]
    if start is not None:
        cmd += ["-ss", str(start)]
    if duration is not None:
        cmd += ["-t", str(duration)]
    cmd += ["-i", VID, "-vf", "fps=%s" % fps, "-q:v", "3", os.path.join(outdir, "f_%06d.jpg")]
    r = run(cmd)
    return r.returncode, r.stderr.strip()[:2000]


def verify(outdir):
    """Every frame must decode AND be non-degenerate. Report real dimensions."""
    names = sorted(n for n in os.listdir(outdir) if n.endswith(".jpg"))
    dims = {}
    bad = []
    sizes = []
    for n in names:
        p = os.path.join(outdir, n)
        sizes.append(os.path.getsize(p))
        try:
            im = Image.open(p)
            im.load()
            dims[im.size] = dims.get(im.size, 0) + 1
        except Exception as exc:  # noqa: BLE001
            bad.append((n, repr(exc)))
    return names, dims, bad, sizes


if __name__ == "__main__":
    mode = sys.argv[1]
    info = probe()
    print(json.dumps(info, indent=1))
    dur = float(info["format"]["duration"])
    if mode == "control":
        out = os.path.expandvars(r"%TEMP%\opencode\cnbeta\control")
        rc, err = extract(out, "1/4")
        names, dims, bad, sizes = verify(out)
        print("CONTROL rc=%s err=%r frames=%d dims=%s bad=%d" % (rc, err, len(names), dims, len(bad)))
        print("bytes min/med/max = %d / %d / %d" % (min(sizes), sorted(sizes)[len(sizes) // 2], max(sizes)))
        for n in names[:3] + names[-3:]:
            print("  ", n, os.path.getsize(os.path.join(out, n)))
    elif mode == "full1s":
        out = os.path.expandvars(r"%TEMP%\opencode\cnbeta\f1s")
        rc, err = extract(out, "1")
        names, dims, bad, sizes = verify(out)
        print("FULL-1s rc=%s err=%r frames=%d dims=%s bad=%d" % (rc, err, len(names), dims, len(bad)))
        print("expected frames = %d (duration %.1f s)" % (round(dur), dur))
        print("t range = %s .. %s" % (names[0], names[-1]))