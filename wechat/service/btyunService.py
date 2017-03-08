#!/usr/bin/python3
# -*- coding: utf-8 -*-
import bs4
import urllib.request as request
import socket
from wechat.service.mysqlService import Mysql
from wechat.service.utilsService import Utils

class BTyunCatch(object):
    def __init__(self):
        self

    # 获取html页面
    def getHtml(self, url):
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码18030
        timeout = 20
        socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
        utils = Utils()
        head = utils.getOpener()
        try:
            page = head.open(url)
        except request.URLError:
            return 0
        if page:
            html = page.read()
            data =utils.ungzip(html)
            return data.decode('utf-8')
        else:
            return "0"

    #
    def getHash(self, url, lable):
        html = self.getHtml(url)
        if html:
            # file = judgeFile(filePath)
            soup = bs4.BeautifulSoup(html, "lxml")
            data = soup.select(".media-list li")
            datas = []
            utils = Utils()
            for i in data:
                _title = i.select("h4")[0].get_text()
                _listMagnet = i.select("h4 a")[0]['href'][1:][:-5] #获取磁力链接
                _size = i.select(".media-more span")[1].get_text()
                _create = i.select(".media-more span")[0].get_text()
                _hot = i.select(".media-more span")[2].get_text()
                size = utils.transformation(_size[:-2], _size[-2:])
                msg = {
                    'title': _title,
                    'listMagnet': _listMagnet,
                    'listXunlei': '',
                    'size': size,
                    'create': _create,
                    'hot': _hot
                }
                datas.append(msg)
                # file.write(str(title)+str(list))
            mysql = Mysql()
            mysql.connect(datas, lable)
            # file.close()
            return datas
        else:
            return 0

