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


　モニタに映し出された原稿用紙のマス目を、次々と文字が埋めていく。
　原田は必死に言葉を絞り出し、それを小説という形に修正していた。
　いつもならサイドテーブルに置いた沖優里の指示が書かれたプロットの通りに場面や感情を文章に起こしていけば良い。けれど今はそれが一番頼りにしてはいけないものなのだ。
　自分で考えて、自分で物語の道筋を見つける。
　登場人物たちが何を考え、何を思い、何をしようとしているのか。
　それも彼らの裏側、いや、基盤になっているのは沖優里であり、沖愛里であり、原田貴明であり、優里と愛里の父親でもある。
　病気を知り、余命がそう長くないと判明した准教授の室尾は彼を先生と仰いできた美郷の前から忽然と姿を消してしまう。
　最愛の人と気づいた室尾のことを必死に探し歩くが、やがてボロボロになり、美郷は愛を探すことを諦めてしまう。
　そして、自分が求めていたものは愛ではなく、ただの恋だったのではないかと気づく。
　そのまま時は過ぎ、街ですれ違ってもそれと分からない二人にまで関係が薄まってしまった、というところで物語は終わりを迎える。
　それは優里が望む、自分の人生の終焉だった。
　生きていても、死んでいても、相手から切り離された関係性になってしまえば何も思われなくて良い。
　恋愛はそれの渦中にいる時だけ楽しめば良いのだと、彼女は言いたいのだ。
　けれど、原田はその考えが間違っていると、今明確に感じていた。
「でもどうすればいいんだよ！」
　室尾が姿を消し、それに彼女が気づいてからの行動が、どうしても優里のプロット通りにしか物語が進まない。何度も消しては書き直してを繰り返し、遂には全く新しい原稿ファイルにして書き出そうとしたが、今までに紡がれた物語の強制力に逆らうことが出来なかった。
　原田は再び真っ白になったモニタの原稿用紙を睨みつける。
　気づくとコーヒーカップが空になっていた。
　カップを手に立ち上がると、家の電話が鳴った。
　また投資の営業だろうか。それとも太陽光発電や保険、あるいは健康食品の方か。
　原田は受話器を持ち上げて、相手の第一声を聞く。
「先生！　生きてますか？」
　村瀬ナツコだった。
「何だよ、村瀬さんか。どうして固定電話になんて掛けてくるんです？」
「先生の携帯が繋がらないからですよ。それで愛里ちゃんから連絡受けて慌てて電話したんです」
　その言葉に子機を持ったまま自分のパソコンの前まで戻り、慌てて脇に置いたスマートフォンの画面を覗き込む。
「……すみません。電池が切れてました」
　大人しく充電器にセットすると、村瀬ナツコ経由で愛里からの伝言を聞く。
「えっと、何ですかそれ」
「だから、わたしにはよく分からないんですけど、彼女のお姉さんが探しものをしていたんじゃないかって」
　そんな話は聞いたことないし、そもそも村瀬自身が理解して話している訳じゃない。やはり直接愛里に尋ねた方が良いだろう。
　そこまで考えて村瀬ナツコに返事をしようとした時に、ふと思いついた。
「あの、村瀬さん」
「何ですか？」
「今からうち、来れます？」
「会社なんでちょっとお時間掛かりますけど、あれですか？　愛里ちゃんを連れていけってことですか？」
　彼女なりに気を回したのかも知れないが、それは原田が望むこととは違っていた。
「愛里君はそのまま病院に居てもらって下さい。それよりも、ちょっと頼みたいことがあるんです」
「改まって何です？　わたしは先生の申し出断ったことありませんよ」
　何度か原田一人で考えた企画書を突き返されたことがあったが、それは申し出ではなかったらしい。
「三人目の結城貴司になってもらえませんか？」
　言葉の意味が理解できなかったのか、理解した上での沈黙だったのか分からない。
　とにかく原田はその文言を二度、三度と繰り返したが、
「せ、先生……」
　電話の向こうで村瀬ナツコは震え始めて、何やらお経なようなブツブツとした喋り方であれやこれやと否定の言葉を投げかけてくる。
「勘違いしているようだけど、今恋愛教室の最終巻を書いているんですが」
「え！？」
　今度は耳が痛くなるほどの大声を出し、
「どういう風の吹き回しなんですか！　てか、絶対に書かないとかこの前言ってたじゃないですか！　何があったんですか！」
　喚き始めた。
「あの、話、聞く気あります？」
「……す、すみません」
「お願いしたいのは、今書いているものが結城貴司らしいかどうかを判断してもらいたいんですよ」
　次は再び沈黙だ。
「僕一人ではどんなに頑張ったところでもう一人の結城貴司、つまり沖優里の生み出したプロットを捻じ曲げて本当の恋愛教室のラストシーンなんて迎えられないんです。けど、ずっと結城貴司を傍で見続けてきた村瀬さんなら、僕が全然自信を持てないような展開や内容になっていたとしても、それが結城貴司だと判断できるんじゃないかって思うんです」
「先生」
「お願いします、村瀬さん」
　自分一人の力では絶対に沖優里は超えられない。
　それは最初から分かり切っていたことだった。
　それでも今死地に向かおうとしている彼女に対して原田が出来るたった一つのことは、本当の恋愛教室の最後を書き上げることしかない。それを沖優里に聞かせることこそが、原田の最後の彼女への告白だった。
「先生！　それは違います」
「何が違うんだ？　僕が書けば結城貴司になる可能性がある。それを村瀬さんは否定するのか？」
「違うんですよ。わたしは書き上げられたものが結城貴司かどうかなんて、一度だって考えたことないんです！」
　え……。
　今度はこちらが言葉を失う番だった。
「だって編集者である前に、一人の読者、それも一番最初に原稿が読める特別な読者なんですよ。それが結城貴司らしいかどうかなんて、考えて読む訳ないじゃないですか。だからお前は半人前なんだとか編集長からは言われますけど、でもわたしはいつも一人の読者としての普通の感覚を忘れたくないんです。先生の原稿が本になって届く先は、ファンの方かも知れないし、そうでない、全くの先生の名前を知らない通りすがりの人かも知れない。誰に届くか分からない。でも、その本を手に取って、開いてみて、面白いとか、感動したとか、何かしら生きる力が湧いてきたとか、切なかったとか……何かしら感じてもらいたいじゃないですか。そこには結城貴司かどうかなんて、小さな問題なんです。結城貴司だから大ヒットしているんじゃなくて、作品が人の心に届いたから人気になっているんだって、そう思いたいじゃないですか！」
　ありがとう。
　と、声に出したつもりだったけれど、原田のそれは涙に塗れていた。
「……ごめん。あの、その、そんなつもりじゃなかったんだけど、僕はとても基本的なことを忘れてしまっていたんだね」
「誰だって、沢山忘れ物をしながら生きてるんですよ。でもね、忘れているなら思い出せばいい。思い出せないなら、誰かに教えてもらえばいい」
　それは恋愛教室の第一巻で室尾が最後に美郷に言う台詞だった。
「ほらね、先生の言葉は、読んだ誰かにとってちゃんと宝物になっているんですから、もっと自信持って下さいよ」
「うん……そうだね。村瀬さん」
　まさか自分がかつて書いた言葉に泣かされるとは思わなかった。
「それじゃあ先生。これから支度して会社出ますね。先生が一番だと思う原稿を、とにかく仕上げて下さい。わたしだけじゃなく、世界中の読者が待ってますから」
　まるでエールのような言葉を送り、村瀬ナツコは電話を切った。
　受話器を元に戻すと、原田は改めて愛里が伝えようとしていた言葉の意味を考える。
　沖優里は、何を探していたのだろう。
　ひょっとするとそれは、原田が探し求めていたものと同じものなのかも知れない。
            "),
            )

## episode
def ep_main(w: World):
    return w.episode("__episode__",
            ## NOTE
            sc_main(w),
            )