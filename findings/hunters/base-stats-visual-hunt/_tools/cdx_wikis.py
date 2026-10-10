#!/usr/bin/env python3
"""CDX index probe for candidate Blustone wiki corpora, with retries and a
mandatory positive control.

A curl 000 / gateway error is a TRANSPORT failure, never a negative. Every probe
here reports http status + byte count + row count so the caller can tell the
three apart. The control probe (web.archive.org root) must return 200 before any
zero row-count below is allowed to count as a real negative.
"""
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"
CDX = "https://web.archive.org/cdx/search/cdx?"


def fetch(url, timeout=180, tries=6):
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            b = e.read()
            if e.code in (502, 503, 504) and a < tries - 1:
                time.sleep(5 * (a + 1)); continue
            return e.code, b
        except Exception:
            if a < tries - 1:
                time.sleep(5 * (a + 1)); continue
            return None, b"transport-failed"
    return None, b"transport-failed"


def probe(label, domain, out=None, limit="20000"):
    params = {"url": domain, "matchType": "domain", "output": "text",
              "collapse": "urlkey", "limit": limit}
    url = CDX + urllib.parse.urlencode(params)
    st, body = fetch(url)
    text = body.decode("utf-8", "replace")
    lines = [l for l in text.split("\n") if l.strip()]
    rows = lines[1:] if lines and lines[0].startswith("net,") else lines
    print(f"[{label}] http={st} bytes={len(body)} datarows={len(rows)}  ({domain})")
    if st != 200:
        print("     NOT A NEGATIVE -- query failed; will retry later.")
        return None
    # how many are /wiki/ style content pages?
    wiki = [r for r in rows if "/wiki/" in r.split(" ")[2] if len(r.split(" ")) > 2]
    print(f"     rows with /wiki/ in URL: {len(wiki)}")
    for r in wiki[:12]:
        print("       " + r[:200])
    if out:
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print(f"     saved -> {out}")
    return rows


def main(outdir):
    import os
    os.makedirs(outdir, exist_ok=True)

    st, body = fetch("https://web.archive.org/")
    ok = st == 200 and len(body) > 100000
    print(f"[CONTROL web.archive.org] http={st} bytes={len(body)} -> {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("ABORT: control failed.")
        return 2

    targets = [
        ("vsfanwiki_miraheze", "vsfanwiki.miraheze.org", "cdx-vsfanwiki-miraheze.tsv"),
        ("blustone_miraheze", "blustone.miraheze.org", "cdx-blustone-miraheze.tsv"),
        ("blustone_fandom", "blustone.fandom.com", "cdx-blustone-fandom.tsv"),
        ("blustone2_miraheze", "blustone2.miraheze.org", None),
    ]
    got = {}
    for label, dom, fn in targets:
        got[label] = probe(label, dom, os.path.join(outdir, fn) if fn else None)
        print()

    # Retry any that failed, once, to rule out a flaky gateway.
    for label, dom, fn in targets:
        if got.get(label) is None:
            print(f"--- RETRY {label} ---")
            got[label] = probe(label + "-retry", dom, os.path.join(outdir, fn) if fn else None)
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
