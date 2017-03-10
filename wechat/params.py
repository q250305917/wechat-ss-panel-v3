#常量设置
class Params(object):

    #站点名称
    CLIENT_NAME = 'MarkSS'

    #站点域名
    CLIENT_DOMAIN = 'http://markss.club'

    #公众号的名称
    APP_NAME = 'YUNSO云搜'

    #公众号验证的TOCKEN
    APP_TOCKEN = 'yunso2016'

    #无码时提示获取QQ群
    QQqun = '570508797'

    #推荐安卓下载的地址
    Android_download = '"https://bit.no.com:43110/shadowsocksr.bit/ssr_3.2.7.14.apk"'

    #推荐PC下载地址
    PC_download = '"https://pan.baidu.com/s/1skEESaT"'

    #签到最少流量 单位MB
    checkinMin = '1000'
    #签到最大流量
    checkinMax = '3000'

    #是否开启允许添加管理员为微信好友(未认证订阅号或服务号无法使用请保持False)
    IS_ADD_FIREND = False

<<<<<<< HEAD
    #站长二维码路径（可自定义路径）
    ADMIN_QRCODE = '/home/django/wechat-ss-panel-v3/static/image/1.jpg'
=======
    #站长二维码路径（可自定义路径,未认证订阅号或服务号无法使用请保持为空)
    ADMIN_QRCODE = 'D:\PY\wechat-ss-panel-v3\static\image\/1.jpg'
>>>>>>> 43c98f83084f97f01f46d11faa177d3f2a809556

    #所属行业，默认IT科技，更多行业参数请参考https://mp.weixin.qq.com/wiki/5/6dde9eaa909f83354e0094dc3ad99e05.html
    INDUSTRY_ID = {
        "industry_id1": "2",
        "industry_id2": "4"
    }

    #菜单
    MENU = {
     "button": [
      {
        "name": "小工具",
        "sub_button": [
        {
            "type": "click",
            "name": "随机电影",
            "key": "电影+随机"
        },
        {
            "type": "click",
            "name": "站长",
            "key": "站长"
        },
        ]
      },

      {
        "name": CLIENT_NAME,
        "sub_button": [
        {
            "type": "click",
            "name": "邀请码",
            "key": "邀请码"
        },
        {
           "type": "click",
           "name": "签到",
           "key": "签到"
        },
        {
           "type": "click",
           "name": "私有节点",
           "key": "私有节点"
        },
        {
           "type": "click",
           "name": "科学上网",
           "key": "科学上网"
        },
        {
           "type": "view",
           "name": "登录",
           "url": CLIENT_DOMAIN
        },
       ]
   }]
}
