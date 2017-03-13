from django.conf import settings
from json import loads, dumps  # 接收和返回JSON
import urllib, requests
class WeChat(object):
    def __init__(self):
        self.appid = settings.GLOBAL_SETTINGS['AppID']
        self.secret = settings.GLOBAL_SETTINGS['AppSecret']
        self.AccessToken = self.getAccessToken()

    # 获取微信AccessToken
    def getAccessToken(self):
        url = str('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=')+str(self.appid)+str('&secret=')+str(self.secret)
        data = urllib.request.urlopen(url).read()
        data = data.decode('utf-8')
        jsonData = loads(data)
        if self.checkResult(jsonData) == False:
            return jsonData['access_token']
        else:
            return jsonData['errmsg']

    # 检查结果是否正确
    def checkResult(self, res):
        if 'errcode' in res:
            if res['errcode'] != 0:
                return res
        return False

    # 请求接口 post
    # @params url param
    def request_post(self, url, param=''):
        create_url = urllib.request.Request(url)
        data = dumps(param, ensure_ascii=False)
        data = bytes(data, 'utf8')
        msg = urllib.request.urlopen(create_url, data).read()
        json = msg.decode('utf-8')
        return json

    # 请求接口get
    def request_get(self, url):
        msg = urllib.request.urlopen(url).read()
        json = msg.decode('utf-8')
        return json

    # 上传临时素材接口
    def uploadMediaTmp(self, path, type):
        filedata = {
            type: open(path, "rb")
        }
        url = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token='+self.AccessToken+str('&type=')+str(type)
        json = requests.post(url, files=filedata).json()
        return json

    # 获取临时素材接口
    def getMediaTmp(self, media_id):
        url = str('https://api.weixin.qq.com/cgi-bin/media/get?access_token=ACCESS_TOKEN')+str(self.AccessToken)+str('&media_id=')+str(media_id)
        return self.request_get(url)

    # 自定义菜单接口（创建）
    def createTable(self, param):
        url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token='+self.AccessToken
        json = self.request_post(url, param)
        return json

    # 自定义菜单接口（删除）
    def deleteTable(self):
        url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token='+self.AccessToken
        return self.request_get(url)


    #获取用户资料
    def getUserInfo(self, openid):
        url = str('https://api.weixin.qq.com/cgi-bin/user/info?access_token=')+str(self.AccessToken)+str('&openid=')+str(openid)+str('&lang=zh_CN')
        return self.request_get(url)

    #设置所属行业
    def setTemplate(self, param):
        url = 'https://api.weixin.qq.com/cgi-bin/template/api_set_industry?access_token='+self.AccessToken
        json = self.request_post(url, param)
        return json

    #获取行业信息
    def getIndustry(self):
        url = str('https://api.weixin.qq.com/cgi-bin/template/get_industry?access_token=')+str(self.AccessToken)
        return self.request_get(url)

    #获得模板ID
    def getIndustryTemplateId(self, param):
        url = 'https://api.weixin.qq.com/cgi-bin/template/api_add_template?access_token='+self.AccessToken
        json = self.request_post(url, param)
        return json