# import os
# def get_fname():
#     '用于获取并返回文件名'
#     while 1:
#         fname = input('请输入文件名： ')
#         if not os.path.exists(fname):
#             break
#         print('文件已存在，请重试!')
#
#     return fname
#
# def get_content():
#     '用于获取并返回文件内容'
#     content = []
#     print('请输入内容，在单独的一行输入end结束。')
#     while 1:
#         line = input('(end to quit): ')
#         if line == 'end':
#             break
#         content.append(line)
#     return content
#
#
# def wfile(fname, content):
#     '用于将内容写入文件'
#     with open(fname, 'w') as  fobj:
#         fobj.writelines(content)
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     content = ['%s\n' % line for line in content]
#     wfile(fname, content)

# import os
# def get_fname():
#     while 1:
#         fname = input('请输入文件名： ')
#         if not os.path.exists(fname):
#             break
#         print('文件已存在，请重试')
#     return fname
#
# def get_content():
#     content = []
#     print('请输入内容，以end结束')
#     while 1:
#         line = input('(end to qiut : )')
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
#     content = ['%s\n' % line for line in content ]
#     wfile(fname, content)

# print('%s is %s years old' % ('tom', 20) )
#
# print('%f' % (5/3))
#
# print('%.2f' % (5/3))
#
# print('%8.2f' % (5/3))
#
# print('%e' % 1230000000000000)
#
# print('%#o' % 10)
#
# print('%#x' % 10)

# print('{} is {} years old'.format('bob', 20))
# print('{} is {} years old'.format( 20,  'bob'))
# print('{1} is {0} years old'.format( 20,  'bob'))
# print('{0[1]} is {0[0]} years old'.format( [20,  'bob']))

s1 = '\tHello World!\t'
print(s1.strip())
print(s1.lstrip())
print(s1.rstrip())