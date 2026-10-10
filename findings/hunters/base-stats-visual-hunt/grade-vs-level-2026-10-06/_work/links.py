import sys, re, html as H
sys.path.insert(0, '.')
from pagetext import load

for f in ['20190405051840_https_blustone_jp_archives_2250.html',
          '20190330070910_https_blustone_jp_archives_2867.html']:
    t = load(f)
    print('==', f)
    for m in re.finditer(r'(?i)<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', t, re.S):
        u = m.group(1)
        txt = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        if '/archives/' in u or re.search(r'育成|ランク|鍛', txt):
            print('   ', u, '|', H.unescape(txt)[:60])