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


　病院の夜間入り口を抜けると、ひっそりとした空気が通路を支配していた。
　原田貴明はプリントアウトの入った鞄を小脇に抱えて、集中治療室を目指す。
　家を出る時に愛里にＬＩＮＥを送っておいたのだけれど、タクシーを降りてから確認したが既読すら付いていなかった。おそらく優里の傍にいるのだろう。
　原田は原稿を書き終えるといつも最後に「了」の文字を手書きで入れる。それは沖優里にすら話していない、自分だけの儀式だった。印刷し終えた大量のＡ４用紙に並ぶ文字を一つ一つ拾っていき、最後まで読み終えてこれでイケる。そう感じた時にだけあまり上手くないが味があると言われる自分の手書きで、物語に終止符を打つ。
　本来であればそれを一番最初に担当の村瀬ナツコに見せるが、彼女は今、原田の家で原田が持っているのと同じ原稿を見ながら大量の赤ペンを入れていることだろう。
　今回は一切見直しをしていない。
　だからまだ「了」の字も書かれていない。
　てにをはすら正しく使われていないかも知れない。
　それでもやっと見つけた物語を正しい終わりを、一番に沖優里に伝える必要があった。
　彼女にはもう一人の結城貴司としてそれを聞く義務がある。
　いや、理由はそれだけじゃない。
　エレベータの前で立ち止まり、逸る気持ちでボタンを押す。
　どうしてもっと早く気づけなかったのだろう。
　一番大切なことはいつだってすぐ傍に転がっているのに、いつも遠くの綺麗な景色ばかり探して、足元の小石に躓いてしまう。
　エレベータに乗り込み、三階に向かう。
　目を閉じればあの日の制服姿の沖優里を、思い出すことができた。
　彼女に巡り合うまで原田は女性というのは恐ろしく生々しいものだとしか見られなかった。
　男性の筋肉質だったり、毛深かったり、油の臭いだったりがしてくるようなそれとは異なり、原田にとって女性とは着飾った顔と作られた香りとどこまでも埋まってしまう柔らかい肉の塊でしかなかった。
　だが沖優里だけは原田が見てきたどの女性とも違っていて、それはジャングルの奥地を歩いていたら突然全面ガラス張りのビルに遭遇したような、文化圏そのものの差異が具現化したような人間だった。
　だから正確には原田の彼女に対する気持ちの名前は「憧れ」なのかも知れない。
　一匹の猿が自分に愛を教えようとしてくれた人間に恋をするかのような、叶わない、届かない、次元の異なるすれ違い。それは平行線ですら描けず、ただただ存在しない神を見るように彼女を見上げているしかないのだ。
　控室のドアをノックして中を見てみたが、誰もいなかった。
　集中治療室の前室に入り、そこで身支度を整える。
　原稿の持ち込みについて尋ねればおそらく駄目だと言われるだろうと覚悟して、ジャケットの内側に潜ませた。その上から滅菌エプロンを身に着け、彼女の病室に向かう。
　足元のスイッチを押して、ドアをスライドさせる。
　すぐ左手側に複数の看護師が常駐しているが、何やら忙しなく動いていた。
　だから原田は会釈もせず、三メートルほど先の優里の部屋のドアに真っ直ぐ向かった。
　ドアを開ける。
「お姉ちゃん！」
　愛里の叫び声だった。
　見れば彼女の寝かされたベッドの周囲に愛里、高正、葉子と揃っていて、別の医師が優里の体の上に覆いかぶさっている。
　何が、起こっているのだろう。
「嫌！　お姉ちゃん！」
　愛里の声は掠れて涙混じりになり、ベッドに向かおうとするのを葉子が押さえつけた。
「あ、あの……」
　高正がゆっくりと原田を見る。
　初めて見る、魂が抜けたような表情だった。
　原田は改めて沖優里に視線を向ける。
　担当の吉崎医師が行っているのは、電気ショックによる蘇生措置だ。
　どん、と言う音と共に彼女の体が跳ね上がる。
　モニタに表示された波形は大きく乱れるが、それはやがて平坦になり、彼女が生きていないことを教えてくれる。
　何が起こったのか、考えようとしたけれど、上手く頭が働かない。
「もう一度」
　吉崎医師は再度蘇生措置を行う。
　その光景を見つめながら、原田の頭の中には自分が描いた恋愛教室の、最後の場面が蘇っていた。


