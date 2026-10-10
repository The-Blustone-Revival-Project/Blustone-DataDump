#!/usr/bin/env python
"""Print images + text of one cached blustone.jp archives page."""
import re, html, sys

p = sys.argv[1]
t = open(p, encoding='utf-8', errors='replace').read()
imgs = re.findall(r'(?:src|href)=["\']([^"\']+?\.(?:jpg|jpeg|png|gif))["\']', t, re.I)
print('IMAGES (%d):' % len(dict.fromkeys(imgs)))
for i in dict.fromkeys(imgs):
    print('   ', i)
b = re.sub(r'(?is)<script.*?</script>', ' ', t)
b = re.sub(r'(?is)<style.*?</style>', ' ', b)
b = re.sub(r'(?s)<[^>]+>', ' ', b)
b = html.unescape(re.sub(r'\s+', ' ', b))
key = sys.argv[2] if len(sys.argv) > 2 else None
i = b.find(key) if key else 0
if i < 0:
    i = 0
print('\nTEXT:')
print(b[max(0, i - 300):i + 4000])
