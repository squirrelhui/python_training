# import os
#
# print('starting...')
# ret_val = os.fork()
# if ret_val:
#     print('Hello from parent')
# else:
#     print('Hello from child')
# print('Hello World!')

# import os
# print('starting...')
#
# ret_val = os.fork()
#
# if ret_val:
#     print('Hello from parent')
# else:
#     print('Hello from child')
#
# print('Hello World')

# import  os
#
# print('starting...')
#
# for i in range(3):
#     rev_val = os.fork()
#     if not rev_val:
#         print('Hello World!')
#         exit()
#
# print('done')

# try:
#     list = 5 * [0]
#     x = list[5]
#     print("Done")
# except IndexError:
#     print("Index out of bound")
# import re
# sentence = 'we are humans'
# matched = re.match(r'(.*) (.*?) (.*)', sentence)
# print(matched.groups())
import os
os.