# それいけ！訪問マッサージはり・きゅう ホームページ

大阪市鶴見区の訪問マッサージ・はり・きゅう「それいけ！訪問マッサージはり・きゅう」の公式ホームページです。
HTML・CSS・JavaScript だけで作った静的サイトで、GitHub Pages で公開します。

## ファイル構成

```
index.html     トップ
service.html   サービス
about.html     会社概要
recruit.html   採用情報
news.html      お知らせ
contact.html   お問い合わせ（Formspree で送信）
thanks.html    送信完了（メニューには出さない）
css/style.css  見た目
js/main.js     メニューの開閉・フォーム送信
images/        画像
video/         求人動画
.nojekyll      GitHub Pages にそのまま公開させるための空ファイル（消さない）
```

## 公開のしかた（GitHub Pages）

1. GitHub で新しいリポジトリを作る（Public を選ぶ）
2. このフォルダの中身をすべてアップロードする
3. リポジトリの「Settings」→「Pages」を開く
4. 「Build and deployment」の Source を「Deploy from a branch」、Branch を「main」「/(root)」にして Save
5. 数分後、`https://（GitHubのユーザー名）.github.io/（リポジトリ名）/` で表示される

## 更新のしかた

- 文章や見た目を変えるときは、先に手元の CONTENT.md・DESIGN.md を直してから HTML に反映する（運用ルールは手元の CLAUDE.md）
- 変更したファイルを GitHub にアップロードし直すと、数分で公開中のページに反映される

## 注意

- お問い合わせフォームの送信先（contact.html の `action`）は、確認なしに変えない
- 「HP素材」フォルダの元ファイルや、CONTENT.md・DESIGN.md・CLAUDE.md はこのリポジトリに入れない（公開リポジトリは誰でも中身を見られるため）
