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
　　　　※


　別に愛里だってアルバイトの件をそのままにしておいて良い、とは思っていなかった。ただ店に出かけるのは気が引けたし、電話を掛けて小田川さんが出たら何て説明すれば良いか分からない。
　原田が村瀬ナツコとの打ち合わせに出かけてしまい、愛里は夕食に何を作ろうかぼんやりと考えながら、スマートフォンを操作していた。
　写真のデータを覗くと、そこには僅か三ヶ月の間に撮り溜めた涌井祐介とのツーショットが沢山残されていた。祐介は時に笑顔、時に不満げで、それに対して愛里だけはいつも幸せそうにキラキラと笑っていた。
　幸せだった。
　確かに涌井祐介は彼氏としてはあまり良い男ではなかったのかも知れない。けどそれでも愛里にとっては素敵な男性であり、彼氏だった。
　ただ、こんな思い出をいつまでも残しておく訳にもいかない。
　削除しよう。
　そう決めて指を置こうとした時だ。
　ＬＩＮＥの通知がある。涌井祐介からだった。
＞この前は悪かった。
　今更謝ってもらっても、愛里の中では既に終わらせた関係だった。
　それでもその謝罪を皮切りに次々と送られてくる誠実な文面に、愛里は目を逸らすことができず、ずっと読んでしまう。
＞明後日バイト入ってるだろ？
＞もし辞めるつもりなら言っておいてやるけど
　返事をしても、良いのかな。
　原田はさっさとアドレスやＩＤを削除するなり何なりして関わり合いにならないようにしておけ、と言っていたけれど、まだ手付かずのままだった。
　確かにアルバイトの件はどうにかしなければならないし、逆にこれは良い機会かも知れない。
　そう考えて「お願い」と返信をする。
　涌井はすぐ返事を送ってきて、
＞やっと答えてくれた
＞細かい手続きとかあるから
＞明日、直接会わないか？
　そこから続け様にメッセージが届く。
　愛里は時刻や場所の相談をしてから、最後にこう付け加えておいた。
＞言っとくけど、もう新しい人と付き合ってるから


　部屋の主である原田貴明は、結局夕方になっても戻ってこなかった。
　愛里はＬＩＮＥで少し出かけると送っておいて、彼から貰った合鍵を手にマンションを出る。一応夕食はテーブルの上にラップをして置いておいた。冬だし、暫くそのままでも大丈夫だろう。ただクリームシチューだけはレンジでいいから温めて食べてとメモを残しておいた。
　原田のグレィのダウンジャケットを借りてきたが、前にも一度借りたから文句は言われないだろう。愛里には一回りほど大きくて、着ていると何だか安心できる。
　駅には仕事帰りの人が沢山いて、それと逆行するように列を進んで改札を潜る。
　涌井祐介と同棲していた頃は仕事帰りにはいつも乗っていた電車だったが、数日訪れなかっただけでもう懐かしさを感じた。
　灰色のボディに朱色のラインが引かれた車両が金切り音をさせてホームに滑り込んでくる。
　ドアが開くと背中を押されるようにして乗り込むが、入り口付近に立っているだけで精一杯で、とても座るなんて無理だ。小柄な愛里はスーツの男性たちに潰されそうになりながらも、動き出した電車の揺れに耐えていた。
　彼氏がいない。
　その事実が不意に体を覆い、急に周りの男性たちの視線が恐くなった。


