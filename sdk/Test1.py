# -*- coding: utf-8 -*-
from mod import Test2 as md #从包里导入模块，并创建模块的引用

import mod #导入包
modObj3=mod.Test2 #创建包引用

modObj1 = mod.Test2 #一个模块创建对象

modObj2 = md.Modu() #创建一个类的对象
# mod_main2 = mod.


def myPrint():
        print("Test2.myPrint()")
        modObj1.printRet("import pgk")
        md.printRet("import mode")
        modObj2.printRet("import class obj")
        modObj3.Modu.printRetStatic("import class static ")
        md.Modu.printRetStatic("md.Modu.printRetStatic")
        md.Modu().printRet("md.Modu().printRet")


myPrint()