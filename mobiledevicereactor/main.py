#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013/01/26

@author: koyamatk
'''
import time

from ActionExecutor import ActionExecutor

if __name__ == '__main__':
    ae = ActionExecutor()
    for i in xrange(10):
        ae.execute()
        print "before sleep"
        time.sleep(5)
        print "after sleep"