'''
Created on 2013/03/16

@author: koyamatk
'''

import sqlite3
import datetime

class MailAction(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def do_action(self,user_name,device_status):
        pass
    
        if device_status == True:
            line = 'hibiya'
            direction = 'nakameguro'
    
            d = datetime.datetime.now()
            is_weekday = d.weekday()
            operation_date = ''
            
            if is_weekday == 5 or is_weekday == 6: 
                operation_date = 'holiday'
            else:
                operation_date = 'weekday'
            
            con = sqlite3.connect("mobiledevicereactor.sqlite")
            c = con.cursor()
            #query = "select line, direction, departure_time from timetable where line=" + line + " and direction="+ direction + " and operation_date="+ operation_date + " and departure_time>time('now','localtime') and departure_time<time('now', '+60 minutes', 'localtime');"
            query = 'select line, direction, departure_time from timetable where line="' + line + '" and direction="'+ direction + '" and operation_date="'+ operation_date + '" and departure_time>time("now","localtime") and departure_time<time("now", "+360 minutes", "localtime");'
    
            c.execute(query)
            list = c.fetchall()
            for row in list:
                print row
            
            c.close()
            con.close()