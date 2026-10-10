"""Extract the document text with the position of each embedded image, so every
image can be located in context before viewing."""
import html as htmlmod
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
G = os.path.join(HERE, "gdoc")

with open(os.path.join(G, "faq.html"), encoding="utf-8") as f:
    h = f.read()

# Replace each img tag with a marker so image order is preserved in the text.
n = [0]


def repl(m):
    n[0] += 1
    return "\n[[IMAGE %02d]]\n" % n[0]


h2 = re.sub(r'<img[^>]*>', repl, h)
txt = re.sub(r"<[^>]+>", " ", h2)
txt = htmlmod.unescape(txt)
lines = [re.sub(r"\s+", " ", l).strip() for l in txt.split("\n")]
lines = [l for l in lines if l]
out = "\n".join(lines)
with open(os.path.join(G, "faq_html_text.txt"), "w", encoding="utf-8",
          newline="\n") as f:
    f.write(out)
print("images in order: %d ; text lines: %d" % (n[0], len(lines)))
