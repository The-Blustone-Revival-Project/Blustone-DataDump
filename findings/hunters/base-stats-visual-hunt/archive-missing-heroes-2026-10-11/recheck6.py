"""Batch 4 (retry): primary-JP CDX filter per hero, ALL captures, no collapse. Long backoff."""
import time, random, os, urllib.parse, json
import requests
WORK = os.path.dirname(os.path.abspath(__file__))
S = requests.Session()
S.headers.update({"User-Agent": "Blustone-DataDump-research-recheck/1.0 (single-session, rate-limited)"})

def get(url, timeout=90):
    time.sleep(20 + random.uniform(0, 10))
    return S.get(url, timeout=timeout, allow_redirects=True)

PRIMARY = [
    ("064", "\u30bc\u30e9\u30cb\u30a6\u30e0"),
    ("065", "\u30c6\u30ec\u30b5"),
    ("066", "\u30e1\u30a2\u30ea\u30fc"),
    ("068", "\u30bb\u30ec\u30cd"),
    ("070", "\u30a2\u30ea\u30a2"),
    ("071", "\u30a2\u30cd\u30e2\u30cd"),
    ("072", "\u30aa\u30fc\u30c9\u30ea\u30fc"),
    ("073", "\u30bd\u30d5\u30a3\u30a2"),
    ("074", "\u30ec\u30aa\u30f3"),
    ("075", "\u30d9\u30e9"),
    ("076", "\u30b8\u30e5\u30cb\u30a2"),
    ("077", "\u30d6\u30ed\u30f3\u30c7\u30a3"),
    ("080", "\u30a6\u30a7\u30b9\u30c8\u30d5\u30a3\u30fc\u30eb\u30c9"),
    ("081", "\u30e2\u30cb\u30ab"),
    ("084b", "\u30cd\u30ba\u30df"),
    ("089", "\u30af\u30e9\u30e9"),
    ("090", "\u30ab\u30c8\u30ea\u30fc\u30ca"),
    ("092", "\u30c6\u30df\u30b9"),
    ("096", "\u30a8\u30b9\u30c6\u30eb"),
]

summary = {}
for cid, frag in PRIMARY:
    enc = urllib.parse.quote(frag, safe="")
    url = ("https://web.archive.org/cdx/search/cdx?url=blustone.jp/hunter/*"
           "&output=json&fl=timestamp,original,statuscode,digest"
           f"&filter=original:.*{enc}.*&limit=50")
    try:
        r = get(url)
        fn = f"cdx-retry-{cid}.json"
        open(os.path.join(WORK, fn), "wb").write(r.content)
        print(cid, "http", r.status_code, "len", len(r.content), flush=True)
        summary[cid] = {"http": r.status_code, "body_head": r.text[:120]}
    except Exception as e:
        print(cid, "TRANSPORT", repr(e), flush=True)
        summary[cid] = {"transport_failure": repr(e)}
with open(os.path.join(WORK, "retry-summary.json"), "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print("DONE batch4")