　小説恋愛教室は、准教授の室尾久嗣とその大学の生徒である優木美郷の物語、として表面上は描かれているが、実は原田貴明の告白に対する、沖優里からの長い長い返答の文章だった。
　そのことに気づけたのは沖愛里が言っていたと村瀬ナツコから聞いた「優里は探し物をしていた」という謎の伝言だ。
　物語全体を優里の物語として考え直す、という観点は事前に気づいていたけれど、てっきり彼女と彼女の父親の物語として読み直せばいいのだとばかり思い込んでいたから、大事なことを見落としていたのだ。
　事実はとても単純だった。
　原田貴明は卒業の日、彼女に告白をした。
　それに対して彼女は彼に「小説を書いてみないか」と尋ねてきた。
　その返答に完全にはぐらかされたのだとばかり思ってしまい、その言葉がまさか原田に対する返事の一部になっていたとは考えなかったのだ。
　というか、そんな宇宙経由で東京駅から有楽町に向かう、みたいな常人には理解し難いことを咄嗟にやってしまうのが、沖優里という人間なのだ。そのことに当時の原田も、今の原田も、おそらく五十年後の原田ですらも、思い至れないだろう。
　主人公の室尾は沖優里であり、生徒として色々なことを教わることになる優木美郷こそが、原田貴明だったのだ。
　優里のプロットでは最終的に病気であることを美郷に知られた室尾は何も言わずに関係を絶ち、彼女の前から永遠に姿を消してしまう。
　これは沖優里が原田の気持ちに対して何も答えることなく去ってしまおうとしているのと同じなのだ。
　ただ、沖優里は彼女の気持ちの仔細を恋愛教室という小説に託している。
　作中では内容こそ出てこないが、優木美郷は同じように室尾が彼の研究室に残したその研究論文を紐解きながら、彼がどう考えていたのかを探ろうとする部分が登場する。けれど美郷はそこに書かれたことを半分以上理解出来ないまま、悲しみにくれて街中を歩き彷徨う。
　一月、三ヶ月、半年と時間だけが経ち、やがて美郷は街中ですれ違っても彼に気づくことがなくなってしまっている、というのが優里が提示した作品の答えであり、彼女の原田に対する返答なのだ。
　忘れて下さい。
　ただ、それだけのことを、これだけ手間を掛けて彼女は原田に伝えようとしていたのだ。
　それを原田は書き換えた。
　失意のまま、美郷は街で彼とすれ違う。
　横断歩道を渡ってしまった彼に対して「好き」でも「愛している」でもなく、ある言葉だけを叫ぶ。
　それこそが、原田の彼女に対する気持ちだった。


