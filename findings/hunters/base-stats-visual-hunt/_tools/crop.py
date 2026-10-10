#!/usr/bin/env python
"""Crop + upscale a region of an image so small numerals can be read reliably."""
import sys
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
box = tuple(int(x) for x in sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 3.0
im = Image.open(src)
print('source size:', im.size, '-> cropping', box)
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print('saved', out, c.size)
