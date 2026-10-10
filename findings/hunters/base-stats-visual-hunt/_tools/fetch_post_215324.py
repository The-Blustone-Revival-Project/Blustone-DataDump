#!/usr/bin/env python3
"""Fetch the archived share_en post 215324 body and extract every <img> URL.

CONTROL FIRST: a Naver-cafe image the prior lane proved retrievable
(75605/303/534/001/725a8e...jpg -> 200 / 57,414 bytes). Only if that passes may
any 404 below be reported as a real negative.
"""
import html
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"
CDX = "https://web.archive.org/cdx/search/cdx?"


def fetch(url, timeout=180, tries=5):
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read(), r.headers.get("Content-Type", "")
        except urllib.error.HTTPError as e:
            b = e.read()
            if e.code in (502, 503, 504) and a < tries - 1:
                time.sleep(4 * (a + 1)); continue
            return e.code, b, ""
        except Exception:
            if a < tries - 1:
                time.sleep(4 * (a + 1)); continue
            return None, b"transport", ""
    return None, b"transport", ""


def main():
    # ---------- CONTROL ----------
    ctrl = ("https://web.archive.org/web/20210903030305id_/http://bs.visualshower.com/"
            "files/attach/images/75605/303/534/001/725a8e175454a533e96dac68fc5fdb49.jpg")
    st, b, ct = fetch(ctrl)
    ok = st == 200 and len(b) == 57414
    print(f"[CONTROL known-good image] http={st} bytes={len(b)} ct={ct} -> {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("ABORT.")
        return 2

    # ---------- exact-URL CDX for the post ----------
    for target in ["bs.visualshower.com/index.php?mid=share_en&document_srl=215324",
                   "bs.visualshower.com/?mid=share_en&document_srl=215324"]:
        q = CDX + urllib.parse.urlencode({"url": target, "output": "text", "limit": "200"})
        st2, b2, _ = fetch(q)
        t = b2.decode("utf-8", "replace")
        rows = [l for l in t.split("\n") if l.strip()][1:]
        print(f"\n[CDX exact] {target}\n  http={st2} rows={len(rows)}")
        for r in rows[:20]:
            print("   " + r[:230])

    # ---------- fetch the post body itself ----------
    cands = [
        "https://web.archive.org/web/20180209003234id_/http://bs.visualshower.com/?mid=share_en&document_srl=215324",
    ]
    # discover every capture of the post body via prefix on the query params
    q = CDX + urllib.parse.urlencode({"url": "bs.visualshower.com/index.php",
                                      "matchType": "prefix", "output": "text", "limit": "50000",
                                      "filter": "original:.*document_srl=215324.*"})
    st3, b3, _ = fetch(q)
    t3 = b3.decode("utf-8", "replace")
    rows3 = [l for l in t3.split("\n") if l.strip()][1:]
    print(f"\n[CDX prefix index.php w/ document_srl=215324] http={st3} rows={len(rows3)}")
    bodies = []
    for r in rows3:
        f = r.split(" ")
        if len(f) < 7 or f[4] != "200":
            continue
        bodies.append((f[1], f[2], f[3]))
    for ts, url, mime in bodies[:20]:
        print(f"   200 {mime:12s} {ts} {url[:170]}")
        cands.append(f"https://web.archive.org/web/{ts}id_/{url}")

    print("\n=== FETCHING BODIES ===")
    for u in cands[:8]:
        s, body, ct = fetch(u)
        print(f"\n--- {u[:150]}")
        print(f"    http={s} bytes={len(body)} ct={ct}")
        if s != 200:
            continue
        txt = body.decode("utf-8", "replace")
        imgs = re.findall(r'<img[^>]+src="([^"]+)"', txt, re.I)
        # Naver cafe stores attachments in a hidden _comment fragment too
        imgs += re.findall(r'https?://[^\s"\'<>]*?/files/attach/images/[^\s"\'<>]+', txt)
        seen = set()
        for i in imgs:
            i = html.unescape(i)
            if i in seen:
                continue
            seen.add(i)
            print("    IMG " + i[:230])
        if not seen:
            # try to find the attachment markup naver uses (quoted-printable)
            plain = re.sub(r"=\s*\n", "", txt)
            for m in re.findall(r"[0-9a-f]{32}\.(?:jpg|jpeg|png|gif|JPG|PNG)", plain, re.I):
                print("    HASH " + m)
    return 0


if __name__ == "__main__":
    sys.exit(main())
