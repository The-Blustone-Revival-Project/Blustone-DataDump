#!/usr/bin/env python3
"""Harvest EVERY archived revision of the 11 vsfan stat-table hero pages and
parse each one's Character Attributes table.

Prior lane read exactly ONE revision of each of these pages. The archive holds
several revisions per page. If a revision predates/postdates the T3 caption, or
fills in the Life/Attack/Defense rows, this is where a T1/T2/T4 observation
would be.

Method notes / traps honoured:
  * exact-URL CDX (never the availability API -- documented FALSE NEGATIVES for
    '?'-query URLs);
  * a positive control fetch runs first and must succeed;
  * every fetch reports http status + byte count, and dedup is by CONTENT
    sha256 so a re-crawl of the same revision is not counted twice;
  * Wayback rewrites image src to im_ even for uncaptured images, so image
    presence is never used as a positive signal here.
"""
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"
CDX = "https://web.archive.org/cdx/search/cdx?"

TARGETS = ["Captain", "Hermes", "Riko", "Bear", "Diana", "Joy",
           "Kain", "Lantern", "Pansy", "Patrone", "Scar"]

CATALOG = {"Captain": "009", "Hermes": "023", "Riko": "024", "Bear": "036",
           "Diana": "031", "Joy": "035", "Kain": "029", "Lantern": "001",
           "Pansy": "057", "Patrone": "033", "Scar": "032"}


def fetch(url, timeout=180, tries=4):
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            body = e.read()
            if e.code in (502, 503, 504) and attempt < tries - 1:
                time.sleep(4 * (attempt + 1)); continue
            return e.code, body
        except Exception as e:
            if attempt < tries - 1:
                time.sleep(4 * (attempt + 1)); continue
            return None, str(e).encode("utf-8", "replace")
    return None, b""


def cdx(url_prefix):
    q = CDX + urllib.parse.urlencode({"url": url_prefix, "matchType": "prefix",
                                      "output": "text", "limit": "5000"})
    st, body = fetch(q)
    if st != 200:
        return st, None
    lines = [l for l in body.decode("utf-8", "replace").split("\n") if l.strip()]
    return st, lines[1:] if lines and lines[0].startswith("net,") else lines


TAG = re.compile(r"<[^>]+>")
CELL = re.compile(r"<t[hd][^>]*>(.*?)</t[hd]>", re.S | re.I)


def clean(s):
    s = TAG.sub(" ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def parse_tables(txt):
    """Return every wikitable as a list of (row -> [cells])."""
    out = []
    for m in re.finditer(r"<table[^>]*class=\"wikitable\"[^>]*>(.*?)</table>", txt, re.S | re.I):
        tbl = m.group(1)
        cm = re.search(r"<caption>(.*?)</caption>", tbl, re.S | re.I)
        caption = clean(cm.group(1)) if cm else None
        rows = []
        for rm in re.finditer(r"<tr[^>]*>(.*?)</tr>", tbl, re.S | re.I):
            cells = [clean(c) for c in CELL.findall(rm.group(1))]
            if cells:
                rows.append(cells)
        out.append((caption, rows))
    return out


def find_attr_table(tables):
    for cap, rows in tables:
        if any("Character Attributes" in " ".join(r) for r in rows):
            return cap, rows
    return None, None


def pull(rows, label):
    for r in rows:
        for i, c in enumerate(r):
            if c.lower() == label.lower() and i + 1 < len(r):
                return r[i + 1]
    return None


def oldid_of(txt):
    m = re.findall(r"oldid=(\d+)", txt)
    return m[-1] if m else None


def main(outdir):
    os.makedirs(outdir, exist_ok=True)

    # ---------- POSITIVE CONTROL (must pass before any negative is believed) ----------
    st, body = fetch("https://web.archive.org/web/20190821024308id_/https://vsfan.net/wiki/Beckhen")
    ok = (st == 200 and len(body) == 88572)
    print(f"[CONTROL] Beckhen id_ -> http={st} bytes={len(body)} expect=88572  {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("ABORT: positive control failed; no negative may be reported.")
        return 2

    results = []
    for title in TARGETS:
        tq = urllib.parse.quote(title)
        st, rows = cdx(f"vsfan.net/wiki/{tq}")
        if st != 200 or rows is None:
            print(f"  [{title}] CDX http={st} -> SKIP (no negative claimed)")
            results.append({"title": title, "error": f"cdx_http_{st}"})
            continue
        caps = []
        for r in rows:
            p = r.split(" ")
            if len(p) < 7:
                continue
            if p[4] == "200" and "text/html" in p[3]:
                caps.append((p[1], p[2], int(p[6])))
        caps.sort()
        print(f"\n=== {title} (catalog {CATALOG[title]}): {len(caps)} HTML-200 captures ===")
        seen = {}
        for ts, orig, cdxlen in caps:
            url = f"https://web.archive.org/web/{ts}id_/{orig}"
            st2, b = fetch(url)
            if st2 != 200:
                print(f"    {ts} http={st2} bytes={len(b)}  FETCH FAILED")
                results.append({"title": title, "ts": ts, "http": st2})
                continue
            sha = hashlib.sha256(b).hexdigest()
            dup = seen.get(sha)
            seen[sha] = ts
            txt = b.decode("utf-8", "replace")
            tables = parse_tables(txt)
            cap, rows2 = find_attr_table(tables)
            life = pull(rows2, "Life") if rows2 else None
            atk = pull(rows2, "Attack") if rows2 else None
            dfen = pull(rows2, "Defense") if rows2 else None
            asp = pull(rows2, "Attack Speed") if rows2 else None
            transc = sorted(set(re.findall(r"Transcendence[^<]{0,40}", txt, re.I)))
            print(f"    {ts} http=200 bytes={len(b)} cdxlen={cdxlen} oldid={oldid_of(txt)}"
                  f" {'DUP-of-' + dup if dup else 'UNIQUE'}")
            print(f"        caption={cap!r}")
            print(f"        Life={life!r} Attack={atk!r} Defense={dfen!r} AttackSpeed={asp!r}")
            if transc:
                print(f"        TRANSCENDENCE STRINGS: {transc[:6]}")
            results.append({
                "title": title, "catalog": CATALOG[title], "ts": ts, "url": url,
                "http": st2, "bytes": len(b), "cdxlen": cdxlen,
                "sha256": sha, "oldid": oldid_of(txt),
                "duplicate_of": dup, "caption": cap,
                "life": life, "attack": atk, "defense": dfen, "attack_speed": asp,
                "transcendence_strings": transc,
            })
        print(f"    -> {len(caps)} captures, {len(seen)} distinct contents")

    out = os.path.join(outdir, "vsfan-11hero-all-revisions.json")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(results, f, indent=1, ensure_ascii=False)
    print(f"\nsaved -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
