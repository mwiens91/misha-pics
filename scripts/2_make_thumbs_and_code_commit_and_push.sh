#!/usr/bin/env bash

./1_make_thumbs_and_code.sh

git pull

git add ../pics
git commit -m "Add new cat pics"

git -C ../../misha add js/gallery.js
git -C ../../misha commit -m "Add new cat pics"

git push
git -C ../../misha push
