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
　原田貴明はパソコンのモニタを見ながら、日付が変わって今日から四月なのだとぼんやり思った。
　部屋はまだ衣替えも全然済まされてなくて、冬物のコートがハンガーにぶら下がったままで、少し冷えるからと今もタートルネックのセーターを着ているくらいだ。
　カップを手に取りコーヒーを飲もうとして、既に空になっていることに気づいた。
　キッチンの方に視線を向けたが、そこに沖愛里はいない。
　と、メール通知のポップアップがあり、開いて見ると村瀬ナツコからだった。
　コーヒーを湧かしてからにしようか、と考えたが、こんな時間にわざわざ送ってきたくらいだから緊急の用件かも知れないと、中身に目を通す。
「何だって……」
　それは恋愛教室第四巻の五度目の直し原稿についてのものだったのだが、わざわざ病院に行って沖優里に見せて許可を得てきたと書かれていた。
「真面目なのはいいんだけど……」
　メールで済ませれば良いのに、どうも村瀬ナツコは最近原稿確認と称して沖優里の見舞いに行くことが増えた。
　高正医師などの尽力により心停止から回復した沖優里は、その後順調に体調が戻り、今は通常の入院病棟へと移って療養している。もう暫くしたら体力を戻す為のリハビリに取り組むことになっているそうだが、心臓が弱っていることから人工心臓を取り付けることも検討しているらしい。
　今まではそういった提案にも乗り気でなかった彼女がどうして気持ち変わりをしたのかは分からないが、村瀬ナツコの話では高正誠司のＬＩＮＥのＩＤを手に入れてとても喜んでいたそうだ。
　修正が必要な箇所は幾つかの表現と、優木美郷が見つけて読み込む室尾の研究論文の内容についての手直しだった。論文の元原稿は優里が書いたものから部分的に抜粋して掲載することになりそうだと、村瀬ナツコからのメールには書かれていた。
　結局最後まで結城貴司は沖優里におんぶに抱っこの状態で、その作家の経歴にエンドマークを迎えることになりそうだ。
　席を立ち、キッチンに向かう。
　カップを置いて、棚からコーヒーの粉を取ろうとしたところで、インタフォンが鳴らされた。
　出てみると、沖愛里と桜庭美樹だった。
　マンションの入り口の電子ロックを解除して上がってくるように言うと、一分ほどで再びインタフォンが鳴る。
　コーヒーメーカーをセットしてスッチを入れると、原田は二人を迎える為に玄関へと向かう。
　鍵を開けてやると、楽しげな声と共にドアが開けられ、そこにはナースのコスプレをした愛里と美樹が立っていた。
「部屋を間違えてない？」
　そう言ってドアを閉めてしまおうとすると、
「センセ！　待って待って！」
　慌てて愛里が足を挟む。
　どう見ても仕事用のものではなく、男女で遊ぶ為の衣装にしか思えないその丈が短い上にスリットまで入ったピンク色の制服から、彼女の太腿が露出していた。
「一体何のつもりだ？」
「美樹が恥ずかしいから早く中に入れてよ」
「愛里君は恥ずかしくないの？」
「センセに見てもらう為だし」
　彼女の笑顔には勝てないな。
　そう感じて二人を中に入れると、ドアをロックする。
　リビングに駆けていくと、桜庭美樹は必死に原田に頭を下げて謝った。
「だって愛里がどうしても着なきゃ許さないって言うから」
「将来立派な看護師になるっていう決意表明なんだから、友達として付き合ってくれたっていいじゃん？」
　ゴボゴボと音をさせてキッチンでコーヒーが落とし終えたのが分かったが、それに気づいた愛里は慣れた様子でコーヒーメーカーに向かっていく。
「将来？　どういうこと？」
　残った美樹に尋ねると、どうもこの春から看護の専門学校に入ったというのだ。全くの初耳であることと、彼女と看護師という組み合わせに驚いたものの、意外と似合っているかもな、とコーヒーを運んできたエロい格好のナースを見て思った。
　その姿はどう見ても風俗店のそれだが、彼女の気配りの良さやてきぱきと物事をこなすところは、看護師に向いているかも知れない、という原田の真面目な観察結果だ。
「それでセンセ。原稿はもう出来たの？」
「次の直しでたぶん最後だと思うよ。そうしたら、結城貴司は終了だ」
　その言葉に、桜庭美樹が泣きそうになる。
「ほんとに結城貴司辞めちゃうんですか？」
「そうだね。優里さんはもう続ける意志がないらしいし、彼女なしじゃ結城貴司じゃないからね。次からは原田貴明としてイチから……いやゼロからかな、再出発だ」
　そう。
　結城貴司は、恋愛教室の第四巻の出版を以って、一旦終わりを迎える。
　編集長の岩槻からは同じ名前のまま活動する道を何とか模索するよう要請されたが、村瀬ナツコが食い下がって原田と沖優里の意志が尊重される形となった。
　それが決まった時、原田は自分が思いの外すっきりとした気持ちだったことに驚いた。
　それでもよく考えてみれば、恋愛教室というとても長い長い一つの恋愛を終えた後の気分は、こんな風に晴れ晴れとしたものかも知れない。
　恋が終わる時は悲しいもの、というのは当然かも知れないが、それは失ったと感じたことの瞬間的な悲しみであって、永遠には続かない。いつかは自分の中でどうにかこうにか整理が付いて、気持ちが決着したと感じられるようになった時には、こんな風に意外とすっきりとしているものだったりするのだろう。
　沖愛里は毎日ではないが、それでもこうして時々桜庭美樹と二人で遊びにやってくる。
　本人はまだ原田のことを諦めていないと言うが、それでも学校が始まれば今ほどの頻度ではやってこられなくなるだろう。
　桜庭美樹はこの秋からの留学を考えているらしいが、本気で小説を勉強して将来は第二の結城貴司を名乗るのだと、妙に息巻いている。
　沖優里は村瀬ナツコ経由で入ってくる様々な情報からすると、彼女なりに自分の人生というものについて真面目に考え始めているのかも知れないと感じられた。
　原田は自分自身が作家として本当に通用するのかどうか、その第一作の原稿を村瀬ナツコに渡すことになっているが、未だにプロットすら作れていなかった。前途多難とはこのことだろうが、それでも気持ちは沈んだりしていない。
　駄目なら、また次の恋を探せばいい。
　そんな風に考えられるようになったからだ。
　それは変化だろうか。
　それとも諦めだろうか。
　結城貴司なら、きっとこんな風に答えるだろう。
『人間はその人生で何度か恋をする。その中で一番最初に恋をするのは誰だと思う？　それは誰もが知っていて、誰もにとって一番身近な人物だよ。そう。自分自身。人はいつも自分に恋をして、自分に失恋して、そしてまた次の自分に恋をしながら、本当の恋愛を求めて彷徨い歩くものなんだ』
　そして、君と私の恋愛教室は、君の中でまた続いていく。

（了）
            "),
            )

## episode
def ep_main(w: World):
    return w.episode("__episode__",
            ## NOTE
            sc_main(w),
            )