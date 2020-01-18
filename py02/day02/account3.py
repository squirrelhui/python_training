import os
import pickle
from time import strftime

def save(fname):
    try:
        amount = int(input('金额： '))
        comment = input('备注： ')
    except ValueError:
        print('无效的金额。')
        return
    except (KeyboardInterrupt, EOFError):
        print('\n886')
        exit(101)

    date = strftime('%Y-%m-%d')

    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    balance = records[-1][-2] + amount

    line = [date, amount, 0, balance, comment]

    records.append(line)

    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    try:
        amount = int(input('金额： '))
        comment = input('备注： ')
    except ValueError:
        print('无效的金额。')
        return
    except (KeyboardInterrupt, EOFError):
        print('\n886')
        exit(101)

    date = strftime('%Y-%m-%d')

    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    balance = records[-1][-2] - amount

    line = [date, 0, amount, balance, comment]

    records.append(line)

    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    print('%-12s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))

    for line in records:
        print('%-12s%-8s%-8s%-12s%-20s' % tuple(line))

def show_menu():
    cmds ={'0':save, '1':cost, '2':query}
    prompt = """(0)save
(1)cost
(2)query
(3)exit
please enter your choice(0/1/2/3):"""
    fname = '2.data'
    init_data = [['2020-01-09', 0, 0, 10000, 'init data']]
    if not os.path.exists(fname):
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)
    while 1 :
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt,  EOFError):
            choice = '3'

        if choice not in ['0', '1', '2', '3']:
            print('invalid option please try again')
            continue
        if choice == '3':
            print('\n886')
            break
        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()