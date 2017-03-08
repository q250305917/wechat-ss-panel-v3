#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import hashlib
import urllib.parse
import wechat.wechat.receive as receive
import wechat.wechat.reply as reply
import random
from wechat.params import Params
from django.http import HttpResponse,HttpResponseBadRequest
from wechat.service.magnetService import MagnetCatch
from wechat.service.diaosiService import DiaosiCatch
from wechat.service.btyunService import BTyunCatch
from wechat.service.utilsService import Utils
from wechat.service.wechatService import WeChat
from wechat.models import Magnet, NodeSs, SsInviteCode, UserCode, User, UserBind, SsNode
from json import dumps #接收和返回JSON
import urllib


#包装csrf请求，避免django认为其实跨站攻击脚本
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
#主页显示
wechat = WeChat()
AccessToken = wechat.getAccessToken()

def home(request):
    count = Magnet.objects.count() * int(11)
    return HttpResponse(AccessToken)

#爬行数据
def getList(name):
        urlname = urllib.parse.quote(name)
        pages_2 = 1
        diaosi = DiaosiCatch()
        while pages_2 < 20:
            host_2 = "http://www.diaosisou.com/list/"+str(urlname)+"/"+str(pages_2)
            diaosiHtml = diaosi.getHash(host_2, name)
            if diaosiHtml:
                pages_2 += 1
            else:
                pages_2 = 21

#后台爬虫
@csrf_exempt
def bgurlBTpeer(name):
    urlname = urllib.parse.quote(name)
    pages = 1
    Catch = MagnetCatch()
    while pages < 20:
        host = "http://www.btpeer.com/list/"+str(urlname)+"-first-asc-"+str(pages)
        btpeerHtml = Catch.getHash(host, name)
        # pages += btpeerHtml
        if btpeerHtml:
            pages += 1
        else:
            pages = 21

#后台爬虫
@csrf_exempt
def bgurlBTyun(name):
    urlname = urllib.parse.quote(name)
    pages = 1
    Catch = BTyunCatch()
    while pages < 20:
        host = "http://www.btyunsou.com/search/"+str(urlname)+"_ctime_"+str(pages)+".html"
        btyunHtml = Catch.getHash(host, name)
        # pages += btpeerHtml
        if btyunHtml:
            pages += 1
        else:
            pages = 21

#微信公众号后台统一入口
@csrf_exempt
def checkToken(request):
    if request.method == 'GET':
        signature = request.GET.get('signature')
        echostr = request.GET.get('echostr')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        token = Params.APP_TOCKEN
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        for val in list:
            sha1.update(val.encode())
            hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature: ", hashcode, signature)
        if hashcode == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse('Verify Failed')
    else:
        webData = request.body
        # print("Handle Post webdata is ", webData)   #后台打日志
        recMsg = receive.parse_xml(webData)
        if recMsg.MsgType == 'event':
            if recMsg.Event == 'subscribe':
                key = Params.APP_NAME
            else:
                key = recMsg.EventKey.decode("utf-8")
        else:
            key = recMsg.Content.decode("utf-8")
        openid = recMsg.FromUserName
        L = validate(key, openid)
        if L[0] == True:
            con = getTextForDB(L[1])
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = con
                replyMesssage = reply.TextMsg(toUser, fromUser, content)
                return HttpResponse(replyMesssage.send())
            else:
                print("暂且不处理")
                return HttpResponse("success")
        else:
            con = L[1]
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            if con[0] == 'image':
                mediaId = con[1]
                print(mediaId)
                replyMesssage = reply.ImageMsg(toUser, fromUser, mediaId)
            else:
                content = con
                replyMesssage = reply.TextMsg(toUser, fromUser, content)
            return HttpResponse(replyMesssage.send())

#公众号请求进入数据库查询
def getTextForDB(key):
        con = str()
        if key == "随机":
            data = Magnet.objects.all()
            max = data.count()
            i = 1
            while i < 10:
                item = random.randint(0, max)
                text = str(data[item].mgTitle)+str('\n')+str("Magnet:?xt=urn:btih:")+str(data[item].mgList)+str('\n')+str('\n')
                con = str(con)+str(text)
                i += 1
        else:
            data = Magnet.objects.filter(mgLable__contains=key) | Magnet.objects.filter(mgTitle__contains=key)
            datas = data.order_by('-mgHot')[0:10]
            if datas:
                for val in datas:
                    text = str(val.mgTitle)+str('\n')+str("Magnet:?xt=urn:btih:")+str(val.mgList)+str('\n')+str('\n')
                    con = str(con)+str(text)
            else:
                con = "暂时未查询到您需要的资源，正在启动爬虫......请30秒后重新搜索您查找的资源"
                getList(key)
        return con

