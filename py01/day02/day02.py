# if 3 > 0:
#     print('yes')
#     print('ok')
#
# if 'to' in 'python':
#     print('true')
# else:
#     print('false')
#
# if -0.0:
#     print('任何值为0的数字都是False')
#
# if 0.0000001:
#     print('任何为非0的数字都是False')
#
# if ' ':
#     print('空格也是一个字符,非空字符串为True')
#
# if []:
#     print('空列表')
# else:
#     print('空列表不输出')
#
# if ():
#     print('空元祖')
# else:
#     print('空元组不输出')
#
# if {}:
#     print('空字典')
# else:
#     print('空字典不输出')
#
# if None:
#     print('None为False,取反为True')
#
# if not None:
#     print('None为False,取反为True')
#
# if not 0:
#     print('数字0为False,取反为True')

# a, b = 10, 20
# if a <= b:
#     smaller = a
# else:
#     samller = b
# print(smaller)

# a, b = 100, 20
# smaller = a if a <= b else  b
# print(smaller)

# import getpass
# username = input('请输入用户名: ')
# passwd = getpass.getpass('请输入密码: ')
# if username == 'bob' and  passwd == '123456' :
#     print('login successful')
# else:
#     print('login incorrect')

# c = 'login successful'
# d = 'login incorrect'
# a = c if username == 'bob' and  passwd == '123456' else d
# print(a)

# point = int(input('请输入成绩: ' ))
# if point >= 90 :
#     print('优秀')
# elif point >= 80 :
#     print('好')
# elif point >= 70 :
#     print('良')
# elif point >= 60 :
#     print('及格')
# else:
#     print('你要努力了')

# if 70 > point >= 60:
#     print('及格')
# elif 80 > point >=70:
#     print('良')
# elif 90 > point >=80:
#     print('好')
# elif point >= 90:
#     print('优秀')
# else:
#     print('你要努力了!!!')

# import random
# choices = ['剪刀', '石头', '布']
# computer = random.choice(choices)
# player = input('请出拳(剪刀/石头/布): ')
# print('Your choice:%s , computer choice:%s' % (player, computer))
# if player == '剪刀':
#     if computer == '剪刀':
#         print('\033[32;1mdraw\033[0m')
#     elif computer == '石头':
#         print('\033[31;1mYou lose!!!\033[0m')
#     else:
#         print('\033[31;1mYou Win!!!\033[0m')
# elif player == '石头':
#     if computer == '剪刀':
#         print('\033[31;1mYou Win!!!\033[0m')
#     elif computer == '石头':
#         print('\033[32;1mdraw\033[0m')
#     else:
#         print('\033[31;1mYou lose!!!\033[0m')
# else:
#     if computer == '剪刀':
#         print('\033[31;1mYou lose!!!\033[0m')
#     elif computer == '石头':
#         print('\033[31;1mYou Win!!!\033[0m')
#     else:
#         print('\033[32;1mdraw\033[0m')

# import random
# choices = ['剪刀', '石头', '布']
# win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]
# computer = random.choice(choices)
# player = input('请出拳(剪刀/石头/布): ')
# print("Your choice: %s, Computer's choice: %s" % (player, computer))
# if player == computer:
#     print('\033[32;1mdraw\033[0m')
# elif [player, computer] in win_list:
#     print('\033[31;1mYou Win!!!\033[0m')
# else:
#     print('\033[31;1mYou lose!!!\033[0m')

# import random
# choices = ['剪刀', '石头', '布']
# win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]
# prompt = '''(0)剪刀
# (1)石头
# (2)布
# 请选择(0/1/2): '''
# computer = random.choice(choices)
# index = int(input(prompt))
# player = choices[index]
# print("Your choice: %s, Computer's choice: %s" % (player, computer))
# if player == computer:
#     print('\033[32;1mdraw\033[0m')
# elif [player, computer] in win_list:
#     print('\033[31;1mYou Win!!!\033[0m')
# else:
#     print('\033[31;1mYou lose!!!\033[0m')

# result = 0
# counter = 1
# while counter < 101:
#     result += counter
#     counter += 1
# print(result)

# import random
# choices = ['剪刀', '石头', '布']
# win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]
# prompt = '''(0)剪刀
# (1)石头
# (2)布
# 请选择(0/1/2): '''
# win = 0
# lose = 0
# while win < 2 and lose < 2 :
#     computer = random.choice(choices)
#     index = int(input(prompt))
#     player = choices[index]
#     print("Your choice: %s, Computer's choice: %s" % (player, computer))
#     if player == computer:
#         print('\033[32;1mdraw\033[0m')
#     elif [player, computer] in win_list:
#         print('\033[31;1mYou Win!!!\033[0m')
#         win += 1
#     else:
#         print('\033[31;1mYou lose!!!\033[0m')
#         lose += 1

