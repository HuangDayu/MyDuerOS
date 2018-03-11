# -*- coding: utf-8 -*-

import sys
sys.path.append('app/')
import wakeup_trigger_main

while True:
    if wakeup_trigger_main.getText() != "":
        print(wakeup_trigger_main.getText())
    else:
        pass