# -*- coding: utf-8 -*-

from sdk.wakeup_trigger_main import wakeup_trigger_main

while True:
    if wakeup_trigger_main.getText() != "":
        print(wakeup_trigger_main.getText())
    else:
        pass