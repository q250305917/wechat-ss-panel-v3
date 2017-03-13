#!/usr/bin/python3
# -*- coding: utf-8 -*-
from wechat.models import Magnet

class Mysql(object):
    def __init__(self):
        self

    # 连接数据库保存数据
    # key判断是否来自后台自动爬虫
    def connect(self, data, lable, key=0):
        for i in data:
            str = "'"
            if i['title'].find(str):
                i['title'] = i['title'].replace("'"," ")
            i['title'] = i['title'] if i['title'] else 0
            i['size'] = i['size'] if i['size'] else 0
            i['listMagnet'] = i['listMagnet'] if i['listMagnet'] else 0
            i['hot'] = i['hot'] if i['hot'] else 0
            i['listXunlei'] = i['listXunlei'] if i['listXunlei'] else 0
            if not key:
                if not Magnet.objects.filter(mgTitle__contains=i['title']):
                    new = Magnet(mgTitle=i['title'], mgSize=i['size'], mgList=i['listMagnet'], mgCreate=i['create'], mgHot=i['hot'], mgLable=lable, mgList_1=i['listXunlei'])
                    new.save()
            else:
                if not (Magnet.objects.filter(mgTitle__contains =  i['title']) or len(i['title']) > 255):
                    Magnet.objects.get_or_create(mgTitle=i['title'], mgSize=i['size'], mgList=i['listMagnet'], mgCreate=i['create'], mgHot=i['hot'], mgLable=lable, mgList_1=i['listXunlei'])

    # 查询热门相关,查询排行前15的
    def getHotList(self):
        sql = "select *,MAX(mgHot) AS sort from app_Magnet group by mgLable ORDER BY sort DESC"
        data = Magnet.objects.raw(sql)[:10]
        return data