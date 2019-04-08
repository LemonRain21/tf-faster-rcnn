# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 09:23:44 2019

@author: QinLong

批量修改文件名

"""

import os
path='F:\\VOC2018\\Annotations\\twotxt\\'       

#获取该目录下所有文件，存入列表中
f=os.listdir(path)
name_len = 6 #图片名字的长度

n=1
for i in f:
    
    #设置旧文件名（就是路径+文件名）
    oldname=path+f[n-1]
    
    #设置新文件名
    prefix = '0'*(name_len - len(str(n)))
    newname=path+prefix+str(n)+'.txt'
    
    #用os模块中的rename方法对文件改名
    os.rename(oldname,newname)
    print(oldname,'======>',newname)
    
    n+=1
