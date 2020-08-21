# -*- coding: utf-8 -*-
"""Config: the renai-kyoshitsu
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
PERSONS = (
        # main
        ("harada", "原田", "原田,貴明", 27, "male", "小説家", "me:僕"),
        ("airi", "愛里", "沖,愛里", 20, "female", "バイト", "me:アタシ:harada:センセ"),
        ("yuri", "優里", "沖,優里", 27, "female", "入院患者", "me:私:harada:君"),
        # sub
        ("miki", "美樹", "桜庭,美樹", 20, "female", "大学生", "me:私"),
        ("murase", "村瀬", "村瀬,ナツコ", 29, "female", "編集者", "me:わたし"),
        ("takamasa", "高正", "高正,誠司", 47, "male", "内科医", "me:私"),
        ## family
        # mob
        # extra
        )

CHARAS = (
        )

STAGES = (
        # Area
        # Place
        # Ride
        # Part
        )

DAYS = (
        # main
        ("current", "令和元年", 1,10, 2019),# NOTE: 平成最後
        # sub
        )

TIMES = (
        ("earlymorning", "早朝", 6,0),
        ("morning", "朝", 8,0),
        ("inmorning", "午前", 10,0),
        ("noon", "正午", 12,0),
        ("afternoon", "午後", 14,0),
        ("evening", "夕方", 17,0),
        ("night", "夜", 20,0),
        ("deepnight", "深夜", 2,0),
        )

ITEMS = (
        # main
        # sub
        )

WORDS = (
        )

