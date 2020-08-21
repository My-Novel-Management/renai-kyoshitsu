# -*- coding: utf-8 -*-
"""Story config.
"""
################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
# 2) AREAS
#       エリア設定
# 3) STAGES
#       舞台基本設定
# 4) DAYS
#       年月日設定
# 5) TIMES
#       時間帯基本設定
# 6) ITEMS
#       小道具設定
# 7) WORDS
#       辞書設定
# 8) RUBIS
#       ルビ設定
# 9) LAYERS
#       レイヤ設定
#
################################################################


PERSONS = (
        # Tag / 氏,名 / 歳 / 誕生日 / 性別 / 職業 / 呼称 / 紹介
        ("taro", "太郎", "", 40,(1,1), "male", "作家"),
        ##
        ("airi", "愛里", "沖,愛里", 20,(1,1), "female", "アルバイト（喫茶店）", "me:アタシ:k_wakui:祐介"),
        ("yuri", "優里", "沖,優里", 27,(1,1), "female", "入院中（心臓）", "me:ワタシ"),
        ("harada", "原田", "原田,誠司", 27,(1,1), "male", "作家", "me:僕"),
        ## 出版社
        ("natsu", "ナツコ", "村瀬,ナツコ", 28,(1,1), "female", "編集者", "me:わたし"),
        ## 喫茶店
        ("wakui", "涌井", "涌井,祐介", 27,(1,1), "male", "喫茶店店員", "me:俺"),
        ("miho", "美保", "小田川,美保", 28,(1,1), "female", "喫茶店店員", "me:私"),
        ("shino", "詩乃", "織田,詩乃", 19,(1,1), "female", "大学生", "me:わたし"),
        ## 病院
        ## その他
        )

AREAS = (
        # Tag / 名前 / x,y / 備考
        )

STAGES = (
        # Tag / 名前 / Area / 紹介
        ("wakuiapart", "涌井のアパート", "Tokyo"),
        ("airiapart", "愛里のアパート", "Tokyo"),
        ("haradamanshion", "原田のマンション", "Tokyo"),
        ## 病院
        ("yuriroom", "優里の病室", "Tokyo"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("current", "current", 1,1,2020),
        ("airi_depart", "愛里がふられた日", 12,13, 2018),
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        )

WORDS = (
        # Tag / 名前 / 紹介
        )

RUBIS = (
        # Base / Rubi / Exclusion / Type
        )

LAYERS = (
        # Key / Title / Words
        )

