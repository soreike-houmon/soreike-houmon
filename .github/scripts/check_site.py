"""公開前チェック：ページ内のリンク・画像・CSS・JS・動画のファイルが、すべて存在するか確かめる。
1つでも見つからなければ失敗させ、公開を止める。"""
import pathlib, re, sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
pattern = re.compile(r'(?:href|src|poster)="([^"]+)"')
problems = []

pages = sorted(root.glob("*.html"))
if not (root / "index.html").exists():
    problems.append("index.html（トップページ）がありません")

for page in pages:
    for ref in pattern.findall(page.read_text(encoding="utf-8")):
        if ref.startswith(("http://", "https://", "//", "tel:", "mailto:", "#", "data:")):
            continue
        path = ref.split("#")[0].split("?")[0]
        if path and not (root / path).exists():
            problems.append(f"{page.name}: {ref} が見つかりません")

if problems:
    print("公開前チェックで問題が見つかりました：")
    print("\n".join("  - " + p for p in problems))
    sys.exit(1)
print(f"公開前チェックOK（{len(pages)}ページ）")
