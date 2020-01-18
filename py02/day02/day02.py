# def func1():
#     print('in func1')
#     func2()
#
# def func2():
#     print('in func2')
#
# func1()

# def get_age(name, age):
#     print('%s is %s years old' % (name, age))

# get_age('tom', 20)
# get_age(20, 'tom')
# get_age(age=20, name='tom')
# get_age('tom', age=20)

# get_age(age=20, 'tom')

# def func1(*args):
#     print(args)
#
# func1('hao')
# func1('hao', 123)
# func1()
#
# def func2(**kwargs):
#     print(kwargs)
#
# func2()
# func2(name='tom', age=2)

# import random
#
# choice = random.choice('ab')
#
# print(choice)

# from random import randint
#
# def func1(x):
#     return True if x % 2 == 1  else False
#
# if __name__ == '__main__':
#     nums = [randint(1, 100) for i in range(10)]
#     print(nums)
#     result = filter(func1, nums)
#     print(list(result))
#     result1 = filter(lambda  x: True if x %2 == 1 else False, nums)
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

# x = 10
# def func1():
#     print(x)
#
# func1()
#
# def func2():
#     y = 222
#     print(y)
# func2()
#
# def func3():
#     x = 333
#     print(x)
# func3()
#
# def func4():
#     global x
#     x = 888
#     print(x)
# func4()
# print(x)
#
# from functools import partial
# def add(a, b, c, d, e):
#     return a + b + c + d + e
#
# add(10, 20, 30, 40, 9)
# add(10, 20, 30, 40, 10)
# add(10, 20, 30, 40, 110)
#
# myadd = partial(add,10, 20, 30, 40)
#
# print(myadd(555))

# def func1(x):
#     if x == 1:
#         return 1
#     return x * func1(x - 1)
# #          5 * func1(4)
# #          5 * 4 * func1(3)
# #          5 * 4 * 3 * func1(2)
# #          5 * 4 * 3 * 2 * func1(1)
# #          5 * 4 * 3 * 2 * 1
# if __name__ == '__main__':
#     result = func1(5)
#     print(result)

def mygen():
    yield 100
    a = 10 +20
    yield a
    yield 200

mg = mygen()
print(list(mg))