#!/usr/bin/env python3
"""Targeted parallel fetch of the highest-prioritity blustone.jp screenshots.

Priority is by article subject (equipment / rank-up / training / stat), because a
stat panel (HP/ATK/DEF with visible empty slots) can only appear in those.

Controls run first (archive root, known image rankup.jpg, known hero 051 page).
"""
import os, re, sys, json, time, hashlib, threading, queue
import urllib.request, urllib.error
from io import BytesIO
from PIL import Image

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"
SIGS = {b"\xff\xd8\xff": "jpeg", b"\x89PNG": "png", b"GIF8": "gif", b"BM": "bmp"}
BASE = 'http://web.archive.org/web/'
OUT = 'hero-panel-level-images-2026-10-06'
MAN = os.path.join(OUT, '_manifest.json')


def fetch(url, timeout=120, tries=3):
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            b = e.read()
            if e.code in (502, 503, 504) and a < tries - 1:
                time.sleep(2 * (a + 1)); continue
            return e.code, b
        except Exception:
            if a < tries - 1:
                time.sleep(2 * (a + 1)); continue
    return None, b''


def sig(b):
    for s, n in SIGS.items():
        if b.startswith(s):
            return n
    return None


# (priority label, url)  -- captured timestamps are supplied per item
ITEMS = [
    # --- rank-up / growth-theory / training articles
    ('rankup-1', '20190331213910', 'https://blustone.jp/wp-content/uploads/2018/11/rank1-1024x911.jpg'),
    ('rankup-2', '20190331213910', 'https://blustone.jp/wp-content/uploads/2018/11/rank2-1024x911.jpg'),
    ('rankup-3', '20190403182150', 'https://blustone.jp/wp-content/uploads/2018/11/rank3-1024x911.jpg'),
    ('rankup-4', '20190403182150', 'https://blustone.jp/wp-content/uploads/2018/11/rank4-1024x911.jpg'),
    ('rankup-d', '20191121222851', 'https://blustone.jp/wp-content/uploads/2018/11/d.jpg'),
    ('rankup-img', '20190331213910', 'https://blustone.jp/wp-content/uploads/2018/11/rankup.jpg'),
    ('rankup-png', '20190331102005', 'https://blustone.jp/wp-content/uploads/2018/11/rankup.png'),
    ('rank-png', '20190403205201', 'https://blustone.jp/wp-content/uploads/2018/11/rank.png'),
    ('star5-a', '20190405051840', 'https://blustone.jp/wp-content/uploads/2019/02/1548136677.jpg'),
    ('star5-b', '20191118072651', 'https://blustone.jp/wp-content/uploads/2019/02/1548137184.jpg'),
    ('star5-c', '20191118072651', 'https://blustone.jp/wp-content/uploads/2019/02/1548138716.jpg'),
    ('star5-d', '20191121194838', 'https://blustone.jp/wp-content/uploads/2019/02/1548136677.jpg'),
    ('star5-rank3', '20190405051840', 'https://blustone.jp/wp-content/uploads/2019/01/rank3.jpg'),
    ('star5-img5729', '20190330070910', 'https://blustone.jp/wp-content/uploads/2019/01/IMG_5729.png'),
    # --- training / gym
    ('traning-png', '20190403102507', 'https://blustone.jp/wp-content/uploads/2018/11/traning.png'),
    ('traning1', '20191122213323', 'https://blustone.jp/wp-content/uploads/2018/11/traning1.jpg'),
    ('traning2', '20191121070729', 'https://blustone.jp/wp-content/uploads/2018/11/traning2.jpg'),
    ('gym', '20190403213524', 'https://blustone.jp/wp-content/uploads/2018/11/gym.jpg'),
    ('gim1', '20191210182452', 'https://blustone.jp/wp-content/uploads/2018/11/gim1.jpg'),
    ('gim2', '20191118072759', 'https://blustone.jp/wp-content/uploads/2018/11/gim2.jpg'),
    # --- equipment / crystal
    ('equip1', '20191122162722', 'https://blustone.jp/wp-content/uploads/2018/11/equip1-1024x911.jpg'),
    ('equipment', '20190403114918', 'https://blustone.jp/wp-content/uploads/2018/11/equipment.jpg'),
    ('crystal', '20190403194557', 'https://blustone.jp/wp-content/uploads/2018/11/crystal.jpg'),
    ('capacity', '20190403125104', 'https://blustone.jp/wp-content/uploads/2018/11/capacity.png'),
    ('attribute', '20190403235249', 'https://blustone.jp/wp-content/uploads/2018/11/attribute.png'),
    ('type', '20190403184249', 'https://blustone.jp/wp-content/uploads/2018/11/type.png'),
    # --- transcendence (capa)
    ('capa1', '20190330070910', 'https://blustone.jp/wp-content/uploads/2018/11/capa1-1024x911.jpg'),
    ('capa2', '20190403161635', 'https://blustone.jp/wp-content/uploads/2018/11/capa2-1024x911.jpg'),
    ('capa', '20190401022918', 'https://blustone.jp/wp-content/uploads/2019/03/capa.jpg'),
    ('capa-full', '20191121194812', 'https://blustone.jp/wp-content/uploads/2018/11/capa2.jpg'),
    ('1542365712', '20191121223254', 'https://blustone.jp/wp-content/uploads/2018/11/1542365712-300x267.jpg'),
    ('1542365835', '20191121144053', 'https://blustone.jp/wp-content/uploads/2018/11/1542365835-300x267.jpg'),
    ('1542365925', '20191121070352', 'https://blustone.jp/wp-content/uploads/2018/11/1542365925-300x267.jpg'),
    ('1542366108', '20191216045912', 'https://blustone.jp/wp-content/uploads/2018/11/1542366108-300x267.jpg'),
    ('1542366153', '20191122213132', 'https://blustone.jp/wp-content/uploads/2018/11/1542366153-300x267.jpg'),
    ('1542366172', '20191210184847', 'https://blustone.jp/wp-content/uploads/2018/11/1542366172-300x267.jpg'),
    ('1542366194', '20191211121234', 'https://blustone.jp/wp-content/uploads/2018/11/1542366194-300x267.jpg'),
    ('1542366264', '20191210193622', 'https://blustone.jp/wp-content/uploads/2018/11/1542366264-300x267.jpg'),
    # --- big guides / ranking articles (large 1024px screenshots)
    ('prio-1551068175', '20190330070910', 'https://blustone.jp/wp-content/uploads/2019/03/1551068175-1024x911.jpg'),
    ('prio-1551427143', '20190403143704', 'https://blustone.jp/wp-content/uploads/2019/03/1551427143-1-1024x911.jpg'),
    ('prio-1551430697', '20190404023807', 'https://blustone.jp/wp-content/uploads/2019/03/1551430697-1024x911.jpg'),
    ('prio-1551433025', '20190403125358', 'https://blustone.jp/wp-content/uploads/2019/03/1551433025-1024x911.jpg'),
    ('prio-15514278172', '20190403133544', 'https://blustone.jp/wp-content/uploads/2019/03/15514278172-1024x448.jpg'),
    ('prio-TOP', '20190403172525', 'https://blustone.jp/wp-content/uploads/2019/01/TOP-1024x906.jpg'),
    ('prio-0d40-11', '20190331172016', 'https://blustone.jp/wp-content/uploads/2019/01/0d40a5e4a645fc6b96e767d64ac0878e-11-1024x882.jpg'),
    ('prio-0d40-full', '20191121195218', 'https://blustone.jp/wp-content/uploads/2019/02/0d40a5e4a645fc6b96e767d64ac0878e.jpg'),
    ('prio-1543460677', '20191121223111', 'https://blustone.jp/wp-content/uploads/2018/11/1543460677-1024x911.jpg'),
    ('prio-1543461051', '20190403191923', 'https://blustone.jp/wp-content/uploads/2018/11/1543461051-1024x911.jpg'),
    ('prio-1543461573', '20190404004932', 'https://blustone.jp/wp-content/uploads/2018/11/1543461573-1024x607.jpg'),
    ('prio-1544600633', '20191122163105', 'https://blustone.jp/wp-content/uploads/2018/12/1544600633-1024x911.jpg'),
    ('prio-1544668601', '20191121194851', 'https://blustone.jp/wp-content/uploads/2018/12/1544668601-1024x911.jpg'),
    ('prio-1544671642', '20191210191719', 'https://blustone.jp/wp-content/uploads/2018/12/1544671642-1024x911.jpg'),
    ('prio-biginner1', '20190403130500', 'https://blustone.jp/wp-content/uploads/2018/11/biginner1-1024x910.jpg'),
    ('prio-fishing1', '20190404100256', 'https://blustone.jp/wp-content/uploads/2018/11/fishing1-1024x910.jpg'),
    ('prio-party', '20190404062222', 'https://blustone.jp/wp-content/uploads/2018/11/party.jpg'),
    ('prio-market', '20190403114035', 'https://blustone.jp/wp-content/uploads/2018/11/market.jpg'),
    ('prio-fight', '20190403143422', 'https://blustone.jp/wp-content/uploads/2018/11/fight.jpg'),
    ('prio-detective', '20190403162501', 'https://blustone.jp/wp-content/uploads/2018/11/detective.jpg'),
    ('prio-excavation', '20190403184102', 'https://blustone.jp/wp-content/uploads/2018/11/excavation.jpg'),
    ('prio-jigoku', '20190403054928', 'https://blustone.jp/wp-content/uploads/2018/11/jigoku.jpg'),
    ('prio-jigoku2', '20190403103312', 'https://blustone.jp/wp-content/uploads/2018/11/jigoku2.jpg'),
    ('prio-ginkan', '20190403172800', 'https://blustone.jp/wp-content/uploads/2018/11/gingan-300x296.jpg'),
    ('prio-sinkirou', '20190403090651', 'https://blustone.jp/wp-content/uploads/2018/11/sinkirou.jpg'),
    # --- 2019/01 and 2019/02 article galleries (equipment / rank / training)
    ('g1-1547530477', '20190403192343', 'https://blustone.jp/wp-content/uploads/2019/01/1547530477-1024x911.jpg'),
    ('g1-1547530839', '20190404000851', 'https://blustone.jp/wp-content/uploads/2019/01/1547530839-1024x911.jpg'),
    ('g1-1547531028', '20190403190441', 'https://blustone.jp/wp-content/uploads/2019/01/1547531028-1024x911.jpg'),
    ('g1-1547531163', '20190403160821', 'https://blustone.jp/wp-content/uploads/2019/01/1547531163-1024x911.jpg'),
    ('g1-1547531314', '20190403230916', 'https://blustone.jp/wp-content/uploads/2019/01/1547531314-1024x911.jpg'),
    ('g1-1547531476', '20190403205141', 'https://blustone.jp/wp-content/uploads/2019/01/1547531476-1024x911.jpg'),
    ('g1-1547534994', '20190403191029', 'https://blustone.jp/wp-content/uploads/2019/01/1547534994-1024x911.jpg'),
    ('g1-1548235686', '20190405055741', 'https://blustone.jp/wp-content/uploads/2019/01/1548235686-1024x911.jpg'),
    ('g1-1548235710', '20190405091928', 'https://blustone.jp/wp-content/uploads/2019/01/1548235710-1024x911.jpg'),
    ('g1-1548235742', '20190405071006', 'https://blustone.jp/wp-content/uploads/2019/01/1548235742-1024x911.jpg'),
    ('g1-1548235768', '20191115010520', 'https://blustone.jp/wp-content/uploads/2019/01/1548235768-1024x911.jpg'),
    ('g2-1550199154', '20190403123514', 'https://blustone.jp/wp-content/uploads/2019/02/1550199154-1024x607.jpg'),
    ('g2-1550200766', '20190403124218', 'https://blustone.jp/wp-content/uploads/2019/02/1550200766-1024x910.jpg'),
    ('g2-1550200979', '20190403121239', 'https://blustone.jp/wp-content/uploads/2019/02/1550200979-1024x910.jpg'),
    ('g2-1550201188', '20190403174240', 'https://blustone.jp/wp-content/uploads/2019/02/1550201188-1024x910.jpg'),
    ('g2-1550201353', '20190403113449', 'https://blustone.jp/wp-content/uploads/2019/02/1550201353-2-1024x910.jpg'),
    ('g2-1550201669', '20191121223058', 'https://blustone.jp/wp-content/uploads/2019/02/1550201669-1024x910.jpg'),
    ('g2-1550473238', '20191118021940', 'https://blustone.jp/wp-content/uploads/2019/02/1550473238-1024x911.jpg'),
    ('g2-1550474475', '20190403193251', 'https://blustone.jp/wp-content/uploads/2019/02/1550474475-1024x911.jpg'),
    ('g2-1550733537', '20190403163545', 'https://blustone.jp/wp-content/uploads/2019/02/1550733537-1024x911.jpg'),
    ('g2-1550735696', '20190403122747', 'https://blustone.jp/wp-content/uploads/2019/02/1550735696-1024x911.jpg'),
    ('g2-1551089100', '20190403221018', 'https://blustone.jp/wp-content/uploads/2019/02/1551089100-1024x911.jpg'),
    ('g2-1551089150', '20190403140334', 'https://blustone.jp/wp-content/uploads/2019/02/1551089150-1024x911.jpg'),
    ('g2-1551085767', '20191121195121', 'https://blustone.jp/wp-content/uploads/2019/02/1551085767-1024x911.jpg'),
    # --- full-size beckhen/harry article images
    ('bh-6117', '20191121195418', 'https://blustone.jp/wp-content/uploads/2019/02/IMG_6117.png'),
    ('bh-6096', '20190403190457', 'https://blustone.jp/wp-content/uploads/2019/02/IMG_6096.png'),
    ('bh-6118', '20191121195218', 'https://blustone.jp/wp-content/uploads/2019/02/IMG_6118-1.png'),
    ('bh-6107', '20191121222821', 'https://blustone.jp/wp-content/uploads/2019/02/IMG_6107.png'),
    ('bh-f451', '20190403162000', 'https://blustone.jp/wp-content/uploads/2019/02/f451b5ab735c737b8d88ae5eaf5df838.png'),
    ('bh-9d46', '20190403163000', 'https://blustone.jp/wp-content/uploads/2019/02/9d46d839ed187d2682b387195f56b022.png'),
]

