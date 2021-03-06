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
「アタシは沖愛里。愛に里って書いて、愛里だよ。宜しく」
　そう言って目の前の露出の多い女は、自分の右手を原田貴明の前に差し出した。けれど彼はそれを目を細めて見ながら、握り返すということができずにいた。
「ん？　ねえ、握手。してくれないの？」
　大きな瞳を何度か瞬かせ、沖愛里は原田を覗き込む。膝頭が丸見えな丈の短いスカートからその肉付きの良い太腿がよく見えたけれど、原田はそれが見たくて俯いた訳じゃない。
「ねえ」
　声が不機嫌になる。
「ねえってば」
　原田は隣に立つ高正誠司の顔を、助けを求めるように見やる。白衣の間から覗くブルーのストライプ柄のタイは年季が入り、随分と色褪せて見えた。
「まあまあ。彼も病み上がりで疲れているんだ。それにちょっと訳ありでね。あまり他人と接触することが得意ではないんだ」
「そうなの？　ごめんなさい」
　素直に謝った彼女は、突然はっとして「あ」と声に出す。
「もしかして、センセが倒れたのって、アタシの所為？」
「気にしなくていい。僕が気をつけるべきことだ」
「そんなことない」
　そう言って、彼女は原田の前に進み出る。勢いで、そのまま自分に抱きついてくるんじゃないかと思ったが、五十センチくらいまでで、何とか彼女は踏みとどまってくれた。
「駄目なことはちゃんと駄目って言ってよね。アタシ、そういうの、ちゃんと守るタイプだから」
「ああ、わかった。けど……あまり近づかないでくれ」
「ええー。それじゃあ恋愛できない」
　まるで駄々っ子だ。唇を尖らせてふくれて見せる。意識してやってるのか自然とそうなるのかは分からないが、こういうのを「かわいい」と感じる男性も一定数いるだろう。原田はこの手の仕草をする女性を「面倒そうだ」としか思わなかった。
「村瀬さん」
　赤縁の眼鏡を外して拭いていた彼女が、返事をして慌ててそれを掛け直す。
「彼女をタクシーで家まで送ってあげてもらえないかな」
「なんで？」
　そう言ったのは愛里だ。
「いや、救急車でここまで来てもらったんだから、送っていかないと悪いだろう？」
「センセが送ってくれればいいのに」
　返事を期待する目を向けられたが、原田はそれを無視して村瀬ナツコに「頼む」と口だけ動かして伝えた。
「それじゃあ、先生。また後で連絡します。じゃあ、行きましょうか……えーと」
「愛里」
「愛里ちゃん」
　村瀬ナツコは先に歩き出したが、愛里はそれを追いかけようとして立ち止まり、
「ちょっとスマホ貸して」
　と、原田のシャツの胸ポケットから飛び出ていたそれを強引に取り出す。
　高正は苦笑してそれを見たが、返せと口に出す前に彼女は勝手に何やら登録を済ませてしまった。
「アタシのＬＩＮＥのＩＤとメールアドレス、それに電話番号も入れてあるから、あとで確認のＬＩＮＥしとくね。じゃ、センセ」
　ほい、と宙に投げて、手を振って行ってしまう。
　危なく落としかけたが、何とか両手でスマートフォンを受け取ると、そこに登録されてしまった彼女のアドレスなどを確認する。
「どう思います」
「可愛い子じゃないか。君にはああいうタイプの方が合ってるかも知れないよ」
　高正は笑いを噛み殺しながら答えたが、原田はそれに対して首を横に何度も振る。
「そうじゃなくて、僕が無事でいられるかどうかって話です。そもそも恋愛を教えるなんて、女性アレルギィの僕には到底無理な命題なんですよ」
「そんなことはないだろう。君はベストセラー恋愛作家の結城貴司じゃないか」
　自分は結城貴司じゃない。
　そう口に出そうとしたが、高正に言っても仕方ないと思って止めておく。
「そもそも恋愛というのはね、誰でもできるけれど何一つ正解がない。そういう人生の難問の一つなんですよ」
　手にしたスマートフォンは短く震え、ＬＩＮＥの通知を告げる。早速愛里からだ。思わず指が触れて画面に展開されたメッセージを視界に入れて、原田は眉根を寄せて首を横にした。

＞センセって彼女いないんだ？　ヨカッタ。ナツコさんから聞いたの。
            "),
            )

## episode
def ep_main(w: World):
    return w.episode("__episode__",
            ## NOTE
            sc_main(w),
            )
