# -*- coding: utf-8 -*-
'''
Created on Oct 10, 2017

@author: ClaudeGan
'''
import time
import datetime

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print now
# import calendar
# cal = calendar.month(2017,10)
# print cal
# print time.localtime()
print datetime.datetime.now()+datetime.timedelta(hours=-3)
print datetime.datetime.combine(datetime.datetime.now(),datetime.time(12,1,1,1))
import time
last_month = time.localtime()[1]-1 or 12
print last_month

