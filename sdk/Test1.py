# -*- coding: utf-8 -*-
from mod import Test2 as md #从包里导入模块，并创建模块的引用

import mod #导入包
modObj3=mod.Test2 #创建包引用

modObj1 = mod.Test2 #一个模块创建对象

modObj2 = md.Modu() #创建一个类的对象
# mod_main2 = mod.

import json
import sys
if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')

def myPrint():
        print("Test2.myPrint()")
        modObj1.printRet("import pgk")
        md.printRet("import mode")
        modObj2.printRet("import class obj")
        modObj3.Modu.printRetStatic("import class static ")
        md.Modu.printRetStatic("md.Modu.printRetStatic")
        md.Modu().printRet("md.Modu().printRet")

def testJson():
        string="{u'header': {u'dialogRequestId': u'521ffb5061314bdd8a47edcf7f5871c2', u'namespace': u'ai.dueros.device_interface.screen', u'name': u'RenderVoiceInputText', u'messageId': u'5cafb1ded6144a77a94cf4884f91e1d3'}, u'payload': {u'text': u'\u660e\u5929\u5929\u6c14\u600e\u4e48\u6837', u'type': u'INTERMEDIATE'}}"
        string = string.replace("u'", "'")  # 这里比较简单，实际中需要用正则条件替换
        print(string)
        string = string.replace("'", '"')
        textDict = json.loads(string)
        ret = textDict['payload']['text']
        #ret = ret.decode('unicode-escape')
        print("返回结果::::::::::::::::::" + ret)

myPrint()
testJson()