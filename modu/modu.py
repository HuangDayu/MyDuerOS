# -*- coding: utf-8 -*-
import wakeup_trigger_main

def getText():
    text=wakeup_trigger_main.getText()
    text=re.sub('\'','\"',text)
    textDict = json.loads(text) #产生dict
    text=textDict['payload']['text']
    print(text)
    return text