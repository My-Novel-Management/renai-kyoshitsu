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


「愛里君？」
　原田は何度もそう呼びかけたけれど電話はすぐに切れてしまった。
　自分から掛け直してみたが通じない。ＬＩＮＥをしてみても今度は既読にすらならなくなった。
　完全に電源が切られてしまったようだ。
　そこに、インタフォンが鳴らされる。
「あの、桜庭です」
「あ、はい」
　慌てて玄関のオートロックを開けて部屋まで上がってきてもらったけれど、その桜庭美樹も何故か涙で目元がぐちゃぐちゃになっていた。
「どうしたんだ？」
「愛里が……涌井祐介に連れ去られたんです」
　どういうことなのだろう。
　今さっき電話していた彼女が泣いていたのは何か酷いことをされているからなのだろうか。
「すまないんだが、ちょっと詳しく事情を聞かせてもらえないかな」
　ティッシュを鼻頭に当てたままの桜庭美樹にそう言うと、
「その前にお水もらっても良いですか？」
　そう断ってから席を立った。


「それじゃあ最近の週刊誌騒動から愛里君が突然いなくなったことまで全部涌井祐介の仕業だったってこと？」
「分からないですけど、おそらくは」
　桜庭美樹の話はよくまとまっていて内容が理解し易かった。
　十分ほどで全てを話し終えると、ひとまず原田は警察に連絡をしようと固定電話の受話器を持ち上げる。
　だがそこで再びインタフォンが鳴らされた。
　桜庭美樹を見たが彼女は知らないと首を横に振る。
　原田は一旦受話器を置くと、インタフォンの応答に出た。
「はい……」
「やっと帰宅されたんですね。習志野です。今日はお話伺わせてもらえますよね？」
　声の主はこの前取材にやってきた記者だった。
「ひょっとして、わたしが付けられてたんですかね？」
　それは考えなかったが、タイミングからするとその可能性もあるだろう。
「すみません。今それどころじゃなくて」
　原田の正直な気持ちだ。
　今は自分のことで煩わされている場合じゃない。
　相手を無視し応答用の受話器を置こうとして、けれど唐突に目の前が閃いたような感覚に陥る。原稿を書いている時にも稀に経験するのだけれど、バラバラだったものが急に一つに集まって道が拓ける瞬間があるのだ。そうなるとずっと進まなかった原稿が嘘のようにすらすらと書き進むことができる。
「あの……お話してもいいですよ」
「え？」
　相手の驚きが手に取るように伝わってきたが、逆にチャンスだと思って続ける。
「交換条件です。まずはそちらの情報源である涌井祐介の連絡先を教えて下さい」
「原田さん？」
「それから警察のツテはありますか？　あるなら連絡して彼に少女が誘拐されていると通報して下さい」
　記者は続け様に原田が指図するものだから、話している内に「ちょっと待ってくれ！」と大きな声で遮ろうとする。だが構わずに原田は続ける。
「そして警察が向かっている間に、今から僕らと一緒に涌井祐介の勤務する店に同行して下さい。そこで彼と彼の店のやっていることを写真に収めて下さい。彼、あるいは彼の関係者は麻薬をやっています」
「あんた……」
「その代わりに結城貴司の謎と、原田貴明個人の情報については全てあなただけに提供します。悪い話じゃないでしょう？」
「先生？」
　桜庭美樹が心配そうに声を掛けたが、それを手で制して原田はもうひと押しする。
「まだ世間の誰も知らない、本当の結城貴司の秘密があるんです」
「……分かった。それで、まず何からすればいいんだ？」
　その返事に一瞬安堵したものの、原田は自分の頭の中で順番を整理し直すと、改めて「習志野順太」と名乗った記者に対して警察に連絡を取るように言った。
「桜庭さん」
「はい？」
「君は一旦マンションに帰って、ご飯でも食べて落ち着いて連絡を待っててもらいたい。愛里君を助け出したら、君のところで暫く預かってもらうかも知れないから」
「先生のところじゃないんですか？」
　それに対して原田は頷くことはせずにただ寂しげな微笑を返すに留めた。


