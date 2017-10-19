# -*- coding: utf-8 -*-
'''
Created on Oct 10, 2017

@author: ClaudeGan
'''
# import json
# data = {"name":"小名","gender":"男","data":{"name":"小名","gender":"男"}}
# jsondata = json.dumps(data,ensure_ascii=False,sort_keys=True,indent=4)
# 
# print(jsondata)
dir = 'f:/python_test/img/新建文本文档.txt'.decode('utf-8')
with open(dir,'a+') as file:
   for line in file.readlines():
        print line.decode('gb2312')
        file.write('\r\n中文'.encode('gb2312'))