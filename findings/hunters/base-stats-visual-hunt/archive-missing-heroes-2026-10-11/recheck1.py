"""Missing-heroes recheck: CDX census + positive control.
Work dir only: findings/hunters/base-stats-visual-hunt/archive-missing-heroes-2026-10-11/
One shared Session, jitter between requests, 429 = transport (never content negative).
"""
import json, time, random, sys, os
import requests

WORK = os.path.dirname(os.path.abspath(__file__))
UA = "Blustone-DataDump-research-recheck/1.0 (contact: research; rate-limited single session)"
S = requests.Session()
S.headers.update({"User-Agent": UA})

def get(url, timeout=60):
    time.sleep(1.5 + random.uniform(0, 1.5))
    r = S.get(url, timeout=timeout, allow_redirects=True)
    return r

def save(name, data):
    p = os.path.join(WORK, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(data)
    print("wrote", p, len(data))

def saveb(name, data: bytes):
    p = os.path.join(WORK, name)
    with open(p, "wb") as f:
        f.write(data)
    print("wrote", p, len(data))

# 1. positive control: Beckhen Dec-2019 id_ raw
ctrl_url = ("https://web.archive.org/web/20191216060610id_/"
            "https://blustone.jp/hunter/"
            "%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5/"
            "%E3%83%95%E3%82%A1%E3%82%A4%E3%83%88%E3%82%AF%E3%83%A9%E3%83%96%E3%81%AE%E5%AE%88%E8%AD%B7%E8%80%85%E3%80%8C%E3%83%99%E3%83%83%E3%82%B1%E3%83%B3%E3%80%8D")
print("fetching positive control...")
try:
    r = get(ctrl_url)
    print("control http", r.status_code, "len", len(r.content), "final", r.url[:120])
    saveb("control-beckhen-20191216060610.html", r.content)
    txt = r.text
    checks = {
        "basic_ability": "\u57fa\u672c\u80fd\u529b\u5024" in txt,
        "combat_8709": "8709" in txt,
        "hp_1678": "1678" in txt,
    }
    print("control checks:", checks)
    with open(os.path.join(WORK, "control-check.json"), "w", encoding="utf-8") as f:
        json.dump({"url": ctrl_url, "status": r.status_code,
                   "len": len(r.content), "checks": checks}, f, ensure_ascii=False, indent=2)
    if not (checks["basic_ability"] and checks["combat_8709"]):
        print("CONTROL FAILED - aborting batch")
        sys.exit(2)
    print("CONTROL PASSED")
except Exception as e:
    print("CONTROL TRANSPORT FAILURE:", repr(e))
    with open(os.path.join(WORK, "control-check.json"), "w", encoding="utf-8") as f:
        json.dump({"url": ctrl_url, "transport_failure": repr(e)}, f, ensure_ascii=False, indent=2)
    sys.exit(3)

# 2. wildcard census collapse=urlkey (discovery)
cdx1 = ("https://web.archive.org/cdx/search/cdx?url=blustone.jp/hunter/*"
        "&output=json&fl=timestamp,original,statuscode,digest"
        "&filter=statuscode:200&collapse=urlkey&limit=1000")
print("fetching wildcard census...")
try:
    r = get(cdx1)
    print("cdx1 http", r.status_code, "len", len(r.content))
    save("cdx-hunter-wildcard-collapse.json", r.text)
    rows = json.loads(r.text) if r.text.strip() else []
    print("urlkeys (excl header):", max(0, len(rows)-1))
except Exception as e:
    print("CDX1 TRANSPORT FAILURE:", repr(e))
    with open(os.path.join(WORK, "cdx-hunter-wildcard-collapse.json"), "w", encoding="utf-8") as f:
        f.write("")
    sys.exit(4)
