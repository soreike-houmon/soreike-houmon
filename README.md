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
404.html       ページが見つからないとき
css/style.css  見た目
js/main.js     メニューの開閉・フォーム送信
images/        画像
video/         求人動画
sitemap.xml    Google 向けのページ一覧
robots.txt     検索エンジン向けの案内（サイトマップの場所）
.github/       自動公開の設定と公開前チェック
```

## 経緯（2026年11月）

- 11月7日、GitHub アカウントが一時停止されたため、公開先を Xserver に移した。この間、サイトは Mac の `_build/build.py` で作り直し、デザインも変えた
- 11月10日、アカウントの停止が解除されたので、公開先を GitHub Pages に戻した。Xserver で公開していた版（11月9日時点）をこのリポジトリに入れた
- `.htaccess`（Xserver 用の転送設定）と `counter.php`（アクセスカウンター）は GitHub Pages では動かないので入れていない。カウンターは数が読めないときは表示されない作り
- 11月10日、作り方を「社長の Mac の `_build/build.py` が正本 → PR → 社長がマージ」に一本化した（HTML をこのリポジトリで直接直さない）
- 11月10日、コラムの予約公開を新しいデザイン用に作り直して再開した（下の「コラムの予約公開」）

## コラムの予約公開（2026年11月10日〜）

- 3日に1本（CONTENT 7-5 の公開予定表どおり）。家族向けコラムは11月20日
- 予約分は `scheduled/site` ブランチの `.scheduled/<公開日>/`（公開日ごとのサイト全体）。Mac の `_build/build_schedule.py` でまとめて作る
- 毎朝 6:41（日本時間）に `.github/workflows/scheduled-publish.yml` が、その日の分でサイトを差し替えて公開する
- 安全装置：予約分を作ったあとに main を変えると、上書きせずに失敗で止まる（GitHub からメールが届く）。そのときは予約分を作り直して `scheduled/site` を入れ替え、Actions で手動実行する
- **サイトを変える PR をマージしたら、必ず予約分も作り直す**

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
