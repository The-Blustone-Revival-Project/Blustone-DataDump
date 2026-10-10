import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"analysis\VSFan"
for root, d, files in os.walk(p):
    for f in sorted(files):
        e = os.path.splitext(f)[1].lower()
        if e in (".jpg", ".pdf", ".docx", ".xlsx", ".md", ".apk"):
            fp = os.path.join(root, f)
            print("%10d  %s" % (os.path.getsize(fp), fp))