#验证返回信息
def validate(text,openid=''):
    con = str()
    if str(text)[:3] == "电影+":
        return (True,str(text)[3:])
    elif str(text) == "科学上网":
        con = getNode()
        return (False,con)
    elif str(text) == "邀请码":
        con = getCode(openid)
        return (False,con)
    elif str(text)[:7].lower() == "markss+":
        con = bindAccount(str(text)[7:], openid)
        return (False,con)
    elif str(text) == "签到":
        con = signed(openid)
        return (False,con)
    elif str(text) == "私有节点":
        con = getPrivateNode(openid)
        return (False,con)
    elif str(text) == "站长":
        con = getUserQrcode()
        return (False,con)
    else:
        con = str("参考菜单回复获得对应功能：")+str('\n')+\
              str("1、回复：电影+电影名称/相关主演，获取相应的电影磁力")+str('\n')+\
              str("2、回复：电影+随机，随机获取电影磁力")+str('\n')+\
              str("3、回复：科学上网，获取免费shadowsock账号")+str('\n')+\
              str("4、回复：邀请码，获取MarkSS邀请码")+str('\n')+\
              str("5、回复：MarkSS+账号+密码，输入MarkSS账号密码进行绑定")+str('\n')+\
              str("6、回复：签到，MarkSS签到，悄悄告诉你关注绑定后，PC端跟公众号一共可以签到两次呢！")+str('\n')+\
              str("7、回复：私有节点，获取已绑定的私有节点")+str('\n')+\
              str("8、回复：站长，获取公众号管理员，添加好友，一起搞事情")+str('\n')
        if text == Params.APP_NAME:
            con = str("欢迎关注")+str(Params.APP_NAME)+str("公众号")+str('\n\n')+str(con)
        return (False, con)

#获取公开节点列表
def getNode():
    con = str()
    data = NodeSs.objects.all()
    for val in data:
        text = str('IP：')+str(val.node_name)+str('\n')+\
               str('密码：')+str(val.node_server)+str('\n')+\
               str('端口：')+str(val.node_method)+str('\n')+\
               str('加密方式：')+str(val.node_info)+str('\n')+\
               str('服务地址：')+str(val.node_status)+str('\n\n')
        con = str(con)+str(text)
    con = str(con)+str('登录https://markss.club注册可以获得速度更快的属私有的节点，公开节点不定期更新')+str('\n')+\
          str('安卓下载地址：')+str("'<a href=")+str(Params.Android_download)+str(">点击下载</a>'")+str('\n')+\
          str('PC下载地址：')+str("'<a href=")+str(Params.PC_download)+str(">点击下载</a>'")+str('\n')+\
          str('IOS推荐：应用商店下载Shadowrocket')
    return con

#获取邀请码
def getCode(openid):
    data = UserCode.objects.filter(openid=openid)
    con = str()
    if data:
        con = str('邀请码：')+str(data[0].code)+str('\n')+str('注意：邀请码每人只能获取并使用一次，请妥善保存好自己的邀请码')
    else:
        code = SsInviteCode.objects.using('db1').filter(user_id=1)
        if code:
            for val in code:
                if UserCode.objects.filter(code=val.code):
                    con = str("邀请码已发放完毕，或添加Q群")+str(Params.QQqun)+str("向群主直接索取")
                else:
                    UserCode.objects.create(openid=openid, code=val.code)
                    con = str('邀请码：')+str(val.code)+str('\n')+str('注意：邀请码每人只能获取并使用一次，请妥善保存好自己的邀请码')
                    break
            print(con)
        else:
            con = str("邀请码已发放完毕，或添加Q群")+str(Params.QQqun)+str("向群主直接索取")
    return con

#绑定账号
def bindAccount(text, openid):
    list = text.split('+')
    login = list[0]
    utlis = Utils()
    pawd = utlis.md5(list[1].encode('utf-8'))
    if UserBind.objects.filter(openid=openid):
        con = "该账号已经完成绑定，无需再次绑定"
    else:
        user = User.objects.using('db1').filter(email=login, pass_field=pawd)
        if user:
            modify = int(time.time())-int(24)*int(3601)
            modify = time.localtime(modify)
            if UserBind.objects.create(userid=user[0].id, openid=openid, modify=time.strftime('%Y-%m-%d %H:%M:%S', modify)):
                con = "绑定成功，现在可以使用签到和私有节点功能"
            else:
                con = "绑定失败，请重新绑定"
        else:
            con = "账号或密码有误，请重新确认"
    return con

