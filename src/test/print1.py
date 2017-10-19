# -*- coding: utf-8 -*-

'''
Created on Sep 26, 2017

@author: Administrator
'''
import codecs
import chardet
with codecs.open("F:\\python_test\\test.txt","r") as f:
        lines = f.readlines()
        print len(lines)
        for line in lines:
            print chardet.detect(line)
            print 'aaa'
        
with codecs.open("F:\\python_test\\test.txt","w") as f_w:
    for line in lines:
        line = line.decode('gb2312').encode('utf-8')
        print chardet.detect(line)
        print 'bbb'
        if "taste" in line:
            line = line.replace("taste","tasting")
            arr = [line,'123']
            line = ''.join(arr)
        print chardet.detect(line)
        print 'ccc'
        f_w.write(line.decode('utf-8'))
