#!/usr/bin/env python3

import json
import os
from PIL import Image

PICS_DIR = "../pics"
THUMBS_DIR = "../pics/thumbs"

all_pics = sorted([f for f in os.listdir(PICS_DIR) if f[-3:] == "jpg"], reverse=True)
all_thumbs = sorted(os.listdir(THUMBS_DIR), reverse=True)

pics_list = []

for pic, thumb in zip(all_pics, all_thumbs):
    # Get dimensions
    pic_path = os.path.join(PICS_DIR, pic)
    thumb_path = os.path.join(THUMBS_DIR, pic)

    with Image.open(pic_path) as im:
        pic_w, pic_h = im.size

    with Image.open(thumb_path) as im:
        thumb_w, thumb_h = im.size

    # Put everything relevant in the list
    pics_list.append(
        {
            "kind": "image",
            "height": pic_h,
            "width": pic_w,
            "imgtHeight": thumb_h,
            "imgtWidth": thumb_w,
            "src": os.path.join("/", pic),
            "srct": os.path.join("/thumbs/", thumb),
        }
    )

pics_json = json.dumps(pics_list, indent=2)

# Pipe this to a file
print(pics_json)
