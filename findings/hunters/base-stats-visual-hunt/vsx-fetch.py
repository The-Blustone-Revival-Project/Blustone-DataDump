# -*- coding: utf-8 -*-
"""vsx-fetch: fetch EVERY archived revision of the 57 hero pages + index pages."""
import io, json, os, re, time, urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_wf1_cache")
RAW = os.path.join(CACHE, "raw")
os.makedirs(RAW, exist_ok=True)
CDX = "https://web.archive.org/cdx/search/cdx"

HEROES = [
    "Acerola", "Akasha", "Apollon", "Athena", "Balian", "Bear", "Beckhen",
    "Bibi", "Bright", "Bruce_Bang", "Calibur", "Captain", "Crocus", "Denali",
    "Diana", "Dino", "Dumble", "Edward", "Gerard", "Gullveig", "Harley",
    "Hecate", "Heidi", "Hermes", "Joy", "Juno", "Kain", "Karl", "Karl_Steiner",
    "Lantern", "Lapis", "Levi", "Lily_%26_Lyla", "Locke", "Metis", "Mowgli",
    "Natalia", "Nene", "Octavia", "Pansy", "Papillon", "Patrone", "Rebecca",
    "Riko", "Robin", "Santa_Clauster", "Scar", "Sienna", "Sunny", "Sylvester",
    "Teddy_Bomber", "TeddyBomber", "Therapy", "Tyltyl", "Vincent", "Windblade",
    "Yuri",
]
INDEX_PAGES = ["List_of_Hunters", "Hunters", "List_of_Blustone_Items",
               "Guide_to_Blustone", "List_of_Blustone_Stories", "Monsters",
               "Hunter", "Roles", "Element_Type", "Fight_Club", "Abyss_Area",
               "Fight_Club_Shop", "Veteran_Status", "Hunters%27_Drop_Rate",
               "Hunter_Gym", "Hunter_Shop", "Purchase", "White_Island"]


def fetch(url, tries=5, sleep=2.0, timeout=120):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (research; blustone-base-stats-lane)"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except Exception as e:
            last = e
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


def slug(form):
    return re.sub(r"[^A-Za-z0-9]+", "_", form)[-78:]


def main():
    manifest = {}
    mpath = os.path.join(CACHE, "hero-revision-manifest.json")
    if os.path.exists(mpath):
        with io.open(mpath, encoding="utf-8") as f:
            manifest = json.load(f)
    targets = HEROES + INDEX_PAGES
    for i, t in enumerate(targets, 1):
        title = urllib.parse.unquote_plus(t)
        forms = ["https://vsfan.net/wiki/%s" % t,
                 "https://vsfan.net/w/index.php?title=%s" % t]
        n_new = 0
        for form in forms:
            rows, err = cdx(form, matchType="exact", limit="500",
                            fl="timestamp,original,mimetype,statuscode,digest,length")
            if err:
                print("[%2d/%2d] %-26s CDX-ERR %s" % (i, len(targets), title, err), flush=True)
                continue
            for r in rows or []:
                if r["statuscode"] != "200":
                    continue
                ts, key = r["timestamp"], slug(form) + "__" + r["timestamp"]
                path = os.path.join(RAW, key + ".html")
                if os.path.exists(path) and os.path.getsize(path) > 0:
                    nbytes = os.path.getsize(path)
                else:
                    st, body = fetch("https://web.archive.org/web/%sid_/%s"
                                     % (ts, r["original"]))
                    if not isinstance(body, (bytes, bytearray)):
                        continue
                    with io.open(path, "wb") as f:
                        f.write(body)
                    nbytes = len(body)
                    n_new += 1
                manifest.setdefault(t, [])
                if not any(x["timestamp"] == ts and x["form"] == form
                           for x in manifest[t]):
                    manifest[t].append({"form": form, "timestamp": ts,
                                        "digest": r["digest"], "bytes": nbytes,
                                        "cdx_len": r.get("length"), "ok": True})
        print("[%2d/%2d] %-26s revs200=%d new=%d"
              % (i, len(targets), title, len(manifest.get(t, [])), n_new), flush=True)
        with io.open(mpath, "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=1)
    print("TOTAL listed=%d" % sum(len(v) for v in manifest.values()))


if __name__ == "__main__":
    main()