# import random
# choices = ['剪刀', '石头', '布']
# win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]
# prompt = '''(0)剪刀
# (1)石头
# (2)布
# 请选择(0/1/2): '''
# win = 0
# lose = 0
# while 1 :
#     computer = random.choice(choices)
#     index = int(input(prompt))
#     player = choices[index]
#     print("Your choice: %s, Computer's choice: %s" % (player, computer))
#     if player == computer:
#         print('\033[32;1mdraw\033[0m')
#     elif [player, computer] in win_list:
#         print('\033[31;1mYou Win!!!\033[0m')
#         win += 1
#     else:
#         print('\033[31;1mYou lose!!!\033[0m')
#         lose += 1
#     if win == 2 or lose == 2 :
#         break

# result = 0
# counter = 0
#
# while counter < 100 :
#     counter += 1
#     if counter % 2 :
#         continue
#     result += counter
# print(result)

# import random
# num = random.randint(1, 100)
# counter = 0
# while counter < 7 :
#     answer = int(input('请猜一个数字(1-100之间): '))
#     if answer > num :
#         print('猜大了')
#     elif answer < num :
#         print('猜小了')
#     else:
#         print('猜对了')
#         break
#     counter +=1
# else:
#     print('正确答案是: ', num)

# s1 = 'abc'
# for i in s1:
#     print(i)
# print('*' * 30)
#
# num = [111, 222, 333]
# for i in num:
#     print(i)
# print('*' * 30)
#
# users = ('kate', 'cuihua', 'dachui')
# for user in users:
#     print(user)
# print('*' * 30)
#
# adict = {'name': 'tom', 'age': 25}
# for key in adict:
#     print(key, adict[key])
# print('*' * 30)

# result = 0
# for i in range(1,10000001):
#     result +=i
# print(result)

# fib = [0, 1]
# for i in range(8):
#     fib.append(fib[-1] + fib[-2])
# print(fib)

# fib = [0, 1]
# n = int(input('长度: '))
# for i in range(n - 2):
#     fib.append(fib[-1] + fib[-2])
# print(fib)

# x, y = 3, 4
# smaller = x if x < y else y
# print(smaller)

# user = input('请输入用户名: ')
# passwd = input('请输入密码: ')
# if user == 'bob' and passwd == '123456':
#     print('Login successful')
# else:
#     print('Login incorrect')

# score = int(input('请输入成绩: '))
# if 70 > score >= 60:
#     print('及格')
# elif 80 > score >= 70:
#     print('良')
# elif 90 > score >= 80:
#     print('好')
# elif score >= 90:
#     print('优秀')
# else:
#     print('你不够努力啊')

# import random
# choices = ('剪刀', '石头', '布')
# win_list = [['剪刀','布'], ['石头', '剪刀'], ['布', "石头"]]
# cplayer = random.choices(choices)
# player = input('请出拳(剪刀/石头/布): ')
# print('电脑: %s , 官人: %s' % (cplayer, player))
# if cplayer == player :
#     print('\033[32;1m这么巧\033[0m')
# elif [cplayer, player] in win_list:
#     print('\033[31;1m你输了\033[0m')
# else:
#     print('\033[31;1m你赢了\033[0m')

# import random
# choices = ['剪刀', '石头', '布']
# win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']] #将人胜利的情况前提定义至列表中,人在前,机器在后
# computer = random.choice(choices)
# player = input('请出拳(剪刀/石头/布): ')
# print("Your choice: %s, Computer's choice: %s" % (player, computer))
# if player == computer:
#     print('\033[32;1mdraw\033[0m')
# elif [player, computer] in win_list:
#     print('\033[31;1mYou Win!!!\033[0m')
# else:
#     print('\033[31;1mYou lose!!!\033[0m')

# import random
# choices = ['剪刀', '石头', '布']
# win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]
# computer = random.choice(choices)
# playerc = input('''请出拳:
# 0=剪刀
# 1=石头
# 2=布
# ''')
# index = playerc
# player = choices[int(index)]
# print("Your choice: %s, Computer's choice: %s" % (player, computer))
# if player == computer:
#     print('\033[32;1mdraw\033[0m')
# elif [player, computer] in win_list:
#     print('\033[31;1mYou Win!!!\033[0m')
# else:
#     print('\033[31;1mYou lose!!!\033[0m')

# sum = 0
# couter = 1
# while couter <= 100:
#     sum += couter
#     couter +=1
# print(sum)

