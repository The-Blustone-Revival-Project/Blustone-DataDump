import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.abspath(os.path.join(HERE, '..', '..',
                                 'grade-vs-level-factor-2026-10-06.md'))
b = open(p, 'rb').read()
t = b.decode('utf-8')
checks = [
    ('U+FFFD', t.count('\ufffd'), 0),
    ('CR', t.count('\r'), 0),
    ('CRLF', t.count('\r\n'), 0),
    ('mojibake U+00C3', t.count('\ufffd') if False else t.count('\u00c3'), 0),
    ('em-dash U+2014', t.count('\u2014'), None),
    ('CJK U+4E00-9FFF', sum(1 for c in t if 0x4E00 <= ord(c) <= 0x9FFF), None),
    ('kana U+3040-30FF', sum(1 for c in t if 0x3040 <= ord(c) <= 0x30FF), None),
    ('Hangul AC00-D7A3', sum(1 for c in t if 0xAC00 <= ord(c) <= 0xD7A3), None),
]
ok = True
for name, got, want in checks:
    flag = ''
    if want is not None:
        flag = ' OK' if got == want else ' ** FAIL **'
        if got != want:
            ok = False
    print('%-22s : %-6d%s' % (name, got, flag))
print('trailing newline       :', 'yes' if t.endswith('\n') else 'NO')
print('bytes                  :', len(b))
print('HEALTH                 :', 'PASS' if ok else 'FAIL')

# folder-wide CR scan (trap #14)
folder = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
bad = []
for root, dirs, files in os.walk(folder):
    for f in files:
        if f.endswith(('.md', '.json', '.py')):
            fp = os.path.join(root, f)
            try:
                if b'\r\n' in open(fp, 'rb').read():
                    bad.append(fp)
            except Exception:
                pass
print('folder-wide CRLF files:', len(bad))
for x in bad[:10]:
    print('   ', x)