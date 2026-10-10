import os

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.abspath(os.path.join(HERE, '..'))

# 1. ensure the report ends with exactly one newline
rep = os.path.abspath(os.path.join(HERE, '..', '..',
                                   'grade-vs-level-factor-2026-10-06.md'))
b = open(rep, 'rb').read()
b2 = b.rstrip(b'\r\n') + b'\n'
if b2 != b:
    open(rep, 'wb').write(b2)
    print('report trailing newline fixed (%d -> %d bytes)' % (len(b), len(b2)))
else:
    print('report trailing newline already ok')

# 2. normalise CRLF -> LF in this lane's text/JSON scratch files
fixed = []
for root, dirs, files in os.walk(FOLDER):
    for f in files:
        if not f.endswith(('.md', '.json', '.py')):
            continue
        fp = os.path.join(root, f)
        d = open(fp, 'rb').read()
        if b'\r\n' in d:
            open(fp, 'wb').write(d.replace(b'\r\n', b'\n'))
            fixed.append(os.path.relpath(fp, FOLDER))
print('CRLF normalised in %d file(s):' % len(fixed))
for x in fixed:
    print('   ', x)