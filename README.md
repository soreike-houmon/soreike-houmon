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
sitemap.xml    Google 向けのページ一覧
.github/       自動公開の設定と公開前チェック
```

## 公開のしかた（自動）

main ブランチ（本番）が更新されると、GitHub Actions が自動で次の作業をします（設定ファイル：`.github/workflows/deploy.yml`）。

1. 公開前チェック：全ページのリンク・画像・CSS・JS・動画のファイルがそろっているか確かめる（`.github/scripts/check_site.py`）
2. チェックに合格したら、サイトのファイルだけをまとめて GitHub Pages に公開する
3. 問題が見つかった場合は公開せず、今のページをそのまま残す

公開先：https://www.soreike-houmon.com/
公開の状況は、リポジトリの「Actions」タブで確認できる（緑のチェック＝成功、赤の×＝失敗）。

## 更新のしかた

1. Claude が変更を作り、「変更の提案（プルリクエスト）」を出す
2. 北田さんが内容を確認して「Merge pull request」を押す
3. 数分で自動的に公開される

文章や見た目を変えるときは、先に手元の CONTENT.md・DESIGN.md を直してから HTML に反映する（運用ルールは手元の CLAUDE.md）。

## 注意

- お問い合わせフォームの送信先（contact.html の `action`）は、確認なしに変えない
- 「HP素材」フォルダの元ファイルや、CONTENT.md・DESIGN.md・CLAUDE.md はこのリポジトリに入れない（公開リポジトリは誰でも中身を見られるため）
