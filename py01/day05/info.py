# info = {}
#
# def new_user():
#     user = input('请输入用户名： ')
#     passwd = input()
# def login():
#
# def show_menu():
#     prompt = '''
# (0)用户登陆
# (1)用户注册
# (2)退出
# '''
#     cmds = ["0", new_user(), '1', login()]
#     while 1:
#         choice = input(prompt).strip()
#
#         if choice == 2:
#             print('\n886')
#             break
#
#         cmds = [choice]()

# import getpass
#
# info = {}
#
# def register():
#     '用于注册用户'
#     user = input('请输入用户名：').strip()
#
#     if user and (user not in info):
#         passwd = input('请输入密码：')
#         info[user] = passwd
#
#     else:
#         print('用户已存在，请登录或修改密码！')
#
# def login():
#     '用于验证登陆'
#     user = input('请输入用户名：').strip()
#     passwd = getpass.getpass('请输入密码：')
#     #if user in info and passwd == info[user]:
#     if info.get(user) == passwd:
#         print('login successful')
#     else:
#         print('login incorrect!')
#
# def show_menu():
#     cmds = {'0':register, '1':login}
#     prompt = """
# (0)注册
# (1)登陆
# (2)退出
# 请输入（0/1/2）：
#     """
#     while 1:
#         choice = input(prompt).strip()
#         if choice not in ['0', '1', '2']:
#             print('无效输入，请重试')
#             continue
#
#         if choice == '2':
#             print('\n886')
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
#     username = input('please enter username: ')
#     if username and username not in userdb:
#         passwd = input('please enter password: ')
#         userdb[username] = passwd
#     else:
#         print('用户名为空或用户不存在')
#
# def login():
#     username = input('please enter username: ')
#     passwd = getpass.getpass('please enter password: ')
#
#     if userdb.get(username) == passwd:
#         print('login successful')
#     else:
#         print('login incorrect')
#
# def show_menu():
#     cmds = {'0':register, '1':login}
#     prompt = """(0)register
# (1)login
# (2)exit
# please enter(0/1/2): """
#     while 1:
#         choice = input(prompt).strip()
#
#         if choice not in ['0', '1', '2']:
#             print('invaild enter!')
#
#         if choice == '2':
#             print('\n886')
#             break
#
#         cmds[choice]()
# if __name__ == '__main__':
#     show_menu()
#
# import crypt
# import randpass2
#
# password = input('passwd: ')
#
# cp = crypt.crypt(password,'$6$%s$' % randpass2.randpass())
#
# print(cp)