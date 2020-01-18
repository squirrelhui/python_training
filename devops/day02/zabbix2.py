import requests,json

url = 'http://192.168.1.11/api_jsonrpc.php'
headers = {'content-type': 'application/json'}

# 获取版本号不需要认证，可以直接请求
# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [], #参数
#     "id": 888 #随便给定一个数字，表示作业号
# }

# 获取admin用户的token
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }

# 获取全部用户
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.get",
#     "params": {
#         "output": "extend"
#     },
#     "auth": "7e4c47b5e110ce3749334837517fc108",
#     "id": 1
# }

# 获取主机信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#
#             ]
#         }
#     },
#     "auth": "7e4c47b5e110ce3749334837517fc108",
#     "id": 1
# }

# 删除hostid为10264主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10264" #删除hostid
#     ],
#     "auth": "7e4c47b5e110ce3749334837517fc108",
#     "id": 1
# }

# 获取组信息 'groupid': '2', 'name': 'Linux servers
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "7e4c47b5e110ce3749334837517fc108",
#     "id": 1
# }

# 获取模板信息 'templateid': '10001'
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux"
#             ]
#         }
#     },
#     "auth": "7e4c47b5e110ce3749334837517fc108",
#     "id": 1
# }


# 创建nsd1908web1主机，它在Linux server组中，应用Template
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "nsd1908web1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.10",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0, # 主机资产记录
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "7e4c47b5e110ce3749334837517fc108",
    "id": 1
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
