# -*- coding: utf-8 -*-
import os
from app.framework.player import Player
import random

class PromptTone(object):
    '''
    提示音播放类(用于唤醒态提示)
    '''

    mp3List = ['snowboy-10.mp3','snowboy-13.mp3','snowboy-1.mp3','snowboy-4.mp3','snowboy-7.mp3',
        'snowboy-11.mp3','snowboy-14.mp3','snowboy-2.mp3','snowboy-5.mp3','snowboy-8.mp3',
        'snowboy-12.mp3','snowboy-15.mp3','snowboy-3.mp3','snowboy-6.mp3','snowboy-9.mp3']
    listLen=len(mp3List)

    def __init__(self, player):
        self.player = player
        i=random.randint(0, PromptTone.listLen)
        url='../resources/'+PromptTone.mp3List[i]
        resource = os.path.realpath(os.path.join(os.path.dirname(__file__), url))
        self.resource_uri = 'file://{}'.format(resource)

    def play(self):
        '''
        提示音播放
        :return:
        '''
        self.player.play(self.resource_uri)
