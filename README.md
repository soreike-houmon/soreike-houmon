# 予約公開の置き場（scheduled/site）

`.scheduled/<公開日>/` に、その日に公開するサイト全体（HTML・sitemap.xml・robots.txt・css）が入っています。
main の `.github/workflows/scheduled-publish.yml` が毎朝 6:41（日本時間）に、その日の分でサイトを差し替えます。
作り直しは社長の Mac の `_build/build_schedule.py` で行い、このブランチを丸ごと入れ替えます。手で直さないでください。
