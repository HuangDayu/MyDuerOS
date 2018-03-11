# -*- coding: utf-8 -*-

from app import wakeup_trigger_main

while True:
    if "" != wakeup_trigger_main.getText():
        print(wakeup_trigger_main.getText())
    else:
        pass