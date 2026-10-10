import re, os, html, sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_archives_work', 'pages')

def load(f):
    p = os.path.join(BASE, f)
    if not os.path.exists(p):
        return None
    return open(p, encoding='utf-8', errors='replace').read()

def article_text(t):
    m = re.search(r'(?is)<div class="entry-content"(.*?)(<footer|post-tags|id="sidebar"|class="post-navigation")', t)
    body = m.group(0) if m else t
    body = re.sub(r'(?is)<script[^>]*>.*?</script>', ' ', body)
    body = re.sub(r'(?is)<style[^>]*>.*?</style>', ' ', body)
    txt = re.sub(r'(?s)<[^>]+>', '\n', body)
    txt = html.unescape(txt)
    lines = [l.strip() for l in txt.split('\n')]
    lines = [l for l in lines if l]
    return '\n'.join(lines)

def all_urls(t):
    urls = []
    for m in re.finditer(r'(?i)(?:src|data-src|srcset)\s*=\s*"([^"]+)"', t):
        for u in m.group(1).split(','):
            u = u.strip().split(' ')[0]
            if u and u not in urls:
                urls.append(u)
    for m in re.finditer(r'(?i)href\s*=\s*"([^"]+\.(?:jpg|jpeg|png|gif|webp)[^"]*)"', t):
        u = m.group(1)
        if u not in urls:
            urls.append(u)
    return urls

if __name__ == '__main__':
    for f in sys.argv[1:]:
        t = load(f)
        if t is None:
            print('MISSING', f); continue
        print('#' * 30, f, len(t))
        print(article_text(t)[:4000])
        print()