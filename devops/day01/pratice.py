# import os
# import time
#
# ret_val = os.fork()
# if ret_val:
#     print('in parent')
#     time.sleep(30)
#     print('parent done')
# else:
#     print('in child')
#     time.sleep(15)
#     print('child done')

# import os
# import subprocess
# import time
#
# def ping(host):
#     result = subprocess.run(
#         'ping -c2 %s &> /dev/null ' % host, shell=True
#     )
#
#     if result.returncode == 0:
#         print('%s:up' % host)
#     else:
#         print('%s:down' % host)
#
# if __name__ == '__main__':
#     ips = ['176.121.202.%s' % i for i in range(1, 255)]
#     for ip in ips:
#         ret_val = os.fork()
#         if not ret_val:
#             ping(ip)
#             exit()

# import os
# import time
#
# ret_val = os.fork()
#
# if ret_val:
#     print('父进程')
#     result = os.waitpid(-1, 0)
#     print(result)
#     time.sleep(5)
# else:
#     print('子进程')
#     time.sleep(20)
#     print('child done')

# import threading
# import subprocess
#
# def ping(host):
#     result = subprocess.run(
#         'ping -c2 %s &> /dev/null' % host, shell=True
#     )
#
#     if result.returncode == 0:
#         print('%s:up' % host)
#     else:
#         print('%s:down' % host)
#
# if __name__ == '__main__':
#     ips = ['176.121.202.%s' % i for i in range(1, 255)]
#     for ip in ips:
#         t = threading.Thread(target=ping, args=(ip, ))
#         t.start()

# import threading
# import subprocess
#
# class Ping:
#
#     def __call__(self, host):
#
#         result = subprocess.run(
#             'ping -c2 %s &> /dev/null' % host, shell = True
#         )
#
#         if result.returncode == 0:
#             print('%s:up' % host)
#         else:
#             print('%s:down' % host)
#
# if __name__ == '__main__':
#     ips = ['176.121.202.%s' % i for i in range(1, 255)]
#     for ip in ips:
#         t = threading.Thread(target=Ping(), args=(ip, ))
#         t.start()

# import threading
# import subprocess
#
# class Ping:
#     def __init__(self, host):
#         self.host = host
#
#     def __call__(self):
#         result = subprocess.run(
#             'ping -c2 %s &> /dev/null ' % self.host, shell = True
#         )
#
#         if result.returncode ==0:
#             print('%s:up' % self.host)
#         else:
#             print('%s:down' % self.host)
# if __name__ == '__main__':
#     ips = ['176.121.202.%s' % i for i in range(1, 255)]
#
#     for ip in ips:
#         t = threading.Thread(target=Ping(ip))
#         t.start()
#         t.start()

# from urllib import request
# import sys
#
# def download(html, fname):
#     url = request.urlopen(html)
#     with open(fname, 'wb') as fobj:
#         while 1:
#             data = url.read(4096)
#             if not data:
#                 break
#             fobj.write(data)
#
# if __name__ == '__main__':
#     download(sys.argv[1], sys.argv[2])

# from urllib import request
# url = 'http://www.sina.com'
# headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"}
# r = request.Request(url, headers=headers)
# html = request.urlopen(r)
# html.read()

# import wget
# import os
# import re
#
# def get_patt(fname, patt, charset='utf8'):
#
#     result = []
#     cpatt = re.compile(patt)
#     with open(fname, encoding=charset) as fobj:
#         for line in fobj:
#             m = cpatt.search(line)
#             if m:
#                 result.append(m.goup())
#
#     return  result
#
# if __name__ == '__main__':
#     url = 'http://www.qq.com'
#     down_dir = '/tmp/qq'
#     fname = '/tmp/qq/qq.html'
#     img_patt = '(http|https)://[\w./-]+.(jpg|jpeg|png|gif)'
#
#     if not os.path.exists(down_dir):
#         os.mkdir(down_dir)
#
#     if not os.path.exists(fname):
#         wget.download(url, fname)
#
#     img_list = get_patt(fname, img_patt, 'gb2312')
#
#     for img_url in img_list:
#         wget.download(img_url, down_dir)

import paramiko
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('192.168.1.10', username='root', password='a')
# result = ssh.exec_command('id root; id zhangsan')
# len(result)
#
# stdin, stdout, stderr = ssh.exec_command('id root; id zhangsan')
#
# out = stdout.read()
#
# err = stderr.read()
#
# print(out)
#
# print(err)