lock = threading.Lock()


def main():
    os.makedirs(OUT, exist_ok=True)
    print('=== CONTROLS ===')
    c1 = fetch(BASE)[0] == 200
    s, b = fetch(BASE + '20190403182150id_/http://blustone.jp/wp-content/uploads/2018/11/rankup.jpg')
    c2 = (s == 200 and sig(b) == 'jpeg' and len(b) > 50000)
    s, b = fetch(BASE + '20191216060610id_/https://blustone.jp/hunter/'
                 '%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5/'
                 '%E3%83%95%E3%82%A1%E3%82%A4%E3%83%88%E3%82%AF%E3%83%A9%E3%83%96%E3%81%AE'
                 '%E5%AE%88%E8%AD%B7%E8%80%85%E3%80%8C%E3%83%99%E3%83%83%E3%82%B1%E3%83%B3%E3%80%8D')
    c3 = (s == 200 and b'8709' in b and b'1678' in b)
    print('  C1 root %s  C2 rankup.jpg %dB %s  C3 hero051 %s'
          % ('PASS' if c1 else 'FAIL', len(b), 'PASS' if c2 else 'FAIL',
             'PASS' if c3 else 'FAIL'))
    if not (c1 and c2 and c3):
        print('ABORT')
        return 2

    man = {}
    if os.path.exists(MAN):
        for r in json.load(open(MAN, encoding='utf-8')):
            man[r['name']] = r
    added = []
    q = queue.Queue()
    for it in ITEMS:
        if it[2].split('/')[-1] in man:
            continue
        q.put(it)

    def worker():
        while True:
            try:
                label, ts, url = q.get_nowait()
            except queue.Empty:
                return
            name = url.split('/')[-1]
            got = None
            for t in [ts] + ['20190403130000', '20191118000000', '20191216000000']:
                arc = BASE + t + 'id_/' + url
                s, b = fetch(arc)
                sg = sig(b)
                if s == 200 and sg:
                    got = (t, b, sg); break
                if s == 200 and len(b) == 3357:
                    got = (t, b, 'PARKING'); break
            with lock:
                row = man.get(name, {'url': url, 'name': name})
                if got:
                    t, b, sg = got
                    row.update({'status': 'ok' if sg != 'PARKING' else 'parking',
                                'fetch_ts': t, 'bytes': len(b), 'kind': sg,
                                'label': label,
                                'sha256': hashlib.sha256(b).hexdigest()})
                    if sg != 'PARKING':
                        p = os.path.join(OUT, name)
                        if not os.path.exists(p) or os.path.getsize(p) != len(b):
                            open(p, 'wb').write(b)
                        try:
                            im = Image.open(BytesIO(b)); row['w'], row['h'] = im.size
                        except Exception as e:
                            row['dim_error'] = str(e)
                else:
                    row.update({'status': '404', 'label': label})
                added.append(row)
                print('  %-18s %-9s %-46s %s' % (label, row['status'], name[:46],
                      ('%dx%d %dB' % (row.get('w', 0), row.get('h', 0), row.get('bytes', 0)))
                      if row['status'] == 'ok' else ''))
                json.dump(list(man.values()), open(MAN, 'w', encoding='utf-8'),
                          ensure_ascii=False, indent=1)

    ts_ = [threading.Thread(target=worker) for _ in range(6)]
    [t.start() for t in ts_]
    [t.join() for t in ts_]
    print('\nitems attempted: %d ; manifest size %d'
          % (len(added), len(man)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
