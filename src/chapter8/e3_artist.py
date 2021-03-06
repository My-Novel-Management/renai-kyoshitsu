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
def sc_main(w: World):
    hara, airi, yuri = W(w.harada), W(w.airi), W(w.yuri)
    inside, outside = W(w.inside), W(w.outside)
    wakui = W(w.wakui)
    return w.scene("main",
            hara.do("
　東京駅には原田の叔父の方が早くに到着していた。
　既に十一時を過ぎていて、最近気に入っているという蕎麦屋にいるとメールが入っていることに気づいたのは、新幹線を降りてしまってからだった。
　原田はホームで桜庭美樹と村瀬ナツコの二人と別れ、一人叔父の許に急いだ。
　ランチタイムを前にした駅構内の店舗はどこも混み始めていて、
「食べていかないのか？　うまいぞ」
　店を覗き込んだ原田にそう言ってくれたが、ゆっくりできそうになかったし、何より対応してくれた女性店員が彼の顔を見るなり驚いていたので、騒ぎになる前にと早々に叔父を引き連れて退散した。
「それで、容態の方はどうなんですか」
　中央線のホームへと足早に向かいながら、叔父に尋ねる。
「詳しいことは分からないんだが、今朝早くに施設から連絡を貰ってね。いつもの女性職員さんが頻りに倒れて病院に運ばれたけど大丈夫ですって繰り返すもんだから、逆に心配になっちまったよ。命どうこうって話ではないみたいなんだけど、還暦超えたら人間いつ何があってもおかしくないだろうしな」
　確か叔父も来年あたり六十になるはずだ。明日は我が身の心境なのかも知れない。
「病院には施設の方が付き添ってくれたりしてるんですか？」
「いや、それもよく分からん。何しろこっちも気が動転してたからね」
　細かいことはあまり考えないようにする。叔父は昔からそういう人種だ。
　原田は色々と聞き出したい欲求を仕舞い込み、スマートフォンを取り出して画面に視線を落とす。村瀬ナツコと桜庭美樹からそれぞれに心配の声がＬＩＮＥされていたが、それ以外の通知は何一つなかった。


　更に一時間ほどを費やして八王子まで行くと、タクシーに乗って施設の人から聞いた父親の入院先へと向かった。
　命に別状はない。
　その一言を再度施設の職員から聞いて、叔父の表情はいつもの見舞いとそう変わらないものになっていたが、原田の方は想像の外から降って湧いた父親の入院話への動揺に、何とも居心地の悪い思いが継続していた。
「ところで貴明君」
　あと五分ほどで着きますよ。
　そう運転手に言われた時だった。
「何ですか」
「いや、何でもない。忘れてくれ」
「はあ」
　要領を得ない。
　叔父は車窓から外を眺めやり、何度か溜息をついただけで、それ以降は病院に到着するまで何も喋らなかった。


　受付で病室の場所を教えてもらい、二階に上がった。
　普段自分が通院してある程度慣れているつもりだったが、場所が変われば勝手も変わってくるものだ。原田は戸惑いがちに案内板を見ながら、入院棟であるＢ館へと向かう。
　その後ろから叔父はついて歩いてくるが、すれ違う若い看護師たちが楽しげに喋るのにいちいち目を取られていた。
「奥から二番目の病室ですね」
「ああ」
　車椅子や点滴を持って歩く患者をやり過ごして部屋に近づいていくと、見るまでもなく自分の肉親が元気でいる様子が伝わってきた。
「只で描いてもらえると思うな！　それに俺は裸しか描かんぞ。さあ、そこの看護師。さっさとその桜色のものを取れ！」
「何言ってるんですか。まだ寝てて下さいって先生からも言われたでしょ？」
　六人部屋の一番窓際のベッドの上で、浅黒い肌の男が二人の看護師を相手に騒いでいた。
　それを見るなり、原田は自分の目の前を覆う。
「元気そうで良かったじゃないか。なあ貴明君」
「そうですね」
　感情の籠らない声を叔父に返すと、気分が悪くなったので一度席を外してから改めて父親に会おうと考えた。けれどその原田の目がもう一度父親を見た時、そのやせ細った首筋に光るものが流れるのを目撃してしまった。
　すぐに表情を顰め、起こしていた上半身を折り畳んで蹲ってしまう。
「おい……」
　叔父は驚いていたが、父親を見ていた看護師の一人は声を掛けながら肩に手を掛け、もう一人が駆け足で廊下に出ていく。慣れた様子だが、容態の急変は彼女たちにとっても一大事だろう。
「俺はまだ死なんぞ！　筆を持ってこい！」
　だがその看護師の腕を払い退けて体を起こすと、彼女の胸にすがりついて何度も「絵を描かせろ」と言う。その声には先程まで笑って見物していた同室の入院患者を黙らせるだけでなく、騒がしかった通路側の人間たちまでぴたりと黙らせてしまう狂気があった。
「兄さん。病人なんだから大人しくしててくれよ」
　ベッドまで歩いて近づいた叔父が怒り気味にそう言ったが、父はその姿に気づくなり、
「佳寿。筆だ。筆をひと揃い買ってこい。それに晴美を呼べ。やっぱあいつじゃなきゃ、描く気がせん」
　崩れた笑みで彼にそう言った。
「兄さん……」
　叔父はそう呟くのが精一杯で、原田の母が既に亡くなっていることも、もう画家として価値が無くなってしまっていることも、何一つ彼に返せないまま、その場に突っ立っていた。
　原田はその様子を病室の入り口でただ黙って見つめていたが、自分の呼吸が止まっていたことに気づいて咽ると、悪寒を催して、慌ててトイレを探して駆け出した。


　結局原因は分からないが、本人によると足元がおぼつかなくて施設のベッドから落ちて暫く動けなくなったらしい。担当した内科医は頭部のＭＲＩの撮影がまだだが貧血が原因の転倒を疑っていると言っていた。
　精密検査であと二日は入院が続くというので、叔父は近所にホテルを探してそこで暫く様子を見ると言っていた。
　駅前で叔父と別れ、原田が自宅マンションに戻れたのはすっかり辺りが暗くなった夜の九時前のことだった。
　帰りの車内で村瀬ナツコと桜庭美樹にはそれぞれ一大事ではなかったことと、自分は自宅に帰ることをＬＩＮＥしておいたが、二人とも安心したという返事が入っていた。
　玄関のドアを開け、五日ぶりの自宅の臭いを嗅ぐ。
　沖愛里は相変わらず帰ってこず、ＬＩＮＥに送っておいたものへの返事もない。だがよく見ると既読になっていた。今までは既読すら付かず、携帯電話をどこかに忘れてしまっているのかな等と思っていたくらいだ。
　原田はリビングまでやってきて電気を付けると、ダウンジャケットを脱がずにそのまま腰を下ろしてスマートフォンを操作する。
　ここ数日あったことと、何か自分に対して不満があるのなら言って欲しいこと、それから、まだ恋愛教室の途中であること等をつらつらと書いて、彼女に送りつけた。
　一分ほど経過してから確認すると、やはりそれも既読になっている。
　けれど返事は来ない。
　どうしてなんだ。
　そんな苛立ちに舌打ちが出る。
「もう……何でこんな気分になるんだ」
　スマートフォンを置いてそのまま背中から寝転ぶと、大きく腕を開いて天井を仰ぎ見た。
　恋。
　そんな文字が脳裏を過ったが、馬鹿馬鹿しいと一蹴する。
　だがそんな原田を嘲笑うかのようにスマートフォンが音を立てて震え、その画面には『沖愛里』という名前と電話の印が表示された。
「え？」
　意味も分からないまま、手を伸ばす。
　通話が始まると、いきなり彼女の泣き声が原田の鼓膜に響いた。
            "),
            )

## episode
def ep_main(w: World):
    return w.episode("__episode__",
            ## NOTE
            sc_main(w),
            )
