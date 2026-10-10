import sys, os, re, glob, html as H
PAGES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pages')

def entry(t):
    """Strip header/footer, keep the article region in DOM order."""
    i = t.find('<div id="content"')
    if i < 0:
        i = t.find('<div class="site-content"')
    if i < 0:
        i = 0
    j = t.find('<footer')
    if j < 0:
        j = len(t)
    b = t[i:j]
    b = re.sub(r'(?is)<script[^>]*>.*?</script>', ' ', b)
    b = re.sub(r'(?is)<style[^>]*>.*?</style>', ' ', b)
    # mark images and links inline
    b = re.sub(r'(?i)<img[^>]*?alt="([^"]*)"[^>]*?src="([^"]+)"[^>]*>', r'[IMG \1 \2]', b)
    b = re.sub(r'(?i)<img[^>]*?src="([^"]+)"[^>]*>', r'[IMG \1]', b)
    b = re.sub(r'(?i)<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', r'[\2 -> \1]', b, flags=re.S)
    b = re.sub(r'(?i)<h([1-6])[^>]*>', r'\n\n### ', b)
    b = re.sub(r'(?i)</h[1-6]>', '\n', b)
    b = re.sub(r'(?i)<(p|div|li|br)[^>]*>', '\n', b)
    txt = re.sub(r'<[^>]+>', ' ', b)
    txt = H.unescape(txt)
    lines = [re.sub(r'\s+', ' ', l).strip() for l in txt.split('\n')]
    return '\n'.join(l for l in lines if l)

for p in sorted(glob.glob(os.path.join(PAGES, '*.html'))):
    t = open(p, encoding='utf-8', errors='replace').read()
    ti = re.search(r'(?is)<title>(.*?)</title>', t)
    print('#' * 25, os.path.basename(p))
    print('TITLE:', H.unescape(ti.group(1)).strip() if ti else '?')
    print(entry(t)[:6000])
    print()