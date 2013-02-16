#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013/01/26

@author: kawamuramasato
'''

import pyaudio
import wave
import commands

class Action(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def do_action(self,user_name,device_status):
        """
        Action
        """
        print user_name
        print device_status
        print "Not Implements"
        
        chunk=1024
        filename
        if device_status == False:
            filename='okaeri.wav'
        else:
            filename='itera.wav'
        
        playdata = "aplay "+ filename
        results_aplay = commands.getoutput(playdata)
         
        '''    
        wf = wave.open(filename,'rb')
        p=pyaudio.PyAudio()
        stream = p.open(format =p.get_format_from_width(wf.getsampwidth()),channels = wf.getnchannels(),rate = wf.getframerate(),output = True)
        ##print wf.getformat_from_width(wf.
        remain = wf.getnframes()
    
        while remain > 0 :
            s = min(chunk, remain)
            data = wf.readframes(s)
            stream.write(data)
            remain = remain - s
        stream.close()
        p.terminate()
        '''
        print "end of module"
    
        
