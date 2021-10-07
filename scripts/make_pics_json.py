#!/usr/bin/env python3

import json
import os

PICS_DIR = "../pics"
THUMBS_DIR = "../pics/thumbs"

all_pics = sorted([f for f in os.listdir(PICS_DIR) if f[-3:] == "jpg"], reverse=True)
all_thumbs = sorted(os.listdir(THUMBS_DIR), reverse=True)

pics_list = []

for p, t in zip(all_pics, all_thumbs):
    pics_list.append({"src": os.path.join("/", p), "srct": os.path.join("/thumbs/", t)})

pics_json = json.dumps(pics_list, indent=2)

# Pipe this to a file
print(pics_json)