　どん、と再びの電気ショック。
　何度やっても無理だと諦めたような声の吉崎医師。
　高正は「代われ！」と彼を押しのけて、自分の手で沖優里の胸を押し下げる。
　戻ってこい。
　戻ってこいと何度も叫び。
　愛里は泣いている。
　優里のことを、お姉ちゃんと呼びながら泣いている。
　葉子はただ組んだ手を口元に持っていき、ずっと祈りを捧げている。
　看護師たちはどうすればいいのか二人の医師を見て、互いに固まっている。
　原田にできることは、何もないと分かっていた。
　それでも、まだ、優里が生きている内に、伝えなければならない言葉を、絞り出す。
「分かったんだ。僕は君に比べて全然頭もよくないし、とても一人で結城貴司としてはやっていけない。君はそこまで分かった上で、僕に結城貴司をやらせた」
「何を言ってるんだ？　頭がおかしくなったのか？」
　吉崎は原田を睨んで「黙っていてくれ」と言う。
「なあ聞いてくれ。まだ生きている君に、生きている内に、こんな僕でもそこに辿り着けたことを、伝えなきゃならないんだ」
「センセ……？」
「小説恋愛教室は、沖優里。君からの長い長い返事だった。僕の告白に対する、君なりの誠意の沢山込められた、とても長い返事だった。そうだろう？」
　心拍を測っている電子音が乱れる。
「君は冷たい人間じゃない。ただ人との距離の取り方が分からず、恐れ、それを気取られまいと強がって冷静な振りをする。けれど相手がどう考え、どういう風に見て、どんな人間なのかをすぐに見抜いて、相手にあまりよく思われないように振る舞うことを選ぶんだ。そうすれば近づかずに、心を開かずに済むから。君は自分の母親とは違うベクトルで、人間関係に、特に男性に対する関係の作り方に不器用だったんだ。それが自分でもよく分かっていた。でもそんな君のことを、僕は本気で愛した。憧れだよ、と君は笑うかも知れないけれど、それでも真っ直ぐに君のことを愛そうとした。その気持ちを正面から受け止めることは出来なくて、けれど真摯なそれに対して君なりに誠実に答えようとしたその結果が、小説恋愛教室だったんだ」
　誰も原田に対して声を上げなくなっていた。
「恋愛教室第四巻の原稿を、書き終えたよ」
　電子音の波が、ざわつく。
「君の返事を理解した上で、僕はそれを書き換えた。だって僕は、もう一人の結城貴司だから。あれは……あんな終わり方は、君自身をただ傷つけるだけじゃないか。いつか死んでいなくなる。それは人間誰しもそうだよ。だから愛さないで下さい？　忘れて下さい？　それが恋愛だなんて格好つけてみたところで、ほんとはただ自分が寂しい人なんだと知られたくないだけじゃないか！」
　戻ってこい。
「君は誰かに告白したことはあるのか？　誰かに振られたことがあるのか？　恋をして、その相手がどんな人間かもよく知らないまま好きだと口にして、その想いを受け入れてもらえなくて、それでもまだ相手が好きで、もう失恋というゴールを迎えているのにまだ次のレースに望む気になれずずっとそこで佇んだまま、また同じスタートラインに戻ろうとしている。そんな恋愛を、くだらない、つまらないと言って切り捨てながら、ほんとはただそれが羨ましくて仕方なくて、寂しいって言えなくて」
　戻ってこい。
「一人でもちゃんと生きていけると演じながら、周りより少しだけ高い位置に立って自分は安全地帯からそれを見やって、こっそり笑って悦に入っている振りを見せながら、それでも本当はこの小説に描いたみたいに、いつもいつも恋愛とは何か、男と女の人間関係とは何なのか、必死に考えていたんだろう！？」
　戻ってこい。沖優里。
「君だって僕と同じじゃないか。同じ人間で、同じくらい不器用な人間で、ただ好きな人に好きと言えない寂しさを他人に見せないようにしている人間で」
　戻ってきて、思い切り叩いてくれ。
「一人になったらあれは言わない方が良かったとか、こう言ってあげたら良かったとか、そんな反省ばかりを繰り返しながら、次はちゃんと出来るかどうか分からずに、やっぱり他人が恐くて、また大丈夫な振りを繰り返す。そんな不器用な生き方しか出来なくて」
　笑って、原田君は何も分かってないと言ってくれ。
「死ぬことでしか自分の人生をどうにかする方法がないだなんて考えてばかりだったとか、そんな寂しい本音、せめて自分の大切な人にくらい伝えてくれよ」
　大嫌いと、思い切り振ってくれ。
「沖優里！」
　そして、僕は。
「君に」
　一番大切な気持ちを、伝えるよ。
「ありがとう」
　と。
            "),
            )

## episode
def ep_main(w: World):
    return w.episode("__episode__",
            ## NOTE
            sc_main(w),
            )
