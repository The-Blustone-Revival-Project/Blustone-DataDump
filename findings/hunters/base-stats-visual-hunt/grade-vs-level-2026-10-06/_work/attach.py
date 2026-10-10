import re, os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pagetext import load, all_urls

rows = {}
for f in sys.argv[1:]:
    t = load(f)
    if t is None:
        print('MISSING', f); continue
    title = re.search(r'(?is)<title>(.*?)</title>', t)
    print('#' * 20, f)
    print('  title:', (title.group(1).strip() if title else '?')[:160])
    for u in all_urls(t):
        if re.search(r'(?i)uploads/|\.jpg|\.png|\.jpeg', u):
            print('   IMG', u)
    # any mention of the filename
    for m in set(re.findall(r'[A-Za-z0-9_\-.]+\.(?:jpg|jpeg|png)', t, re.I)):
        if 'btn-' in m or 'thum-' in m or 'lesser' in m or 'VisualShower' in m:
            continue
        print('   FN ', m)
    print()