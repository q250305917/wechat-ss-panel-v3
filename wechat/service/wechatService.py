from django.conf import settings
from json import loads, dumps #接收和返回JSON
import urllib
class WeChat(object):
    def __init__(self):
        self.appid = settings.GLOBAL_SETTINGS['AppID']
        self.secret = settings.GLOBAL_SETTINGS['AppSecret']

    #获取微信AccessToken
    def getAccessToken(self):
        url = str('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=')+str(self.appid)+str('&secret=')+str(self.secret)
        data = urllib.request.urlopen(url).read()
        data = data.decode('utf-8')
        jsonData = loads(data)
        if self.checkResult(jsonData) == False:
             return jsonData['access_token']
        else:
            return jsonData['errmsg']

    #检查结果是否正确
    def checkResult(self, res):
        if 'errcode' in res:
            if res['error'] != 0:
                return res
        return False