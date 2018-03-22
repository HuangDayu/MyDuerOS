#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import os
cf = configparser.ConfigParser()
path2=os.path.abspath('.')
print(path2)
path3=path2+"/config.ini"
cf.read(path3)

def getConfigValue(groupName,name):
    value =  cf.get(groupName,name)
    return value