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
「お昼を食べながらでも良いかな？」
　内科の診察室に乗り込んでいったところ、白衣姿の高正医師は愛里の顔を見るなりそう言った。姉の紹介だと口にする前に全部理解していたかのような返答に、ひょっとすると同じ種類の人間なのかと邪推したが、どうやら事前に姉の優里から連絡を貰っていたらしい。
　愛里は大人しく電話番号を教えると、一階に入っているチェリーズコーヒーで時間を潰すことにした。
　高正誠司は耳に掛かる髪に僅かに白いものが混ざっていたが、スーツかジャケットのようなしっかりした仕立てのものを着ていれば愛里の同世代の女性からも人気が出そうな、雰囲気の良いおじさまだった。
　姉が人物を「素敵」と評することは稀で、どんな男性なのだろうと少しだけ期待したのだけれど、愛里にとっては原田の方がずっと魅力的に思えた。大人の余裕、というのだろうか。そんな雰囲気を纏っている男性には、少し苦手意識がある。
　頼んだミルクチャイは仄かにスパイスの香りがして、冷たくなっていた体を温めてくれた。
　そのシナモンの匂いの所為だろうか。
　姉が”あの人”と呼ぶ、かつての愛里たちの母親が作ってくれたアップルパイのことを、不意に思い出した。料理が好きな人で、小さな愛里たちに食べさせるおやつも大半が彼女の手作りだった。姉はよく食べ残していたが、愛里はその残りまで平らげてしまうほど、大好きだった。思えば今の料理好きも、そんな母親の味が染み付いているからなのかも知れない。
　と、電話が鳴る。
「あ、はい。愛里です」
　高正からで、今向かっているというから一階のカフェにいることを伝えると、五分くらいで彼は姿を現した。白衣を脱いで、ブラウンの薄いチェック柄になったらジャケットに着替えている。
「外に出よう。君は何か食べたかな？」
「アタシはまだですけど」
「なら一緒に食べよう。良い店がある」
　近づいた時に煙草の匂いがしなかったことに安堵して、愛里は彼に続いて病院を出た。
　路地を歩きながら愛里は手短に用件を話したが、笑うばかりで取り合ってくれない。
「そこだよ」
　外に黒板の立て看板を出している、小さな店だった。洋食屋、だろうか。ランチにトマトスープが付いてくると書かれていたけれど、いつもの愛里の昼食の価格からすると高い部類に入った。
　店内は一時過ぎにも関わらずまだ満席で、それでも三分ほどで二人分の空席が出来て、カウンターに横並びで腰を下ろした。
「飲み物だけ……」
　そう言いかけたが、高正が「奢る」というので付き合って同じランチメニューを注文することにした。
「で。私のことはお姉さんから何と聞いているのかな？」
「素敵な人……」
　その言葉に、また大きな笑い声を出した。
「そうか。素敵か。やはり彼女はいざ自分の問題となると語彙力が失われてしまうようだね」
「素敵って悪い言葉なんですか？」
「そうじゃないよ。ただね、沖優里が使う言葉としては陳腐だ、という評価をせざるを得ない。彼女はね、本来もっと素晴らしい言葉を使って物事を表現する。だから常に彼女と話す時は緊張するし、こちらも一言一言を大事にする。それに、気難しい。機嫌を損ねてしまえばそれ以上話さない、なんてことも多々あったから」
　随分と姉に詳しいようだった。愛里は目の前に差し出されたランチプレートを受け取りながら、この男性のどこが気に入ったのか考えようとしたが、横顔を見れば見るほど、ある人物によく似ていた。それは愛里たちの父親だ。父の笑顔は見たことがなかったが、それでも笑うと高正のような表情をするのかも知れない、と思える程にはそっくりだ。
「会うほどの人間じゃない、と優里君は君のことを評していたが、私に会わせたくなかっただけかも知れないね」
「そんなこと言ってたんですか？」
「ああ」
　半球形に盛られたご飯はターメリックで色付けされていたが、バターの風味が香るチキンライスになっている。
「それで愛里君はさ、原田君のことが好きなんだよね？」
「はい。好きです」
　何故だろう。口にした途端に、胸の奥の方がきゅっと締め付けられた。今まで原田の前で好きと言っても、こんな風に感じたことはなかったのに。
「で、彼の女性アレルギィを治したいと？」
「そうなんです。今のアタシがセンセにしてあげられること、センセの一番役に立つことって何だろうって考えたらそれかなって思って」
　高正はデミグラスソースに沈んだハンバーグを切り分けながら、愛里を横目で見やると、
「それが君の愛し方なんだね」
　そう言ってから口に切れ端を運んだ。
「おそらく優里君も言ってたと思うが、彼は決して病気じゃない」
「え、けど」
「確かに女性に触れられることで冷や汗や蕁麻疹が出たり痙攣したり、失神してしまうこともある。だがね、精神的なものが原因であって薬物などの化学療法で治療できるようなものじゃないんだ。それに、思うんだけど、原田君。君と同棲を始めてから、少し症状が緩和してないかな？」
　以前の状態をよく知らないから比べようがなかったが、最近は愛里の方が注意をして触れないようにしているので、息苦しくなるようなことは減っていた。
「何なら今日帰ってから彼に抱きついてみると良い。きっと以前みたいに倒れてしまうようなことにはならないはずだよ」
「本当、ですか？」
　さあ。どうだろう。
　そう笑って返されたが、考えてもみないことだったので、愛里は自分の中に抑え込んでいた欲求がふっと顔を見せるのを感じていた。
「それでだ。もし仮に抱きついても大丈夫だったら、君はどうするつもりなんだ？　キスでもするのかな？」
　原田の女性アレルギィが治っていたら。
　分からない。
　考えようとするほどに頭が痛くなり、愛里はサーモンフライの残りを無理やり口に押し込んだ。


