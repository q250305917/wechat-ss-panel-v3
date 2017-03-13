#!/usr/bin/python3
# -*- coding: utf-8 -*-
import bs4
import time
import urllib.request as request
import urllib.error as error
import pyquery as jq
import socket
from wechat.service.mysqlService import Mysql
from wechat.service.utilsService import Utils

class MagnetCatch(object):
    def __init__(self):
        self

    # 获取html页面
    def getHtml(self,url):
        # if page == 1:
        #     sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码18030
        timeout = 20
        socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
        # sleep_download_time = 3
        # time.sleep(sleep_download_time) #这里时间自己设定
        try:
            page = request.urlopen(url)
        except request.URLError:
            return 0
        if page:
            html = page.read()
            return html.decode('utf-8')
        else:
            return "0"

    # 获取页面分析页面数据并抓取所需数据
    def getHash(self, url, lable):
        html = self.getHtml(url)
        # print(html)
        if jq.PyQuery(html).find(".search-item"):
            # file = judgeFile(filePath)
            soup = bs4.BeautifulSoup(html,"lxml")
            data = soup.select(".search-item")
            datas = []
            for i in data:
                _title = i.select(".item-title a")
                _list = i.select(".item-list p")
                _create = i.select(".item-bar span b")[0].get_text()
                _size = i.select(".item-bar span b")[1].get_text()
                _hot = i.select(".item-bar span b")[2].get_text()
                _s = _size.split()
                utils = Utils()
                size = utils.transformation(_s[0], _s[1])
                title = _title[0].get_text()
                _listMagnet = _list[0].get_text()[5:]
                msg = {
                    'title': title,
                    'listMagnet': _listMagnet[20:],
                    'listXunlei': '',
                    'size': size,
                    'create': _create,
                    'hot': _hot
                }
                datas.append(msg)
            mysql = Mysql()
            mysql.connect(datas, lable)
            # file.close()
            return datas
        else:
            return 0

