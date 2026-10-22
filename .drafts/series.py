"""連載カードの生成。usage: series.py <repo> <最新の公開回>  -> 公開済みの全回のカードを書き換える"""
import sys, re
EP = [
 (1,"鍼灸（はり・きゅう）ってなに？ はりは痛い？ おきゅうは熱い？","2026-10-21","2026年10月21日"),
 (2,"刺激は強いほど効く？ 鍼灸の「ちょうどいい刺激」","2026-10-22","2026年10月22日"),
 (3,"訪問の鍼灸では、どんなことをするの？","2026-10-23","2026年10月23日"),
 (4,"鍼灸師になったきっかけと、訪問のやりがい","2026-10-24","2026年10月24日"),
 (5,"はりには、どんな種類があるの？","2026-10-25","2026年10月25日"),
 (6,"おきゅうには、どんな種類があるの？","2026-10-26","2026年10月26日"),
 (7,"便秘が気になるときに押したい、3つのツボ","2026-10-27","2026年10月27日"),
 (8,"足首、かたくないですか？ 足首と足指のセルフケア","2026-10-28","2026年10月28日"),
]
NEXT = {1:"「刺激は強いほど効くの？」",2:"「訪問の鍼灸では、どんなことをするの？」",3:"「鍼灸師になったきっかけ」と「訪問のやりがい」",
        4:"「はりの種類」",5:"「おきゅうの種類」",6:"「便秘が気になるときのツボ」"}
NEXT_TEXT = {7:"次回は、聞き手の北田の「かたい足首」を、田中さんに見てもらいます。"}
def card(cur, latest):
    lis=[]
    for n,t,iso,ja in EP:
        if n==cur: lis.append(f'            <li>第{n}回　{t}<span class="series-note">（この記事）</span></li>')
        elif n<=latest: lis.append(f'            <li><a href="column-staff-shinkyu-{n}.html">第{n}回　{t}</a></li>')
        else: lis.append(f'            <li>第{n}回　{t}<span class="series-note">（{ja}公開予定）</span></li>')
    nxt_t = NEXT_TEXT.get(cur) or (f'次回は、{NEXT[cur]}を田中さんにお聞きします。' if cur in NEXT else '')
    nxt = f'          <p>{nxt_t}</p>\n' if nxt_t else ''
    return ('        <div class="card series-nav">\n          <p class="series-nav-title">連載の記事（現場の先生に聞いてみた）</p>\n'
            '          <ol class="series-list">\n'+"\n".join(lis)+'\n          </ol>\n'+nxt+'        </div>')
if __name__=="__main__":
    repo, latest = sys.argv[1], int(sys.argv[2])
    for n in range(1, latest+1):
        p=f"{repo}/column-staff-shinkyu-{n}.html"; s=open(p,encoding="utf-8").read()
        s2=re.sub(r'        <div class="card series-nav">.*?\n        </div>', lambda m: card(n,latest), s, count=1, flags=re.S)
        open(p,"w",encoding="utf-8").write(s2); print(p, "updated" if s2!=s else "same")
