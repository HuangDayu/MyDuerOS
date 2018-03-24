#!/usr/bin/env python
# -*- coding: utf-8 -*-
class father():
    def call_children(self):
        child_method = getattr(self, 'out')# 获取子类的out()方法
        child_method() # 执行子类的out()方法

class children(father):
    def out(self):
        print "hehe"


child = children()
child.call_children()