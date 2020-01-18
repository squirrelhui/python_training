import os, pickle, datetime

data = []
line = [['日期', '收入', '支出', '余额', '备注'], ['2010-01-08', 0, 0, 10000,'init data']]

def income():
    date = input('请输入日期：(回车即输入今天的日期)')
    inmoney = int(input('请输入收入金额： '))
    beizhu = input('请输入备注：')
    outmoney = 0
    value = (inmoney + line[-1][-2])

    # if not date:
    #     print('请输入日期')
    # else:
    data = [date, inmoney, outmoney, value, beizhu]
    # data.append(date)
    # data.append(inmoney)
    # data.append(outmoney)
    # data.append(value)
    # data.append(beizhu)

    line.append(data)
    # print(line)
    with open('/tmp/win.txt', 'a+b') as fobj:
         pickle.dump(line, fobj)

def pay():
    date = input('请输入日期：(回车即输入今天的日期)')
    inmoney = 0
    outmoney = int(input('请输入支出金额： '))
    beizhu = input('请输入备注：')
    value = (line[-1][-2] - outmoney)

    data = [date, inmoney, outmoney, value, beizhu]
    # data.append(date)
    # data.append(inmoney)
    # data.append(outmoney)
    # data.append(value)
    # data.append(beizhu)

    line.append(data)
    # print(line)
    with open('/tmp/win.txt', 'a+b') as fobj:
         pickle.dump(line, fobj)

def check():
    with open('/tmp/win.txt', 'r') as fobj:
        for line in fobj:
            print(line)

def value():
    with open('/tmp/win.txt', 'r.') as fobj:
        alist = fobj.readlines()
    print(alist[-1][-2])
def show_menu():
    cmds = {'0':income, '1':pay, '2': check, '3': value}
    prompt = """(0)收入
(1)支出
(2)查询收支情况
(3)余额
(4)退出
请输入(0/1/2/3/4)"""

    while 1:
        choice = input(prompt).strip()

        if choice not in '01234':
            print('请输入(0/1/2/3/4)')
            continue

        if choice == '4':
            print('\n886')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()