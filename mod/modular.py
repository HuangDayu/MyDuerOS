#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

class Modular:
    def getDuerOSRet(self,ret):
        ret=ret.decode('utf-8')
        ret = ret.replace("'", '"')
        ret = ret.replace("u", "")  # 这里比较简单，实际中需要用正则条件替换
        ret = ret.replace("\\", "/")
        textDict = json.loads(ret)
        ret = textDict['payload']['text']
        print("返回结果::::::::::::::::::"+ret)
        return ret