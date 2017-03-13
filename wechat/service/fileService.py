#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import time
import urllib.parse
class File(object):
    def __init__(self):
        self
    # 生成一个新的文件夹或返回文件路径
    def mkdirFile(self):
        # 定义文件夹的名字
        t = time.localtime(time.time())
        foldername = str(t.__getattribute__("tm_year"))+"-"+str(t.__getattribute__("tm_mon"))+"-"+str(t.__getattribute__("tm_mday"))
        picpath = 'D:\\MagnetDownload\\%s' % (foldername) #下载到的本地目录
        if not os.path.exists(picpath):   #路径不存在时创建一个
            os.makedirs(picpath)
            print('创建文件夹')
        return picpath

    # 判断文件是否存在，存在则打开，否则新建
    def judgeFile(self,fileName):
        fileName = urllib.parse.unquote(fileName)
        file = open(fileName,'a')
        print('正在存放磁力链接......')
        return file
