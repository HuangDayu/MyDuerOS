#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import os
import time

import datetime
import pygame
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
            md=Modular()
            md.findChildren()
            #self.findChildren()
            self.getTTS("好的")
        return ret

    #为授权使用
    def getTTS(self,text):
        playObj.setIsPlay(False)
        result = aipSpeech.synthesis(text, 'zh', 1, {
            'vol': 5,
        })
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('/tmp/tts.mp3', 'wb') as f:
                f.write(result)

        fileUrl="file:///tmp/tts.mp3"
        os.system('sudo mplayer /tmp/tts.mp3')
        #playObj.play(fileUrl)
        # file=r'/tmp/tts.mp3'
        # pygame.mixer.init()
        # print("播放tts.mp3")
        # track = pygame.mixer.music.load(file)
        # pygame.mixer.music.play()
        #time.sleep(10)
        #pygame.mixer.music.stop()

    def findChildren(self):
        child_mothod = getattr(self,"publishs")
        child_mothod()

    # class father():
    #     def call_children(self):
    #         child_method = getattr(self, 'out')  # 获取子类的out()方法
    #         child_method()  # 执行子类的out()方法
    #
    # class children(father):
    #     def out(self):
    #         print "hehe"

    all_subclasses = {'0': '0'}

    def get_all_classes(model):
        """
        获取父类的所有子类
        """

        for subclass in model.__subclasses__():
            # print(subclass._meta.abstract)
            if (not (subclass.__name__) in Modular.all_subclasses.keys()) and (not subclass._meta.abstract):
                Modular.all_subclasses[subclass.__name__] = subclass
            Modular.get_all_classes(subclass)
            print(Modular.all_subclasses.__str__())
        return Modular.all_subclasses

    def do_collection(model=None, date=None):
        """
        执行收集数据的方法
        """
        allclasses = Modular.get_all_classes(StatBaseModel)
        if date:
            date = datetime.date.today() + datetime.timedelta(days=-1)
        if model:
            fn_collect = getattr(allclasses[model], 'collect', None)
            if callable(fn_collect):
                fn_collect(date)
            print("执行{0}的collect 方法".format(model))
            return
        for item, value in allclasses.items():
            fn_collect = getattr(value, 'collect', None)
            if callable(fn_collect):
                fn_collect(date)
                print("执行{0}的collect 方法".format(item))
