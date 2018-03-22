#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class Modu:
    #对象调用
    def printRet(self,ret):
        print("new Modular().printRet%s",ret)

    #静态方法，类调用
    @staticmethod
    def printRetStatic(ret):
        print("Modular().printRetStatic%s", ret)



def printRet(ret):
    print("mod_mian.printRet()%s", ret)

# while True:
#     if "" != wakeup_trigger_main.getText():
#         print(wakeup_trigger_main.getText())
#     else:
#         pass


    # # text1=re.sub('\'','\"',text1)
    # text1 = text1.replace("'", '"')
    # text1 = text1.replace("u", "")  # 这里比较简单，实际中需要用正则条件替换
    # text1 = text1.replace("\\", "/")
    # textDict = json.loads(text1)
    # text1 = textDict['payload']['text']
    # text = text1

if __name__ == '__main__':
    pass


    # text1=str(ret)
    # if 'FINAL' in text1:
    #     #text1=re.sub('\'','\"',text1)
    #     text1 = text1.replace("'", '"')
    #     text1 = text1.replace("u", "") #这里比较简单，实际中需要用正则条件替换
    #     text1 = text1.replace("\\", "/")
    #     textDict = json.loads(text1)
    #     text1=textDict['payload']['text']
    #     text=text1
    # else :
    #     text=""