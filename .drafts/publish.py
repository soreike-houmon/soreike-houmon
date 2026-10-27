"""毎朝の公開準備：main の作業ツリーで実行する。
usage: python3 .drafts/publish.py <YYYY-MM-DD>  （.drafts は drafts/staff-shinkyu ブランチから取り出しておく）
公開日が今日以前で、まだ main にない回をすべて追加する。追加した回の番号を表示する（なければ NONE）。"""
import sys, json, glob, os, re, shutil
sys.path.insert(0, ".drafts"); import series
today = sys.argv[1]
metas = sorted((json.load(open(p, encoding="utf-8")) for p in glob.glob(".drafts/meta-*.json")), key=lambda m: m["n"])
todo = [m for m in metas if m["iso"] <= today and not os.path.exists(f"column-staff-shinkyu-{m['n']}.html")]
if not todo: print("NONE"); sys.exit(0)
# 見た目（記事内写真のスタイル）がまだなければ反映
if ".article-figure" not in open("css/style.css", encoding="utf-8").read():
    shutil.copy(".drafts/style.css", "css/style.css")
# サイトのアドレス（独自ドメインに移っても、sitemap.xml のトップのアドレスに合わせる）
OLD_BASE = "https://soreike-houmon.github.io/soreike-houmon/"
_sm = open("sitemap.xml", encoding="utf-8").read()
BASE = re.search(r"<loc>(https://[^<]+?/)</loc>", _sm).group(1)
for m in todo:
    n = m["n"]
    page = open(f".drafts/column-staff-shinkyu-{n}.html", encoding="utf-8").read().replace(OLD_BASE, BASE)
    open(f"column-staff-shinkyu-{n}.html", "w", encoding="utf-8").write(page)
    s = open("column.html", encoding="utf-8").read()
    item = f'''      <ul class="column-list">
        <li>
          <a href="column-staff-shinkyu-{n}.html">
            <span class="news-meta"><time datetime="{m['iso']}">{m['date_ja']}</time></span>
            <span class="column-list-title">{m['list_title']}</span>
            <span class="column-list-text">{m['list_text']}</span>
          </a>
        </li>
'''
    s = s.replace('      <ul class="column-list">\n', item, 1); open("column.html", "w", encoding="utf-8").write(s)
    sm = open("sitemap.xml", encoding="utf-8").read()
    prev = max(k for k in range(1, n) if f"column-staff-shinkyu-{k}.html" in sm)
    a = f"column-staff-shinkyu-{prev}.html</loc></url>\n"
    sm = sm.replace(a, a + f"  <url><loc>{BASE}column-staff-shinkyu-{n}.html</loc></url>\n")
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
latest = max(m["n"] for m in todo)
for k in range(1, latest + 1):
    p = f"column-staff-shinkyu-{k}.html"; s = open(p, encoding="utf-8").read()
    s = re.sub(r'        <div class="card series-nav">.*?\n        </div>', lambda _: series.card(k, latest), s, count=1, flags=re.S)
    open(p, "w", encoding="utf-8").write(s)
print(" ".join(str(m["n"]) for m in todo))
