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


　沖愛里はマスクの中に溜息を落としながら、目を閉じたまま呼吸器が被せられた姉のことを見守っていた。
　担当の吉崎医師によれば、不審者（どうも原田貴明のことらしい）の応対に無理やり目覚めたことで心臓に負担が掛かった所為で、再び体を休めなければならなくなったと言っていた。
　そんなことがあるのだろうか、と愛里なんかは思うけれど、事実姉は起きる気配が全然ない。
　先程まで一緒に付いてくれていた高正医師も、義母の葉子の姿もない。
　食事を取りに席を外すと言っていたが、自分はとてもそんな気分にはなれなかった。
　もう一度、と手元にある姉からの遺書を開いてみる。
　一番身近な人間だった妹へ。
　という書き出しから始まるそれは一篇の小説のようで、読み易い言葉で書かれているにも関わらず、愛里には意味が難解な箇所が沢山あった。原田が傍にいたら色々と質問も出来ただろうが、姉に告白のようなことをして病室を追い出されてしまったのだ。今頃一人で落ち込んでいることだろう。
「これから私がここに書くことは、今までに貴女に言ったことのない、本当の気持ちです」
　そんな告白に続いて、姉は他所に男を作っては家から逃げ出し、挙句に病に冒されて亡くなってしまった母親を恨んでいたこと、そんな母に代わり、自分が愛里をちゃんとした女性に育てなければならないというプレッシャーの中に常にいたことなどが書き出されている。
　確かに小さい頃、愛里は常に姉の厳しい視線に怯えながら生活をしていた。
　家に殆ど帰ってこない父、家から何だかんだと理屈をつけて抜け出そうとする母。祖父母は同居しておらず、育児をするのは自分たちしかいなかった。
　姉は体が弱く、それでも部屋の掃除だけは怠らなかった。
　家事の大半は幼い愛里が引き受けた。
　時折、様子を見に訪れてくれる叔母だけが家族と親の温もりを与えてくれたけれど、それらは所詮、一時のものでしかなく、家族は一緒にいるべきだ、という叔母のお節介は結果的に優里と愛里を精神的に追い詰めるものだった。
　その叔母も母の死後、徐々に家には来なくなり、やがて後妻となる葉子が、入籍する前から頻繁に家を訪れるようになった。
　彼女は料理も上手く、正に父が望むような”女らしい女性”像を演じていた。
　そう。姉の遺書には葉子の言動が全て「演技」と書かれている。
　愛里は未だに葉子のことがよく理解できない。
　嫌いでも苦手でもないけれど、一緒にいると少し疲れてしまう、というのが本音だった。
「嫌いだけれど、あの人の定年後に一緒に暮らそうと言ってくれています。もし愛里さえ良ければ、一緒に行ってしまっても構わない」
　この話はさっき初めて葉子の口から聞かされた。遺書の内容を見た愛里の質問に答える形でだったが、優里の容態が安定するまでは話さないつもりだったと言われた。
　姉ではないけれど、愛里自身も、父親と一緒に暮らす姿は想像出来ない。
　嫌い、ではない。
　けれどどんなに頑張ったところで好きにはなれない。
　そんな男性だ。
　姉の遺書の内容の半分は、こうした家族についてのことだった。
　姉との会話の中で愛里が薄々感じていたものが多かったが、それでも文字にして目にすると、わざわざ書き残すほど姉は二人を嫌っていたのだということを実感する。
　ただそれは姉の本音の中でも前置きに過ぎず、二枚目の便箋に移った冒頭で、いきなり次の文言が現れるのだ。
「貴女が、羨ましいと思ったことは、一度しかない……」
　声に出してみる。
　一度もない、なら理解出来た。
　そもそも姉からすれば自分なんかは羨む部分の全くない存在にしか思われていない、と愛里は感じていたし、実際に会話の中でも冗談ですらそういった類の言葉が出たことはなかった。
　何度も読み返した部分を、愛里は今一度声に出してみる。
「原田君が、貴女に愛情を感じ始めている。そう感じた時に初めて、愛里のことが羨ましいと思ったのです」
　酷く混乱する。
　姉は原田貴明のことを、振った。
　それは学生時代、彼が初めて告白した時だけじゃなく、今改めてした告白も酷い断りようをした。そう聞いている。
　それなのに、何故羨ましいなどと感じるのだろう。
　誰かに愛されたい。
　それだけなら、これまで愛里は沢山の男性に愛されてきた。例えそれが姉に鼻で笑われるような偽物の薄っぺらい愛情だったとしても、誰かに愛されてきたと言えるだけのものを愛里は感じていた。
　それなのに、今までの彼氏たちには姉は一切そんな感情を抱いていなかった。
　それが何故原田貴明に対してだけ、そんなことを思ったのだろう。
　理解出来なかった。
「ねえ、お姉ちゃん……本当はセンセのこと、原田さんのこと愛していたの？」
　当然答えてなんてもらえない。
　それでも愛里は姉がどんな気持ちでこの告白を自分に対して残したのか、その意味について考えようとしていた。
　規則正しい呼吸音。
　心拍を測る機械も一定のリズムで電子音を発している。
　点滴は残り三分の一程度になっていたが、それが何の薬を入れられたものなのか、愛里には分からない。
　何も知らない。
　何も出来ない。
　ただ、見守っているしか出来ない。
　それは原稿を書いている原田を見ている時の状況にそっくりだった。
　何か自分に出来ることはないかと部屋を掃除してみたり、食べたいものを聞いて食事の準備をしたり、洗濯や片付けものをしたり、そんなことしか出来ない。
　でもそれが小さい頃からの愛里の日常だった。
　まだ姉が病院ではなく、家にいた頃。姉の機嫌を伺いながら、それを損ねないようにと、家事に勤しんだ。
　だから彼氏という名前の男性たちと一緒に暮らすことになっても、そのスタイルは変わらなかった。
　今思えば、そうしていることで、ちゃんとした関係を作ることから逃げていたのかも知れない。
　姉に向き合うことが恐くて、とりあえず怒られないように、できれば喜んでもらえるようにと、そうやって身の回りの世話をすることで、姉が何を考え、何に苛立っているのかを考えずに済ませようとしていたのだ。
　それが、原田との同棲生活で変わっていった。
　もっと知りたい。
　その感情が、初めてちゃんと小説を、それも三冊も読み切ることに繋がった。
　力にはなれなくても、同じものを見て、同じようなことを考えて、時にはちょっと意見も言ったりして、そうやって少しずつ関係を深めようという気に、自然となれた。
　相手が原田だったから、なのか、それとも姉が準備して導いてくれた結果なのかは、分からない。
「ひょっとして……そんなアタシのことを、羨ましいと感じたの？　ねえ、お姉ちゃん」
　本当の恋愛を探していたのは、愛里ではなく姉、優里の方だったということだろうか。
　愛里はスマートフォンを控室に残してきたことに気づいて、慌てて席を立った。
　センセに、原田貴明に、聞いてもらいたい。
　会いたい。
　彼の言葉が、どうしても今必要だと感じていた。
            "),
            )

## episode
def ep_main(w: World):
    return w.episode("__episode__",
            ## NOTE
            sc_main(w),
            )
