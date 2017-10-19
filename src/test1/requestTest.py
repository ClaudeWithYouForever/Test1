# -*- coding: utf-8 -*-
'''
Created on Oct 9, 2017

@author: ClaudeGan
'''
import requests
import json

# preload = {'key1':'value1','key2':'value2'}
# # r=requests.get("http://pythontab.com/justTest",params=payload);
# # print r.url
# r = requests.post('http://pythontab.com/postTest',json=preload)
# print r.text.encode('utf-8')
def saveIMG(imgURL,imgName = 'test.jpg'):
    r=requests.get(imgURL,stream=True)
    image = r.content
    dir = 'f:/python_test/img/'
    finallyPath = ''.join([dir,imgName])
    print("保存图片"+dir+imgName+"\n")
    with open(finallyPath,'wb') as jpg:
        jpg.write(image);
        
if __name__ == '__main__':
    saveIMG('http://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1507555056754&di=de7397dc3d5836ecf45f8d35298372a1&imgtype=0&src=http%3A%2F%2Fh.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F8c1001e93901213f4fcd061c5de736d12e2e9570.jpg');

