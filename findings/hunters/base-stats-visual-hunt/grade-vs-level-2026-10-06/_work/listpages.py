import sys, os, re, json, html as H, glob
sys.path.insert(0, '.')
import wb

PAGES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pages')

def ups(text):
    out = []
    for m in re.finditer(r'(?i)(?:src|data-src|srcset)\s*=\s*"([^"]+)"', text):
        for u in m.group(1).split(','):
            u = u.strip().split(' ')[0]
            if '/wp-content/uploads/' in u and u not in out:
                out.append(u)
    return out

for p in sorted(glob.glob(os.path.join(PAGES, '*.html'))):
    t = open(p, encoding='utf-8', errors='replace').read()
    ti = re.search(r'(?is)<title>(.*?)</title>', t)
    ti = H.unescape(ti.group(1)).strip() if ti else '?'
    print('#', os.path.basename(p))
    print('   title:', ti[:90])
    for u in ups(t):
        print('   IMG', u)
    print()