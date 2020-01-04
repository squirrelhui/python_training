# print('hello world')
#
# if 3 > 0 :
#     print('ok')
#     print('yes')
#
# x = 3; y = 4
# print(x + y)

# print('hello world!')
# print('hello', 'world!')
# print('hello' + 'world!')
# print('hello', 'world', sep='###')
# print('#' * 50)
# print('how are you?', end='')

# print(5 / 2)
# print(5 // 2)
# print(5 % 2)
# print(5 ** 3)
# print(5 > 3)
# print(3 > 5)
# print(20 > 10 > 5)
# print(not 20 > 10)

# number = input('请输入数字： ')
# print(number)
# print(type(number))
# print(int(number) + 10)
# print(number + str(10))

# username = input('username: ')
# print('welcome', username)
# print('welcome ' + username)

# sen = 'tom\'s pet is a dog'
# sen2 = "tom's pet is a dog"
# sen3 = "tom said:\"hello world!\""
# sen4 = 'tom said:"hello world!"'
#
# print(sen)
# print(sen2)
# print(sen3)
# print(sen4)

# words = """
# hello
# world
# abcd"""
# print(words)
#
# py_str = 'python'
# len(py_str)
# py_str[0]
# 'python'[0]
# py_str[-1]
# py_str[2:4]
# py_str[2:]
# py_str[:]
# py_str[::2]
# py_str[1::2]
# py_str[::-1]
#
# py_str + 'is good'
# py_str * 3

# alist = [10, 20, 30, 'bob', 'alice', [4, 5, 6]]
# a = len(alist)
# b = alist[-1]
# c = alist[-1][-1]
# print(a, b, c)
# d = 10 in alist
# e = 'o' in alist
# print(d, e)
# alist.append(200)
# print(alist)

# atuple = (10, 20, 30, 'bob', 'alice', [4, 5, 6])
# a = len(atuple)
# b = 10 in atuple
# c = atuple[2]
# d = atuple[3:5]
# print(a, b, c, d)

# if 3 > 0 :
#     print('ok')
#
# if 10 in [10, 20, 30]:
#     print('ok')
#
# if -0.0:
#     print('yes')
#
# if [1, 2]:
#     print('yes')
#
# if ' ':
#     print('yes')

# a = 1000
# b = 200
# if a < b:
#     smaller = a
# else:
#     smaller =b
# print(smaller)
#
# s = a if a < b else b
#
# print(s)

# import getpass
# username = input('username: ')
#
# password = getpass.getpass('passwod: ')
# if username == 'bob' and password == '123456':
#     print('login successful')
# else:
#     print('login incorrect')

# import random
# num = random.randint(1, 10)
# answer = int(input('guess: '))
# if answer > num:
#     print('猜大了')
# elif answer < num:
#     print('猜小了')
# else:
#     print('bingo')
#
# print('the number', num)

# score = int(input('请输入分数: '))
#
# if score >= 90:
#     print('优秀')
# elif score >= 80:
#     print('好')
# elif score >= 70:
#     print('良')
# elif score >= 60:
#     print('pass')
# else:
#     print('fuck')

# score = int(input('请输入分数： '))
# if score >= 60 and score < 70:
#     print('pass')
# elif 70 <= score <80:
#     print('good')
# elif 80 <= score <90:
#     print('nice')
# elif score >=90 :
#     print('beautiful')
# else:
#     print('fuck')

# import random
# all_choices = ['石头','剪刀','布']
# computer = random.choice(all_choices)
# player = input('请出拳： ')
# print("your choice: %s, computer's choice:%s" % (player, computer))
# if player == '石头':
#     if computer == '石头':
#         print('draw')
#     elif computer == '剪刀':
#         print('you win')
#     else:
#         print('you lose')
# elif player == '剪刀':
#     if computer == '石头':
#         print('you lose')
#     elif computer == '剪刀':
#         print('draw')
#     else:
#         print('you win')
# else:
#     if computer == '石头':
#         print('you win')
#     elif computer == '剪刀':
#         print('you lose')
#     else:
#         print('draw')

# import  random
# all_choices = ['石头','剪刀','布']
# win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# prompt = '''(0)石头
# (1)剪刀
# (2)布
# 请选择： '''
# computer = random.choice(all_choices)
# ind = int(input(prompt))
# player = all_choices[ind]
# print("your choice: %s, computer choice: %s" % (player, computer))
# if player == computer:
#     print('\033[32;1m平局\033[0m')
# elif [player, computer] in win_list:
#     print('\033[31;1mYOU WIN!!!\033[0m')
# else:
#     print('\033[32;1mYOU LOSE!!!\033[0m')

# import random
# num = random.randint(1, 10)
# while 1:
#     answer = int(input('guess: '))
#     if answer > num:
#         print('猜大了')
#     elif answer < num:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break

# import random
# num = random.randint(1, 100)
# counter = 0
# while counter < 5:
#     answer = int(input('guess the number: '))
#     if answer > num:
#         print('too big')
#     elif answer < num:
#         print('too small')
#     else:
#         print('bingo')
#         break
#     counter +=1
# else:
#     print('the number is  ', num)

# sum = 0
# couter = 1
# while couter < 101:
#     sum += couter
#     couter += 1
# print(sum)

# while 1:
#     yn = input('Continue(y/n): ')
#     if yn in ['n', 'N']:
#         break
#     print('i am coming...')

# sum = 0
# counter = 0
# while counter < 100:
#     counter += 1
#     if counter % 2 == 1 :
#         continue
#     sum += counter
# print(sum)

# astr = 'hello'
# alist = [10, 20, 30]
# atuple = ('bob', 'tom', 'alice')
# adict = {'name':'john','age':23}
# for ch in astr:
#     print(ch)
# for i in alist:
#     print(i)
# for name in atuple:
#     print(name)
# for key in adict:
#     print('%s:%s' % (key,adict[key]))

# range(10)
# sum = 0
# for i in range(1, 101):
#     sum +=i
# print(sum)

# fib = [0, 1]
# for i in range(int(input('请输入数列长度： '))):
#     fib.append(fib[-1] + fib[-2])
# print(fib)

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%s*%s=%s' % (j,i,j*i), end=" ")
#     print()

# a = [10 + 5 for i in range(10)]
# print(a)
# b = [10 + i for i in range(10)]
# print(b)

hi = 'hello world!'
def pstar(n=50):



