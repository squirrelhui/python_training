import requests
import getpass
import json

headers = {'Content-Type': 'application/json;charset=utf-8'}
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "我就是我, 是不一样的烟火@156xxxx8827好好学习天天向上"
#     },
#     "at": {  #@哪些人
#         "atMobiles": [
#             "156xxxx8827",
#             "189xxxx8325"
#         ],
#         "isAtAll": False
#     }
# }

# data = {
#     "msgtype": "link",
#     "link": {
#         "text": """这个即将发布的新版本，创始人xx称它为“红树林”。
# 而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？好好学习天天向上""",
#         "title": "时代的火车向前开",
#         "picUrl": "https://img04.sogoucdn.com/app/a/100520021/1b3ca90c535d64ad658a44a63de6a225",
#         "messageUrl": "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI"
#     }
# }

# data = {
#      "msgtype": "markdown",
#      "markdown": {
#          "title":"今晚打老虎",
#          "text": "## 2020年1月14日晚在DD吧好好学习天天向上\n" +
#                  "> 一共约了10个同学" +
#                  "> ![screenshot](http://www.sinaimg.cn/dy/slidenews/36_img/2012_22/21346_985978_781272.jpg)\n"  +
#                  "> #### 2020年1月14日发布 [详细信息](http://www.dianping.com/) \n"
#      },
#     "at": {
#         "atMobiles": [
#             "156xxxx8827",
#             "189xxxx8325"
#         ],
#         "isAtAll": False
#     }
#  }

# data = {
#     "actionCard": {
#         "title": "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
#         "text": """![screenshot](http://www.sinaimg.cn/dy/slidenews/36_img/2012_22/21346_985978_781272.jpg)
#  ### 乔布斯 好好学习天天向上
#  Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划""",
#         "hideAvatar": "0",
#         "btnOrientation": "0",
#         "btns": [
#             {
#                 "title": "内容不错",
#                 "actionURL": "https://www.163.com/"
#             },
#             {
#                 "title": "不感兴趣",
#                 "actionURL": "https://www.qq.com/"
#             }
#         ]
#     },
#     "msgtype": "actionCard"
# }

data = {
    "feedCard": {
        "links": [
            {
                "title": "纪念老特拉福德110周年，乐高发布模型套装，售价250镑（好好学习天天向上）",
                "messageURL": "https://voice.hupu.com/soccer/2533006.html",
                "picURL": "https://c2.hoopchina.com.cn/uploads/star/event/images/200115/8ea57b7fbce259f110cdfbbdb234a8c772367663.png"
            },
            {
                "title": "曼晚列曼联夏窗引援名单：麦迪逊、格雷利什和范德贝克 (好好学习天天向上)",
                "messageURL": "https://voice.hupu.com/soccer/2533089.html",
                "picURL": "https://c1.hoopchina.com.cn/uploads/star/event/images/200115/c674a0025af52c45355af49bd65f739013cb466c.jpg"
            }
        ]
    },
    "msgtype": "feedCard"
}






# url是钉钉机器人webhook地址
url = 'https://oapi.dingtalk.com/robot/send?access_token=97af668f3da6979e347e82368616722804dee13a3a163f0ca552992bef01f594'

r = requests.post(url, headers=headers, data=json.dumps(data))

print(r.json())