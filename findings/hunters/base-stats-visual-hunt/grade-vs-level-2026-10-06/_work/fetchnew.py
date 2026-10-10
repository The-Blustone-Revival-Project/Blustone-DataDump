"""Batch-fetch every image URL not already in the prior manifest. Records real
decoded dimensions + sha256. Full-size originals first."""
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import crawl

HERE = os.path.dirname(os.path.abspath(__file__))
RESIZE = re.compile(r'-\d{2,4}x\d{2,4}\.')


def is_fullsize(u):
    """True for a WordPress original (no -WxH resize suffix, no -e<epoch> suffix)."""
    base = u.rsplit('/', 1)[-1]
    if RESIZE.search(base):
        return False
    if re.search(r'-e\d{10}', base):
        return False
    return True


def main():
    d = json.load(open(os.path.join(HERE, 'all-images.json'), encoding='utf-8'))
    prior = set()
    pm = os.path.abspath(os.path.join(
        HERE, '..', '..', 'hero-panel-level-images-2026-10-06', '_manifest.json'))
    for r in json.load(open(pm, encoding='utf-8')):
        prior.add(r['url'])
    targets = [u for u in d['imgs'] if u not in prior]
    targets.sort(key=lambda u: (0 if is_fullsize(u) else 1, u))
    print('targets: %d (%d full-size)'
          % (len(targets), sum(1 for u in targets if is_fullsize(u))), flush=True)
    done = {}
    outp = os.path.join(HERE, 'new-images.json')
    if os.path.exists(outp):
        done = json.load(open(outp, encoding='utf-8'))
    todo = [u for u in targets if u not in done]
    print('resuming, %d already done' % len(done), flush=True)
    # skip the parking-page-only boilerplate (nav sprites, present in every page)
    todo = [u for u in todo if u not in SKIP]
    res = crawl.par(todo, crawl.get_img, workers=8, label='new-images')
    for r in res:
        if r.get('orig'):
            done[r['orig']] = r
    json.dump(done, open(outp, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    ok = sum(1 for r in done.values() if r.get('ok'))
    print('DONE. recovered %d new images, saved to %s' % (ok, outp), flush=True)


SKIP = set()

if __name__ == '__main__':
    main()