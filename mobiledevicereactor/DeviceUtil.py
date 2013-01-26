#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013/01/26

@author: kawamuramasato
'''
import commands


class DeviceUtil(object):
    '''
    classdocs
    '''
    prev_macaddress_list = []
    registered_users = [('00:00:00:00:00:00','user1'),('00:00:00:00:00:01','user2')]

    def __init__(self):
        '''
        Constructor
        '''
        
    def get_devices_status(self):
        """
        同一LAN上に存在する端末のMACアドレスをスキャンし、MACアドレスの一覧と前回スキャンした際に
        存在したかのステータスをリスト形式で返却する。
        出ていったMACアドレスには"True"を、入ってきたMACアドレスには"False"を付与している。
        
        :rtype: list
        :return: [(macaddress(string), status(boolean))]
        """
        macaddress_list = self._scan_macaddress()
        
        outgoing_mac_addr = [mac for mac in self.prev_macaddress_list if mac not in macaddress_list]
        incomming_mac_addr = [mac for mac in macaddress_list if mac not in self.prev_macaddress_list]
        ## existing_mac_addr = [mac for mac in self.prev_macaddress_list if mac in macaddress_list]
        
        devices_status = []
        
        for mac in outgoing_mac_addr:
            devices_status.append((mac,True))
        
        for mac in incomming_mac_addr:
            devices_status.append((mac,False))
        
        self.prev_macaddress_list = macaddress_list
        
        return devices_status
    
    def get_registered_devices(self):
        """
        登録されているMACアドレスとそれに対応するユーザ名の一覧を返す。
        
        :rtype: List
        :return: [(macaddress(string),user_name(string))]
        """    
        return self.registered_users
        
        
    
    def get_registered_device(self, macaddress):
        """
        引数で指定するMACアドレスに対応するユーザを登録されているリストから検索し、
        MACアドレスとユーザ名の組を返却する
        :param macaddress String: macaddress
        :rtype: tuple
        :return: (macaddress(string), user_name(string))
        """
        for registered_user in self.registered_users:
            if macaddress == registered_user[0]:
                return registered_user
        
        return (macaddress,'')
    
    def _scan_macaddress(self):
        """
        :return: ([macaddress(string)])
        """
        
        result_arp = commands.getoutput("arp -a")
        macaddr_list = [result_arp.split(' ')[3] for result_arp in result_arp.split('¥n')]
        
        return macaddr_list
        
        pass