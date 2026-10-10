"""Targeted fetch of the highest-value untried full-size images, low concurrency
with retries (archive.org refuses connections when hammered)."""
import json
import os
import re
import sys
import time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb
import crawl

HERE = os.path.dirname(os.path.abspath(__file__))
U = 'https://blustone.jp/wp-content/uploads/'

PRIORITY = [
    # the star5 article's OWN rank3 (distinct from 2018/11/rank3)
    U + '2019/01/rank3.jpg', U + '2019/01/rank3-768x683.jpg',
    U + '2019/01/rank3-300x267.jpg',
    # capacity transcendence full sizes
    U + '2019/02/capa2.jpg', U + '2019/03/capa.jpg', U + '2018/11/capacity.png',
    # rank-up / training article screens
    U + '2018/11/IMG_9719.jpg', U + '2018/11/d.jpg', U + '2018/11/rankup.jpg',
    U + '2018/11/traning.png', U + '2018/11/CV.jpg', U + '2018/11/party.jpg',
    # the 0d40a5e4 family full sizes (star3->4 review siblings)
    U + '2019/01/0d40a5e4a645fc6b96e767d64ac0878e.jpg',
    U + '2019/01/0d40a5e4a645fc6b96e767d64ac0878e-1.jpg',
    U + '2019/01/0d40a5e4a645fc6b96e767d64ac0878e-2.jpg',
    U + '2019/01/0d40a5e4a645fc6b96e767d64ac0878e-3.jpg',
    U + '2019/01/0d40a5e4a645fc6b96e767d64ac0878e-4.jpg',
    U + '2019/01/0d40a5e4a645fc6b96e767d64ac0878e-5.jpg',
    U + '2019/01/0d40a5e4a645fc6b96e767d64ac0878e-7.jpg',
    U + '2019/01/0d40a5e4a645fc6b96e767d64ac0878e-8.jpg',
    U + '2019/01/0d40a5e4a645fc6b96e767d64ac0878e-10.jpg',
    U + '2019/01/0d40a5e4a645fc6b96e767d64ac0878e-11.jpg',
    # big / late 2019/01 originals
    U + '2019/01/IMG_0281.jpg', U + '2019/01/TOP.jpg', U + '2019/01/IMG_0156.jpg',
    U + '2019/01/IMG_5750.jpg', U + '2019/01/IMG_5782.png',
    U + '2019/01/IMG_5988.png', U + '2019/01/IMG_5991.png',
    U + '2019/01/IMG_5997.png', U + '2019/01/3b03d4c98052f3dc1f586442a1ff8be4.jpg',
    U + '2019/01/82cd89bf6e3e7beeac7a6a7e3c296e8a.jpg',
    U + '2019/01/1547530477.jpg', U + '2019/01/1547530839.jpg',
    U + '2019/01/1547531028.jpg', U + '2019/01/1547531476.jpg',
    U + '2019/01/1547534994.jpg', U + '2019/01/1548235710.jpg',
    # 2019/02 originals
    U + '2019/02/IMG_0281.jpg', U + '2019/02/IMG_0448.jpg',
    U + '2019/02/IMG_0410.jpg', U + '2019/02/IMG_4885.jpg',
    U + '2019/02/IMG_9737.jpg', U + '2019/02/harry-s.jpg',
    U + '2019/02/1550474475.jpg', U + '2019/02/1550733537.jpg',
    U + '2019/02/1550735696.jpg', U + '2019/02/1551068175.jpg',
    U + '2019/02/1551089150.jpg',
    U + '2019/02/IMG_6096.png', U + '2019/02/IMG_6107.png',
    U + '2019/02/IMG_6117.png', U + '2019/02/IMG_6118.png',
    U + '2019/02/IMG_6303.png', U + '2019/02/IMG_6369.png',
    U + '2019/02/IMG_6370.png', U + '2019/02/IMG_6373.png',
    U + '2019/02/IMG_6429.png', U + '2019/02/IMG_6430.png',
    U + '2019/02/IMG_6431.png', U + '2019/02/IMG_6432.png',
    U + '2019/02/IMG_6433.png', U + '2019/02/IMG_6434.png',
    U + '2019/02/IMG_6481.png',
    # 2019/03 originals
    U + '2019/03/1551427143-1.jpg', U + '2019/03/1552976108.jpg',
    U + '2019/03/1553741645.jpg', U + '2019/03/1553741962.jpg',
    U + '2019/03/1553742530.jpg',
    U + '2019/03/IMG_1115.jpg', U + '2019/03/IMG_1153.jpg',
    U + '2019/03/IMG_1354.jpg', U + '2019/03/IMG_1364.jpg',
    U + '2019/03/IMG_1365.jpg', U + '2019/03/IMG_6660.png',
    U + '2019/03/IMG_6662.png', U + '2019/03/IMG_6666.png',
    U + '2019/03/IMG_6686.png', U + '2019/03/IMG_6693.png',
    U + '2019/03/IMG_6694.png', U + '2019/03/IMG_6778.png',
    U + '2019/03/IMG_6828.png', U + '2019/03/IMG_6834.png',
    U + '2019/03/5hunters.png', U + '2019/03/priority.png',
    U + '2019/03/0001.jpg',
]


def fetch_retry(u, tries=3):
    for k in range(tries):
        rec = crawl.get_img(u)
        if rec.get('ok') or rec.get('why') == 'no-capture':
            return rec
        time.sleep(4 * (k + 1))
    return rec


def main():
    res = crawl.par(PRIORITY, fetch_retry, workers=3, label='priority')
    out = {}
    for r in res:
        if r.get('orig'):
            out[r['orig']] = r
    json.dump(out, open(os.path.join(HERE, 'priority-images.json'), 'w',
                        encoding='utf-8'), ensure_ascii=False, indent=1)
    ok = [r for r in res if r.get('ok')]
    print('recovered %d/%d' % (len(ok), len(PRIORITY)))
    for r in sorted(ok, key=lambda x: x['orig']):
        print('  %-8s %5sx%-5s %-9s %s' % (r['bytes'], r['w'], r['h'],
                                         r['sha256'][:12],
                                         r['orig'].rsplit('/', 1)[-1]))


if __name__ == '__main__':
    main()