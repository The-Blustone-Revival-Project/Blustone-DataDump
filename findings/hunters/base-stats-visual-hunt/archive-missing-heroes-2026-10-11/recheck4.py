"""Batch 2: index ALL-captures CDX + Dec index fetch + 2020 wildcard CDX. One shared session, jitter."""
import time, random, os, json
import requests
WORK = os.path.dirname(os.path.abspath(__file__))
S = requests.Session()
S.headers.update({"User-Agent": "Blustone-DataDump-research-recheck/1.0 (single-session, rate-limited)"})

def get(url, timeout=90):
    time.sleep(3 + random.uniform(0, 3))
    return S.get(url, timeout=timeout, allow_redirects=True)

def wb(url, name):
    r = get(url)
    print(name, "http", r.status_code, "len", len(r.content))
    open(os.path.join(WORK, name), "wb").write(r.content)
    return r

# control per batch
ctrl = ("https://web.archive.org/web/20191216060610id_/"
        "https://blustone.jp/hunter/%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5/"
        "%E3%83%95%E3%82%A1%E3%82%A4%E3%83%88%E3%82%AF%E3%83%A9%E3%83%96%E3%81%AE%E5%AE%88%E8%AD%B7%E8%80%85%E3%80%8C%E3%83%99%E3%83%83%E3%82%B1%E3%83%B3%E3%80%8D")
r = wb(ctrl, "control-batch2-beckhen.html")
assert r.status_code == 200 and "8709" in r.text and "\u57fa\u672c\u80fd\u529b\u5024" in r.text, "batch2 control failed"
print("BATCH2 CONTROL PASSED")

# index CDX, ALL captures, no collapse
idx_cdx = ("https://web.archive.org/cdx/search/cdx?url=blustone.jp/hunter/%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5"
           "&output=json&fl=timestamp,original,statuscode,digest&limit=100")
r = wb(idx_cdx, "cdx-index-all.json")
print(r.text[:600])

# Dec index fetch id_ raw
dec = ("https://web.archive.org/web/20191209130354id_/https://blustone.jp/hunter/%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5")
r = wb(dec, "index-20191209130354.html")
print("dec index has profile links:", r.text.count("/hunter/"))

# 2020+ wildcard census
y2020 = ("https://web.archive.org/cdx/search/cdx?url=blustone.jp/hunter/*"
         "&output=json&fl=timestamp,original,statuscode,digest"
         "&filter=statuscode:200&collapse=urlkey&from=2020&limit=1000")
r = wb(y2020, "cdx-hunter-from2020.json")
print(r.text[:600])
print("DONE batch2")
