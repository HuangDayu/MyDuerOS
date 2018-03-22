#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')

from app.framework import player
playObj = player.Player()
#file:///tmp/205472.mp3
class Modular:
    def getDuerOSRet(self,string):
        string = string.replace("u'", "'")  # 这里比较简单，实际中需要用正则条件替换
        string = string.replace("'", '"')
        textDict = json.loads(string)
        ret = textDict['payload']['text']
        # ret = ret.decode('unicode-escape')
        print("返回结果:" + ret)
        if ret == '打开台灯':
            player.Player.setIsPlay(False)
            print('设置为False')
        return ret