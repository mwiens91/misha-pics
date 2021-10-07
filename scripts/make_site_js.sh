#!/usr/bin/env bash

awk 'NR==FNR { a[n++]=$0; next } /data/ { for (i=0;i<n;++i) print a[i]; next }1' data raw_site_js.js
