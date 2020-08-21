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
　薄っすらと開いた目は車窓の外の対抗車のハイビームを幾つか確認する。
　もうすっかり暗くなってしまった。
　タクシーの運転手は原田が告げた駅前までやってきて、この先はどうするのか尋ねるので、もう少し先の路地に入ったところで下ろしてもらうように言って、再びシートに頭を預ける。
　編集長の岩槻の言葉は、最後にはただの激励になっていた。
　お酒が入って本当に言いたかったことがうまく伝えられたかどうか分からない。そもそも結城貴司は次の一冊を出して引退しますというその一言を受け入れてもらえればそれで充分なのだろうが、原田の言葉には猛反対する二人を押し切ってそれを認めさせるだけの力はない。
　結局なあなあのまま適当になだめられて、まずは問題の恋愛教室第四巻の初稿を提出することで何とか解放された。
「お客さん？」
　目を開けると、いきなり場所が駅前から移動している。
　五分くらいだろうか。寝てしまっていたようだ。
「ここで大丈夫です」
　そう答えて体を起こすと、コートのポケットの中に村瀬ナツコから貰ったタクシーチケットを探す。マンションの前までは行かないで下さい。そう言われていたけれど、自分みたいな人間がそこまでニュースバリューがあるとは思えなかった。
「どうも」
　支払いを終え、後部席から出る。
　夜風が上気した頬に冷たく、それでも足取りはふわふわとして何とも現実感が薄い。
　酒にはあまり強くないが、時々はこうして飲みたくもなる。頭を使わず、ただよく分からない流れに任せるまま歩いて、締め切りにもマスコミにも追われない、そんな落ち着いた時間を過ごせればそれが一番良いような気分になれる。
　百メートルほど歩いてマンションの前まで到着すると、一度スマートフォンを取り出して沖愛里から連絡が入っていないか確認をした。
　何もない。
　最近は以前ほど執拗に連絡をしてこなくなった。
　彼女の方も慣れてきたのだろう。最初の頃はあれこれとＬＩＮＥで質問をしてくるものだから、面倒になって全部まとめてレポートで出してくれとか言ってしまったこともある。頭の回転は悪くないし、気もよく利く。悪くない女性だとは思う。
　それなら何か問題があるのか。
　電子ロックを開け、エレベータに乗り込む。
　問題なら、山積みだ。
　原田は何より女性アレルギィなのだ。そんな人間がまともに女性を愛せる訳がない。だから今でも初恋の沖優里に対して想いを寄せ続けている。そうすればこれ以上誰も傷つけずに済む。
　アルコールが回っているからか、自問自答がいつもより高速で繰り返された。
　玄関のドアノブに鍵を差し込む。
　大きな音がして解錠されると、そっと覗き込むようにしてドアを開けた。だが中は暗いままだ。誰も帰っていない。
　一応「ただいま」と言ってみるが、返事もない。
　まだ愛里は帰っていないようだ。
　リビングまで歩いていき電気を点ける。
　明るくなった部屋は原田が出かけた時そのままで、夕食の準備をしてから再び出かけていった、というようなこともない。テーブルの上は飲み終えたコーヒーのカップが一つ、あるだけだ。
　再度スマートフォンを見て、やはり何も連絡がないことを確認すると、愛里宛てに先に寝ているとだけＬＩＮＥを送っておいて、コートをハンガーに引っ掛けるとそのまま寝室に向かった。
　もう瞼が重くて仕方ない。
　このまま倒れてしまえば気持ちよくなれるだろう。ただ明日の朝のことを考えて、何とか五歩ばかり踏ん張る。それでもこらえ切れずにシャツを脱ぐことはできず、顔面からベッドにダイブした。


　インタフォンだ。
　鳴っている。
　二度、三度と鳴らされる。
　荷物だろうか。
　昨夜はタクシーに乗ったところから記憶がなかった。
　それでも何とか寝室までは無事に辿り着いたようで、リビングに出ると明かりが点けたままになっていた。
「愛里君？」
　返事はない。
　仕方なく応答に出ると、マンションの一階で原田が出るのを待っていたのは、桜庭美樹だった。
            "),
            )

## episode
def ep_main(w: World):
    return w.episode("__episode__",
            ## NOTE
            sc_main(w),
            )