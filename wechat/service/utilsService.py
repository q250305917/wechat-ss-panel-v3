#!/usr/bin/python3
# -*- coding: utf-8 -*-
#工具服务类
import base64
import hashlib
import time
import gzip
import http.cookiejar
import urllib.request as request
class Utils(object):
    def __init__(self):
        self

    header = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'www.btpeer.com',
        'DNT': '1'
    }

    #简单校验Token
    def tokenCheck(self, code):
        token = 'yunso'
        if(code == token):
            return True
        else:
            return False

    #简单单位转换
    def transformation(self, size, cp):
        if cp == 'GB':
            size = float(size)*int(1024)*int(1024)*int(1024)
            return int(size)
        elif cp == 'MB':
            size = float(size)*int(1024)*int(1024)
            return int(size)
        elif cp == 'KB':
            size = float(size)*int(1024)
            return int(size)

    #单位转换
    def flowAutoShow(self, value):
        #量换算
        tokb = 1024
        tomb = 1024*1024
        togb = tomb*1024
        if value > togb:
            return str(round((value/togb), 2))+"GB"
        elif value > tomb:
            return str(round((value/tomb), 2))+"MB"
        elif value > tokb:
            return str(round((value/tokb), 2))+"KB"
        else:
            return str(round(value,2))+""


    #获取当前时间
    def dateformation(self):
        ISOTIMEFORMAT='%Y-%m-%d %X'
        t = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
        return t

        # 解压页面
    def ungzip(self,data):
        data = gzip.decompress(data)
        return data

    # 浏览器头响应
    def getOpener(self):
        # deal with the Cookies
        cj = http.cookiejar.CookieJar()
        pro = request.HTTPCookieProcessor(cj)
        opener = request.build_opener(pro)
        header = []
        for key, value in self.header.items():
            elem = (key, value)
            header.append(elem)
        opener.addheaders = header
        return opener

    #中文编码转换base64
    def utf8_base64(self, string):
        unicode = string.encode("gbk")
        newStr = base64.b64encode(unicode)
        # md5 = hashlib.md5()
        # md5.update(unicode)
        # endMd5 = md5.hexdigest()
        return newStr

    #base64编码转换中文
    def base64_utf8(self, string):
        unicode = base64.b64decode(string)
        newStr = unicode.decode('gbk')
        return newStr

    #md5加密处理
    def md5(self, str):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()

    # Time 当前日期和时间的时间戳
    # 只返回日期时间戳
    def timeStamp(self, Time):
        lastCheck = time.strftime('%Y-%m-%d 00:00:00', time.localtime(Time))
        timeArray = time.strptime(lastCheck, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        return timeStamp