　各所への連絡を終えた原田は、桜庭美樹と共にマンション一階に下りると、玄関前で待っていた習志野と合流して、美樹とは別れた。
　呼んでおいたタクシーに乗り込み、習志野の指示で発車する。
「その誘拐された女ってのは、あんたの彼女より大切なのか？」
　涌井祐介に何と吹き込まれたのかは知らないが、未だに桜庭美樹が結城貴司の彼女と認識されていることにやや戸惑う。
「本当に彼女はただの知人です。どうせならつい先日まで同棲していた沖愛里の方を彼女にしてあげれば良かったのに」
「沖愛里は涌井祐介の彼女なんですよね？　二股だったってことですか？」
　メモ帳ではなくボイスレコーダーを取り出した習志野を制してそれを仕舞わせると、原田は続ける。
「全部終わってからちゃんと説明しますよ。けど、今はもう沖愛里は涌井祐介の彼女ではありません。彼女は被害者です。そして涌井祐介は加害者であり、犯罪者です。だからあなたに通報してもらった訳ですから」
　分からない。
　そうぼやいて頭を振る。
　どうやら習志野という記者は一度信じてしまったことを頭から追い出すのが苦手なようで、その後何度も桜庭美樹のことを原田の彼女と言い、沖愛里のことを涌井の彼女と呼んだ。
　タクシーは新宿方面に向かっていたが、混雑する道路がその歩みを鈍くする。
　遠くではパトカーのサイレンが鳴り響き、そこに途中から救急車のサイレンも混ざり始めた。
　夜がどんどん更けていく。
　車窓から眺めやると、ビルの明かりがまだ幾つも煌々と照らされていて、都市は眠ることを忘れてしまっているのだな、と原田は感じた。
　新宿駅前の交差点を抜けた辺りでのことだった。
　突然原田のスマートフォンが鳴る。
　モニタには『織田病院』とある。原田が通院している病院であると同時に、彼女の姉である沖優里が入院しているらしい場所だ。
「あ、原田君か。今家か？」
　相手は原田の担当医師である内科医の高正だった。
「外なんですけど……何でしょう」
　高正が直に連絡を寄越すことは珍しいどころか記憶にある範囲では初めてのことだった。
「それが、その……沖優里のことで」
「何ですか？」
「急に容態が悪くなってね。ついさっき集中治療室に運ばれた。ご家族の方には電話を入れたのだけれど妹さんに連絡がつかなくてね。ひょっとしたらと思って掛けてみたんだ」
　タイミングが悪い。
　そう思ったが、すぐに自分の中で沖優里と沖愛里の二人を天秤に掛けていたことに気づき、その考えを振り払った。
「実はちょっと立て込んでいて、今その妹さんの方を救出に向かっているところなんです」
「救出？　どういうことだ？」
「詳しく話している余裕はないんですが、端的に誘拐事件です」
　おお。参ったな。
　そんな呟きが漏れ聞こえたが、原田はひとまず落ち着いたら病院に連絡を入れると約束して、高正からの電話を切った。
「相手は誰なんです？」
「えっとね……結城貴司、の知り合いかな」
「あなたが結城貴司なんですよね？」
　習志野は睨むように目元を細くするが、信号が切り替わって動き出したタクシーに揺られてその表情が緩んだ。
「結城貴司には本物がいるんですよ……僕はね、偽物の方なんです」
「何だって！？」
　大きな声を出した習志野は驚きで頭を窓ガラスにぶつけたが、”偽物”と自分の口から出たことへの驚きは、原田自身の方がずっと大きかった。
　もう一人の結城貴司。
　そう説明するだけで良かったのに、何故わざわざそんな言い方をしたのか。
　きっと愛里がこの場にいれば原田のことを怒ってくれただろう。
　それとも沖優里であれば、もっと辛辣に罵ってしまっただろうか。
　愛里のことを考えなければいけないのに、心の半分以上は沖優里の容態が気がかりで仕方なかった。
「なんて酷い男なんだ……」
　思わずぼやいてしまった言葉を、習志野は咄嗟に録音する。
「あ、いや……すみません」
「いいんですよ。本当に、酷い男なんですから」
            "),
            )


## episode
def ep_main(w: World):
    return w.episode("__episode__",
            ## NOTE
            sc_main(w),
            )