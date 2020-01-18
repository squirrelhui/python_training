from random import randint, choice

def exam():
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}

    '用于出题，让用户作答'
    # 随机生成两个数字
    nums = [randint(1, 100) for i in range(2)]

    # 降序排列
    nums.sort(reverse=True)

    # 随机选出加减法
    op = choice('+-')

    # 计算出正确的答案
    result = cmds[op](*nums)

    # 要求用户作答，并判断正误
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    counter = 0
    while counter < 3 :
        try:
            answer = int(input(prompt))
        except :
            print('')
            continue

        if answer == result:
            print('very good!!!')
            break
        print('不对哦！！！')

        counter +=1

    else:
        print('\033[31;1m正确答案是：%s%s\033[0m' % (prompt, result))
def main():
    while 1:
        exam()
        try:
            yn = input('Continue(y/n)? ').strip()[0] #取第一个字符
        except IndexError:
            print('请重新输入。')
            continue
        except (KeyboardInterrupt, EOFError):
            yn == 'nN'

        if yn in 'nN':
            print('\n886')
            break

if __name__ == '__main__':
    main()