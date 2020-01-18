# import hashlib
# m = hashlib.md5(b'123456')
# print(m.hexdigest)

# import tarfile
#
# tar = tarfile.open('/tmp/nsd1908/demo/a.tar.gz', 'w:gz')
# # tar.add('/etc/shadow')
# tar.add('/etc/hosts')
# tar.close()
#
# tar = tarfile.open('/tmp/nsd1908/demo/a.tar.gz')
# tar.extractall(path='/tmp/nsd1908/demo')
# tar.close()

# import re

# m = re.search('f..', 'food')
# print(m.group())
#
# t = re.finditer('f..', 'seafood is food')
# print(t)

# print(re.split('-|\.', 'hello-world-how-are-you.tar.gz'))
#
# print(re.sub('X', 'tom', 'Hi X. Nice to meet you, X'))

# class Role:
#     def __init__(self, name, weapon):
#         self.name = name
#         self.weapon = weapon
#     def show_me(self):
#         print('我是%s， 我的武器是%s' % (self.name, self.weapon))
#     def say(self, words):
#         print(words)
# # if __name__ == '__main__':
# #     lb = Role('LB', 'GUN')
# #     print(lb.name, lb.weapon)
# #     lb.show_me()
# #     lb.say('good day commander')
# #
# #     zf = Role('ZF', 'knife')
# #     zf.show_me()
# #     zf.say('nonono')
#
# class Warrior(Role):
#     def __init__(self, name, weapon, country):
#         Role.__init__(self, name, weapon)
#         self. coutry = country
#
#     def attack(self, target):
#         print('物理攻击：%s ' % target)
#     def shout(self):
#         print('my coutry is  %s' % self.coutry)
#
# class Mege(Role):
#     def attack(self, target):
#         print('法术攻击：%s' % target)
#
# if __name__ == '__main__':
#     gy = Warrior('GY', 'chair', 'USA')
#     gy.show_me()
#     gy.say('gogogo')
#     gy.attack('bob')
#     gy.shout()

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return '书名是%s ' % self.title
#
#     def __call__(self):
#         print('作者是%s ' % self.author)
#
# if __name__ == '__main__':
#     py_book = Book('python', 'hetland')
#     print(py_book)
#     py_book()