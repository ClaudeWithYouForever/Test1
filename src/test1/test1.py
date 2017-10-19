# -*- coding: utf-8 -*-
'''
Created on Oct 9, 2017

@author: ClaudeGan
'''
class dog(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print "%s吃啊飒飒" %(self.name)
def run():
    print "runing ....asas"
if __name__ == "__main__":
    choise = raw_input("请输入要调用的方法")
    d = dog('Happy')
    if hasattr(d,choise):#判断一个对象是否有对应的字符串方法
        func=getattr(d,choise)#根据字符串去获取对象里相应的方法或属性的内存地址对象
        func()
    else:
        setattr(d,choise,run())#setattr（obj，y，fun）相当于obj.y=fun，fun可以是属性或者方法
        #d.choise
        v=getattr(d,choise)
        print(v)
    
        
    