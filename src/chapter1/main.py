# -*- coding: utf-8 -*-
"""Chapter: story 1
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.chapter1.e1_dumped import ep_dumped
from src.chapter1.e2_runaway import ep_runaway
from src.chapter1.e3_passout import ep_passout
from src.chapter1.e4_onthebed import ep_onthebed
from src.chapter1.e5_teachmelove import ep_teachmelove


## define alias
W = Writer
_ = W.getWho()

## chapter
def ch1_cantsay(w: World):
    return w.chapter("第一話「もう恋なんてしない」",
            ep_dumped(w),
            ep_runaway(w),
            ep_passout(w),
            ep_onthebed(w),
            ep_teachmelove(w),
            )
