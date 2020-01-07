# from random import choice
#
# all_chs = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#
# def ran_pass(n=8):
#     result = ''
#     for i in range(n):
#         ch = choice(all_chs)
#         result += ch
#     return result
#
# if __name__ == '__main__':
#     print(ran_pass())
#     print(ran_pass(6))

# from random import choice
# from string import ascii_letters, digits
#
# all_chs = ascii_letters + digits
#
# def ran_pass(n=8):
#     result = ''
#     for i in range(n):
#         ch = choice(all_chs)
#         result += ch
#     return result
#
# if __name__ == '__main__':
#     print(ran_pass())
#     print(ran_pass(6))

# from random import choice
# from string import printable
#
# all_chs = printable
#
# def ranpass(n=8):
#     result = ''
#     for i in range(n):
#         chs = choice(all_chs)
#         result += chs
#     return result
# if __name__ == '__main__':
#     print(ranpass())
#     print(ranpass(10))

# from random import choice
# from string import printable
# all_chs = printable
#
# def ranpass(n=8):
#     result = ''
#     for i in range(n):
#         ch = choice(all_chs)
#         result += ch
#     return result
# if __name__ == '__main__':
#     print(ranpass())
#     print(ranpass(15))
#
# from random import choice
# from string import ascii_letters,digits
# all_chs = ascii_letters + digits
# def ranpass(n=8):
#     result = ''
#     for i in range(n):
#         ch = choice(all_chs)
#         result += ch
#     return result
# if __name__ == '__main__':
#     print(ranpass())
#     print(ranpass(10))

# import shutil
# f1 = open('/bin/touch','rb')
# f2 = open('/tmp/tch', 'wb')
# shutil.copyfileobj(f1, f2)
# f1.close()
# f2.close()
#
# shutil.copy('/etc/hosts','/tmp/')
# shutil.copy2('/etc/hosts', '/tmp/zhuji')

# import shutil
# shutil.copytree('/etc/security', '/tmp/anquan')
# shutil.move('/tmp/anquan', '/var/tmp')
# shutil.chown('/tmp/tch', 'tom', 'tom')
# shutil.rmtree('/var/tmp/anquan')
#
# import subprocess
# subprocess.run('ls')
# subprocess.run('ls /tmp', shell='true')

# result = subprocess.run('ls /tmp', shell=True)
# print(result)
# print(result.args)
# print(result.returncode)

import subprocess
# result = subprocess.run('ls /tmp', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(result)
# print(result.args)
# print(result.returncode)

# result = subprocess.run('id root; id zhangsan', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# result = subprocess.run('id root; id zhangsan', shell=True)
#
# print(result.stderr)
# print(result.stdout)
# print(result.stdout.decode())

# a = b = 10
# b = 20
# print(a)
# print(b)

# a, b = 10, 20
# c, d = (100, 200)
# e, f = 'xy'
# g, h = ['tom', 'jerry']
# i, j = {'name': 'bob' , 'age':50}
# print(a, b)
# print(c, d)
# print(e, f)
# print(g, h)
# print(i, j)
# print(i['name'])

import keyword
print(keyword.kwlist)