# import random
# choices = ['剪刀', '石头', '布']
# win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]
# win = 0
# lose = 0
# draw = 0
# while win < 2 and lose < 2:
#     computer = random.choice(choices)
#     playerc = input('''请出拳:
#     0=剪刀
#     1=石头
#     2=布
#     ''')
#     index = playerc
#     player = choices[int(index)]
#     print("Your choice: %s, Computer's choice: %s" % (player, computer))
#     if player == computer:
#         print('\033[32;1mdraw\033[0m')
#         draw +=1
#     elif [player, computer] in win_list:
#         print('\033[31;1mYou Win!!!\033[0m')
#         win +=1
#     else:
#         print('\033[31;1mYou lose!!!\033[0m')
#         lose +=1
# print('win= %s, lose= %s, draw= %s' % (win, lose, draw))
#
# import random
# choices = ['剪刀', '石头', '布']
# win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]
# win = 0
# lose = 0
# draw = 0
# while 1:
#     computer = random.choice(choices)
#     playerc = input('''请出拳:
#     0=剪刀
#     1=石头
#     2=布
#     ''')
#     index = playerc
#     player = choices[int(index)]
#     print("Your choice: %s, Computer's choice: %s" % (player, computer))
#     if player == computer:
#         print('\033[32;1mdraw\033[0m')
#         draw +=1
#     elif [player, computer] in win_list:
#         print('\033[31;1mYou Win!!!\033[0m')
#         win +=1
#     else:
#         print('\033[31;1mYou lose!!!\033[0m')
#         lose +=1
#     if win == 2 or lose == 2:
#         break
# print('win= %s, lose= %s, draw= %s' % (win, lose, draw))

# import random
# num = random.randint(1, 100)
# counter = 0
# while counter < 7:
#     answer = int(input('请猜数:'))
#     if answer > num:
#         print('猜大了')
#     elif answer < num:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break
#     counter +=1
# else:
#     print('正确的是: ', num)

# s1 = 'abc'
# for i in s1:
#     print(i)
# print('*' * 30)
#
# num = [111, 222, 333]
# for i in num:
#     print(i)
# print('*' * 30)
#
# users = ('kate', 'cuihua', 'dachui')
# for user in users:
#     print(user)
# print('*' * 30)
#
# adict = {'name': 'tom', 'age': 25}
# for key in adict:
#     print(key, adict[key])
# print('*' * 30)
#
# fib = [0, 1]
# for i in range(8):
#     fib.append(fib[-1] + fib[-2])
# print(fib)
#
# fib = [0, 1]
# n = int(input('lenth: '))
# for i in range(n - 2):
#     fib.append(fib[-1] + fib[-2])
# print(fib)

# for i in range(1, 10):
#     for k in range(1, i + 1):
#         print('%d*%d=%d' % (i, k, i * k), end=' ')
#     print()
#
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print('%d*%d=%d' % (j, i, i * j), end=' ')
#         j += 1
#     print("")
#     i += 1
#
# for i in range(1, 10):
#     for k in range(1, i + 1):
#         print('%d*%d=%d' % (i, k, i * k), end=' ')
#     print()
#
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print('%d*%d=%d' % (j, i, i * j), end=' ')
#         j += 1
#     print("")
#     i += 1
# import random
# choices = ['剪刀', '石头', '布']
# win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]
# win = 0
# lose = 0
# draw = 0
# while 1:
#     computer = random.choice(choices)
#     playerc = input('''请出拳:
#     0=剪刀
#     1=石头
#     2=布
#     ''')
#     index = playerc
#     player = choices[int(index)]
#     print("Your choice: %s, Computer's choice: %s" % (player, computer))
#     if player == computer:
#         print('\033[32;1mdraw\033[0m')
#         draw +=1
#     elif [player, computer] in win_list:
#         print('\033[31;1mYou Win!!!\033[0m')
#         win +=1
#     else:
#         print('\033[31;1mYou lose!!!\033[0m')
#         lose +=1
#     if win == 2 or lose == 2:
#         break
# print('win= %s, lose= %s, draw= %s' % (win, lose, draw))
# import random
# choices = ['剪刀', '石头', '布']
# win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]
# win = 0
# lose = 0
# draw = 0
# while 1:
#     computer = random.choice(choices)
#     playerc = input('''请出拳:
#     0=剪刀
#     1=石头
#     2=布
#     ''')
#     index = playerc
#     player = choices[int(index)]
#     print("Your choice: %s, Computer's choice: %s" % (player, computer))
#     if player == computer:
#         print('\033[32;1mdraw\033[0m')
#         draw +=1
#     elif [player, computer] in win_list:
#         print('\033[31;1mYou Win!!!\033[0m')
#         win +=1
#     else:
#         print('\033[31;1mYou lose!!!\033[0m')
#         lose +=1
#     if win == 2 or lose == 2:
#         break
# print('win= %s, lose= %s, draw= %s' % (win, lose, draw))