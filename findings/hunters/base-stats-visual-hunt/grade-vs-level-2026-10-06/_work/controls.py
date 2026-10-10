"""Positive controls -- must pass before any zero is recorded."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb

CONTROLS = [
    # (label, ts, original)
    ('C1-root', None, 'http://web.archive.org/'),
    ('C2-rankup-jpg', '20190403182150', 'https://blustone.jp/wp-content/uploads/2018/11/rankup.jpg'),
    ('C3-img5729-mar', '20190330070910', 'https://blustone.jp/wp-content/uploads/2019/03/IMG_5729.png'),
    ('C4-img5729-jan', '20191121144145', 'https://blustone.jp/wp-content/uploads/2019/01/IMG_5729-e1548139622568.png'),
    ('C5-known-1024', '20190403124314', 'https://blustone.jp/wp-content/uploads/2019/01/1548235686-1024x911.jpg'),
]

if __name__ == '__main__':
    ok = 0
    for label, ts, orig in CONTROLS:
        if ts is None:
            st, body, hdr = wb.get(orig)
            w, h, k = wb.dims(body)
            print('%-18s %-5s bytes=%-8d dims=%sx%s %s' % (label, st, len(body), w, h, k))
            ok += 1 if st == 200 else 0
            continue
        rec, body = wb.probe(ts, orig)
        print('%-18s %-5s bytes=%-8d dims=%sx%s %-5s ok=%s' % (
            label, rec['status'], rec['bytes'], rec['w'], rec['h'], rec['kind'], rec['ok']))
        ok += 1 if rec['ok'] else 0
    print('CONTROLS PASSED %d/%d' % (ok, len(CONTROLS)))