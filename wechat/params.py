#常量设置
class Params(object):

    #站点名称
    CLIENT = 'CLIENT_NAME'

    #公众号的名称
    APP_NAME = 'YUNSO云搜'

    #公众号验证的TOCKEN
    APP_TOCKEN = 'yunso2016'

    #无码时提示获取QQ群
    QQqun = '570508797'

    #推荐安卓下载的地址
    Android_download = 'href="https://bit.no.com:43110/shadowsocksr.bit/ssr_3.2.7.14.apk'

    #推荐PC下载地址
    PC_download = 'href="https://pan.baidu.com/s/1skEESaT'

    #签到最少流量 单位MB
    checkinMin = '1000'
    #签到最大流量
    checkinMax = '3000'


    #菜单
    menu = {
     "button": [
      {
          "type": "click",
          "name": "随机电影",
          "key": "电影+随机"
      },
      {
           "name": "MarkSS",
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
           ]
       }]
    }