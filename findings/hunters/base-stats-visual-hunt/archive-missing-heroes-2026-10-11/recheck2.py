"""Retry wildcard census with backoff; preserve raw bodies."""
import time, random, os
import requests
WORK = os.path.dirname(os.path.abspath(__file__))
S = requests.Session()
S.headers.update({"User-Agent": "Blustone-DataDump-research-recheck/1.0 (single-session, rate-limited)"})
url = ("https://web.archive.org/cdx/search/cdx?url=blustone.jp/hunter/*"
       "&output=json&fl=timestamp,original,statuscode,digest"
       "&filter=statuscode:200&collapse=urlkey&limit=1000")
for attempt in range(1, 6):
    time.sleep(8 + random.uniform(0, 6))
    try:
        r = S.get(url, timeout=90)
        print(f"attempt {attempt}: http {r.status_code} len {len(r.content)}")
        open(os.path.join(WORK, f"cdx-wildcard-attempt{attempt}-{r.status_code}.txt"), "wb").write(r.content)
        t = r.text
        print(t[:400])
        if r.status_code == 200 and t.strip().startswith("["):
            open(os.path.join(WORK, "cdx-hunter-wildcard-collapse.json"), "w", encoding="utf-8").write(t)
            import json
            rows = json.loads(t)
            print("OK rows:", len(rows)-1)
            break
        else:
            print("not usable, will retry if attempts remain")
    except Exception as e:
        print(f"attempt {attempt} transport failure:", repr(e))
else:
    print("ALL ATTEMPTS TRANSPORT-LIMITED")
