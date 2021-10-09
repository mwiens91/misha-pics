#!/usr/bin/env bash

./make_thumbs.py
./make_pics_json.py > data
./make_site_js.sh > new_js.js

yui-compressor new_js.js > mini_js.js

mv mini_js.js ../../misha/js/gallery.js
rm data
rm new_js.js
