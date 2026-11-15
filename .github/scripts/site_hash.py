# -*- coding: utf-8 -*-
"""サイトの中身（HTML・sitemap.xml・robots.txt・css/style.css）の指紋を出す。
予約公開で、公開中の main が「予約を作ったときの想定どおり」かを確かめるために使う。
使い方: python3 .github/scripts/site_hash.py <フォルダ>
"""
import glob
import hashlib
import os
import sys

root = sys.argv[1] if len(sys.argv) > 1 else '.'
files = sorted(os.path.basename(p) for p in glob.glob(os.path.join(root, '*.html')))
files += ['sitemap.xml', 'robots.txt', 'css/style.css']
h = hashlib.sha256()
for f in files:
    h.update(f.encode('utf-8') + b'\0')
    with open(os.path.join(root, f), 'rb') as fh:
        h.update(hashlib.sha256(fh.read()).digest())
print(h.hexdigest())
