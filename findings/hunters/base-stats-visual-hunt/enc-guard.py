"""Encoding guard for this workspace.

GUARD-encoding-and-archive-traps.md: a prior agent destroyed Hangul content with
PowerShell file I/O.  This tool is the only sanctioned reader/writer path:
pure bytes in, pure bytes out, plus a U+FFFD / Hangul / CJK / line-ending audit.

Usage:
  python enc-guard.py baseline <file> [<file> ...]   -> write baseline json
  python enc-guard.py check    <file> [<file> ...]   -> audit + diff vs baseline
  python enc-guard.py write    <file>               -> rewrite file byte-identically
                                                     (proves a no-op rewrite is safe)
"""
import io, os, sys, json, hashlib, unicodedata

BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '.enc-baseline.json')


def scan(path):
    raw = open(path, 'rb').read()
    txt = raw.decode('utf-8', errors='replace')
    b = {
        'size': len(raw),
        'sha256': hashlib.sha256(raw).hexdigest(),
        'fffd': txt.count('\ufffd'),
        'hangul': sum(1 for c in txt if '\uac00' <= c <= '\ud7a3'
                      or '\u1100' <= c <= '\u11ff'
                      or '\u3130' <= c <= '\u318f'
                      or '\ua960' <= c <= '\ua97f'
                      or '\ud7b0' <= c <= '\ud7ff'),
        'cjk': sum(1 for c in txt if '\u4e00' <= c <= '\u9fff'
                   or '\u3400' <= c <= '\u4dbf'
                   or '\uf900' <= c <= '\ufaff'
                   or '\u3000' <= c <= '\u303f'
                   or '\uff00' <= c <= '\uffef'),
        'crlf': raw.count(b'\r\n'),
        'cr': raw.count(b'\r'),
        'lf': raw.count(b'\n'),
        'nonascii': sum(1 for c in txt if ord(c) > 127),
        'chars': len(txt),
        'final_newline': raw.endswith(b'\n'),
        'bom': raw.startswith(b'\xef\xbb\xbf'),
    }
    return b, raw


def main():
    cmd = sys.argv[1]
    files = sys.argv[2:]
    if cmd == 'baseline':
        db = {}
        if os.path.exists(BASELINE):
            db = json.load(io.open(BASELINE, 'r', encoding='utf-8'))
        for f in files:
            s, _ = scan(f)
            db[os.path.basename(f)] = s
        io.open(BASELINE, 'w', encoding='utf-8', newline='\n').write(
            json.dumps(db, indent=1, sort_keys=True))
        for f in files:
            s = db[os.path.basename(f)]
            print("BASELINE %-52s size=%-8d fffd=%d hangul=%-5d cjk=%-4d crlf=%-5d cr=%-5d lf=%-6d nonascii=%-6d"
                  % (os.path.basename(f), s['size'], s['fffd'], s['hangul'], s['cjk'],
                     s['crlf'], s['cr'], s['lf'], s['nonascii']))
        return

    db = json.load(io.open(BASELINE, 'r', encoding='utf-8')) if os.path.exists(BASELINE) else {}
    bad = 0
    for f in files:
        s, _ = scan(f)
        k = os.path.basename(f)
        base = db.get(k)
        flag = []
        if s['fffd'] != 0:
            flag.append('*** U+FFFD=%d ***' % s['fffd']); bad = 1
        if base:
            # HARD invariants: any change means content damage.
            for field in ('fffd', 'hangul', 'cjk', 'crlf', 'cr', 'bom', 'final_newline'):
                if s[field] != base[field]:
                    flag.append('*** %s %s -> %s ***' % (field, base[field], s[field])); bad = 1
            # EXPECTED to change on an intentional edit; reported, never fatal.
            for field in ('size', 'lf', 'chars', 'nonascii', 'sha256'):
                if s[field] != base[field]:
                    flag.append('(ok %s %s -> %s)' % (field, base[field], s[field]))
        else:
            flag.append('(no baseline)')
        print("%-4s %-52s size=%-8d fffd=%d hangul=%-5d cjk=%-4d crlf=%-5d cr=%-5d lf=%-6d nonascii=%-6d %s"
              % ('FAIL' if flag and bad else 'ok', k, s['size'], s['fffd'], s['hangul'],
                 s['cjk'], s['crlf'], s['cr'], s['lf'], s['nonascii'], ' '.join(flag)))
    sys.exit(bad)


if __name__ == '__main__':
    main()
