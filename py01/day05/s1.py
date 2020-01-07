stack = []

def push_it():
    data = input('请输入数据： ')
    if data:
        stack.append(data)
    else:
        print('输入为空')

def pop_it():
    if stack:
        print('弹除了%s' % stack.pop())
    else:
        print('列表为空')

def view_it():
    print(stack)

def show_menu():
    prompt = '''
(0)push
(1)pop
(2)view
(3)exit
'''
    while 1:
        choice = input(prompt).strip()

        if choice not in ['0','1', '2', '3']:
            print('无效输入')
            continue
        elif choice == '0':
            push_it()
        elif choice == '1':
            pop_it()
        elif choice == '2':
            view_it()
        else:
            print('\n88')
            break

if __name__ == '__main__':
    show_menu()