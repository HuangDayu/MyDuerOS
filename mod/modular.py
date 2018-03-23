#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import os
from aip.aip import AipSpeech
if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')

from app.framework import player
playObj = player.Player()

from cnf import config as cnfg
APP_ID = cnfg.getConfigValue("user","app_id")
API_KEY = cnfg.getConfigValue("user","client_id")
SECRET_KEY = cnfg.getConfigValue("user","client_secret")
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

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
            playObj.setIsPlay(False)
            self.getTTS("好的")
        return ret

    #为授权使用
    def getTTS(self,text):
        result = aipSpeech.synthesis(text, 'zh', 1, {
            'vol': 5,
        })
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('/tmp/tts.mp3', 'wb') as f:
                f.write(result)

        fileUrl="file:///tmp/tts.mp3"
        playObj.play(fileUrl)


