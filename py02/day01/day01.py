# import time

# print(time.time())
# print(time.ctime())
# print(time.localtime())
#
# t = time.localtime()
# print(t)
# print(t.tm_year)

import time
# result = 0
#
# start = time.time()
#
# for i in range(10000001):
#     result += i
#
# end = time.time()
#
# print(result)
# print(end - start)

# print(time.strftime('%Y-%m-%d %H:%M:%S'))
#
# print(time.strftime('%a'))
#
# print(time.strftime('%A'))

# t1 = time.strptime('2020-01-08 10:30:00', '%Y-%m-%d %H:%M:%S')
# print(t1)
# t = time.localtime()
# print(t)
# print(t > t1)

# from datetime import datetime

# print(datetime.now())
#
# t = datetime.now()
# print(t.year)
# print(t.month)
# print(t.day)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)

# from datetime import datetime,timedelta
#
# days = timedelta(days=100, hours=1)
# t = datetime.now()
# print(t - days)
# print(t + days)

# from datetime import datetime, timedelta
#
# days = timedelta(days=100, hours=1)
# t = datetime.now()
# print(t - days)
# print(t + days)
#
# import os

# print(os.path.basename('/tmp/nsd1908/hosts'))
# print(os.path.dirname('/tmp/nsd1908/hosts'))
# print(os.path.split('/tmp/nsd1908/hosts'))
# print(os.path.join('/tmp/nsd1908', 'hosts'))

# import pickle
# shopping_list = ['apple', 'banana', 'egg']
# with open('/tmp/a.txt', 'wb') as fobj:
#     pickle._dump(shopping_list, fobj)
#
# with open('/tmp/a.txt', 'rb') as ffobj:
#     alist = pickle.load(ffobj)
#
# print(type(alist))
#
# print(alist)

# import pickle
# shopping_list = ['apple', 'banana', 'egg']
#
# with open('/tmp/a.txt', 'wb') as fobj:
#     pickle._dump(shopping_list, fobj)
#
# with open('/tmp/a.txt', 'rb') as gobj:
#     alist = pickle.load(gobj)
#
# print(type(alist))
# print(alist)

# import pickle
# shopping_list = ['apple', 'banana', 'egg']
#
# with open('/tmp/a.txt', 'wb') as fobj:
#     pickle.dump(shopping_list, fobj)
#
# with open('/tmp/a.txt', 'rb') as gobj:
#     alist = pickle.load(gobj)
#
# print(type(alist))
# print(alist)