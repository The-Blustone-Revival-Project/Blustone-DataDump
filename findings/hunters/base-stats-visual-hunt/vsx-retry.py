# -*- coding: utf-8 -*-
"""vsx-retry: fetch the missing pages with long backoff.  web.archive.org
started refusing connections mid-run, so back off hard and retry patiently."""
import io, json, os, re, sys, time, urllib.request, urllib.parse

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "_wf1_cache", "raw")
# HTTPS to web.archive.org is refused on this host (WinError 10061) while plain
# HTTP answers 200/145187 bytes -- verified this session.  Use http://.
CDX = "http://web.archive.org/cdx/search/cdx"

# hero pages not yet holding >=1 real (non-parking) capture
WANT_HERO = ["Lily_%26_Lyla", "Robin", "Santa_Clauster", "Scar", "Sienna",
             "Sunny", "Sylvester", "Teddy_Bomber", "TeddyBomber", "Therapy",
             "Tyltyl", "Vincent", "Windblade", "Yuri"]
WANT_INDEX = ["List_of_Hunters", "List_of_Blustone_Items", "Guide_to_Blustone",
              "List_of_Blustone_Stories", "Monsters", "Hunters", "Hunter",
              "Roles", "Element_Type", "Fight_Club", "Fight_Club_Shop",
              "Abyss_Area", "Veteran_Status", "Hunters%27_Drop_Rate",
              "Hunter_Gym", "Hunter_Shop", "Purchase", "White_Island",
              "Hunter_Supply_Station", "Post_Office", "Midgard_Snowfields"]


def fetch(url, tries=4, sleep=5.0, timeout=120):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (blustone research; low rate)"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except Exception as e:
            last = e
            print("      retry %d: %s" % (i + 1, type(e).__name__), flush=True)
            time.sleep(sleep * (i + 1))
    return None, ("ERR %r" % (last,))


def cdx(url, **kw):
    q = {"url": url, "output": "json"}
    q.update(kw)
    st, body = fetch(CDX + "?" + urllib.parse.urlencode(q))
    if not isinstance(body, (bytes, bytearray)):
        return None, str(body)
    try:
        data = json.loads(body.decode("utf-8", "replace"))
    except Exception as e:
        return None, "JSONERR %r" % (e,)
    if not data:
        return [], None
    return [dict(zip(data[0], r)) for r in data[1:]], None


def slug(f):
    return re.sub(r"[^A-Za-z0-9]+", "_", f)[-78:]


def do(title):
    got = 0
    for form in ("https://vsfan.net/wiki/%s" % title,
                 "https://vsfan.net/w/index.php?title=%s" % title):
        rows, err = cdx(form, matchType="exact", limit="500",
                        fl="timestamp,original,statuscode,digest,length")
        if err:
            print("    CDX-ERR %s" % err[:90], flush=True)
            continue
        for r in rows or []:
            if r["statuscode"] != "200":
                continue
            path = os.path.join(RAW, slug(form) + "__" + r["timestamp"] + ".html")
            if os.path.exists(path) and os.path.getsize(path) > 0:
                continue
            st, body = fetch("http://web.archive.org/web/%sid_/%s"
                             % (r["timestamp"], r["original"]))
            if not isinstance(body, (bytes, bytearray)):
                continue
            with io.open(path, "wb") as f:
                f.write(body)
            got += 1
            time.sleep(1.2)
    return got


def main():
    for i, t in enumerate(WANT_HERO + WANT_INDEX, 1):
        print("[%2d/%2d] %-24s" % (i, len(WANT_HERO + WANT_INDEX), t), flush=True)
        n = do(t)
        print("    new=%d" % n, flush=True)
        time.sleep(1.0)


if __name__ == "__main__":
    main()