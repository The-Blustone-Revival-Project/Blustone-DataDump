"""Map every cached page -> image URLs, and report which rank-up-ish article uses what."""
import json, os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pagetext import load, all_urls

PAGEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        '..', '..', '_archives_work', 'pages'))

def main():
    fname2pages = collections.defaultdict(set)
    page2fns = {}
    titles = {}
    for fn in sorted(os.listdir(PAGEDIR)):
        if not fn.endswith('.html'):
            continue
        t = load(fn)
        if t is None:
            continue
        m = re.search(r'(?is)<title>(.*?)</title>', t)
        import html as H
        titles[fn] = H.unescape(m.group(1)).strip() if m else '?'
        ups = [u for u in all_urls(t) if '/wp-content/uploads/' in u]
        fns = sorted(set(u.rsplit('/', 1)[-1] for u in ups))
        page2fns[fn] = fns
        for f in fns:
            fname2pages[f].add(fn)
    out = {'fname2pages': {k: sorted(v) for k, v in fname2pages.items()},
           'page2fns': page2fns, 'titles': titles}
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'page-map.json')
    json.dump(out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('pages', len(page2fns), 'distinct image filenames', len(fname2pages))
    return fname2pages, page2fns, titles

if __name__ == '__main__':
    main()