# from random import choice
# import string
# all_chs = string.ascii_letters + string.digits
#
# def ran_pass(n=8):
#     result = ''
#
#     for i in range(n):
#         ch = choice(all_chs)
#         result += ch
#
#     return result
#
# if __name__ == '__main__':
#     print(ran_pass())
#     print(ran_pass(4))
#     print(ran_pass(10))

from random import randint

# alist = list()
# print(list('hello'))
# print(list((10, 20, 30)))
# print(str['f', 'u', 'c', 'k'])

# import shutil
# shutil.copy('/bin/touch', 'rb')
# shutil.copy('/etc/hosts', '/tmp/zhuji')
# shutil.copytree('/etc/security', '/tmp/anquan')
# shutil.move('/tmp/anquan', '/var/tmp')
# shutil.chown('/tmp/zhuji', 'root', 'root')
# shutil.rmtree('/var/tmp/anquan')

# import subprocess
# subprocess.run('ls')
#
# subprocess.run('ls /opt', shell=True)

# import os
#
# def get_fname():
#     while 1:
#         fname = input('请输入文件名： ')
#         if not os.path.exists(fname):
#             break
#         print('file exsist!please try again')
#
#     return fname
#
# def get_content():
#     content = []
#     print('请输入内容，载单独的一行输入ｅｎｄ结束')
#     while 1:
#         line = input('[end to qiut: ]')
#         if line == 'end':
#             break
#         content.append(line)
#     return content
#
# def wfile(fname, content):
#     with open(fname, 'w') as fobj:
#         fobj.writelines(content)
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     content = ['%s\n' % line for line in content]
#     wfile(fname, content)

