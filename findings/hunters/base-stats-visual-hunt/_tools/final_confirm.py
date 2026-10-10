#!/usr/bin/env python3
"""Final confirmation pass:
 (a) every archived revision of 10 MORE hero pages -> is oldid always the same?
 (b) what ARE the 2021 ~2,2xx-byte captures? (suspected dead-wiki stubs)
 (c) the two pages whose content genuinely changed: Blustone, Hunter_Supply_Office.

CONTROL FIRST: Beckhen id_ -> 200 / 88,572 bytes (ledger value).
"""
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"


def fetch(url, timeout=150, tries=4):
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            b = e.read()
            if e.code in (502, 503, 504) and a < tries - 1:
                time.sleep(3 * (a + 1)); continue
            return e.code, b
        except Exception:
            if a < tries - 1:
                time.sleep(3 * (a + 1)); continue
            return None, b""
    return None, b""


TAG = re.compile(r"<[^>]+>")
CELL = re.compile(r"<t[hd][^>]*>(.*?)</t[hd]>", re.S | re.I)


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(TAG.sub(" ", s))).strip()


def parse_attr(t):
    for m in re.finditer(r"<table[^>]*class=\"wikitable\"[^>]*>(.*?)</table>", t, re.S | re.I):
        tbl = m.group(1)
        rows = [[clean(c) for c in CELL.findall(r.group(1))]
                for r in re.finditer(r"<tr[^>]*>(.*?)</tr>", tbl, re.S | re.I)]
        rows = [r for r in rows if r]
        if any("Character Attributes" in " ".join(r) for r in rows):
            cm = re.search(r"<caption>(.*?)</caption>", tbl, re.S | re.I)
            return (clean(cm.group(1)) if cm else None), rows
    return None, None


def pull(rows, lab):
    if not rows:
        return None
    for r in rows:
        for i, c in enumerate(r):
            if c.strip().lower() == lab.lower() and i + 1 < len(r):
                return r[i + 1].strip()
    return None


def oldid(t):
    m = re.findall(r"oldid=(\d+)", t)
    return m[-1] if m else None


HEROES = ["Denali", "Sylvester", "Hecate", "Levi", "Rebecca", "Bright",
          "Gerard", "Robin", "Edward", "Karl_Steiner"]


def main(inv_path):
    inv = json.load(open(inv_path, encoding="utf-8"))

    st, b = fetch("https://web.archive.org/web/20190821024308id_/https://vsfan.net/wiki/Beckhen")
    ok = st == 200 and len(b) == 88572
    print(f"[CONTROL] Beckhen id_ http={st} bytes={len(b)} -> {'PASS' if ok else 'FAIL'}")
    if not ok:
        return 2

    print("\n########## (a) all revisions of 10 more hero pages")
    for h in HEROES:
        recs = [r for r in inv.get(h, [])
                if r["status"] == "200" and "text/html" in r["mime"]]
        recs.sort(key=lambda r: r["ts"])
        print(f"\n=== {h}")
        for r in recs:
            u = f"https://web.archive.org/web/{r['ts']}id_/{r['url']}"
            s, body = fetch(u)
            if s != 200:
                print(f"   {r['ts']} http={s}")
                continue
            t = body.decode("utf-8", "replace")
            cap, rows = parse_attr(t)
            tr = sorted(set(re.findall(r"Transcendence\s*Level[^<]{0,12}", t, re.I)))
            print(f"   {r['ts']} http=200 bytes={len(body)} oldid={oldid(t)} "
                  f"attrTable={'Y' if rows else 'N'} cap={cap!r} "
                  f"L/A/D={pull(rows,'Life')}/{pull(rows,'Attack')}/{pull(rows,'Defense')} "
                  f"trans={tr}")

    print("\n########## (b) what is a 2021 capture?")
    for title, ts in [("Captain", "20210729182323"), ("Hecate", None)]:
        if ts is None:
            continue
        r = [x for x in inv.get(title, []) if x["ts"] == ts]
        if not r:
            continue
        u = f"https://web.archive.org/web/{ts}id_/{r[0]['url']}"
        s, body = fetch(u)
        print(f"\n--- {title} {ts}: http={s} bytes={len(body)}")
        if s == 200:
            t = body.decode("utf-8", "replace")
            txt = re.sub(r"\s+", " ", html.unescape(TAG.sub(" ", t))).strip()
            print("    TEXT:", txt[:700])

    print("\n########## (c) pages with real content change")
    for title in ["Blustone", "Hunter_Supply_Office"]:
        recs = [r for r in inv.get(title, [])
                if r["status"] == "200" and "text/html" in r["mime"]]
        recs.sort(key=lambda r: r["ts"])
        print(f"\n=== {title}")
        for r in recs:
            u = f"https://web.archive.org/web/{r['ts']}id_/{r['url']}"
            s, body = fetch(u)
            if s != 200:
                print(f"   {r['ts']} http={s}")
                continue
            t = body.decode("utf-8", "replace")
            cap, rows = parse_attr(t)
            tr = sorted(set(re.findall(r"Transcendence\s*Level[^<]{0,12}", t, re.I)))
            print(f"   {r['ts']} http=200 bytes={len(body)} oldid={oldid(t)} "
                  f"attrTable={'Y' if rows else 'N'} L/A/D="
                  f"{pull(rows,'Life')}/{pull(rows,'Attack')}/{pull(rows,'Defense')} trans={tr}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
