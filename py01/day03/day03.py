# for i in range(1, 10):
#     for j in range(1, i+1):
#         print ('hello', end=' ')
#     print()
#
# for i in range(1,10):
#     for j in range(1, i+1):
#         print('%s*%s=%s' % (i, j, i*j), end=' ')
#     print()
#
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%d*%d=%d' % (j, i, i*j), end=' ')
#     print()
#
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if( i != k ) and (i != j) and (j != k):
#                 print (i,j,k)
#
# f = open('/tmp/passwd')
# data = f.read()
# print(data)
#
# f = open('/tmp/passwd')
# f.read(4)
#
# f = open('/tmp/passwd')
# for i in f:
#     print(i, end=' ')
# f.close()
#
# with open('/tmp/passwd') as f:
#     f.readline()
#
# with open('/tmp/passwd') as f:
#     print(f.readlines(), end=' ')
#
# f = open('/tmp/passwd','rb')
# f.seek(16,0)
# print(f.readline(5))
#
# f = open('/tmp/passwd', 'rb')
# f.seek(-5,2)
# print(f.read())
#
# f = open('/bin/ls','rb')
# g = open('/root/ls','wb')
#
# data = f.read()
# g.write(data)
#
# f.close()
# g.close()
#
# src_fname = '/bin/ls'
# dst_fname = '/tmp/list2'
# src_fobj = open(src_fname, 'rb')
# dst_fobj = open(dst_fname, 'wb')
#
# while 1:
#     data = src_fobj.read(4096)
#     if not data:
#         break
#     dst_fobj.write(data)
#
# src_fobj.close()
# dst_fobj.close()
#
# src_fname = '/bin/ls'
# dst_fname = '/tmp/list3'
# src_fobj = open(src_fname, 'rb')
# dst_fobj = open(dst_fname, 'wb')
#
# while 1:
#     data = src_fobj.read(4096)
#     if not data:
#         break
#     dst_fobj.write(data)
#
# src_fobj.close()
# dst_fobj.close()
#
# fib = [0, 1]
# for i in range(8):
#     fib.append(fib[-1] + fib[-2])
# print(fib)
#
# def mk_fib():
#     fib = [0, 1]
#     n = int(input('长度: '))
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#     print(fib)
#
# mk_fib()
#
# def mk_fib():
#     fib = [0, 1]
#     n = int(input('长度: '))
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#
#     print(fib)
#
# mk_fib()
#
#
# def mk_fib():
#     fib = [0, 1]
#     n = int(input('长度: '))
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#
#     return (fib)
#
# alist = mk_fib()
# print(alist)
# blist = [i * 2 for i in alist]
# print(blist)
#
# def mk_fib():
#     fib = [0, 1]
#     n = int(input('长度: '))
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#     return fib
# alist = mk_fib()
# print(alist)
# blist = [i * 2 for i in alist]
# print(blist)
#
# def mk_fib():
#     fib = [0, 1]
#     n = int(input('长度: '))
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#     return fib
# alist = mk_fib()
# print(alist)
# blist = [i * 2 for i in alist]
# print(blist)
#
# def mk_fib():
#     fib = [0, 1]
#     n = int(input('长度: '))
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#     return  fib
# alist = mk_fib()
# print(alist)
# blist = [i * 2 for i in alist]
# print(blist)
#
# def mk_fib(n):
#     fib = [0, 1]
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#     return  fib
# for i in [2, 4, 6, 8, 10, 20]:
#     print(mk_fib(i))
#
# def mk_fib(n):
#     fib = [0, 1]
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#     return  fib
# for i  in [2, 8, 20]:
#     print(mk_fib(i))


