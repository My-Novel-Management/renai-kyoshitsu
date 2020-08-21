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


「ちょっとぉ、どこまで行くの？」
　原田は周囲を確認して、人気がなくなったことに溜息をついた。
「ねえってば！」
「あのな。もう忘れたのか？」
　既に喫茶ブラウンシュガーからは五分以上歩いている。住宅街の路地をバイクが一台通り抜けただけだ。
「アタシさ、まだバイト中なんだけど？」
　愛里は眉根を寄せ、その大きな瞳を原田に向けた。
「いやだからさ……僕は原田貴明であって結城貴司じゃない。外で先生と呼ぶのはよしてくれないか？」
「別にセンセはセンセだからいいじゃん。それよりなんでアタシのこと助けてくれなかったの？　さっき見たでしょ？　祐介にアタシ、振られそうなの。捨てられそうなのよ。どうにかならないの？　あの小説みたく、魔法の言葉とかでさ」
「小説は魔法の言葉なんて使っていない」
「けど……アタシはあれを読んで自分が祐介と同棲した三ヶ月の間、ちゃんと恋愛をしてたんだって思えたよ？　喜んで、悩んで、苦しんで、一緒に笑って、抱き合って、温もりを確かめ合う。同じ空気を吸うことが恋愛だって書いてたじゃん！」
　彼女は大声でそう言い切ると、その目に溢れそうなほどの涙を湛えていた。
　原田はハンカチを取り出す。
　それを何も言わずに受け取ると、愛里は目元に押し付けた。
「化粧落ちるぞ」
「別にアンタは困らないでしょ。それに顔なんていくらでも作り直せる。祐介はね、目が大きくて唇がぼてっとした子が好きなんだ。だから睫毛もたっぷり乗せて、口紅も大きめに塗るの」
　レモングリーンのハンカチは、彼女のシャドウがべったりと着いて黒ずんでしまっていた。
「ところでさ、昨日のアレなんだけど」
「何？」
「まだ君、あのバイト先の男に未練があるんだろう？」
　鼻を啜りながら愛里は頷く。
「だったら、僕が教えられることは何もないよ」
「はぁ！？」
「だってそうだろ？　恋愛っていうのは当人たちの問題で、他人がどうこう言ってみたところでどうにもならないんだよ。アドバイスなんてするだけ無駄。人の恋路を邪魔する奴は馬に蹴られて死んじまえ、という都々逸があってね」
　言葉の意味が分からないのだろう。ただぽかんと開けていた口は徐々に閉じていき、やがて彼女の顔色が変わった。
「ちょっと！　恋愛教室してくれるって言ったじゃん！　恋の苦しみからアタシを助けてくれるんじゃなかったの！？」
「だから、君はまだ恋愛中なんだろ？　だったらその恋を最後までやり切ればいいじゃないか。良い経験になるよ、振られたとしても」
　そう言った原田に愛里は顔を近づける。明らかに怒っている。
「ひっど。あんたそれでも恋愛小説家なの？」
　自分を睨みつける彼女の目を見て、ここは悪役に徹しようと原田は腕組みをした。
「作家なんてね、所詮は登場人物たちを不幸にして楽しんでいる下賤な種族なんだよ。他人の不幸ほどみんな読みたがるからね。で、最後の最後だけちょこっと幸せっぽい雰囲気で終わらせておけば、みんな泣いてくれる。こんなに楽な仕事はないよ」
　白塗りをした上からでも分かる彼女の目元の赤みだった。涙が膨らんでいき、すっと落ちた。
「分かっただろ。こんな僕から恋愛を学ぼうとしたって、また君が泣くだけさ。だからさっさとバイトに戻りなさい」
　これで解放される。
　そう思った時だった。
「あー！　先生！」
　振り返らなくても分かる。
　見れば大声で何度も「先生」と口にしながら路上を駆けてくる。目立つ大きな白い提げ鞄が派手に揺れていたが、村瀬ナツコは気にせずスニーカーでやってきた。
「愛里ちゃんもいた。良かったわ」
「ナツコさん、どうしたんですか？」
　ハンカチで目元を拭いながら愛里が尋ねる。既に下の名前で呼び合う仲らしい。
「ほら、昨日約束したじゃないですか。先生が愛里ちゃんに恋愛教室をする代わりに、原稿の締め切りを一月延ばすって。あれ、何とか編集長に土下座して承諾もらいましたよ。ただ」
　その「ただ」という文言に、原田は村瀬を睨みつける。
「その、ですね。愛里ちゃんにどういう風に恋愛を教えたとか、相手の人とはどうなったとか、そういう諸々をですね、何とかこうエッセィとか短編小説にしてもらってですね……」
「おい、村瀬さん。それって結局僕の仕事が増えただけじゃないのか？」
「まあ、そうなりますよね」
　てへ。と舌を出して右拳を自分の頭の上に載せる。
　きっと愛里みたいな女性がしていればそれなりに可愛いと思う男性もいるのだろうが、村瀬ナツコのそれは原田への追い打ちにしか見えなかった。
「だからさ、今僕はこの子の約束を断ったところなんだ」
　その村瀬ナツコを見て、何度も頷くようにして原田は言った。
「それじゃあ先生原稿下さい」
　しかし彼女は引き下がる様子はなく、両方の掌を見せて笑いかける。
「約束を守らないなら原稿の締め切りだって延ばせません。そうでしょう？　そもそもがですよ、先生これで原稿の締め切り何ヶ月引き延ばしてると思ってるんです？」
　ほんの半年だ、と言おうとしたが、冗談が通じるような目をどちらもしていなかった。
　原田は諦めて、
「わかった」
　と嘆息と共に漏らす。
　急に空腹だったことを思い出したが、肝心のパンケーキ屋には流石にもう戻れない。コンビニでいいか、と思い直した原田の背中で、愛里は電話を掛けているところだった。
「はい。ごめんなさい。今日は体調不良で早退します……」


　翌朝。
　パソコンの前で唸っていた原田は、突然のインタフォンに襲われた。まだ八時にもなっていない。ネットで何か注文していただろうかと思い、応対に立ったが、
「え……」
「愛里だよ。いれて」
　スピーカーから聞こえてきたのは沖愛里の声だった。可愛らしい声で「いれて」と連呼する。
「入れてくれなきゃここでセンセが結城貴司だって叫ぶから」
「分かった分かった。今すぐ入れ」
　一階玄関の電子ロックを外してやると、それからちょうど一分で表のドアの前に彼女が姿を現した。その手には大きなスポーツバッグを持っていて、「今から旅行に行くのか」と言ってやりたかったが、そんな話ではないことはすぐに分かったので止めておいた。
「今日からお世話になります」
　まるでメイド服を意識したような、肩に大きなピンクのフリルが付いたワンピース姿で、愛里は会釈をした。
            "),
            )


## episode
def ep_main(w: World):
    return w.episode("__episode__",
            ## NOTE
            sc_main(w),
            )