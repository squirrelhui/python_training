# import json
#
# adict = {'name': 'tom', 'age':20}
# print(json.dumps(adict))

import requests

# r = requests.get('http://www.qq.com')
# r.text

a = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1579069696648&di=ae80a8ad8a1a06aae4d940d729795079&imgtype=0&src=http%3A%2F%2Fwap.yesky.com%2FuploadImages%2F2015%2F295%2F44%2F6671FD82FL8E_GMOaTRW.jpg')

with open('/tmp/mv.jpg', 'wb') as fobj:
    fobj.write(a.content)