
# !/usr/bin/python3
# -*- coding: utf-8 -*-
from wechat.models import Magnet, NodeSs, SsInviteCode, UserCode, User, UserBind, SsNode


class UserService(object):

    def __init__(self):
        self

    # 获取用户已绑定的UserID
    def get_UserId_By_OpenId(self, openid):
        user = UserBind.objects.filter(openid=openid)
        return user[0].userid if user else False

    # 获取用户信息资料
    def get_User_By_ID(self, id):
        user = User.objects.using('db1').filter(id=id)
        return user[0] if user else False
