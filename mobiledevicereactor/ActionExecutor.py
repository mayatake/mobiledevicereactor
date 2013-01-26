#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013/01/26

@author: kawamuramasato
'''
from DeviceUtil import DeviceUtil

class ActionExecutor(object):
    '''
    classdocs
    '''
    dev_util = DeviceUtil()

    def __init__(self):
        '''
        Constructor
        '''
    
    def execute(self):
        """
        MobileDeviceReactorのメイン処理 
        """
        # get status 
        dev_status = self.dev_util.get_devices_status()
        
        # (user_name, status)
        users = [(self.dev_util.get_registered_device(macaddress)[1], status) \
                        for macaddress, status in dev_status]
        # Load Actions
        actions = self.get_actions()
        # IN FUTURE; do_action is execute of threading. 
        for action in actions:
            for user_name, status in users:
                try:
                    action.do_action(user_name,status)
                except AttributeError,e:
                    print e
        
    def get_actions(self):
        """
        読み込むプラグイン名を返す
        将来的にはpkg_resourceを利用する。
        
        :rtype: List
        :return: アクションオブジェクトのリストを返す
        """
        # TODO: 定数化
        #config = ConfigParser()
        #config.read("../conf/plugins.ini")
        #config.items('plugins')
        module_names = {'Action':'Action'}
        modules =[]
        for name in module_names.keys():
            module = __import__(name, globals(), locals(), [module_names[name]])
            c = getattr(module,module_names[name])
            modules.append(c())
        return modules
