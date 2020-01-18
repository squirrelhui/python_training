# import time
#
# t9 = time.strptime('2019-05-18', '%Y-%m-%d')
# t10 = time.strftime('%Y-%m-%d')
#
# print(t9)
# print(t10)
#
# from datetime import datetime, timedelta
#
# day = timedelta(days=100, hours=1)
#
# t = datetime.now()
# print(t - day)
# print(t + day)

# try:
#     data = int(input('input a number: '))
# except KeyboardInterrupt:
#     print('user cancelled')
# except ValueError:
#     print('you must insert a number')

# try:
#     num = int(input('number: '))
#     result = 100/num
#     print(result)
#     print('done')
# except ValueError:
#     print('只接受数字')
# except ZeroDivisionError:
#     print('不能输入0')
# except EOFError:
#     print('不要输入CTRL+D')
# except KeyboardInterrupt:
#     print('不要CTRL+C')

# try:
#     num = int(input('number:'))
#     result = 100/num
#
# except(KeyboardInterrupt, EOFError):
#     print('\n886')
# except(ValueError, ZeroDivisionError) as e:
#     print('只接受非零数字', e)
# else:
#     print(result)
# finally:
#     print('done')

# def get_info1(name, age):
#     if not 0 < age < 120:
#         raise ValueError('年龄超过范围(1-119)')
#     print('%s is %s years old' % (name, age))
#
# def get_info2(name, age):
#     assert 0 < age < 120, '年龄范围超过设定'
#     print('%s is %s years old' % (name, age))
#
# name = 'nm'
# age = 20
# age2 = 300
#
# try:
#     # get_info1(name, age2)
#     get_info2(name, age2)
# except(ValueError, AssertionError) as e:
#     print('error', e)

# import os
# os.listdir()
# os.mkdir('/tmp/hh')
# os.makedirs('/tmp/hh/nn')
# os.listdir('/tmp/hh/nn')
# os.chdir('/tmp/')
# os.getcwd()

# import shutil,os
#
# shutil.copy('/etc/hosts', '/tmp/hh')
# os.mknod('/tmp/hh/test.txt')
# os.symlink('/etc/hosts', '/tmp/hh/ahosts')

# import os
#
#
# for path, folders, files in os.walk('/home/student/python_training/devops/20200114'):
#     print('%s:' % path)
#     for dir in folders:
#         print(dir, end='\t')
#     for file in files:
#         print(file, end='\t')
#     print('\n')

# import pickle
# shopping_list = ['apple', 'banana', 'egg']
# with open('/tmp/a.txt', 'wb') as fobj:
#     pickle.dump(shopping_list, fobj)
# with open('/tmp/a.txt', 'rb') as fobj:
#     alist = pickle.load(fobj)
#
# print(alist)

# import os
# import pickle
# from time import strftime
#
# def save(fname):
#     try:
#         amount = int(input('金额: '))
#         comment = input('备注: ')
#     except ValueError:
#         print('无效的金额')
#         return
#     except (KeyboardInterrupt, EOFError):
#         print('\n886')
#         exit()
#
#     date = strftime('%Y-%m-%d')
#
#     with open(fname, 'rb') as fobj:
#         records = pickle.load(fobj)
#
#     balance = records[-1][-2] + amount
#
#     line = [date, amount, 0, balance, comment]
#     records.append(line)
#
#     with open(fname, 'wb') as fobj:
#         pickle.dump(records, fobj)
#
# def cost(fname):
#     try:
#         amount = int(input('金额: '))
#         comment = input('备注: ')
#
#     except (KeyboardInterrupt, EOFError):
#         print('\n886')
#         exit()
#     date = strftime('%Y-%m-%d')
#     with open(fname, 'rb') as fobj:
#         records = pickle.load(fobj)
#
#     balance = records[-1][-2] - amount
#
#     line = [date, 0, amount, balance, comment]
#     records.append(line)
#
#     with open(fname, 'wb') as fobj:
#         pickle.dump(records, fobj)
#
# def query(fname):
#     with open(fname, 'rb') as fobj:
#         records = pickle.load(fobj)
#
#     print('%-12s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
#     for line in records:
#         print('%-12s%-8s%-8s%-12s%-20s' % tuple(line))
#
# def show_menu():
#     cmds = {'0':save, '1':cost, '2':query}
#     prompt = """(0)收入
# (1)开销
# (2)查询
# (3)退出
# 请选择(0/1/2/3):"""
#     fname = 'accoyboardInterrupt, EOFError):
#             choice = '3'
#
#         if choice not in ['0', '1', '2', '3']:
#             print('无效的输入,请重试')
#             continue
#
#         if choice == '3':
#             print('\n886')
#             break
#
#         cmds[choice](fname)
#
# if __name__ == '__main__':
#     show_menu()unt.data'
#     init_data = [['2020-01-09', 0, 0, 10000, 'init data']]
#     if not os.path.exists(fname):
#         with open(fname, 'wb') as fobj:
#             pickle.dump(init_data, fobj)
#
#     while 1:
#         try:
#             choice = input(prompt).strip()
#         except(KeyboardInterrupt, EOFError):
#             choice = '3'
#
#         if choice not in ['0', '1', '2', '3']:
#             print('无效的输入,请重试')
#             continue
#
#         if choice == '3':
#             print('\n886')
#             break
#
#         cmds[choice](fname)
#
# if __name__ == '__main__':
#     show_menu()

# from random import randint,choice
#
# def exam():
#     nums = [randint(1, 100) for i in range(2)]
#
#     nums.sort(reverse=True)
#
#     op = choice('+-')
#
#     if op == '+':
#         result = nums[0] + nums[1]
#
#     else:
#         result = nums[0] - nums[1]
#
#     prompt = '%s %s %s = ' % (nums[0], op, nums[1])
#
#     counter = 0
#
#     while counter < 3:
#         try:
#             answer = int(input(prompt))
#         except:
#             print()
#             continue
#
#         if answer == result:
#             print('good')
#             break
#
#         print('wrong!')
#         counter +=1
#
#     else:
#         print('answer is %s' % result)
#
# def main():
#     while 1:
#         exam()
#         try:
#             yn = input('Continue(y/n)?').strip()[0]
#         except IndexError:
#             continue
#         except (KeyboardInterrupt, EOFError):
#             yn = 'n'
#
#         if yn in 'Nn':
#             print('\n886')
#             break
#
# if __name__ == '__main__':
#     main()

# from random import randint
#
# def func1(x):
#     return True if x % 2 == 1 else False
#
# if __name__ == '__main__':
#     nums = [randint(1, 100) for i in range(10)]
#     print(nums)
#     result = filter(func1, nums)
#     print(list(result))
#     result1 = filter(lambda  x: True if x %2 ==1 else False, nums)
#     print(list(result1))

# from random import randint
#
# def func2(x):
#     return x * 2
#
# if __name__ == '__main__':
#     nums = [randint(1, 100) for i in range(10)]
#     print(nums)
#     result = map(func2, nums)
#     print(list(result))
#     result1 = map(lambda x : x * 2, nums)
#     print(list(result1))

