# -*- coding: utf-8 -*-
"""Episode: title
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## define alias
W = Writer
_ = W.getWho()


## scenes
def sc_airi_wakeup(w: World):
    hara, airi, yuri = W(w.harada), W(w.airi), W(w.yuri)
    inside, outside = W(w.inside), W(w.outside)
    wakui = W(w.wakui)
    return w.scene("$airiの目覚め／ふられる",
            airi.be("#寝ている"),
            wakui.be(),
            airi.do("ひやりとした空気が露出した肩を叩いたことに気づいて、沖愛里は目覚める"),
            _.do("薄い布団の上にうつ伏せになっていた彼女はキャミソールが肩からずれていて、その肩紐を直しながら右手を伸ばした。毎朝そこにあったはずの涌井祐介の肉体が感じられない"),
            _.do("もそもそとした声がしているのが分かって、その中に「すみません」という言葉が混ざっているのが聞き取れた"),
            _.do("見ればシャツに腕を通しながら、左肩でスマートフォンを挟み込んで電話を受けている。曲がった背中は骨ばっていて、愛里が昨日クリーニングから取ってきたばかりの白シャツが歪む"),
            wakui.talk("小野川さん。分かってますって。忘れてた訳じゃないですって。詩乃ちゃん今日からですよね"),
            airi.do("そう言えばカレンダーに小さな赤い丸が付けてあった。女優の岩長さとりが涼し気な横顔を見せる一月のそれの、十五日だ"),
            wakui.talk("ほんとすみません。あと五分、いや十分で間に合わせますから"),
            airi.do("電車を乗り継いでも彼が勤めている喫茶店までは三十分はかかる。どう考えても間に合わなかった"),
            _.do("それでも何とか納得させて電話を切ると、祐介は愛里を一瞥してこう言った"),
            wakui.talk("あのさ、昨夜言い忘れてんだけど……お前、今日中に出てってくれる？"),
            airi.talk("え……"),
            _.do("愛里は思わず握った毛布を落としてしまう"),
            wakui.talk("俺もそろそろちゃんとした彼女作ろうと思ってさ。今度入ってきた織田詩乃ちゃん。ああいう真面目を具現化したような子がさ、やっぱ相応しいと思うんだよね"),
            airi.talk("「それ、アタシって、ちゃんとした彼女じゃなかったってこと？"),
            wakui.talk("彼女だと思ってたのか？"),
            airi.do("迷彩柄のボクサーパンツの上にクリーム色のスラックスを履きながら、祐介は続ける"),
            wakui.talk("お前さ、一番始めに体だけでも良いって言ってたじゃん"),
            airi.talk("それは祐介が抱いてみないと付き合えるかどうか分からないって言うから……"),
            wakui.talk("そんな簡単に男にやられる女が”ちゃんとした彼女”面できると思ってんのか？　何度も言ってるだろ。俺はバカな女駄目なんだって"),
            airi.do("ちらりと振り返った背中越しの祐介の二重の目が、冬の空気のように乾燥していて冷たい。それは時々愛里に向けられる目で、愛されていないんじゃないかという不安が胃袋から駆け上がりそうになる"),
            airi.do("首筋に感じた冷気が徐々に広がり始め、愛里は思わず両肩を抱き締めた"),
            _.do("だが祐介は再び背を向けてスタンドから紺色のダウンジャケットを取ると、"),
            wakui.talk("合鍵はポストに入れとけよ。もし忘れたらぶっ殺すから"),
            airi.do("それだけ言って玄関に向かう"),
            _.do("昨夜遅くまで二人分の体温を交換しあった布団の上で座り込んだまま、愛里はスチール製のドアが耳障りな音を立てて閉じたのを一人で聞いた"),
            stage=w.on_wakuiapart_int,
            day=w.in_airi_depart, time=w.at_morning,
            )


## episode
def ep_dumped(w: World):
    return w.episode("__episode__",
            ## NOTE
            sc_airi_wakeup(w),
            )
