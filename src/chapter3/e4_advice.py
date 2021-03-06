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
　気づくとパソコンの前に座ったまま、昼を過ぎていた。
　原田は思い切り腕を上げて伸びをしてから立ち上がると、スマートフォンを手に取って確認する。
　沖愛里からの返信はなかった。
　いきなり押しかけてきて同棲するような女なんだから突然目の前からいなくなっても不思議ではない。けれど、その印象は数日一緒に暮らすことで変わりつつもあったのだ。
　それなのに。
　食パンの袋を開けようとして、思い切り引き裂いてしまった。六枚切りのパンが屑を散らしながらテーブルの上にばら撒かれ、情けなく重なった。愛里がいれば、
「もうセンセは案外不器用なんだから」
　なんて言いながらも綺麗に片付けてくれることだろう。
　何を期待しているんだ。
　彼女がここにやってきてから何もかもの調子が狂っている。
　まともになったものと言えば、お腹の調子くらいなものだ。若い女の手料理だからもっと脂濃いものが多いと思っていたのに、彼女の嗜好なのか歴代の彼氏の好みなのかは分からないが、和風の上品な味付けのものが多く並べられた。
　オーブントースターに二枚入れて焼き上がるのを待つ間、残りパンをラップで包む。ジップロックなどがあればそれに入れておいた方が良いのだろうが、生憎とそんな便利なものは常備していない。
　冷蔵庫を覗いてみたが、ジャムもバターもマーガリンも切らしていた。
　戸棚を探るとふりかけと茶漬けや焼き飯、麻婆豆腐の素なんかが見つかったが、こんがりと焼き上がったトーストには、さて何を付ければ良いだろうか。
　贅沢は言わない。
　普通の苺のジャムで良いから、今ここにあればと切実に願った。


　結局レンジで温めた牛乳と何も付けない素焼きのトーストを無理矢理に押し込んで、マンションを出た。
　向かったのは喫茶ブラウンシュガーだ。
　別に沖愛里の動向が気になった訳じゃない。できれば美味しいパンケーキにありつきたい。そう考えただけだ。
　空はどんよりと灰色で満たされ、頬を切る風がそのうちに雪を運んでくるのではないかと思えた。
　そういえば彼女、原田のダウンジャケットを勝手に持ち出していた。あれは近所の外出に便利だから何かと使うことが多かったのだが、お陰で今は分厚いダークグリーンのコートを着込んでいる。
　路地を曲がると今日も営業中のブラウンシュガーが見えた。オープンテラスには流石に人がいなかったが、それでも見ている内にも客が入っていくので、中は案外席が埋まっているかも知れない。
　店の前で立ち止まり、ガラス戸越しに店内を覗き見る。
　女性の店員が二人、忙しそうに歩き回っていた。愛里や涌井祐介の姿は、どうやら見当たらない。二人とも休みなのだろうか。
　と、女性店員の一人が原田の視線に気づいて笑顔を向けてくる。
　どうしようか。
　一瞬考えたが、相席になるのも困ると考えて小さく手を振り、店の前から歩き去る。
　ラーメンでも食べて帰るか。
　胃袋のきりきりとした感覚が、いつまでも消えそうになかった。


　駅前の本屋を数軒ぶらついてから自宅マンションに戻ってきた。
　原田のようにあまり取材に出掛けず、基本的に家の中でじっとパソコンの前に座って仕事をしているような人間は、運動不足になりがちだ。主治医の高正からも日頃から心がけて出歩くようにと言われている。
　玄関のドアには鍵が掛けられたままで、やはり沖愛里は帰っていなかった。
　いや、そもそも「帰る」という表現がおかしいのだ。
　いつの間に自分は彼女をこの家の住人と認めてしまったのだろうか、と原田は熊のスリッパに足を通して苦笑した。
　また一人に戻っただけじゃないか。何も変わらない。
　パソコンの電源を入れて立ち上がるのを待つ間に、コーヒーを落とそうとキッチンに向かう。
　コーヒーメーカーのポットは底の方がもっと焦げ付いたような汚れがあったはずなのに、いつの間にか新品のように綺麗に掃除されている。
「あ、フィルター……」
　もう無くなるから買っておかないと、と思っていた紙フィルターも新しい物が補充されていた。
「何なんだよ」
　たった一週間ほどのことだ。
　それなのに沖愛里はこんなにも原田の生活圏を侵食していた。
　コーヒーメーカーをセットして、スウィッチを押す。それからパソコンの前に戻ると、脇のテーブルに置いた資料本の下敷きになっていた数枚のプリントアウトを取り出した。
　沖愛里に対する恋愛指示書。
　これは彼女に渡したものとは別の、原田貴明に対するものだった。
　そこには原田が沖愛里に対してどういう手順でどういう指導をすれば良いのか、事細かに書かれている。勿論これを作成したのは原田貴明ではない。もう一人の結城貴司だ。
　そうなのだ。
　結城貴司は原田貴明と、もう一人。別の人間との合作だった。
　いつも彼女に指示を仰ぎ、それに基づいて原田が文章を書き上げる。展開や重要な台詞、人物や舞台の設定、小道具などの詳細についても基本的に彼女の細かい指示書があり、それを補完する形で原田が資料を調べたりしてよりリアリティを追求している。
　原田だけでは結城貴司の小説は書き上げられないのだ。
「沖愛里が出て言った時には……か」
　その指示書には沖愛里が早々に原田のマンションから出ていく可能性についても検討されていた。
　特に注意書きとしてわざわざ赤字にされていた部分には、こうあった。
『沖愛里は涌井祐介に対して完全に気持ちがなくなったと口にしていても、仮に涌井祐介から再び優しい言葉などで同情を誘われた場合、寄りを戻す可能性が非常に高い』
　ひょっとすると涌井祐介から何らかの連絡があったのだろうか。
　愛里から聞いたところでは、新しくバイトで入った織田詩乃という女性が彼の好みらしく、今はその織田詩乃に熱を上げていると言っていた。ただまだ恋人にはなっておらず、その詩乃との関係が上手くいかずに沖愛里に戻ってくる、という可能性もあるのではないだろうか。
　原田は今一度、愛里にＬＩＮＥをする。
＞ひょっとして今涌井祐介と一緒なのか？
　その文面を送ってしまってから、自分が愛里の彼氏気取りに思えて激しく後悔した。
「僕は何をやっているんだ……」
　すっかりコーヒーを抽出し終えたポットから、湯気を上げる濃い茶色の液体をカップに注ぐ。僅かにミルクを加えてスプーンで混ぜ、それを一口飲もうとしたところで、テーブルの上のスマートフォンが鳴った。
　カップを手にしたまま、慌てて向かう。
　沖愛里からの返信だ。
＞うん
　たったニ文字だった。
　なのに原田の脳内では様々なことが想像され、狼狽する。
＞何をやってるんだ！
　そう怒鳴り声を送りつけてやりたくなる。
　だが一方で、沖愛里はそんな女だ、という理解もあり、一旦スマートフォンをテーブルに投げるように置いた。
            "),
            )

## episode
def ep_main(w: World):
    return w.episode("__episode__",
            ## NOTE
            sc_main(w),
            )
