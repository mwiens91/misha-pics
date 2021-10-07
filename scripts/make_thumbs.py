#!/usr/bin/env python3

import os
from PIL import Image, ImageOps

MAX_THUMB_HEIGHT = 400

PICS_DIR = "../pics"
THUMBS_DIR = "../pics/thumbs"

# Set this to True if you want to do a clean sweep of the thumbnails
rewrite_existing = False

all_pics = [f for f in os.listdir(PICS_DIR) if f[-3:] == "jpg"]
all_thumbs = os.listdir(THUMBS_DIR)

for pic in all_pics:
    pic_path = os.path.join(PICS_DIR, pic)
    thumb_path = os.path.join(THUMBS_DIR, pic)

    if not os.path.isfile(thumb_path) or rewrite_existing:
        with Image.open(pic_path) as raw_im:
            with ImageOps.exif_transpose(raw_im) as im:
                w, h = im.size
                a = MAX_THUMB_HEIGHT / h
                im.thumbnail((w * a, h * a), Image.ANTIALIAS)
                im.save(thumb_path)
