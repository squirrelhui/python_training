# class Role:
#     def __init__(self, name, weapon):
#         "__init__是构造器方法，创建实例是，它自动调用,一般用于将属性绑到对象"
#         self.name = name
#         self.weapon = weapon
#
# if __name__ == '__main__':
#     # 实例化时，实例名lb将自动作为第一个参数，传给相关的方法
#     lb = Role('吕布', '方天画戟')
#     print(lb.name, lb.weapon)
#
# class Role:
#     def __init__(self, name, weapon):
#         self.name = name
#         self.weapon = weapon
#
#     def show_me(self):
#         "绑定载实例上的属性，载任意方法中都直接可用"
#         print('我是%s, 我的兵器是%s' % (self.name, self.weapon))
#
# if __name__ == '__main__':
#     lb = Role('吕布', 'gun')
#     print(lb.name, lb.weapon)
#     lb.show_me()

# class Role:
#     def __init__(self, name, weapon):
#         "__init__是构造器方法，创建实例时，它自动调用,一般用于将属性绑到对象"
#         self.name = name
#         self.weapon = weapon
#
#     def show_me(self):
#         "绑定载实例上的属性，载任意方法中都直接可用"
#         print('我是%s, 我的兵器是%s' % (self.name, self.weapon))
#
#     def say(self, words):
#         "没有绑定的变量，是临时变量"
#         print(words)
# if __name__ == '__main__':
#     # 实例化时，实例名lb将自动作为第一个参数，传给相关的方法
#     lb = Role('吕布', '方天画戟')
#     print(lb.name, lb.weapon)
#     lb.show_me()
#     lb.say('马中赤兔，人中吕布')
#
#     zf = Role('张飞', '丈八蛇矛')
#     zf.show_me()

class Role:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def show_me(self):
        print('我是%s，%s是我的，冲啊！！！' % (self.name, self.weapon))

    def say(self, words):
        print(words)

class Warrior(Role):
    def __init__(self, name, weapon, country):
        #Role.__init__(self, name, weapon, country)
        # 以上调用父类方法的语句，也可以使用
        super(Warrior, self).__init__(name, weapon)
        self.country = country

    def attack(self, target):
        print('近身攻击：%s' % target)

class Mage(Role):
    def attack(self, target):
        print('远身攻击：%s' % target)

if __name__ == '__main__':
    gy = Warrior('关羽', '青龙', '蜀')
    km = Mage('孔明', '羽扇')
    gy.show_me()
    km.show_me()
    gy.attack('吕布')
    km.attack('周瑜')