　　　　※


　紫色が混ざったような気持ちの悪い夕焼けの空を見上げながら、原田は村瀬に指定された店に急いだ。
　マンションの近くではない方が良いと言うので、仕方なく混み合う電車を乗り継いで新宿までやってきたが、どこを見ても人ばかりで、この世界にはこんなに人間が暮らしているのだなと圧倒されてしまう。
　だから土曜の夜に出かけるのは嫌だったんだ。
　駅前で待ち合わせた村瀬ナツコの顔を見るなりそう言ってやろうかと思ったが、隣に編集長の岩槻の厳つい顔が並んでいるのに気づいて、
「どうも」
　という無難な挨拶に切り替えた。
「今後はとにかく外出時には男女三人以上で出かけて下さい。つまり先生とわたしが二人きりで打ち合わせをするのも禁止だそうです」
　不満がありそうな口ぶりで村瀬が言うと、早く酒が飲みたいと言い出した岩槻に背中を突かれ、彼女は歩き出した。原田もそれに続く。
　個室を予約してあると言われたが、店そのものも入り組んだ路地の中に立っている雑居ビルの一階と二階に入っていた。
　その二階が個室になっていて、ゆったりとしたワインレッドのベロア生地が貼られたシートには、真っ先に岩槻が腰を下ろした。その対面に原田は座らされ、末席には村瀬が就いて店員との折衝を任された。
「でだ、結城先生。聞いたところ、どうも本当に先生とＪＤの写真だそうじゃない。付き合ってんの？」
　食前酒すら口に含ませることを許さず、原田はグラスに伸ばした手を静止させた。
「そんな訳ないじゃないですか。だから困っているんですよ」
「そう？　別に隠さなくてもいいよ。ここ。ちゃんとしてるとこだし」
　盗聴器などはない、ということだろう。
　けれど仮に何を話しても安全だったとしても、既に桜庭美樹には迷惑を掛けているのだ。ここははっきりとさせておいた方が良い、と思った。
「桜庭さんとはあの日がほぼ初対面です。彼女は沖愛里さんの友人で、僕が書いていた短編小説の取材で付き合ってもらっただけなんです」
「ああ。読んだよアレ」
　運ばれてきた細長い白のプレートを村瀬ナツコが受け取ってそれぞれの前に置くが、そこから手づかみで小さなホイル焼きを掴み取ると、口に入れながら岩槻が言った。
「アレさ、その、結城先生としては納得いってるの？　悪くないとは思うけど、なんて言うか、持ち込みの文学青年が書いたみたいな青臭い作品て、うちの若い子が言ってた」
「編集長。先生も色々と新しい作品にチャレンジなさってて、その一つの方向性としてああいったものを出されただけで。ねえ、先生？」
　原田の表情が歪んだのを見て村瀬が慌てて口を挟んだが、首を横に振ってから「違いますよ」と続ける。
「あれが今の僕の精一杯です。僕だけで書いた作品に対しては村瀬さんもいつもそう言いますよ。悪くないけど物足りない。つまり僕は作家として、限界なんです」
「そんなこと言ってないでさ、恋愛教室みたいな女性どころか男性からも大絶賛の恋愛シリーズ頼みますよ。誰だって向き不向きがあって、結城先生には恋愛を絡めた人間ドラマの深い作品が一番良いんだから」
　岩槻はそのまま苦笑を浮かべ、ロールキャベツを一口で食べる。
　けれど村瀬ナツコは今の原田の言動に疑問を持ったらしい。何度か目をぱちくりとさせると、
「先生。今。何て言われました？」
　そう尋ねた。
「だから。僕は結城貴司の、半分です。結城貴司は、実はもう一人の人間との合作なんです」


　　　　※


　ちょうど原田の告白に編集者たちが驚いている頃、愛里はマンションの前まで戻ってきたところで自分のスマートフォンが鳴ったのを聞いた。
　ＬＩＮＥだ。
　もう必要なくなって削除をしようと思っていたアカウントからの、ゾンビのような連絡だった。

＞週刊誌に結城貴司の写真を売った。取り下げたいなら、俺の家に来い。
＞涌井祐介
            "),
            )

## episode
def ep_main(w: World):
    return w.episode("__episode__",
            ## NOTE
            sc_main(w),
            )
