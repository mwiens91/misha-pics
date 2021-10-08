#!/usr/bin/env bash

./make_thumbs.py
./make_pics_json.py > data
./make_site_js.sh > new_js.js

prettier --write new_js.js

mv new_js.js ../../misha/js/gallery.js
rm data
