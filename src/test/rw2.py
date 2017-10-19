# -*- coding: utf-8 -*-
'''
Created on Sep 26, 2017
@author: Administrator
'''
class rain:
    def __init__(self,id,acc,site):
        self.id = id
        self.acc = acc
        self.site = site
# data = []
# f = open('F:\\python_test\\test.txt','r') 
# f.readline();
# for line in f:
#     lines =  line.decode('gb2312').split('，')
#     obj = rain(lines[0],lines[1],lines[2])
#     data.append(obj)
data =[]
f=open("F:\\python_test\\test1.txt","r")
f.readline()#第一行是列，可以将文件移到第二行开始处
for line in f:
        lines=line.split("，")
        obj=rain(lines[0],lines[1],lines[2])
        data.append(obj)
f.close()
print len(data)
          
    
