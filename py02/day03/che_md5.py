# import hashlib
# import sys
#
# def check_md5(fname):
#     m = hashlib.md5()
#
#     with open(fname, 'rb') as fobj:
#         while 1:
#             data = fobj.read(4096)
#
#             if not data:
#                 break
#             m.update(data)
#
#     return  m.hexdigest()
#
# if __name__ == '__main__':
#     result = check_md5(sys.argv[1])
#
#     print(result)

# import hashlib
# import sys
#
# def check_md5(fname):
#     m = hashlib.md5()
#
#     with open(fname, 'rb') as fobj:
#         while 1:
#             data = fobj.read(4096)
#             if not data:
#                 break
#             m.update(data)
#
#     return m.hexdigest()
#
# if __name__ == '__main__':
#     result = check_md5(sys.argv[1])
#     print(result)
#
# import hashlib
# import sys
#
# def check_md5():
#     m = hashlib.md5
#
#     with open(sys.argv[1], 'rb') as fobj:
#         while 1:
#             data = fobj.read(4096)
#             if not data:
#                 break
#             m.update(data)
#
#     return m.hexdigest()
#
# if __name__ == '__main__':
#     result = check_md5()
#     print(result)