#签到
def signed(openid):
    userID = UserBind.objects.filter(openid=openid)[0].userid
    user = User.objects.using('db1').filter(id=userID)
    con = str
    if user[0]:
        utils = Utils()
        timeStamp = utils.timeStamp(user[0].last_check_in_time)
        updateTime = int(timeStamp) + int(3600)*int(24)
        if time.time() < updateTime:
           con = "您今天已经签到过啦，一天只能签到一次啦"
        else:
            markssuser = User.objects.using('db1').filter(id=userID)
            item = random.randint(int(Params.checkinMin)*1024*1024, int(Params.checkinMax)*1024*1024)
            items = int(item)+int(markssuser[0].transfer_enable)
            ####更新签到日期
            # timeStamp = Utils.timeStamp(time.time())
            ###
            User.objects.using('db1').filter(id=userID).update(transfer_enable=items, last_check_in_time=time.time())
            res = int(item)/int(1024)/int(1024)
            con = str("签到成功，恭喜您获得")+str(res)+str("MB流量")
    else:
        con = str("您还未进行")+str(Params.CLIENT_NAME)+str("账号绑定，请先绑定")
    return con

#获取私有节点
def getPrivateNode(openid):
    user = UserBind.objects.filter(openid=openid)
    if user:
        uid = user[0].userid
        con = str()
        user = User.objects.using('db1').filter(id=uid)[0]
        ssnode = SsNode.objects.using('db1').filter(type=1)
        for val in ssnode:
            text = str(val.name)+str('\n')+str(val.server)+str('\n')+\
                  str('密码：')+str(user.passwd)+str('\n')+\
                  str('端口：')+str(user.port)+str('\n')+\
                  str('加密方式：')+str(user.method)+str('\n')+\
                  str('协议')+str(user.protocol)+str('：')+str(user.protocol_param)+str('\n')+\
                  str('混淆')+str(user.obfs)+str('：')+str(user.obfs_param)+str('\n\n')
            con = str(con)+str(text)
        con = str(con)+"温馨提示：请不要随便暴露自己的节点密码端口"
    else:
        con = "您还未进行MarkSS的账号绑定，请先绑定"
    return con

#获取作者微信
def getUserQrcode():
    con = 'b9mzRCcwRGI_sOXZLxVd7ptJgXWtUWkJt6IcpkSsXeRSRyqPMCAknbBBvvNAE5L-' #作者二维码，通过测试好上传的图片media_id
    return ('image', con)

#自定义创建菜单接口
def createTable(request):
    param = Params.menu
    data = dumps(param, ensure_ascii=False)
    data = bytes(data, 'utf8')
    #params = urllib.parse.urlencode(param).encode('utf-8')
    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token='+AccessToken
    create_url = urllib.request.Request(url)
    msg = urllib.request.urlopen(create_url, data)
    return HttpResponse(msg)

#删除自定义菜单
def deleteTable(request):
    delete_url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token='+AccessToken
    msg = urllib.request.urlopen(delete_url)
    return HttpResponse(msg)

#获取自动回复规则接口测试
def subscribe(request):
    create_url = 'https://api.weixin.qq.com/cgi-bin/get_current_autoreply_info?access_token='+AccessToken
    msg = urllib.request.urlopen(create_url)
    return HttpResponse(msg)

#获取用户个人资料
def getUserInfo(request):
    create_url = str('https://api.weixin.qq.com/cgi-bin/user/info?access_token=')+str(AccessToken)+str('&openid=')+str('ojzjrwA_X2C9RFncMahe3scO-J9g')+str('&lang=zh_CN')
    msg = urllib.request.urlopen(create_url)
    return HttpResponse(msg)

#模板消息接口一个月只能修改一次
def setTemplate(request):
    wechat = WeChat()
    AccessToken = wechat.getAccessToken()
    param = {
        "industry_id1": "2",
        "industry_id2": "4"
    }
    params = urllib.parse.urlencode(param).encode(encoding='UTF8')
    create_url = 'https://api.weixin.qq.com/cgi-bin/template/api_set_industry?access_token='+AccessToken
    msg = urllib.request.urlopen(create_url,params)
    return HttpResponse(msg)

#上传临时素材接口
def uploadImage(request):
    from django.conf import settings
    type = 'image'
    print(open("D://PY/wechat-ss-panel-v3/static/image/1.jpg", "rb"))
    filedata = {
        # "media": str("@")+str(settings.STATIC_URL)+str("image/1.jpg")
        "media": open("D://PY/wechat-ss-panel-v3/static/image/1.jpg", "rb")
    }
    # data = dumps(filedata, ensure_ascii=False)
    # data = bytes(data, 'utf8')
    url = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token='+AccessToken+str('&type=')+str(type)
    create_url = urllib.request.Request(url)
    msg = urllib.request.urlopen(create_url, filedata)
    return HttpResponse(msg)
