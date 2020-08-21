# -*- coding: utf-8 -*-
"""Story: the renai-kyoshitsu
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.renkyo import config as cnf

## title
TITLES = (
        ("１話「もう恋なんてしない」"),
        ("２話「ナチュラルに恋して」"),
        ("３話「恋心」"),
        ("４話「恋するフォーチュンクッキー」"),
        ("５話「シーソーゲーム」"),
        ("６話「恋に落ちて」"),
        ("７話「初恋」"),
        ("８話「小さな恋の唄」"),
        ("９話「恋人よ」"),
        ("１０話「恋」"),
        )

## scenes
### chapter 1
def sc_warmingawake(w: wd.World):
    s = w.scene("ぬるい目覚め", "いつものように目覚めた愛里は突然彼にふられた")
    return s

def sc_writinginsickroom(w: wd.World):
    s = w.scene("病室での執筆", "病室で小さなノートパソコンに打ち込む優里")
    return s

def sc_cannotwriteman(w: wd.World):
    s = w.scene("小説が書けない男", "広いリビングでパソコンに向かう男。作家だった")
    return s

def sc_readygoout(w: wd.World):
    s = w.scene("外出準備", "食べる為に外に出る準備をする原田")
    return s

def sc_lateafternoontown(w: wd.World):
    s = w.scene("昼下がりの街", "午後の陽気の中を歩く原田")
    return s

def sc_favoritecafe(w: wd.World):
    s = w.scene("行きつけの店", "パンケーキの美味しい店にやってくる原田")
    return s

def sc_outofmurase(w: wd.World):
    s = w.scene("窓の外に村瀬", "注文を終えて外を覗くと村瀬ナツコがいた")
    return s

def sc_runawayharada(w: wd.World):
    s = w.scene("村瀬からの逃亡", "村瀬ナツコから逃げ出す")
    return s

def sc_scoutingbookshop(w: wd.World):
    s = w.scene("書店の偵察", "書店を見て時間を潰そうとする原田")
    return s

def sc_womanallergy(w: wd.World):
    s = w.scene("女性アレルギィ", "ファンに見つかり触られた原田は失神する")
    return s

def sc_coldawake(w: wd.World):
    s = w.scene("冷たい目覚め", "肌寒さに目覚めるとそこには高正がいた")
    return s

def sc_waitingroom(w: wd.World):
    s = w.scene("待合室の彼女", "待合室では若い女性が原田を待っていた")
    return s

def sc_requesthim(w: wd.World):
    s = w.scene("愛里の頼み", "愛里と名乗った女性は恋愛作家である彼に恋愛を教えてと迫る")
    return s

### chapter 2
def sc_comeingirl(w: wd.World):
    s = w.scene("押しかけ彼女", "どこで聞いたのか原田の家に訪ねてくる愛里")
    return s

def sc_herability(w: wd.World):
    s = w.scene("愛里の能力", "見た目に反して実に家庭的な愛里は片付けを始める")
    return s

def sc_promise_and_condition(w: wd.World):
    s = w.scene("約束と条件", "村瀬が編集長と約束がついたという。ただし条件付きで")
    return s

def sc_teachstep(w: wd.World):
    s = w.scene("恋の段階", "原田は愛里にしぶしぶ恋愛について教えることになる")
    return s

def sc_gotobreakheart(w: wd.World):
    s = w.scene("ふられる為に", "原田は最初のステップとして涌井にちゃんとふられろと言う")
    return s

def sc_wakui_and_airi(w: wd.World):
    s = w.scene("涌井と愛里", "涌井の前に現れる愛里は、自分の思いの丈をぶつける")
    return s

def sc_interruput(w: wd.World):
    s = w.scene("原田の割り込み", "愛里と涌井の間に入る原田")
    return s

def sc_explainlove(w: wd.World):
    s = w.scene("恋について", "ふられた愛里に恋愛とは何なのか語り始める原田")
    return s

### chapter 3
def sc_yuriinroom(w: wd.World):
    s = w.scene("病室の姉", "愛里の姉・優里は病室にいた")
    return s

def sc_permission(w: wd.World):
    s = w.scene("優里の許可", "姉に原田に教えてもらうことを伝えると珍しく良い返事")
    return s

def sc_homekeeper(w: wd.World):
    s = w.scene("家政婦の愛里", "通い妻となった愛里は掃除から洗濯まで何でもこなす、まるで原田の家政婦にでもなったようだ")
    return s

def sc_whenteachin(w: wd.World):
    s = w.scene("いつ教えてくれるの？", "愛里は原田にいつになったら恋愛教室してくれるのか問い詰める")
    return s

def sc_nocomeher(w: wd.World):
    s = w.scene("来なくなる彼女", "飽きたのか怒ったのか愛里は来なくなる")
    return s

def sc_heradvice(w: wd.World):
    s = w.scene("彼女からのアドバイス", "原田はある人物に愛里のことを相談していた")
    return s

def sc_getbackairi(w: wd.World):
    s = w.scene("愛里を取り戻しに", "彼女が涌井の許に戻ったと知り、取り戻しに向かう")
    return s

def sc_haradahand(w: wd.World):
    s = w.scene("原田の手", "涌井から原田の手が愛里を取り戻す")
    return s

### chapter 4
def sc_novel_lovestory(w: wd.World):
    s = w.scene("短編・恋愛小説", "原田の書く短編小説の内容")
    return s

def sc_writingshortnovel(w: wd.World):
    s = w.scene("短編小説の執筆", "原田はやる気になって短編小説を書いていた")
    return s

def sc_wrongdate(w: wd.World):
    s = w.scene("間違ったデート", "短編小説を読んだ誰もがデートが変だと指摘")
    return s

def sc_appointment(w: wd.World):
    s = w.scene("待ち合わせ", "デートの待ち合わせにやってきたが、そこには美樹だけが待っていた")
    return s

def sc_datestart(w: wd.World):
    s = w.scene("デート開始", "デートを始めるが原田のプランは破壊される")
    return s

def sc_aquarium_line(w: wd.World):
    s = w.scene("水族館の行列", "水族館には列ができていた")
    return s

def sc_in_aquarium(w: wd.World):
    s = w.scene("水族館楽しい？", "やっと館内に入り、女子二人だけは楽しそうに")
    return s

def sc_foodcoat(w: wd.World):
    s = w.scene("フードコートにて", "昼食をフードコートで取る")
    return s

def sc_airi_history(w: wd.World):
    s = w.scene("愛里の恋愛遍歴", "愛里は自分の恋愛について語る")
    return s

def sc_philosophy_harada(w: wd.World):
    s = w.scene("小説家の恋愛哲学", "恋愛小説と実際の恋愛は違うと語り始める")
    return s

def sc_wayback(w: wd.World):
    s = w.scene("二人の帰り道で", "帰り道。愛里の雰囲気が変")
    return s

def sc_crossroad(w: wd.World):
    s = w.scene("告白の横断歩道", "帰り道、愛里は思い切って告白をする")
    return s

### chapter 5
def sc_monthlywoman(w: wd.World):
    s = w.scene("毎月の女", "月に一度、継母は見舞いに訪れた")
    return s

def sc_alonehome(w: wd.World):
    s = w.scene("一人に戻って", "再び一人暮らしに戻った原田")
    return s

def sc_comeuncle(w: wd.World):
    s = w.scene("叔父の来訪", "叔父がきて、父の見舞いに出かけることに")
    return s

def sc_uncletalk(w: wd.World):
    s = w.scene("叔父の話", "叔父は結婚話を持ち出して将来的に誰か父を引き取った方がいいと言い出す")
    return s

def sc_dadhome(w: wd.World):
    s = w.scene("父の施設", "父の施設に入る")
    return s

def sc_sickdad(w: wd.World):
    s = w.scene("病気の父", "気が狂っている父")
    return s

def sc_familyblood(w: wd.World):
    s = w.scene("父の血", "父親の血を感じて")
    return s

def sc_oki_sisters(w: wd.World):
    s = w.scene("沖姉妹", "愛里は優里に会いにやってくる")
    return s

def sc_checkyuri(w: wd.World):
    s = w.scene("愛里は姉に確認する", "原田が大学の同級生と知り、彼のことをどう思っているか確認する")
    return s

def sc_declaration(w: wd.World):
    s = w.scene("宣戦布告", "姉に対して原田を自分のものにすると言い放つ")
    return s

### chapter 6
def sc_airiagain(w: wd.World):
    s = w.scene("愛里再び", "風邪を引いて寝込んでいたところに愛里がきた")
    return s

def sc_cohabitation(w: wd.World):
    s = w.scene("同棲を始める", "愛里はなし崩しで同棲を始めた")
    return s

def sc_webrumor(w: wd.World):
    s = w.scene("悪い噂", "ネットのサイトに結城貴司の噂が出ていた")
    return s

def sc_haradafamily(w: wd.World):
    s = w.scene("原田の家族のこと", "噂の真偽を確かめる愛里に、原田は語る。自分の家族のこととトラウマを")
    return s

def sc_childhood(w: wd.World):
    s = w.scene("幼少期の両親", "原田の幼少期、芸術家の父とモデルの母、そしてトラウマの毎日だった")
    return s

def sc_allergyagain(w: wd.World):
    s = w.scene("アレルギィ再び", "原田は話し終えて失神してしまう")
    return s

def sc_catchthelast(w: wd.World):
    s = w.scene("最後の作品", "原田は彼女から次で最後になると原案のメールを受け取る")
    return s

def sc_wakuimail(w: wd.World):
    s = w.scene("涌井のメール", "原田が打ち合わせで出かけたところに愛里に涌井からメールが入る")
    return s

### chapter 7
def sc_newhomekeeper(w: wd.World):
    s = w.scene("新しい家政婦", "愛里の代わりとして美樹がやってきた")
    return s

def sc_whereabouts(w: wd.World):
    s = w.scene("彼女の行方", "消えてしまった愛里")
    return s

def sc_followuprumor(w: wd.World):
    s = w.scene("噂の続報", "原田の暴露記事はついに週刊誌に掲載される")
    return s

def sc_emergecontact(w: wd.World):
    s = w.scene("緊急連絡", "父の容態が悪化したと緊急で連絡が入る")
    return s

def sc_dadcritical(w: wd.World):
    s = w.scene("父危篤", "行ってみると父は危篤状態だった")
    return s

def sc_mikiproposed(w: wd.World):
    s = w.scene("美樹のプロポーズ", "弱ってしまった原田に美樹はプロポーズする")
    return s

def sc_writercome(w: wd.World):
    s = w.scene("記者来襲", "ずっとつけていた記者がマンションにくる")
    return s

def sc_emergeyuri(w: wd.World):
    s = w.scene("優里の容態悪化", "優里の容態が急変したと高正から連絡がある")
    return s

def sc_choosewhich(w: wd.World):
    s = w.scene("どっちを選ぶか", "愛里が涌井に捕まっていると知るが、どちらに向かうべきか悩む")
    return s

### chapter 8
def sc_haradecision(w: wd.World):
    s = w.scene("原田の決断", "原田は愛里を助けに向かうことに決め、手を尽くす")
    return s

def sc_prepare_rescue(w: wd.World):
    s = w.scene("救出準備", "記者を頼り、相手の情報を調べたり、手配を済ませる")
    return s

def sc_airi_atonement(w: wd.World):
    s = w.scene("愛里の贖罪", "愛里は涌井を助けようとしていた")
    return s

def sc_rushin(w: wd.World):
    s = w.scene("突入", "愛里が勤める違法風俗店に入る")
    return s

def sc_takamasaeye(w: wd.World):
    s = w.scene("優里を見守る目", "高正は優里を見守っている")
    return s

### chapter 9
def sc_safely_airi(w: wd.World):
    s = w.scene("愛里は無事", "助け出された愛里")
    return s

def sc_yuri_condition(w: wd.World):
    s = w.scene("優里の容態", "病院に到着した原田は高正から優里の容態を聞く")
    return s

def sc_yuri_medic_condtion(w: wd.World):
    s = w.scene("優里の病気のこと", "高正は優里が一体どういう病気だったのかを語る")
    return s

def sc_airi_confession(w: wd.World):
    s = w.scene("愛里の告白", "愛里は改めて原田に告白をする")
    return s

def sc_harada_reply(w: wd.World):
    s = w.scene("愛里への答え", "原田は真摯に愛里に応える")
    return s

def sc_airikiss(w: wd.World):
    s = w.scene("愛里の口づけ", "ふられた愛里は原田に姉のことを頼み、キスをする")
    return s

def sc_write_novel(w: wd.World):
    s = w.scene("小説を書く", "原田は最後の小節を書き始めた")
    return s

### chapter 10
def sc_novel_loveclass(w: wd.World):
    s = w.scene("小説恋愛教室", "恋愛教室最終巻の中身")
    return s

def sc_her_family(w: wd.World):
    s = w.scene("彼女の家族", "愛里たちの継母がやってくる")
    return s

def sc_her_dad(w: wd.World):
    s = w.scene("彼女の父親", "愛里の父親がやってくる")
    return s

def sc_truth_of_novel(w: wd.World):
    s = w.scene("小説の真実", "原田は彼女が小説を書かせた意味を語る")
    return s

def sc_love_class(w: wd.World):
    s = w.scene("最後の恋愛教室", "そして原田と優里の恋愛教室が始まる")
    return s

def sc_lastconfession(w: wd.World):
    s = w.scene("最後の告白", "原田の最後の告白。それに対する優里の答え")
    return s

def sc_each_afterwork(w: wd.World):
    s = w.scene("それぞれの後日談", "それぞれの後日談について")
    return s

## episodes
### chapter 1
def ep_dumped_airi(w: wd.World):
    return w.episode("愛里ふられる", "朝起きたら彼に突然振られた",
            sc_warmingawake(w),
            )

def ep_cannotwrite(w: wd.World):
    return w.episode("小説が書けない作家", "原田はずっと小説が書けないでいた",
            # NOTE: 恋愛教室を読む優里のカットを入れておく
            sc_writinginsickroom(w),
            sc_cannotwriteman(w),
            sc_readygoout(w),
            )

def ep_runaway_her(w: wd.World):
    return w.episode("村瀬から逃げる", "熱心な編集から逃げる原田",
            sc_lateafternoontown(w),
            sc_favoritecafe(w),
            sc_outofmurase(w),
            sc_runawayharada(w),
            )

def ep_allergy(w: wd.World):
    return w.episode("女性アレルギィ", "ファンに発見され女性アレルギィで倒れる原田",
            sc_scoutingbookshop(w),
            sc_womanallergy(w),
            )

def ep_waitinghim(w: wd.World):
    return w.episode("彼を待つ女", "目覚めた原田を待っていたのは愛里だった",
            sc_coldawake(w),
            sc_waitingroom(w),
            )

def ep_teachme_love(w: wd.World):
    return w.episode("恋愛を教えて", "愛里は原田に恋愛を教えて欲しいと頼む",
            sc_requesthim(w),
            )

### chapter 2
def ep_beangry(w: wd.World):
    return w.episode("約束が違う", "恋愛教室してくれる約束が果たされないことに怒りだす",
            sc_comeingirl(w),
            )

def ep_promise_murase(w: wd.World):
    return w.episode("約束の条件", "村瀬が編集長に締め切り延期許可をもらってくれたが",
            sc_herability(w),
            sc_promise_and_condition(w),
            )

def ep_lovestep(w: wd.World):
    return w.episode("恋愛のステップ", "原田から恋愛のステップについて教わる",
            sc_teachstep(w),
            sc_gotobreakheart(w),
            )

def ep_brokenlove(w: wd.World):
    return w.episode("失恋すること", "涌井と話す愛里。ちゃんと失恋するために",
            sc_wakui_and_airi(w),
            sc_interruput(w),
            )

def ep_startloveclass(w: wd.World):
    return w.episode("恋愛教室が始まる", "失恋をした愛里。そして恋愛教室が始まる",
            sc_explainlove(w),
            )

### chapter 3
def ep_eldersister(w: wd.World):
    return w.episode("彼女の姉", "愛里の姉",
            sc_yuriinroom(w),
            sc_permission(w),
            )

def ep_dedication(w: wd.World):
    return w.episode("献身的な彼女", "毎日通ってくる彼女の献身性",
            sc_homekeeper(w),
            )

def ep_herlost(w: wd.World):
    return w.episode("来なくなる彼女", "愛里が来なくなる",
            sc_nocomeher(w),
            )

def ep_heradvice(w: wd.World):
    return w.episode("彼女の助言", "実は結城貴司はもうひとりいた。彼女に愛里について助言される",
            sc_heradvice(w),
            )

def ep_getback(w: wd.World):
    return w.episode("愛里の奪還", "愛里を涌井から取り戻す原田",
            sc_getbackairi(w),
            sc_haradahand(w),
            )

### chapter 4
def ep_shortnovel(w: wd.World):
    return w.episode("原田の小説", "短編を書いてみるが",
            sc_novel_lovestory(w),
            sc_writingshortnovel(w),
            sc_wrongdate(w),
            )

def ep_date(w: wd.World):
    return w.episode("デート", "愛里と友人と三人で仮想デートを行うことになる",
            sc_appointment(w),
            sc_datestart(w),
            sc_aquarium_line(w),
            sc_in_aquarium(w),
            )

def ep_complex(w: wd.World):
    return w.episode("愛里のコンプレックス", "愛里は姉にコンプレックスがあることを告白する",
            sc_foodcoat(w),
            sc_airi_history(w),
            )

def ep_philosophy(w: wd.World):
    return w.episode("原田の恋愛哲学", "愛里たちは原田から恋愛がどういうものか聞く",
            sc_philosophy_harada(w),
            )

def ep_confession(w: wd.World):
    return w.episode("愛里の告白", "帰り道。二人きりになったところで愛里は告白する",
            sc_wayback(w),
            sc_crossroad(w),
            )

### chapter 5
def ep_stepmother(w: wd.World):
    return w.episode("彼女の継母", "優里は継母を毛嫌いしていた",
            sc_monthlywoman(w),
            )

def ep_alone(w: wd.World):
    return w.episode("一人暮らし", "原田はまた一人暮らしに戻った",
            sc_alonehome(w),
            sc_comeuncle(w),
            )

def ep_hisdaddy(w: wd.World):
    return w.episode("父の見舞い", "施設に預けられている父の見舞い",
            sc_uncletalk(w),
            sc_dadhome(w),
            sc_sickdad(w),
            sc_familyblood(w),
            )

def ep_airi_and_yuri(w: wd.World):
    return w.episode("愛里と優里", "愛里は優里に原田のことを質問する",
            sc_oki_sisters(w),
            sc_checkyuri(w),
            )

def ep_nevergiveup(w: wd.World):
    return w.episode("愛里は諦めない", "姉を好きと知ったが愛里は諦めないと誓う",
            sc_declaration(w),
            )

### chapter 6
def ep_restart(w: wd.World):
    return w.episode("愛里再始動", "再び愛里が家にやってくる",
            sc_airiagain(w),
            sc_cohabitation(w),
            )

def ep_rumor(w: wd.World):
    return w.episode("悪い噂", "ネットに原田の情報が掲載されていた",
            sc_webrumor(w),
            )

def ep_family(w: wd.World):
    return w.episode("原田の家族", "原田は愛里に自分の家族について語る",
            sc_haradafamily(w),
            sc_childhood(w),
            sc_allergyagain(w),
            )

def ep_lastwork(w: wd.World):
    return w.episode("最後の小説", "原田は編集長らに結城貴司の秘密を打ち明け、最後の作品になると告げる",
            sc_catchthelast(w),
            )

def ep_zombie(w: wd.World):
    return w.episode("ゾンビのように", "愛里のもとに涌井からネットに噂を流したのは自分だと連絡があった",
            sc_wakuimail(w),
            )

### chapter 7
def ep_herfriend(w: wd.World):
    return w.episode("彼女の親友", "愛里と交代で美樹が通い妻になる",
            sc_newhomekeeper(w),
            sc_whereabouts(w),
            )

def ep_dadcrisis(w: wd.World):
    return w.episode("父の悪化", "急に父の容態悪化し、美樹とともにかけつける",
            sc_followuprumor(w),
            sc_emergecontact(w),
            sc_dadcritical(w),
            )

def ep_proposed(w: wd.World):
    return w.episode("美樹のプロポーズ", "美樹から結婚を申し込まれるが",
            sc_mikiproposed(w),
            )

def ep_magazinewriter(w: wd.World):
    return w.episode("雑誌記者", "雑誌記者たちの連日の攻勢にストレスから再び対人恐怖と女性アレルギィ発症",
            sc_writercome(w),
            )

def ep_airi_or_yuri(w: wd.World):
    return w.episode("愛里か優里か", "愛里のピンチと優里の容態悪化が同時に知らされる",
            sc_emergeyuri(w),
            sc_choosewhich(w),
            )

### chapter 8
def ep_determination(w: wd.World):
    return w.episode("決断", "原田は迷いながらも優里より愛里の救出を選ぶ",
            sc_haradecision(w),
            )

def ep_readyrescue(w: wd.World):
    return w.episode("救出準備", "原田は今までに出会った人、ツテを総動員する",
            sc_prepare_rescue(w),
            )

def ep_aboutairi(w: wd.World):
    return w.episode("愛里について", "原田にとって愛里の意味は大きく変わっていた",
            sc_airi_atonement(w),
            )

def ep_rushin(w: wd.World):
    return w.episode("突入", "違法風俗店に愛里を取り戻すために突入する",
            sc_rushin(w),
            )

def ep_yuri_and_takamasa(w: wd.World):
    return w.episode("優里を見守る", "高正は優里を見守っている",
            sc_takamasaeye(w),
            )

### chapter 9
def ep_savedairi(w: wd.World):
    return w.episode("助けられた愛里", "涌井たちにより助けられた愛里",
            sc_safely_airi(w),
            )

def ep_yuristatus(w: wd.World):
    return w.episode("優里の容態", "意識が戻らない優里",
            sc_yuri_condition(w),
            )

def ep_yurisick(w: wd.World):
    return w.episode("優里の病気", "高正は二人に優里の病気について語る",
            sc_yuri_medic_condtion(w),
            )

def ep_airiwords(w: wd.World):
    return w.episode("愛里の言葉", "全てを飲み込んだ上で愛里は原田を好きだと告げる",
            sc_airi_confession(w),
            sc_harada_reply(w),
            )

def ep_kiss(w: wd.World):
    return w.episode("愛里のキス", "自分を振った原田に愛里は最後のキスをする",
            sc_airikiss(w),
            sc_write_novel(w),
            # NOTE: 原田は小説を仕上げる
            )

### chapter 10
def ep_thelastnovel(w: wd.World):
    return w.episode("小説恋愛教室", "恋愛教室を書き切った原田",
            sc_novel_loveclass(w),
            )

def ep_herfamily(w: wd.World):
    return w.episode("彼女の家族", "愛里は控室で継母と話す。そこに父がやってくる",
            sc_her_family(w),
            sc_her_dad(w),
            )

def ep_thetruth(w: wd.World):
    return w.episode("真実", "恋愛教室の原稿を手にやってきた原田は、推測した真実を語る",
            sc_truth_of_novel(w),
            )

def ep_loveclass(w: wd.World):
    return w.episode("君と私の恋愛教室", "小説は彼女から原田に向けて書かれたものだった",
            sc_love_class(w),
            sc_lastconfession(w),
            )

def ep_epilogue(w: wd.World):
    return w.episode("後日談", "その後のそれぞれ",
            sc_each_afterwork(w),
            )

## chapters
def ch1(w: wd.World):
    return w.chapter(TITLES[0],
            # NOTE: 出会い。愛里はふられ、原田は女性アレルギィ
            # NOTE: 同棲することになった
            ep_dumped_airi(w),
            ep_cannotwrite(w),
            ep_runaway_her(w),
            ep_allergy(w),
            ep_waitinghim(w),
            ep_teachme_love(w),
            )

def ch2(w: wd.World):
    return w.chapter(TITLES[1],
            # NOTE: 愛里に恋愛教室をすることになる
            # NOTE: 愛里はちゃんと涌井からふられた
            ep_beangry(w),
            ep_promise_murase(w),
            ep_lovestep(w),
            ep_brokenlove(w),
            ep_startloveclass(w),
            )

def ch3(w: wd.World):
    return w.chapter(TITLES[2],
            # NOTE: 優里の存在。病気のこと
            # NOTE: 涌井の許に戻る愛里。愛里に自分の方に来いと取り戻す
            ep_eldersister(w),
            ep_dedication(w),
            ep_herlost(w),
            ep_heradvice(w),
            ep_getback(w),
            )

def ch4(w: wd.World):
    return w.chapter(TITLES[3],
            # NOTE: デート回。愛里の友人と仲が深まる
            # NOTE: 愛里の軽い告白、原田にはずっと初恋の女性がいることを知る
            ep_shortnovel(w),
            ep_date(w),
            ep_complex(w),
            ep_philosophy(w),
            ep_confession(w),
            )

def ch5(w: wd.World):
    return w.chapter(TITLES[4],
            # NOTE: 初恋の女性が優里だと知った愛里は
            ep_stepmother(w),
            ep_alone(w),
            ep_hisdaddy(w),
            ep_airi_and_yuri(w),
            ep_nevergiveup(w),
            )

def ch6(w: wd.World):
    return w.chapter(TITLES[5],
            # NOTE: 愛里は本当に原田のことが好きだと気づく
            ep_restart(w),
            ep_rumor(w),
            ep_family(w),
            ep_lastwork(w),
            ep_zombie(w),
            )

def ch7(w: wd.World):
    return w.chapter(TITLES[6],
            # NOTE: 原田の優里との出会い回想
            # NOTE: 優里の容態が悪化する
            ep_herfriend(w),
            ep_dadcrisis(w),
            ep_proposed(w),
            ep_magazinewriter(w),
            ep_airi_or_yuri(w),
            )

def ch8(w: wd.World):
    return w.chapter(TITLES[7],
            # NOTE: 愛里は涌井の凶行を止めるために原田から離れる
            # NOTE: 原田は愛里を涌井の手から取り戻すが、優里の許に向かう
            ep_determination(w),
            ep_readyrescue(w),
            ep_aboutairi(w),
            ep_rushin(w),
            ep_yuri_and_takamasa(w),
            )

def ch9(w: wd.World):
    return w.chapter(TITLES[8],
            # NOTE: 病気の優里。愛里は原田に告白して振られる
            # NOTE: 原田は優里に自力で面会する
            ep_savedairi(w),
            ep_yuristatus(w),
            ep_yurisick(w),
            ep_airiwords(w),
            ep_kiss(w),
            )

def ch10(w: wd.World):
    return w.chapter(TITLES[9],
            # NOTE: 原田は優里に告白した
            # NOTE: それぞれのエピローグ
            ep_thelastnovel(w),
            ep_herfamily(w),
            ep_thetruth(w),
            ep_loveclass(w),
            ep_epilogue(w),
            )

## setting
def set_stages(w: wd.World):
    return w

## main
def world():
    w = wd.World(2)
    w.set_db(cnf.PERSONS, cnf.CHARAS,
            cnf.STAGES,
            cnf.DAYS, cnf.TIMES,
            cnf.ITEMS,
            cnf.WORDS)
    set_stages(w)
    return w

def story(w: wd.World):
    return w.story("君と私の恋愛教室",
            ch1(w),
            ch2(w),
            ch3(w),
            ch4(w),
            ch5(w),
            ch6(w),
            ch7(w),
            ch8(w),
            ch9(w),
            ch10(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