　古いアパートが立ち並ぶ住宅街の路地にやってくると、空はすっかり暗がりになっていた。
　愛里はその内の「ひらなみ荘」という汚れたスチールの看板が掛かる木造二階建ての前にやってくる。
　１０５号室の前まで行くと、息を呑んでからインタフォンを押した。ジイィ、と蝉のような音が鳴る。三ヶ月前に来た時には壊れていて、彼女が修理費を出して直してもらったのだ。
　一分ほどあってから、鍵が開けられた。
　ドアが開くと中からスラックス姿の涌井が姿を見せた。
「おう、愛里か。入れよ」
　酒臭い。
　目も少し虚ろで、飲み始めたといった雰囲気ではない。今日は仕事が休みだったのだろうか。
「アタシ、出直す」
「なんでだよ。入れって。バイト、辞めたいんだろ？」
「けど……」
　愛里が顔を顰めると、涌井は察したのか笑みを浮かべながら「大丈夫」と繰り返す。
　不安を感じたけれど、それでも言われるままに中に入った。
「それ、夕食？」
　靴を脱いで上がったところで、床の上にビールの空き缶とあたりめ、チーズ鱈なんかの袋が散らばっているのを見つける。一歩出した黒タイツ足の裏は、音を立てて柿の種を踏んでしまった。
「今日はちょっと、飲みたい気分だったからさ……愛里も飲むだろ」
「アタシはいい」
「そんなこと言うなよ」
　涌井はテーブルの上のビール缶に手を伸ばしたが、どうやら殆ど中身が残ってなかったらしい。
「わりぃ。売り切れだわ」
　そう言って反対にして缶を振る。滴がぼとぼとと落ちたが笑っているだけだ。
「ああ、もう」
　それが我慢できずに愛里はティッシュを取ってテーブルの上を拭う。
「なあ」
　その背中から、彼が腕を回してきた。
「何よ」
「やっぱ、お前がいないと俺駄目なんだわ」
　首筋に彼の唇が当たる。舌がぺろりと舐めて、そのまま吸い付いてきた。
「ちょっと。今日はそういうの」
「寂しかった。お前もそうだろ？」
　キスがいつもより優しい。
　胸の奥がざわついて、片付けようとした手を止めてしまった。
「少しだけだから……な」
「祐介……」
　振り返った愛里の唇に、アルコール臭まみれの祐介の唇が重ねられたが、愛里の目は彼の長い睫毛が濡れているのに気づいて、素直に目を閉じた。


　　　　※


　まさか村瀬ナツコの隣に編集長の岩槻までやってくるとは思わなかった。
　原田は二人から結城貴司がどれほど読者を待たせているのかということについて、滾滾と説教されてしまい、結局何とか短編小説を仕上げると約束をしてしまった。
　マンションに到着した時にはすっかり空腹になっていたが、それでも沖愛里から夕食を作っておいたとＬＩＮＥがあったので我慢して帰ってきたのだ。
　エレベータの浮遊力を感じて胃袋が引き締まる。
　玄関の鍵を開け、明かりを点けてリビングに向かった。
　まだ沖愛里は帰っておらず、テーブルの上には鶏の胸肉を香草で焼いたものに輪切りのゆで卵とトマトのサラダ、それにシチューが入った鍋が置かれていた。ハート型の便箋には「シチューはレンチンでいいから温めて食べること」と注意書きがされていたが、肝心のどこに出かけるのかについては何も記載がなかった。
　鍋くらい温められるよ。
　そう思ったが、上着を脱いで手を洗ってくると何だか面倒になってしまい、結局器に盛ったものをレンジで温めてしまった。
　テレビを点けると彼女が別の男に寝取られたというドラマをやっていて、結城貴司はそんな作品を書かないよなあ、なんて思いながら見ていた。
　十分ほどで食べ終えると、流し台に茶碗を重ねて置いておく。
　バスタブにお湯を張っている間に帰ってくるかと思ったが、風呂から上がっても彼女は戻ってこなかった。
　眠る前にメールとＬＩＮＥの確認をしたが、愛里からは何の連絡もなかった。
　その日は珍しく夢を見なかった。
　結局沖愛里は翌朝になっても原田のマンションには戻ってこなかった。
            "),
            )


## episode
def ep_main(w: World):
    return w.episode("__episode__",
            ## NOTE
            sc_main(w),
            )
