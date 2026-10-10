import io
import os
import sys

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "zoom")


def crop(src, box, scale, name):
    im = Image.open(os.path.join(BASE, src))
    im = im.crop(box)
    im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, name)
    im.save(p)
    print(p, im.size)


if __name__ == "__main__":
    src = sys.argv[1]
    box = tuple(int(x) for x in sys.argv[2].split(","))
    crop(src, box, float(sys.argv[3]), sys.argv[4])
