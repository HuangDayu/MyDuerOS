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


if __name__ == '__main__':
    pass