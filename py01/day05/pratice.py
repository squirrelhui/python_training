# stack = []
# def push_it():
#     item = input('item to push:')
#     stack.append(item)
#
# def pop_it():
#     if stack:
#         print('\033[31;1mPopped %s\033[0m' % stack.pop())
#
#     else:
#         print('\033[31;1mEmpty stack\033[0m')
#
# def view_it():
#     print('\033[32;1m%s\033[0m' % stack)
#
# def show_menu():
#     prompt = """(0)push_it
# (1)pop_it
# (2)view_it
# (3)quit
# please input your choice(0/1/2/3)"""
#
#     cmds = {'0':push_it, '1':pop_it, '2':view_it}
#
#     while 1:
#
#         choice = input(prompt).strip()[0]
#
#         if choice not in "0123":
#             print('invalid input.try again')
#             continue
#
#         if choice == "3":
#             break
#
#         cmds[choice]()
#
# if __name__ == '__main__':
#     show_menu()

# import getpass
#
# userdb = {}
#
# def register():
#     username = input('username: ')
#     if username in userdb:
#         print('\033[31;1m%s already exists.\033[0m' % username)
#
#     else:
#         password = input('password: ')
#         userdb[username] = password
#
# def login():
#     username = input('username: ')
#     password = getpass.getpass('password: ')
#     if userdb.get(username) == password:
#         print('\033[31;1mlogin sucessful\033[0m')
#     else:
#         print('\033[32;1mlogin incorrect\033[0m')
#
# def show_menu():
#     prompt = """(0)register
# (1)login
# (2)quit
# Please input your choice(0/1/2)"""
#     cmds = {'0':register, '1':login}
#
#     while 1:
#         choice = input(prompt).strip()
#         if choice not in "012":
#             print('invalid choice. try again')
#             continue
#
#         if choice == "2":
#             break
#
#         cmds[choice]()
#
# if __name__ == '__main__':
#     show_menu()

# with open('/tmp/a.log') as f1:
#     aset = set(f1)
#
# with open('/tmp/b.log') as f2:
#     bset = set(f2)
#
# with open('/tmp/result.txt', 'w') as f3:
#     f3.writelines(bset - aset)

# stack = []
#
# def push_it():
#     data = input('data: ').strip()
#
#     if data:
#         stack.append(data)
#     else:
#         print('please entry data')
#
# def pop_it():
#     if stack:
#         print('%s is poped' % stack.pop())
#     else:
#         print('stack is empty')
#
# def view_it():
#         print(stack)
#
# def show_menu():
#     cmds = {'0': push_it, '1': pop_it, '2': view_it}
#     prompt = """(0)push
# (1)pop
# (2)view
# (3)exit
# please enter(0/1/2/3): """
#
#     while 1:
#         choice = input(prompt).strip()
#
#         if choice not in ['0', '1', '2', '3']:
#             print('invalid option try again')
#             continue
#
#         if choice == '3':
#             print('\n886')
#             break
#
#         cmds[choice]()
#
# if __name__ == '__main__':
#     show_menu()

import getpass
from randpass2 import randpass
import crypt

userdb = {}

def register():
    username = input('username: ').strip()
    if username and username not in userdb:
        password = input('password: ')
        cpasswd = crypt.crypt(password, '$6$%s$' % randpass())
        userdb[username] = cpasswd
        print(cpasswd)
    else:
        print('user is exsist or you have not enter anything')

def login():
    username = input('username: ').strip()
    password = getpass.getpass('password: ')
    cpasswd = crypt.crypt(password, '$6$%s$' % userdb[username][3:11] )
    if userdb.get(username) == cpasswd:
        print('login successful')
        print(cpasswd)
    else:
        print('login incorrect')
        print(cpasswd)

def show_menu():
    cmds = {'0':register, '1':login}
    prompt = """(0)register
(1)login
(2)exit
please enter(0/1/2):  """

    while 1:
        choice = input(prompt).strip()

        if choice not in "012":
            print('invalid option try again')
            continue

        if choice == "2":
            print('\n886')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()