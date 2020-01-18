import random

def plus(num1, num2):
    prompt = '请输入题目的答案： '
    counter = 0
    while counter < 3 :
        print('请看题：')
        print('%s + %s = ' % (num1, num2))
        choice = int(input(prompt).strip())
        if choice == num1 + num2 :
            print('你答对了！')
            return
        else:
            print('你答错了！')
            counter +=1
            continue

def reduce(num1, num2):
    prompt = '请输入题目的答案： '
    counter = 0
    if num1 > num2 :
        a = num1
        b = num2
    else:
        b = num1
        a = num2

    while counter < 3 :
        print('请看题：')
        print('%s - %s = ' % (a, b))
        choice = int(input(prompt).strip())
        if choice == a - b :
            print('你答对了！')
            return
        else:
            print('你答错了！')
            counter +=1
            continue

def show_menu():
    prompt = """(0)游戏开始
(1)退出
请选择(0/1)"""

    while 1:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        num3 = random.randint(1, 2)

        choice = input(prompt)

        if choice not in ['0', '1']:
            print('无效输入，请重试。')
            continue

        if choice == '0':
            if num3 == 1:
                plus(num1,num2)
            else:
                reduce(num1,num2)

        if choice == '1':
            print('\n886')
            break

if __name__ == '__main__':
    show_menu()


