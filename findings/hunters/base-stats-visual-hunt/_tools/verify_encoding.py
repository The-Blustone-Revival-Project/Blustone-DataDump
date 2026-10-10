import re
import sys

p = sys.argv[1]
raw = open(p, "rb").read()
t = raw.decode("utf-8", "replace")

checks = {
    "bytes": len(raw),
    "chars": len(t),
    "U+FFFD (must be 0)": t.count("\ufffd"),
    "CRLF (must be 0)": t.count("\r\n"),
    "lone CR (must be 0)": len(re.findall(r"\r(?!\n)", t)),
    "LF": t.count("\n"),
    "em-dash U+2014 (expect >0)": t.count("\u2014"),
    "hangul AC00-D7A3 (expect >0)": len(re.findall(r"[\uAC00-\uD7A3]", t)),
    "CJK 4E00-9FFF (expect >0)": len(re.findall(r"[\u4E00-\u9FFF]", t)),
    "kana 3040-30FF (expect >0)": len(re.findall(r"[\u3040-\u30FF]", t)),
    "fullwidth FF01-FF5E (expect >0)": len(re.findall(r"[\uFF01-\uFF5E]", t)),
    "mojibake 'Ã' (must be 0)": t.count("\u00c3"),
    "mojibake 'Â' (must be 0)": t.count("\u00c2"),
    "trailing whitespace lines": len([l for l in t.split("\n") if l != l.rstrip()]),
}
for k, v in checks.items():
    print(f"  {k:42s} = {v}")

ok = (checks["U+FFFD (must be 0)"] == 0 and checks["CRLF (must be 0)"] == 0
      and checks["lone CR (must be 0)"] == 0)
print("\nRESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
