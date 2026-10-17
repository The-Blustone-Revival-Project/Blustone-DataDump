"""Batch 3: Nov alternate-timestamp control + per-hero CDX filtered queries (ALL captures, no collapse).
One shared session + jitter. 429/503 = transport, never content negative."""
import time, random, os, urllib.parse
import requests
WORK = os.path.dirname(os.path.abspath(__file__))
S = requests.Session()
S.headers.update({"User-Agent": "Blustone-DataDump-research-recheck/1.0 (single-session, rate-limited)"})

def get(url, timeout=90):
    time.sleep(2.5 + random.uniform(0, 2.5))
    return S.get(url, timeout=timeout, allow_redirects=True)

def wb(url, name):
    r = get(url)
    print(name, "http", r.status_code, "len", len(r.content), flush=True)
    open(os.path.join(WORK, name), "wb").write(r.content)
    return r

# batch control: Nov alternate-timestamp profile (Crocus 20191115010135) id_ raw
nov = ("https://web.archive.org/web/20191115010135id_/"
       "https://blustone.jp/hunter/%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5/"
       "%E3%83%8D%E3%82%AF%E3%83%AD%E3%83%9E%E3%83%B3%E3%82%B5%E3%83%BC%E3%80%8C%E3%82%AF%E3%83%AD%E3%83%83%E3%82%AB%E3%82%B9%E3%80%8D")
r = wb(nov, "control-batch3-crocus-nov.html")
txt = r.text
ok = r.status_code == 200 and "8535" in txt and "\u57fa\u672c\u80fd\u529b\u5024" in txt
print("NOV CONTROL", "PASSED" if ok else "FAILED")
assert ok, "nov control failed"

# 19 heroes: (catalog_id, english, [jp fragments incl alts])
HEROES = [
    ("064", "Geranium", ["\u30bc\u30e9\u30cb\u30a6\u30e0"]),
    ("065", "Teresa", ["\u30c6\u30ec\u30b5"]),
    ("066", "Mary", ["\u30e1\u30a2\u30ea\u30fc", "\u30de\u30ea\u30fc"]),
    ("068", "Selene", ["\u30bb\u30ec\u30cd"]),
    ("070", "Alia", ["\u30a2\u30ea\u30a2"]),
    ("071", "Anemone", ["\u30a2\u30cd\u30e2\u30cd"]),
    ("072", "Audrey", ["\u30aa\u30fc\u30c9\u30ea\u30fc"]),
    ("073", "Sofia", ["\u30bd\u30d5\u30a3\u30a2"]),
    ("074", "Leon", ["\u30ec\u30aa\u30f3"]),
    ("075", "Bella", ["\u30d9\u30e9"]),
    ("076", "Junia", ["\u30b8\u30e5\u30cb\u30a2", "\u30e6\u30cb\u30a2"]),
    ("077", "Blondie", ["\u30d6\u30ed\u30f3\u30c7\u30a3"]),
    ("080", "Westfield", ["\u30a6\u30a7\u30b9\u30c8\u30d5\u30a3\u30fc\u30eb\u30c9", "\u30a6\u30a8\u30b9\u30c8\u30d5\u30a3\u30fc\u30eb\u30c9"]),
    ("081", "Monica", ["\u30e2\u30cb\u30ab"]),
    ("084", "LotteryMouse", ["\u30de\u30a6\u30b9", "\u30cd\u30ba\u30df", "Lottery"]),
    ("089", "Clara", ["\u30af\u30e9\u30e9"]),
    ("090", "Katrina", ["\u30ab\u30c8\u30ea\u30fc\u30ca"]),
    ("092", "Themis", ["\u30c6\u30df\u30b9"]),
    ("096", "Estelle", ["\u30a8\u30b9\u30c6\u30eb"]),
]

def enc(s):
    return urllib.parse.quote(s, safe="")

results = {}
for cid, en, frags in HEROES:
    # EN filter (romaji safety net)
    f_en = f"https://web.archive.org/cdx/search/cdx?url=blustone.jp/hunter/*&output=json&fl=timestamp,original,statuscode,digest&filter=original:.*{en}.*&limit=50"
    r = get(f_en)
    name = f"cdx-hero-{cid}-EN.json"
    open(os.path.join(WORK, name), "wb").write(r.content)
    print(cid, en, "EN http", r.status_code, "len", len(r.content), flush=True)
    results[(cid, "EN:" + en)] = (r.status_code, r.text[:200])
    if r.status_code in (429, 503):
        print(f"  {cid} EN transport-limited; continuing (NOT a content negative)")
        continue
    for frag in frags:
        f_jp = ("https://web.archive.org/cdx/search/cdx?url=blustone.jp/hunter/*"
                "&output=json&fl=timestamp,original,statuscode,digest"
                f"&filter=original:.*{enc(frag)}.*&limit=50")
        r = get(f_jp)
        safe = enc(frag)[:40]
        name = f"cdx-hero-{cid}-JP.json" if len(frags) == 1 else f"cdx-hero-{cid}-JP-{safe[:20]}.json"
        # avoid overwrite for multi-frag: append
        if len(frags) > 1:
            open(os.path.join(WORK, name), "wb").write(r.content)
        else:
            open(os.path.join(WORK, name), "wb").write(r.content)
        print(f"  {cid} JP http {r.status_code} len {len(r.content)}", flush=True)
        results[(cid, "JP:" + frag)] = (r.status_code, r.text[:200])
        if r.status_code in (429, 503):
            print(f"  {cid} JP transport-limited; continuing (NOT a content negative)")

import json
with open(os.path.join(WORK, "per-hero-cdx-summary.json"), "w", encoding="utf-8") as f:
    json.dump({f"{k[0]} {k[1]}": {"http": v[0], "preview": v[1]} for k, v in results.items()}, f, ensure_ascii=False, indent=2)
print("DONE batch3")
