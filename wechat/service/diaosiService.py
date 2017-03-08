#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import bs4
from wechat.service.mysqlService import Mysql
from wechat.service.utilsService import Utils
class DiaosiCatch(object):
    def __init__(self):
        self

    # 获取html页面
    def getHtml(self, url):
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码18030
        timeout = 20
        socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
        #sleep_download_time = 5
        #time.sleep(sleep_download_time) #这里时间自己设定
        utils = Utils()
        head = utils.getOpener()
        page = head.open(url)
        if page:
            html = page.read()
            data =utils.ungzip(html)
            return data.decode('utf-8')
        else:
            return "0"

    #解析页面分析获取数据
    def getHash(self, url, lable):
        html = self.getHtml(url)
        if html:
            # file = judgeFile(filePath)
            soup = bs4.BeautifulSoup(html,"lxml")
            data = soup.select(".mlist li")
            datas = []
            for i in data:
                _title = i.select(".T1")[0].get_text()
                _listMagnet = i.select(".dInfo a")[0]['href']
                _listXunlei = i.select(".dInfo a")[1]['href']
                _size = i.select(".BotInfo span")[0].get_text()
                # _create = i.select(".BotInfo span")[2].get_text()
                _hot = i.select(".BotInfo span")[3].get_text()
                _s = _size.split()
                utils = Utils()
                date = utils.dateformation()
                size = utils.transformation(_s[0],_s[1])
                # list = str(self.host)+str(_list[0].get_text()[5:])
                msg = {
                    'title': _title,
                    'listMagnet' : _listMagnet[20:],
                    'listXunlei' : _listXunlei[10:],
                    'size' : size,
                    'create': date,
                    'hot':_hot
                }
                datas.append(msg)
                # file.write(str(title)+str(list))
            mysql = Mysql()
            mysql.connect(datas,lable)
            # file.close()
            return datas
        else:
            return 0

