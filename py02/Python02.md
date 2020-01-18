# Python02

# Python02 day01

## 一、时间方法

### （一）时间方法

#### 1、时间表示方式

• 时间戳timestamp:表示的是从1970年1月1日00:00:00开始按秒计算的偏移量
• UTC(Coordinated Universal Time,世界协调时)亦即格林威治天文时间,世界标准时间。在中国为UTC+8。DST(Daylight Saving Time)即夏令时
• 元组(struct_time):由9个元素组成（年，月，日，时，分，秒，一周中的第几天，一年中的第几天，是否使用夏令时）

```python
>>> import time
>>> time.time()            # 运行命令时的时间戳
1578446822.986791
>>> time.ctime()           # UTC时间
'Wed Jan  8 09:28:09 2020'
>>> time.localtime()       # struct_时间
time.struct_time(tm_year=2020, tm_mon=1, tm_mday=8, tm_hour=9, tm_min=30, tm_sec=1, tm_wday=2, tm_yday=8, tm_isdst=0)
>>> t = time.localtime()
>>> t
time.struct_time(tm_year=2020, tm_mon=1, tm_mday=8, tm_hour=9, tm_min=30, tm_sec=47, tm_wday=2, tm_yday=8, tm_isdst=0)
>>> t.tm_year
2020

```



#### 2、struct_time元组

| 索引 | 属性                    | 值             |
| ---- | ----------------------- | -------------- |
| 0    | tm_year                 | 2000           |
| 1    | tm_mon                  | 1-12           |
| 2    | tm_mday                 | 1-31           |
| 3    | tm_hour                 | 0-23           |
| 4    | tm_min                  | 0-59           |
| 5    | tm_sec                  | 0-61           |
| 6    | tm_wday                 | 0-6(0表示周一) |
| 7    | tm_yday(一年中的第几天) | 1-366          |
| 8    | tm_isdst(是否为dst时间) | 默认为-1       |



#### 3、time模块方法

• time.localtime([secs]):将一个时间戳转换为当前时区的struct_time。secs参数未提供,则以当前时间为准
• time.gmtime([secs]):和localtime()方法类似,gmtime()方法是将一个时间戳转换为UTC时区(0时区)的struct_time
• time.time():返回当前时间的时间戳
• time.mktime(t):将一个struct_time转化为时间戳

• time.sleep(secs):线程推迟指定的时间运行。单位为秒
• time.asctime([t]):把一个表示时间的元组或者struct_time表示为这种形式:‘Sun Jun 2023:21:05 1993’。如果没有参数,将会将
time.localtime()作为参数传入
• time.ctime([secs]):把一个时间戳(按秒计算的浮点数)转化为time.asctime()的形式

• time.strftime(format[, t]):把一个代表时间的元组或者struct_time(如由time.localtime()和time.gmtime()返回)转化为格式化的时间字符串。
如果t未指定,将传入time.localtime()
• time.strptime(string[, format]):把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作

```python
>>> time.sleep(3)  #睡眠三秒
>>> time.strftime('%Y-%m-%d %H:%M:%S')
'2020-01-08 09:51:24'
>>> time.strftime('%a')
'Wed'
>>> time.strftime('%A')
'Wednesday'

#将时间字符串转为0元组时间格式
>>> t1 = time.strptime('2020-01-08 10:30:00', '%Y-%m-%d %H:%M:%S')
>>> t = time.localtime()
>>> t > t1
False
```



#### 4、时间样式

| 格式 | 含义                                | 格式 | 含义                                              |
| ---- | ----------------------------------- | ---- | ------------------------------------------------- |
| %a   | 本地简化星期名称                    | %m   | 月份(01	- 12)                                  |
| %A   | 本地完整星期名称                    | %M   | 分钟数(00	- 59)                                |
| %b   | 本地简化月份名称                    | %p   | 本地am或者pm的相应符                              |
| %B   | 本地完整月份名称                    | %S   | 秒(01	- 61)                                    |
| %c   | 本地相应的日期和时间                | %U   | 一年中的星期数(00	– 53,星期日是一个星期的开始) |
| %d   | 一个月中的第几天(01- 31)            | %w   | 一个星期中的第几天(0- 6,0是星期天)                |
| %H   | 一天中的第几个小时(24小时制,00- 23) | %x   | 本地相应日期                                      |
| %I   | 第几个小时(12小时制,01-12)          | %X   | 本地相应时间                                      |
| %j   | 一年中的第几天(001	- 366)        | %y   | 去掉世纪的年份(00	- 99)                        |
| %Z   | 时区的名字                          | %Y   | 完整的年份                                        |

```python
import time

t9 = time.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')

with open('weblog.txt') as fobj:
    for line in fobj:
        t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        #if t9 <= t <= t12:
            #print(line, end='')
         if t > t12:
            break
         if t >= t9:
            print(line, end='')
```





### （二）datatime模块

#### 1、datatime模块方法

• datetime.today():返回一个表示当前本地时间的datetime对象
• datetime.now([tz]):返回一个表示当前本地时间的datetime对象,如果提供了参数tz,则获取tz参数所指时区的本地时间
• datetime.strptime(date_string, format):将格式字符串转换为datetime对象
• datetime.ctime(datetime对象):返回时间格式字符串
• datetime.strftime(format):返回指定格式字符串

```python
>>> from datetime import datetime
>>> datetime.now()   # 返回的是（年，月，日，时，分，秒，毫秒）
datetime.datetime(2020, 1, 8, 10, 57, 50, 893440)
>>> t = datetime.now()
>>> t.year
2020
>>> t.month
1
>>> t.day
8
>>> t.hour
10
>>> t.minute
58
>>> t.second
6
>>> t.microsecond
838514

>>> t.strftime('%Y-%m-%d %H:%M:%S') # 转成时间字符串
'2020-01-08 10:58:06'

#时间字符串转换成datetime对象
>>> datetime.strptime('2020-01-08 09:00:00', '%Y-%m-%d %H:%M:%S')
datetime.datetime(2020, 1, 8, 9, 0)

```





#### 2、时间计算

• 使用timedelta可以很方便的在日期上做天days,小时hour,分钟,秒,毫秒,微妙的时间计算

```python
#可以通过timedelta计算计算时间
>>> from datetime import datetime, timedelta
>>> days = timedelta(days=100, hours=1)    #定义100天零1小时
>>> t = datetime.now()
>>> t- days  # 100天1小时之前的时间
datetime.datetime(2019, 9, 30, 10, 34, 3, 254445)
>>> t+ days  # 100天1小时之后的时间
datetime.datetime(2020, 4, 17, 12, 34, 3, 254445)

```



## 二、异常处理

### （一）异常

#### 1、什么是异常

• 当python检测到一个错误时,解释器就会指出当前流已经无法继续执行下去,这时候就出现了异常
• 异常是因为程序出现了错误而在正常控制流以外采取的行为
• 这个行为又分为两个阶段:
– 首先是引起异常发生的错误
– 然后是检测(和采取可能的措施)阶段

#### 2、python中的异常

• 当程序运行时,因为遇到未解的错误而导致中止运行,便会出现traceback消息,打印异常

| 异常              | 描述                     |
| ----------------- | ------------------------ |
| NameError         | 未声明/初始化对象        |
| IndexError        | 序列中没有没有此索引     |
| SyntaxError       | 语法错误                 |
| KeyboardInterrupt | 用户中断执行             |
| EOFError          | 没有内建输入,到达EOF标记 |
| IOError           | 输入/输出操作失败        |



#### 3、try-except语句

• 定义了进行异常监控的一段代码,并且提供了处理异常的机制

```python
try:
try_suite #监控这里的异常
except Exception[as reason]:
except_suite #异常处理代码
>>>	try:
...		 f	= open('foo.txt')
...	except	FileNotFoundError:
...		 print('No such file')
...
No such file
```



#### 4、带有多个expect的try语句

• 可以把多个except语句连接在一起,处理一个try块中可能发生的多种异常

```python
>>>	try:
...	 	data = int(input('input	a number: '))
...	except KeyboardInterrupt:
...		 print 'user cancelled'
...	except ValueError:
...		 print('you	must input a number!’)
...
input a	number:	hello
you	must input a number!
```



#### 5、捕获所有异常

```python
try :
    num = int(input('number: '))
    result = 100 / num
    print(result)
    print('Done')
except ValueError:
    print('只接受数字')
except ZeroDivisionError:
    print('不能输入0')
except EOFError:
    print('不要CTRL+D')
except KeyboardInterrupt:
    print('不要CTRL+C')
```



#### 6、异常参数

• 异常也可以有参数,异常引发后它会被传递给异常处理器
• 当异常被引发后参数是作为附加帮助信息传递给异常处理器的

```python
try :
    num = int(input('number: '))
    result = 100 / num
    print(result)
    print('done')
except (KeyboardInterrupt, EOFError) as e: # 将异常保存到变量e中
    print('\n886: ',e)
except (ValueError, ZeroDivisionError):
    print('只接受非零数字')
```



#### 7、else字句

• 在try范围中没有异常被检测到时,执行else子句
• 在else范围中的任何代码运行前,try范围中的所有代码必须完全成功

```python
try :
    num = int(input('number: '))
    result = 100 / num

except (KeyboardInterrupt, EOFError):
    print('\n886: ')
except (ValueError, ZeroDivisionError) as e:
    print('只接受非零数字', e)
    exit(101) #101为程序退出码
else:   #异常不发生才会执行的语句放到else中
    print(result)
    
print('done')
```



#### 8、finally字句

• finally子句是无论异常是否发生,是否捕捉都会执行的一段代码
• 如果打开文件后,因为发生异常导致文件没有关闭,可能会发生数据损坏。使用finally可以保证文件总是能正常的关闭

```python
try :
    num = int(input('number: '))
    result = 100 / num

except (KeyboardInterrupt, EOFError):
    print('\n886: ')
except (ValueError, ZeroDivisionError) as e:
    print('只接受非零数字', e)
    exit(101) #101为程序退出码
else:   #异常不发生才会执行的语句放到else中
    print(result)
finall： # 不管异常是否发生，都会执行的语句发到finally  
	print('done')
```



### （二）异常处理

#### 1、raise语句

• 要想引发异常,最简单的形式就是输入关键字raise,后面跟要引发的异常的名称
• 执行raise语句时,Python会创建指定的异常类的一个对象
• raise语句还可指定对异常对象进行初始化的参数

```python
>>> raise ValueError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError
>>> raise IndexError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError
>>> raise abcd  #必须是系统自带的异常模块
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'abcd' is not defined

```



#### 2、断言

• 断言是一句必须等价于布尔值为真的判定
• 此外,发生异常也意味着表达式为假

```python
def get_info(name, age):
    if not 0< age < 120:
        raise ValueError('年龄超过范围（1-119）')
    print('%s is %d years old' % (name, age))

def get_info2(name, age):
    # age在0-120之间什么也不会发生，如果不是，则发生AssertionError异常
    assert 0 < age < 120, '年龄超过范围（1-119）'
    print('%s is %d years old' % (name, age))
```

```python
import get_info

name = 'nb'
age = 20
age2 = 200

try :
    get_info.get_info(name, age)
    get_info.get_info2(name, age2)
except (ValueError, AssertionError) as e:
    print('Error', e)
```



## 三、OS相关模块

### （一）os模块

#### 1、os模块简介

• 对文件系统的访问大多通过python的os模块实现
• 该模块是python访问操作系统功能的主要接口
• 有些方法,如copy等,并没有提供,可以使用shutil模块作为补充

#### 2、os模块方法

| 函数       | 作用               |
| ---------- | ------------------ |
| symlink()  | 创建符号链接       |
| listdir()  | 列出指定目录的文件 |
| getcwd()   | 返回当前工作目录   |
| mkdir()    | 创建目录           |
| chmod()    | 改变权限模式       |
| getatime() | 返回最近访问时间   |
| chdir()    | 改变工作目录       |

```python
>>> import os
>>> os.listdir()  #ls 
>>> os.mkdir('/tmp/aaa')   # mkdir /tmp/aaa
>>> os.makedirs('/tmp/nsd1908/demo')   # mkdir -p /tmp/nsd1908/demo
>>> os.listdir('/tmp/nsd1908')  # ls /tmp/nsd1908
['demo']
>>> os.chdir('/tmp/nsd1908')  # cd
>>> os.getcwd()  # pwd
'/tmp/nsd1908'
>>> import shutil
>>> shutil.copy('/etc/hosts', 'hosts')  #cp
'hosts'
>>> os.mknod('test.txt')  #touch
>>> os.symlink('/etc/passwd', 'mima')  #创建软连接/符号链接

>>> os.listdir()
['demo', 'hosts', 'mima', 'test.txt']
>>> os.chmod('hosts', 0o600) # chmod 600 hosts
>>> os.chmod('hosts', 420) # chmod 644 hosts
>>> os.listdir()
['demo', 'hosts', 'mima', 'test.txt']
>>> os.path.abspath('demo') # 返回绝对路径
'/tmp/nsd1908/demo'

>>> os.path.isabs('/aaa/bbb/cc')  # 路径式绝对路径吗？
True
>>> os.path.isabs('aaa/bbb/cc')
False
>>> os.path.isfile('hosts') # host存在，并且是文件吗？
False
>>> os.path.ismount('/etc') #是挂载点么？
False
>>> os.path.isdir('demo')    # demo存在，并且是目录吗？
True
>>> os.path.islink('mama')   #存在，并且是软连接吗？
False
>>> os.path.exists('/etc/hostname') # 存在吗？
True
>>> os.path.basename('/tmp/nsd1908/hosts')
'hosts'
>>> os.path.dirname('/tmp/nsd1908/hosts')
'/tmp/nsd1908'
>>> os.path.split('/tmp/nsd1908/hosts')
('/tmp/nsd1908', 'hosts')
>>> os.path.join('/tmp/nsd1908','hosts')
'/tmp/nsd1908/hosts'
```

#### 3、os.walk

```python
[student@room9pc01 nsd1908]$ mkdir aaa bbb
[student@room9pc01 nsd1908]$ touch aaa/{a,b,c}.txt
[student@room9pc01 nsd1908]$ touch bbb/{d,e,f}.txt
[student@room9pc01 nsd1908]$ ls
aaa  bbb  demo  hosts  mima  test.txt
[student@room9pc01 nsd1908]$ touch demo/{x,y,z}.txt
[student@room9pc01 nsd1908]$ cd ..
[student@room9pc01 tmp]$ ls -R nsd1908
nsd1908:
aaa  bbb  demo  hosts  mima  test.txt

nsd1908/aaa:
a.txt  b.txt  c.txt

nsd1908/bbb:
d.txt  e.txt  f.txt

nsd1908/demo:
x.txt  y.txt  z.txt

>>> list(os.walk('/tmp/nsd1908'))
[('/tmp/nsd1908', ['demo', 'bbb', 'aaa'], ['hosts', 'mima', 'test.txt']), ('/tmp/nsd1908/demo', [], ['z.txt', 'y.txt', 'x.txt']), ('/tmp/nsd1908/bbb', [], ['d.txt', 'e.txt', 'f.txt']), ('/tmp/nsd1908/aaa', [], ['a.txt', 'b.txt', 'c.txt'])]
>>> alist = list(os.walk('/tmp/nsd1908'))
>>> alist[0]
('/tmp/nsd1908', ['demo', 'bbb', 'aaa'], ['hosts', 'mima', 'test.txt'])
>>> alist[1]
('/tmp/nsd1908/demo', [], ['z.txt', 'y.txt', 'x.txt'])
>>> alist[2]
('/tmp/nsd1908/bbb', [], ['d.txt', 'e.txt', 'f.txt'])
>>> alist[3]
('/tmp/nsd1908/aaa', [], ['a.txt', 'b.txt', 'c.txt'])
# 经过分析，列表由元组构成
# 每个元组都由相同的结构：（路径字符串，路径下目录列表，路径下文件列表）

>>> for data in alist:
...     print(data)
... 
('/tmp/nsd1908', ['demo', 'bbb', 'aaa'], ['hosts', 'mima', 'test.txt'])
('/tmp/nsd1908/demo', [], ['z.txt', 'y.txt', 'x.txt'])
('/tmp/nsd1908/bbb', [], ['d.txt', 'e.txt', 'f.txt'])
('/tmp/nsd1908/aaa', [], ['a.txt', 'b.txt', 'c.txt'])

>>> for path, folders, files in os.walk('/tmp/nsd1908'):
...     print('%s:' % path)
...     for dir in folders:
...             print(dir, end='\t')
...     for file in files:
...             print(file, end='\t')
...     print('\n')
... 
/tmp/nsd1908:
demo    bbb     aaa     hosts   mima    test.txt        

/tmp/nsd1908/demo:
z.txt   y.txt   x.txt   

/tmp/nsd1908/bbb:
d.txt   e.txt   f.txt   

/tmp/nsd1908/aaa:
a.txt   b.txt   c.txt  
```





### （二）pickle模块

#### 1、pickle模块简介

• 把数据写入文件时,常规的文件方法只能把字符串对象写入。其他数据需先转换成字符串再写入文件 。
• python提供了一个标准的模块,称为pickle。使用它可以在一个文件中储存任何python对象,之后又可以把它完整无缺地取出来。

#### 2、pickle模块方法

• 分别调用dump()和load()可以存储、写入

```python
>>> import pickle
>>> shopping_list = ['apple', 'banana', 'egg']
>>> with open('/tmp/a.txt', 'wb') as fobj:
...     pickle.dump(shopping_list, fobj)
 
>>> with open('/tmp/a.txt', 'rb') as fobj:
...     alist = pickle.load(fobj)
... 
>>> type(alist)
<class 'list'>
>>> alist
['apple', 'banana', 'egg']

```

3、案例4:记账程序

1. 假设在记账时,有一万元钱

2. 无论是开销还是收入都要进行记账

3. 记账内容包括时间、金额和说明等

4. 记账数据要求永久存储

   ```python
   import os
   import pickle
   from time import strftime
   
   def save(fname):
       '用于记录收入'
       try:
           amount = int(input('金额: '))
           comment = input('备注: ')
       except ValueError:
           print('无效的金额。')
           # 函数的return类似于循环的break，遇到return将结束函数
           return
       except (KeyboardInterrupt, EOFError):
           print('\nBye-bye')
           exit()
   
       date = strftime('%Y-%m-%d')
       # 取出全部的收支情况列表
       with open(fname, 'rb') as fobj:
           records = pickle.load(fobj)
       # 计算最新余额
       balance = records[-1][-2] + amount
       # 构建收入情况列表
       line = [date, amount, 0, balance, comment]
       records.append(line)
       # 将更新后的收支情况列表写回文件
       with open(fname, 'wb') as fobj:
           pickle.dump(records, fobj)
   
   def cost(fname):
       '用于记录开销'
       try:
           amount = int(input('金额: '))
           comment = input('备注: ')
       except ValueError:
           print('无效的金额。')
           # 函数的return类似于循环的break，遇到return将结束函数
           return
       except (KeyboardInterrupt, EOFError):
           print('\nBye-bye')
           exit()
   
       date = strftime('%Y-%m-%d')
       # 取出全部的收支情况列表
       with open(fname, 'rb') as fobj:
           records = pickle.load(fobj)
       # 计算最新余额
       balance = records[-1][-2] - amount
       # 构建收入情况列表
       line = [date, 0, amount, balance, comment]
       records.append(line)
       # 将更新后的收支情况列表写回文件
       with open(fname, 'wb') as fobj:
           pickle.dump(records, fobj)
   
   def query(fname):
       '用于查询收支情况'
       with open(fname, 'rb') as fobj:
           records = pickle.load(fobj)
   
       # 打印表头
       print('%-12s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
       # 打印内容
       for line in records:
           print('%-12s%-8s%-8s%-12s%-20s' % tuple(line))
   
   
   def show_menu():
       cmds = {'0': save, '1': cost, '2': query}
       prompt = """(0) 收入
   (1) 开销
   (2) 查询
   (3) 退出
   请选择(0/1/2/3): """
       fname = 'account.data'
       init_data = [['2020-01-09', 0, 0, 10000, 'init data']]
       if not os.path.exists(fname):
           with open(fname, 'wb') as fobj:
               pickle.dump(init_data, fobj)
   
       while 1:
           try:
               choice = input(prompt).strip()
           except (KeyboardInterrupt, EOFError):
               choice = '3'
   
           if choice not in ['0', '1', '2', '3']:
               print('无效的输入，请重试。')
               continue
   
           if choice == '3':
               print('\nBye-bye')
               break
   
           cmds[choice](fname)
   
   if __name__ == '__main__':
       show_menu()
   ```

   

   

# Python02 day02

## 一、函数基础

### （一）创建函数

#### 1、def语句

• 函数用def语句创建,语法如下:

```python
def function_name(arguments):
    "function_documentation_string"
    function_body_suite
```

• 标题行由def关键字,函数的名字,以及参数的集合(如果有的话)组成
• def子句的剩余部分包括了一个虽然可选但是强烈推荐的文档字串,和必需的函数体

#### 2、前向引用

• 函数不允许在函数未声明之前对其进行引用或者调用

### （二）调用函数操作符

### 1、函数操作符

• 使用一对圆括号()调用函数,如果没有圆括号,只是对函数的引用
• 任何输入的参数都必须放置在括号中

#### 2、关键字参数

• 关键字参数的概念仅仅针对函数的调用
• 这种理念是让调用者通过函数调用中的参数名字来区分参数
• 这样规范允许参数缺失或者不按顺序

（1）只写参数名，如args， 称作位置参数

（2）写成key=value形式的参数， 称作关键字参数

```python
>>> def get_age(name, age):
...     print('%s is %s years old' % (name, age))
... 
>>> get_age('tom', 20)
tom is 20 years old    # OK
>>> get_age(20, 'tom') # ok ，但语义不对
20 is tom years old
>>> get_age(age=20, name='tom') # ok          
tom is 20 years old
>>> get_age('tom', 20， 30) #错误，参数太多
>>> get_age('tom') #错误，参数不足
>>> get_age(age=20, 'tom') #错误，位置参数需要在关键字参数前面
>>> get_age(20, name='tom') #，name得到了多个值
>>> get_age('tom', age=20) #OK
```



#### 3、参数组

• python允许程序员执行一个没有显式定义参数的函数
• 相应的方法是通过一个把元组(非关键字参数)或字典(关键字参数)作为参数组传递给函数

（1）创建函数时，在参数名前*号，表示参数是元组

（2）创建函数是，载参数明前**号，表示参数是字典

```python
>>> func1()
()
>>> func1('hao')
('hao',)
>>> func1('hao', 123)
('hao', 123)

>>> def func2(**kwargs):
...     print(kwargs)
... 
>>> func2()
{}
>>> func2(name='tom', age=20)
{'name': 'tom', 'age': 20}
```

（3）调用函数时，在序列对象前加*号，表示将序列对象拆分开

（4）调用函数时，在字典对象前加**号，表示将序列对象拆分开

```python
>>> def get_age(name, age):
...     print('%s is %s years old' % (name, age))
... 
>>> user = ['bob', 25]
>>> get_age(user[0], user[1])
bob is 25 years old
>>> get_age(*user)
bob is 25 years old

>>> userdict = {'name':'tom', 'age':20}
>>> get_age(**userdict)
tom is 20 years old
>>> get_age(name='tom', age=20)
tom is 20 years old

```

#### 4、案例1:简单的加减法数学游戏

1. 随机生成两个100以内的数字

2. 随机选择加法或是减法

3. 总是使用大的数字减去小的数字

4. 如果用户答错三次,程序给出正确答案

   ```python
   from random import randint, choice
   
   def exam():
       '用于出题，让用户作答'
       # 随机生成两个数字
       nums = [randint(1, 100) for i in range(2)]
       # 降序排列
       nums.sort(reverse=True)
       # 随机选出加减法
       op = choice('+-')
   
       # 计算出正确答案
       if op == '+':
           result = nums[0] + nums[1]
       else:
           result = nums[0] - nums[1]
   
       # 要求用户作答，并判断正误
       prompt = '%s %s %s = ' % (nums[0], op, nums[1])
       counter = 0
       while counter < 3:
           try:
               answer = int(input(prompt))
           except:
               print()   # 打印回车
               continue
   
           if answer == result:
               print('Very Good!!!')
               break
   
           print('不对哟!!!')
           counter += 1
       else:
           print('\033[31;1m正确答案: %s%s\033[0m' % (prompt, result))
   
   def main():
       while 1:
           exam()
           try:
               yn = input('Continue(y/n)? ').strip()[0]  # 取第一个字符
           except IndexError:
               continue
           except (KeyboardInterrupt, EOFError):
               yn = 'n'
   
           if yn in 'nN':
               print('\nBye-bye')
               break
   
   if __name__ == '__main__':
       main()
   ```

   

### （三）匿名函数

#### 1、lambda

• python允许用lambda关键字创造匿名函数
• 匿名是因为不需要以标准的def方式来声明
• 一个完整的lambda“语句”代表了一个表达式,这个表达式的定义体必须和声明放在同一行

```python
lambda [arg1[, arg2, ... argN]]: expression
>>>	a =	lambda x, y: x + y
>>>	print(a(3, 4))
7

>>> def add(x, y):
...     return x + y
... 
>>> add(10 ,3)
13
>>> lambda x, y : x + y
<function <lambda> at 0x7fc5cf606598>
>>> myadd = lambda x, y : x + y
>>> myadd(10, 20)
30
```

利用匿名函数完善案例1

```python
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
```



#### 2、filter（）函数

• filter(func, seq):调用一个布尔函数func来迭代遍历每个序列中的元素;返回一个使func返回值为true的元素的序列
• 如果布尔函数比较简单,直接使用lambda匿名函数就显得非常方便了

（1）filter函数接受两个参数，第一个参数是函数，第二个参数是序列对象

 	（filter的参数）函数接受一个参数，返回值必须是True或False。

​		将序列对象中的每一个数据交给函数处理，返回真的留下假的丢弃。

```python
from random import randint

def func1(x):
    return True if x % 2 == 1  else False

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result = filter(func1, nums)
    print(list(result))
    result1 = filter(lambda  x: True if x %2 == 1 else False, nums)
    print(list(result1))
```





#### 3、map（）函数

• map(func, seq):调用一个函数func来迭代遍历每个序列中的元素;返回一个经过func处理过的元素序列
• 如果布尔函数比较简单,直接使用lambda匿名函数就显得非常方便了

map函数接受两个参数，第一个参数是函数，第二个参数是序列对象

​	函数接受一个参数，对参数进行加工处理，返回处理结果

​	map调用时，将序列对象逐一个

```python
from random import randint

def func2(x):
    return x * 2

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result = map(func2, nums)
    print(list(result))
    result1 = map(lambda x : x * 2, nums)
    print(list(result1))
```





## 二、函数高级应用

### （一）变量作用域

#### 1、全局变量

• 标识符的作用域是定义为其声明在程序里的可应用范围,也就是变量的可见性
• 在一个模块中最高级别的变量有全局作用域
• 全局变量的一个特征是除非被删除掉,否则它们的存活到脚本运行结束,且对于所有的函数,他们的值都是可以被访问的

（1）在函数外面的标量是全局变量。全局变量从定义开始，到程序借宿，一直可见可用。

```py
>>> x = 10
>>> def func1():
...     print(x)
... 
>>> func1()
10

```





#### 2、局部变量

• 局部变量只时暂时地存在,仅仅只依赖于定义它们的函数现阶段是否处于活动
• 当一个函数调用出现时,其局部变量就进入声明它们的作用域。在那一刻,一个新的局部变量名为那个对象创建了
• 一旦函数完成,框架被释放,变量将会离开作用域

在函数内部的变量是局部变量，只能在函数内部使用

```python
>>> def func2():
...     y = 100
...     print(y)
... 
>>> func2()
100
>>> y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined

```

• 如果局部与全局有相同名称的变量,那么函数运行时,局部变量的名称将会把全局变量名称遮盖住

```python
>>> x = 10
>>> def func3():
...     x = 200
...     print(x)
... 
>>> func3()
200
>>> x
10
```



#### 3、global语句

因为全局变量的名字能被局部变量给遮盖掉,所以为了明确地引用一个已命名的全局变量,必须使用
global语句

```python
>>> def func4():
...     global x
...     x = 100
...     print(x)
... 
>>> func4()
100
>>> x
100
```

### （二）函数式编程

#### 1、偏函数

• 偏函数的概念是将函数式编程的概念和默认参数以及可变参数结合在一起
• 一个带有多个参数的函数,如果其中某些参数基本上固定的,那么就可以通过偏函数为这些参数赋默认值

改造现有函数，

```python
>>> def add(a, b, c, d, e):
...     return a + b + c + d + e
... 
>>> add(10, 20, 30, 40, 3)
103
>>> add(10, 20, 30, 40, 5)
105
>>> add(10, 20, 30, 40, 9)
109
>>> from functools import partial
>>> myadd = partial(add, 10, 20, 30, 40)
>>> myadd(3)
103
>>> myadd(5)
105

>>> int('10101100')  
10101100
>>> int('10101100', base=2)  # 说明数字字符串是2进制数
172
>>> int('11000000', base=2)  
192
>>> int2 = partial(int, base=2) #改造int函数，指定base=2
>>> int2('1100000')
96
>>> int2('11000011')
195

```



#### 2、案例2:简单GUI程序

1. 窗口程序提供三个按钮

2. 其中两个按钮的前景色均为白色,背景色为蓝色

3. 第三个按钮前景色为红色,背景色为红色

4. 按下第三个按钮后,程序退出

   ```python
   
   ```



#### 3、递归函数

一个函数内部又包含了对自身的调用，就是递归函数

• 如果函数包含了对其自身的调用,该函数就是递归的
• 在操作系统中,查看某一目录内所有文件、修改权限等都是递归的应用

```python
5!5*4*3*2*1*
5!=5*4!
5!=5*4*3!
5!=5*4*3*2!
5!=5*4*3*2*1!
1!=1

def func1(x):
    if x == 1:
        return 1
    return x * func1(x - 1)
#          5 * func1(4)
#          5 * 4 * func1(3)
#          5 * 4 * 3 * func1(2)
#          5 * 4 * 3 * 2 * func1(1)
#          5 * 4 * 3 * 2 * 1
if __name__ == '__main__':
    result = func1(5)
    print(result)
```

#### 4、案例3:快速排序

1. 随机生成10个数字

2. 利用递归,实现快速排序

   ```python
   from random import randint
   
   def qsort(seq):
       if len(seq) < 2:
           return seq
       # 假设第一个数是中间值
       middle = seq[0]
       smaller = []
       larger = []
       #遍历后续数字，比中间值小的放到smaller，大的放到larger
       for data in seq[1:]:
           if data <= middle:
               smaller.append(data)
           else:
               larger.append(data)
       # 把三项数据拼接, smaller和larger采用相同的方法继续排序
       return qsort(smaller) + [middle] + qsort(larger)
   
   if __name__ == '__main__':
       nums = [randint(1, 100) for i in range(10)]
       print(nums)
       print(qsort(nums))
   ```

   

#### 5、生成器

本质上是一个函数

可以通过yield语句返回很多中间结果

• 从句法上讲,生成器是一个带yield语句的函数
• 一个函数或者子程序只返回一次,但一个生成器能暂停执行并返回一个中间的结果
• yield 语句返回一个值给调用者并暂停执行
• 当生成器的next()方法被调用的时候,它会准确地从离开地方继续

• 与迭代器相似,生成器以另外的方式来运作
• 当到达一个真正的返回或者函数结束没有更多的值返回,StopIteration异常就会被抛出

```python
>>> def mygen():
...     yield 100
...     a = 10 +20
...     yield a
...     yield 1000
... 
>>> mg = mygen()
>>> mg
<generator object mygen at 0x7f5d279f0360>
>>> 
>>> list(mg)
[100, 30, 1000]
# 生成器只能使用一次，产生一次值，再次使用需要重新赋值。
>>> for i in mg:
...     print(i)    # 输出为空
... 

>>> mg = mygen() #重新赋值后，才可重复取值。
>>> for  i in mg:
...     print(i)
... 
100
30
1000

```



## 三、模块

### （一）模块和文件

#### 1、模块的概念

• 模块支持从逻辑上组织python代码
• 当代码量变得相当大的时候, 最好把代码分成一些有组织的代码段
• 代码片段相互间有一定的联系,可能是一个包含数据成员和方法的类,也可能是一组相关但彼此独立的操作函数
• 这些代码段是共享的,所以python允许“调入”一个模块,允许使用其他模块的属性来利用之前的工作成果,实现代码重用

#### 2、模块文件

• 说模块是按照逻辑来组织python代码的方法,文件是物理层上组织模块的方法
• 一个文件被看作是一个独立模块,一个模块也可以被看作是一个文件
• 模块的文件名就是模块的名字加上扩展名.py

### （二）导入模块

#### 1、搜索路径

• 模块的导入需要一个叫做“路径搜索”的过程
• python在文件系统“预定义区域”中查找要调用的模块
• 搜索路径在sys.path中定义

```python
# python从sys.path定义的路径下搜索模块
>>> import sys
>>> sys.path
['', '/usr/local/lib/python36.zip', '/usr/local/lib/python3.6', '/usr/local/lib/python3.6/lib-dynload', '/home/student/nsd1908/lib/python3.6/site-packages']

# 如果希望自己编写的模块能在任意位置导入，可以定义python.path变量
(nsd1908) [student@room9pc01 day02]$ mkdir /tmp/mylibs
(nsd1908) [student@room9pc01 day02]$ cp qsort.py /tmp/mylibs
(nsd1908) [student@room9pc01 day02]$ export PYTHONPATH=/tmp/mylibs
```



#### 2、模块导入方法

• 使用import导入模块
• 可以在一行导入多个模块,但是可读性会下降
• 可以只导入模块的某些属性
• 导入模块时,可以为模块取别名

python将目录当成特殊的模块,称作包(在python2中,目录下必须有一个名为__init__.py的文件才能成为包)

```python
(nsd1908) [root@room8pc16 day02]# mkdir mydir
(nsd1908) [root@room8pc16 day02]# vim mydir/star.py
hi = 'Hello World!'
def pstar(n=30):
print('*' * n)
if __name__ == '__main__':
pstar()
(nsd1908) [root@room8pc16 day02]# python
>>> import mydir.star
>>> mydir.star.hi
'Hello World!'
>>> mydir.star.pstar()
******************************
```





### （三）内置模块

#### 1、hashlib模块

• hashlib用来替换md5和sha模块,并使他们的API一致,专门提供hash算法

• 包括md5、sha1、sha224、sha256、ha384、sha512,使用非常简单、方便

```python
>>>	import	hashlib
#计算MD5值
>>>	m =	hashlib.md5()
>>>	m.update('hello	world!')
>>>	m.hexdigest()
'fc3ff98e8c6a0d3087d515c0473f8677'

>>> import hashlib
>>> m = hashlib.md5(b'123456')
>>> m.hexdigest()
'e10adc3949ba59abbe56e057f20f883e'
>>> m1 = hashlib.md5()
>>> m1.update(b'12')
>>> m1.update(b'34')
>>> m1.update(b'56')
>>> m1.hexdigest()
'e10adc3949ba59abbe56e057f20f883e'

# md5案例
import hashlib
import sys

def check_md5(fname):
    m = hashlib.md5()

    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

if __name__ == '__main__':
    result = check_md5(sys.argv[1])
    print(result)
```

#### 2、tarfile模块

• tarfile模块允许创建、访问tar文件
• 同时支持gzip、bzip2格式

```python
[root@py01	home]#	ls /home/demo/
install.log mima
[root@py01	home]#	python
>>>	import	tarfile
>>>	tar	=	tarfile.open('/home/demo.tar.gz',	'w:gz')
>>>	tar.add('demo')
>>>	tar.close()


>>> import tarfile
# 压缩
>>> tar = tarfile.open('/tmp/nsd1908/demo/a.tar.gz', 'w:gz')
>>> tar.add('/etc/hosts')
>>> tar.close()
# 解压
>>> tar = tarfile.open('/tmp/nsd1908/demo/a.tar.gz')
>>> tar.extractall(path='/tmp/nsd1908/demo')
>>> tar.close()
```

通过os.walk拼接路径

```python
>>> for path, folders, files in 
```





#### 3、案例4:备份程序

1. 需要支持完全和增量备份

2. 周一执行完全备份

3. 其他时间执行增量备份

4. 备份文件需要打包为tar文件并使用gzip格式压缩

   ```python
   import os
   import tarfile
   import hashlib
   import pickle
   from time import strftime
   
   def check_md5(fname):
       m = hashlib.md5()
   
       with open(fname, 'rb') as fobj:
           while 1:
               data = fobj.read(4096)
               if not data:
                   break
               m.update(data)
   
       return m.hexdigest()
   
   
   def full_backup(src, dst, md5file):
       # 拼接出备份文件的绝对路径
       fname = os.path.basename(src)  # security
       fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
       fname = os.path.join(dst, fname)
   
       # 压缩
       tar = tarfile.open(fname, 'w:gz')
       tar.add(src)
       tar.close()
   
       # 计算每个文件的md5值，将其保存到字典
       md5dict = {}
       for path, folders, files in os.walk(src):
           for file in files:
               key = os.path.join(path, file)
               md5dict[key] = check_md5(key)
   
       # 将字典存入文件
       with open(md5file, 'wb') as fobj:
           pickle.dump(md5dict, fobj)
   
   
   def incr_backup(src, dst, md5file):
       # 拼接出备份文件的绝对路径
       fname = os.path.basename(src)  # security
       fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
       fname = os.path.join(dst, fname)
   
       # 计算每个文件的md5值，将其保存到字典
       md5dict = {}
       for path, folders, files in os.walk(src):
           for file in files:
               key = os.path.join(path, file)
               md5dict[key] = check_md5(key)
   
       # 取出前一天的md5值
       with open(md5file, 'rb') as fobj:
           old_md5 = pickle.load(fobj)
   
       # 比较两个字典，新字典的key不在老字典中，或值不一样，都要备份
       tar = tarfile.open(fname, 'w:gz')
       for key in md5dict:
           if old_md5.get(key) != md5dict[key]:
               tar.add(key)
       tar.close()
   
       # 使用今天的md5值更新md5文件，以便于明天与今天比较
       with open(md5file, 'wb') as fobj:
           pickle.dump(md5dict, fobj)
   
   if __name__ == '__main__':
       src = '/tmp/nsd1908/security'
       dst = '/tmp/nsd1908/backup'
       md5file = '/tmp/nsd1908/md5.data'
       if strftime('%a') == 'Mon':
           full_backup(src, dst, md5file)
       else:
           incr_backup(src, dst, md5file)
   
   
   # (nsd1908) [root@room8pc16 day03]# cp -r /etc/security /tmp/nsd1908/
   # 将security目录备份到backup目录
   # (nsd1908) [root@room8pc16 day03]# ls /tmp/nsd1908/
   # backup  security
   
   ```

   

# Python02 day03

标识符命名网站：https://unbug.github.io/codelf/（支持中文）

## 一、OOP基础

### （一）OOP简介

#### 1、基本概念

在python中，一切皆对象

不同的对象有不同的属性

​	

• 类(Class):用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方
法。对象是类的实例。
• 实例化:创建一个类的实例,类的具体对象。
• 方法:类中定义的函数。
• 对象:通过类定义的数据结构实例。对象包括两个数据成员(类变量和实例变量)和方法

```python
class Role:
    def __init__(self, name, weapon):
        "__init__是构造器方法，创建实例是，它自动调用,一般用于将属性绑到对象"
        self.name = name
        self.weapon = weapon

    def show_me(self):
        "绑定载实例上的属性，载任意方法中都直接可用"
        print('我是%s, 我的兵器是%s' % (self.name, self.weapon))

if __name__ == '__main__':
    # 实例化时，实例名lb将自动作为第一个参数，传给相关的方法
    lb = Role('吕布', '方天画戟')
    print(lb.name, lb.weapon)
    lb.show_me()
```





#### 2、创建类

• 使用 class 语句来创建一个新类,class 之后为类的名称并以冒号结尾
• 类名建议使用驼峰形式

#### 3、创建实例

• 类是蓝图,实例是根据蓝图创建出来的具体对象



### （二）绑定方法

#### 1、构造器

• 当实例化类的对象是,构造器方法默认自动调用
• 实例本身作为第一个参数,传递给self

#### 2、其他绑定方法

• 类中定义的方法需要绑定在具体的实例,由实例调用
• 实例方法需要明确调用

#### 3、案例1:编写游戏人物

1. 创建游戏角色类

2. 游戏人物角色拥有名字、武器等属性

3. 游戏人物具有攻击和行走的方法

4. 武器通过武器类实现

   ```python
   class Role:
       def __init__(self, name, weapon):
           "__init__是构造器方法，创建实例时，它自动调用,一般用于将属性绑到对象"
           self.name = name
           self.weapon = weapon
   
       def show_me(self):
           "绑定载实例上的属性，载任意方法中都直接可用"
           print('我是%s, 我的兵器是%s' % (self.name, self.weapon))
   
       def say(self, words):
           "没有绑定的变量，是临时变量"
           print(words)
           
   if __name__ == '__main__':
       # 实例化时，实例名lb将自动作为第一个参数，传给相关的方法
       lb = Role('吕布', '方天画戟')
       print(lb.name, lb.weapon)
       lb.show_me()
       lb.say('马中赤兔，人中吕布')
   
       zf = Role('张飞', '丈八蛇矛')
       zf.show_me()
   ```

   

## 二、OOP进阶

### （一）组合和派生

#### 1、什么是组合

• 类被定义后,目标就是要把它当成一个模块来使用,并把这些对象嵌入到你的代码中去
• 组合就是让不同的类混合并加入到其它类中来增加功能和代码重用性
• 可以在一个大点的类中创建其它类的实例,实现一些其它属性和方法来增强对原来的类对象

#### 2、组合应用

• 两个类明显不同
• 一个类是另一个类的组件

```python
class Weapon:
    def __init__(self, wname, wtype, strength):
        self.wname = wname
        self.wtype = wtype
        self.strength = strength

class Role:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

if __name__ == '__main__':
    ji = Weapon('方天画戟', '物理', 100)
    lb = Role('吕布', ji)
    print(ji.wname, ji.wtype, ji.strength)
    print(lb.weapon.wname, lb.weapon.wtype, lb.weapon.strength)
```



#### 3、创建子类

• 当类之间有显著的不同,并且较小的类是较大的类所需要的组件时组合表现得很好;但当设计“相同的类但有一些不同的功能”时,派生就是一个更加合理的选择了
• OOP 的更强大方面之一是能够使用一个已经定义好的类,扩展它或者对其进行修改,而不会影响系统中使用现存类的其它代码片段
• OOD(面向对象设计)允许类特征在子孙类或子类中进行继承

• 创建子类只需要在圆括号中写明从哪个父类继承即可

```python
class Role:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def show_me(self):
        print('我是%s，%s是我的，冲啊！！！' % (self.name, self.weapon))

    def say(self, words):
        print(words)

class Warrior(Role):
    def attack(self, target):
        print('近身攻击：%s' % target)

class Mage(Role):
    def attack(self, target):
        print('远身攻击：%s' % target)

if __name__ == '__main__':
    gy = Warrior('关羽', '青龙')
    km = Mage('孔明', '羽扇')
    gy.show_me()
    km.show_me()
    gy.attack('吕布')
    km.attack('周瑜')

```



#### 4、继承

• 继承描述了基类的属性如何“遗传”给派生类
• 子类可以继承它的基类的任何属性,不管是数据属性还是方法



#### 5、通过继承覆盖方法

• 如果子类中有和父类同名的方法,父类方法将被覆盖
• 如果需要访问父类的方法,则要调用一个未绑定的父类方法,明确给出子类的实例

```python
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
        #Role.__init__(self, name, weapon)
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
```



#### 6、多重继承

• python允许多重继承,即一个类可以是多个父类的子类,子类可以拥有所有父类的属性

```python
class A:
    def func1(self):
        print('A func1')

    def func4(self):
        print('A fun4')

class B:
    def func2(self):
        print('B func2')

    def func4(self):
        print('B func4')

class C(A, B):
    def func3(self):
        print('C func3')

    def func4(self):
        print('C func4')


if __name__ == '__main__':
    c1 = C()
    c1.func1()
    c1.func2()
    c1.func3()
    c1.func4()
```





#### （二）特殊方法

#### 1、\__init__方法

• 实例化类实例时默认会调用的方法



#### 2、\__str__方法

• 打印/显示实例时调用方法
• 返回字符串

#### 3、\__call__方法

• 用于创建可调用的实例



```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '《%s》' % self.title
    
    def __call__(self):
        print('《%s》是%s编著的' % (self.title, self.author))

if __name__ == '__main__':
    py_book = Book('Python基础教程', 'Hetland')  #调用__init__
    print(py_book) # 调用__str__，实现打印功能
    py_book() #__call__，将实例以函数方式实现
```





## 三、re模块

### （一）匹配单个字符

#### 1、匹配单个字符

| 记号         | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| .            | 匹配任意字符(换行符除外)                                     |
| [...x-y...]  | 匹配字符组里的任意字符                                       |
| [^...x-y...] | 匹配不在字符组里的任意字符                                   |
| \d           | 匹配任意数字,与[0-9]同义，\D是取反，匹配除任意数字之外的字符 |
| \w           | 匹配任意数字字母字符,与[0-9a-zA-Z_]同义，\W是取反，匹配除任意数字字母之外的字符 |
| \s           | 匹配空白字符,与[ \r\v\f\t\n]同义，\S是取反，匹配除空白字符之外的字符 |



#### 2、匹配一组字符

| 记号     | 说明                                                        |
| -------- | ----------------------------------------------------------- |
| literal  | 匹配字符串的值(按输入匹配的意思)                            |
| re1\|re2 | 匹配正则表达式re1或re2       \|需要\来转义                  |
| *        | 匹配前面出现的正则表达式零次或多次                          |
| +        | 匹配前面出现的正则表达式一次或多次   +需要\来转义           |
| ?        | 匹配前面出现的正则表达式零次或一次    ？需要\来转义         |
| {M,N}    | 匹配前面出现的正则表达式至少M次最多N次        {}需要\来转义 |

#### 3、其他元字符

| 记号 | 说明                                    |
| ---- | --------------------------------------- |
| ^    | 匹配字符串的开始                        |
| $    | 匹配字符串的结尾                        |
| \b   | 匹配单词的边界                          |
| ()   | 对正则表达式分组        （）需要\来转义 |
| \nn  | 匹配已保存的子组                        |

```shell
#给MAC地址加问号
192.168.1.1   000C29123456
192.168.1.2   5254A382C80B

# 1.定位取出MAC地址； 2.每两个数分一组；3.各组间加冒号

:%s/\(..\)\(..\)\(..\)\(..\)\(..\)\(..\)$/\1:\2:\3:\4:\5:\6/
```



### （二）核心函数和方法

#### 1、match函数

• 尝试用正则表达式模式从字符串的开头匹配,如果匹配成功,则返回一个匹配对象;否则返回None

```python
>>> import re
# match从字符串开头，如果匹配到，返回匹配对象；否则返回none
>>> re.match('f..', 'food')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> re.match('f..', 'seafood')
>>> print(re.match('f..', 'seafood'))
None

```



#### 2、search函数

在字符串中查找正则表达式模式的第一次出现,如果匹配成功,则返回一个匹配对象;否则返回None



#### 3、group方法

• 使用match或search匹配成功后,返回的匹配对象可以通过group方法获得匹配内容

```python
>>> re.search('f..', 'seafood')
<_sre.SRE_Match object; span=(3, 6), match='foo'>
>>> m = re.search('f..', 'seafood')
>>> m.group()   #返回匹配到的结果
'foo'

```



#### 4、findall函数

• 在字符串中查找正则表达式模式的所有(非重复)出现;返回一个匹配对象的列表



#### 5、finditer函数

• 在字符串中查找正则表达式模式的所有(非重复)出现;返回一个匹配对象的列表

```python
>>> re.findall('f..', 'seafood is food')  #返回列表
['foo', 'foo']
>>> re.finditer('f..', 'seafood is food')  # finditer返回的是由匹配对象构成的生成器
<callable_iterator object at 0x7f48558e8c88>
>>> list(re.finditer('f..', 'seafood is food'))
[<_sre.SRE_Match object; span=(3, 6), match='foo'>, <_sre.SRE_Match object; span=(11, 14), match='foo'>]
>>> for m in re.finditer('f..', 'seafood is food'):
...     m.group()
... 
'foo'
'foo'

```



#### 6、compile函数

在有大量匹配的情况下，先把正则表达式模式进行编译，会有更好的执行效率

• 对正则表达式模式进行编译,返回一个正则表达式对象
• 不是必须要用这种方式,但是在大量匹配的情况下,可以提升效率

```python
>>>	import	re
>>>	patt =	re.compile('foo')
>>>	m	=	patt.match('food')
>>>	print(m.group())
foo
```





#### 7、split方法

用于分割字符

• 根据正则表达式中的分隔符把字符分割为一个列表,并返回成功匹配的列表
• 字符串也有类似的方法,但是正则表达式更加灵活

#### 8、sub方法

• 把字符串中所有匹配正则表达式的地方替换成新的字符串

```python
>>> re.split('-|\.', 'hello-world-how-are-you.tar.gz')
['hello', 'world', 'how', 'are', 'you', 'tar', 'gz']
>>> re.sub('X', 'tom', 'hi X. Nice to meet you, X')
'hi tom. Nice to meet you, tom'

```



#### 9、案例3:分析apache访问日志

1. 统计每个客户端访问apache服务器的次数

2. 将统计信息通过字典的方式显示出来

3. 分别统计客户端是Firefox和MSIE的访问次数

4. 分别使用函数式编程和面向对象编程的方式实现

   ```python
   import re
   
   def count_patt(fname, patt):
       patt_dict = {}
       cpatt = re.compile(patt)  # 为了更好的性能，将模式编译
   
       # 在文件的每一行进行模式匹配
       with open(fname) as fobj:
           for line in fobj:
               m = cpatt.search(line)
               if m:  # 如果匹配到了内容
                   key = m.group()
                   patt_dict[key] = patt_dict.get(key, 0) + 1
   
       return patt_dict
   
   if __name__ == '__main__':
       fname = 'access_log'
       ip = '^(\d+\.){3}\d+'  # 12345.67890.1.23  192.16.1.20
       br = 'Firefox|MSIE|Chrome'
       result1 = count_patt(fname, ip)
       result2 = count_patt(fname, br)
       print(result1)
       print(result2)
   
   ```

修改为面向对象：

```python
import re

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        patt_dict = {}
        cpatt = re.compile(patt)  # 为了更好的性能，将模式编译

        # 在文件的每一行进行模式匹配
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:  # 如果匹配到了内容
                    key = m.group()
                    patt_dict[key] = patt_dict.get(key, 0) + 1

        return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 12345.67890.1.23  192.16.1.20
    cp = CountPatt(fname)
    result1 = cp.count_patt(ip)
    print(result1)
    br = 'Firefox|MSIE|Chrome'
    result2 = cp.count_patt(br)
    print(result2)
```



#### 10、字典排序

- 字典没有顺序

- 需要将字典转成列表，再排序

  ```python
  >>> adict = {'172.40.58.150': 10, '172.40.58.124': 6, '172.40.58.101': 10, '127.0.0.1': 121, '192.168.4.254': 103, '192.168.2.254': 110, '201.1.1.254': 173, '201.1.2.254': 119, '172.40.0.54': 391, '172.40.50.116': 244}
  >>> alist = list(adict.items())
  >>> alist
  [('172.40.58.150', 10), ('172.40.58.124', 6), ('172.40.58.101', 10), ('127.0.0.1', 121), ('192.168.4.254', 103), ('192.168.2.254', 110), ('201.1.1.254', 173), ('201.1.2.254', 119), ('172.40.0.54', 391), ('172.40.50.116', 244)]
  
  # 列表的sort方法接受一个名为key的参数。key可以是一个函数，它将列表中的每一项作为参数处理，处理后的结果作为排序依据
  >>> def func1(seq):
  ...   return seq[-1]
  ... 
  >>> alist.sort(key=func1)
  >>> alist
  [('172.40.58.124', 6), ('172.40.58.150', 10), ('172.40.58.101', 10), ('192.168.4.254', 103), ('192.168.2.254', 110), ('201.1.2.254', 119), ('127.0.0.1', 121), ('201.1.1.254', 173), ('172.40.50.116', 244), ('172.40.0.54', 391)]
  
  # 使用匿名函数，并实现降序排列
  >>> alist.sort(key=lambda seq: seq[-1], reverse=True)
  >>> alist
  [('172.40.0.54', 391), ('172.40.50.116', 244), ('201.1.1.254', 173), ('127.0.0.1', 121), ('201.1.2.254', 119), ('192.168.2.254', 110), ('192.168.4.254', 103), ('172.40.58.150', 10), ('172.40.58.101', 10), ('172.40.58.124', 6)]
  ```

  

# Python02 day04

## 一、PyMySQL模块

### （一）PyMySQL安装

#### 1、使用pypi

• pypi即python package index
• 是python语言的软件仓库
• 官方站点为https://pypi.python.org

![image-20200111104421016](/home/student/.config/Typora/typora-user-images/image-20200111104421016.png)

#### 2、通过pip安装PyMySQL模块

• 安装依赖包

```shell
[root@localhost packages]#	yum	install	-y	gcc
```

• 本地安装

```shell
[root@localhost packages]#	pip3 install PyMySQL-0.8.0.tar.gz
```

• 在线安装

```shell
[root@localhost packages]#	pip3 install pymysql
```



#### 3、使用国内镜像站点

• 为了实现安装加速,可以配置pip安装时采用国内镜像站点

```shell
[root@localhost ~]#	mkdir ~/.pip/
[root@localhost ~]#	vim	~/.pip/pip.conf
[global]
index-url=http://pypi.douban.com/simple/
[install]
trusted-host=pypi.douban.com
```



### （二）PyMySQL应用

#### 1、连接数据库

```python
# 建立到数据库的连接
conn = pymysql.connect(
    host='127.0.0.1', port=3306,
    user='root', passwd='tedu.cn',
    db='nsd1908', charset='utf8'
)
```



#### 2、游标

```python
# 创建游标，它就像文件对象一样
cur = conn.cursor()
```



#### 3、插入数据

```python
sql1	=	"insert	into	departments(dep_name)	values(%s)"
result	=	cur.execute(sql1,	('development',))
sql2	=	"insert	into	departments(dep_name)	values(%s)"
data	=	[('hr',),	('op',)]
result	=	cur.executemany(sql2,	data)
sql3	=	"insert	into	departments(dep_name)	values(%s)"
data	=	[('行政',),	('财务',),	('运营',)]
result	=	cur.executemany(sql3,	data)
conn.commit()
```



#### 4、查询数据

```python
sql4	=	"select	*	from	departments"
cur.execute(sql4)
result	=	cur.fetchone()
print(result)
result2	=	cur.fetchmany(2)
print(result2)
result3	=	cur.fetchall()
print(result3)
```



#### 5、移动游标

```python
cur.scroll(1, mode="ralative")
cur.scroll(2, mode="absolute")
sql5	=	"select	*	from	departments"
cur.execute(sql5)
cur.scroll(3,	mode='absolute')
result4	=	cur.fetchmany(2)
print(result4)
```



#### 6、修改数据

```python
sql6	=	"update	departments	set	dep_name=%s	where	dep_name=%s"
result	=	cur.execute(sql6,	('operations',	'op'))
print(result)
conn.commit()
```



#### 7、删除记录

```python
sql7	=	"delete	from	departments	where	dep_id=%s"
result	=	cur.execute(sql7,	(6,))
print(result)
conn.commit()
```



#### 8、课上案例

```python
# 建立到数据库的连接
conn = pymysql.connect(
    host='127.0.0.1', port=3306,
    user='root', passwd='tedu.cn',
    db='nsd1908', charset='utf8'
)

# 创建游标，它就像文件对象一样
cur = conn.cursor()

# 编写SQL语句
# mk_dep = """CREATE TABLE departments(
# dep_id INT, dep_name VARCHAR(50),
# PRIMARY KEY(dep_id)
# )"""
# mk_emp = """CREATE TABLE employees(
# emp_id INT, emp_name VARCHAR(20), email VARCHAR(50), dep_id INT,
# PRIMARY KEY(emp_id),
# FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
# )"""
# mk_sal = """CREATE TABLE salary(
# id INT, date DATE, emp_id INT, basic INT, awards INT,
# PRIMARY KEY(id),
# FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
# )"""

# 执行SQL语句
# cur.execute(mk_dep)
# cur.execute(mk_emp)
# cur.execute(mk_sal)
#################################
# 添加记录
# insert1 = 'INSERT INTO departments VALUES(%s, %s)'
# cur.executemany(insert1, [(1, '人事部'), (2, '运维部')])
# cur.executemany(insert1, [(2, '运维部'), (3, '开发部'), (4, '财务部'), (5, '测试部'), (6, '市场部')])
#################################
# 修改
# update1 = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
# cur.execute(update1, ('人力资源部', '人事部'))
#################################
# 删除
# delete1 = 'DELETE FROM departments WHERE dep_name=%s'
# cur.execute(delete1, ('运维部',))
#################################
# 查询
select1 = 'SELECT * FROM departments'
cur.execute(select1)
result1 = cur.fetchone()  # 取一行记录
print(result1)
print('*' * 30)
result2 = cur.fetchmany(2)  # 取出2行记录
print(result2)
print('*' * 30)
result3 = cur.fetchall()  # 取出所有记录
print(result3)


# 确认
conn.commit()

# 关闭游标、关闭连接
cur.close()
conn.close()
```



## 二、SQLAIchemy基础

### （一）SQLAIchemy概述

#### 1、SQLAIchemy安装

• SQLAlchemy由官方收录,可以直接安装

```shell
[root@localhost packages]#	pip3 install sqlalchemy
```



#### 2、SQLAIchemy简介

（1）不限定于某一个数据库，支持大多数主流的关系型数据库

（2）不必书写SQL语句，只要使用python语法即可

（3）sqlalchemy使用ORM模型

​		Object：对象

​		Relationship： 关系

​		Mapper：映射

​		salalchemy将每张表映射位一个class

​		表中的每个字段映射位class的类变量，每个字段都使用Column类定义

​		数据库中的每种数据类型，在sqlalchemy中都有对应的class

​		表中的每个记录，对应sqlalchemy类的实例



• SQLAlchemy是Python编程语下的一款开源软件。提供 SQL 具包及对象关系映 射(ORM) 工具,使用MIT许可证发
• SQLAlchemy“采用简单的Python语言,为高效和高性能的数据库访问设计,实现了完整的企业级持久模型”
• SQLAlchemy的理念是,SQL数据库的量级和性能重要于对象集合;而对象集合的抽象又重要于表和行

• 目标是提供能兼容众多数据库(如 SQLite、MySQL、Postgresql、Oracle、MS-SQL、SQLServer 和Firebird)的企业级持久性模型



#### 3、SQLAIchemy结构

![image-20200113090148185](/home/student/.config/Typora/typora-user-images/image-20200113090148185.png)



#### 4、ORM模型

• ORM即对象关系映射
• 数据库表是一个二维表,包含多行多列。把一个表的内容用Python的数据结构表示出来的话,可以用一个list表示多行,list的每一个元素是tuple,表示一行记录

• 用tuple表示一行很难看出表的结构。如果把一个tuple用class实例来表示,就可以更容易地看出表的结构来



### （二）数据库对象管理

#### 1、连接mysql

• 通过create_engine实现数据库的连接

```python
[root@bogon bin]#	mysql -uroot -ptedu.cn
MariaDB [(none)]>	create	database	tarena default	char	set	utf8;
>>>	from	sqlalchemy import	create_engine
>>>	engine	=	create_engine(
'mysql+pymysql://root:tedu.cn@localhost/tarena?charset=utf8',
encoding='utf8',
echo=True
)
//echo=True表示将日志输出到终端屏幕,默认为False
```



#### 2、声明射影

• 当使用ORM的时候,配置过程从描述数据库表开始
• 通过自定义类映射相应的表
• 通过声明系统实现类映射
• 首先通过声明系统,定义基类

```python
>>>	from	sqlalchemy.ext.declarative import	declarative_base
>>>	Base	=	declarative_base()
```



#### 3、创建映射类

• 一旦创建了基类,就可以创建自定义映射类了

```python
>>>	from	sqlalchemy import	Column,	Integer,	String
>>>	class	Departments(Base):
...					__tablename__	=	'departments'
...					dep_id =	Column(Integer,	primary_key=True)
...					dep_name =	Column(String(20))
...					def __repr__(self):
...									return	"<Department(dep_name='%s')>"	%	self.dep_name
//__repr__是可选项
```



#### 4、创建架构

• 类构建完成后,表的信息将被写入到表的元数据(metadata)

```python
>>>	Departments.__table__
Table('departments',	MetaData(bind=None),	Column('dep_id',	Integer(),	
table=<departments>,	primary_key=True,	nullable=False),	
Column('dep_name',	String(),	table=<departments>),	schema=None)
```

• 通过表的映射类,在数据库中创建表

```python
>>>	Base.metadata.create_all(engine)
```



#### 5、创建映射类的实例

• 创建实例时,并不会真正在表中添加记录

```python
dep_dev =	Departments(dep_name='developments')
print(dep_dev.dep_name)
print(str(dep_dev.dep_id))
```



#### 6、创建回话类

• ORM访问数据库的句柄被称作Session

```python
>>>	from	sqlalchemy.orm import	sessionmaker
>>>	Session	=	sessionmaker(bind=engine)
如果在创建session前还未创建engine,操作如下
>>>	Session	=	sessionmaker()
>>>	Session.configure(bind=engine) //创建engine后执行
```



#### 7、添加新对象

• 会话类的实例对象用于绑定到数据库
• 实例化类的对象,并不打开任何连接
• 当实例初次使用,它将从Engine维护的连接池中获得一个连接
• 当所有的事务均被commit或会话对象被关闭时,连接结束

```python
>>>	session	=	Session()
>>>	session.add(dep_dev)
>>> session.commit()
>>> print(str(dep_dev.dep_id))
>>> session.close()
```



• 可以创建多个实例,批量添加记录

```python
dep_hr =	Departments(dep_name='hr')
dep_op =Departments(dep_name='operations')
dep_finance =Departments(dep_name='财务')
dep_xz =Departments(dep_name='行政’)
Session	=	sessionmaker(engine)
session	=	Session()
session.add_all([dep_hr,	dep_op,	dep_finance,	dep_xz])
session.commit()
session.close()
```



#### 8、外键约束

• ORM映射关系也可用于表间创建外键约束

```python
class	Employees(Base):
__tablename__	=	'employees'
emp_id =	Column(Integer,	primary_key=True)
name	=	Column(String(20))
genda =	Column(String(10))
phone	=	Column(String(11))
dep_id =	Column(Integer,	ForeignKey('departments.dep_id'))
def __repr__(self):
return	"<Employees(name='%s')>"	%	self.name
```



## 三、SQLAIchemy进阶

### （一）查询操作

#### 1、基本查询

• 通过作用于session的query()函数创建查询对象
• query()函数可以接收多种参数

```python
from	myorm import	Session	, Departments
session	=	Session()
for	instance	in	
session.query(Departments).order_by(Departments.dep_id):
print(instance.dep_id,	instance.dep_name)
```



#### 2、使用ORM描述进行查询

• 使用ORM描述符进行查询
• 返回值是元组

```python
from	myorm import Employees, Session	
session	=	Session()
for	name,	phone	in	session.query(Employees.name,	Employees.phone):
print(name,	phone)
```



#### 3、排序

• 通这order_by()函数可以实现按指定字段排序

```python
from	myorm import	Session	, Departments
session	=	Session()
for	instance	in	
session.query(Departments).order_by(Departments.dep_id):
print(instance.dep_id,	instance.dep_name)
```



#### 4、提取部分数据

• 通过“切片”的方式,实现部分数据的提取

```python
from	myorm import	Session	, Departments
session	=	Session()
for	row	in	session.query(Departments,	Departments.dep_name)[2:5]:
print(row.Departments,	row.dep_name)
```



#### 5、结果过滤

• 通过filter()函数实现结果过滤

```python
from	myorm import	Session	, Departments
session	=	Session()
for	row	in	
session.query(Departments.dep_name).filter(Departments.dep_id==2):
print(row.dep_name)
```

• filter()函数可以叠加使用

```python
from	myorm import	Session	, Salary
session	=	Session()
for	row	in	session.query(Salary.emp_id,	Salary.base,	Salary.award)\
.filter(Salary.award>2000).filter(Salary.base>10000):
print(row.emp_id)
```



#### 6、常用过滤操作符

• 相等
query.filter(Employees.name=='john')
• 不相等
query.filter(Employees.name!='john')
• 模糊查询
query.filter(Employees.name.like(' %j '))

• in
query.filter(new_emp.name.in_(['bob', 'john'])
• not in
query.filter(~new_emp.name.in_(['bob', 'john'])
• 字段为空
query.filter(new_emp.name.is_(None))
• 字段不为空
query.filter(new_emp.name.isnot(None))

#### 7、查询对象返回值

• all()返回列表
• first()返回结果中的第一条记录

#### 8、多表查询

• 通过join()方法实现多表查询

```python
q	=	session.query(
Employees.name,	Departments.dep_name).join(Departments)
print(q.all())
```



### （二）修改操作

#### 1、更新数据

• 通过会话的update()方法更新

```python
from	myorm import	Session,	Departments
session	=	Session()
q1	=	session.query(Departments).filter(Departments.dep_id==6)
q1.update({Departments.dep_name:	'运维部'})
session.commit()
session.close()
```





#### 2、删除记录

• 通过会话的delete()方法进行记录删除

```python
from	myorm import	Session,	Departments
session	=	Session()
q1	=	session.query(Departments).get(7)
session.delete(q1)
session.commit()
session.close()
```



#### 3、课上案例

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建连接到数据库的引擎
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器/数据库?参数
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1908?charset=utf8',
    encoding='utf8',
    # echo=True  # 在屏幕上输出日志
)

# 创建一个会话类，用于客户端到服务器的会话连接
Session = sessionmaker(bind=engine)

# 创建实体类（与表关联的类）的基类
Base = declarative_base()

# 创建实体类
class Departments(Base):
    __tablename__ = 'departments'  # 定义库中关联的表
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

    def __str__(self):
        return "[%s: %s]" % (self.dep_id, self.dep_name)

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    # 如果库中没有相关的表则创建，如果已存在，只是映射，不会再创建一遍
    Base.metadata.create_all(engine)
```

```python
# create / retrieve / update / delete
from dbconn import Departments, Employees, Salary, Session

# 创建到数据库的会话实例
session = Session()

# 执行增删改查操作
# hr = Departments(dep_id=1, dep_name='人事部')
# ops = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# qa = Departments(dep_id=4, dep_name='测试部')
# market = Departments(dep_id=5, dep_name='市场部')
# sales = Departments(dep_id=6, dep_name='销售部')
# session.add_all([hr, ops, dev, qa, market, sales])
# u1 = Employees(
#     emp_id=1, emp_name='涂文良',
#     email='twl@163.com', dep_id=2
# )
# u2 = Employees(
#     emp_id=2, emp_name='刘昌艳',
#     email='lcy@qq.com', dep_id=3
# )
# session.add_all([u1, u2])
###############################################
# 查询时，query参数是类名，返回的是实例列表
# qset1 = session.query(Departments)
# print(qset1)   # qset1是sql语句，此时不查询数据库，取值时才查询
# for dep in qset1:
#     print(dep.dep_id, dep.dep_name)
###############################################
# 查询时，query参数是属性，返回的是属性构成的元组
# qset2 = session.query(Employees.emp_name, Employees.email)
# print(qset2)
# for data in qset2:
#     print(data)
###############################################
# 查询部门，按id排序
# qset3 = session.query(Departments).order_by(Departments.dep_id)
# for dep in qset3:
#     print(dep.dep_id, dep.dep_name)
###############################################
# 查询部门，根据id进行过滤
# qset4 = session.query(Departments).filter(Departments.dep_id>1)\
#     .filter(Departments.dep_id<5).order_by(Departments.dep_id)
# for dep in qset4:
#     print(dep.dep_id, dep.dep_name)
###############################################
# 查询email以.com结尾的用户
# qset5 = session.query(Employees).filter(Employees.email.like('%.com'))
# for emp in qset5:
#     print(emp.emp_name, emp.email)
###############################################
# 查询人力资源部和市场部
# qset6 = session.query(Departments)\
#     .filter(Departments.dep_name.in_(['人事部', '市场部']))
# for dep in qset6:
#     print(dep.dep_id, dep.dep_name)

###############################################
# 查询人事部和市场部以外的部门
# qset7 = session.query(Departments)\
#     .filter(~Departments.dep_name.in_(['人事部', '市场部']))
# for dep in qset7:
#     print(dep.dep_id, dep.dep_name)
###############################################
# all()返回所有值的列表
# print(qset7.all())
###############################################
# first()返回匹配内容的第一项
# dep = qset7.first()
# print(dep)
# print(dep.dep_id, dep.dep_name)
###############################################
# 多表查询，query中先写Employees.emp_name，join时写Departments
# query中先写Departments.dep_name，join时写Employees
# qset8 = session.query(Employees.emp_name, Departments.dep_name)\
#     .join(Departments)
# for data in qset8:
#     print(data)
###############################################
# 修改
# qset9 = session.query(Departments).filter(Departments.dep_name=='人事部')
# hr = qset9.first()
# print(hr)
# hr.dep_name = '人力资源部'
###############################################
# 删除
qset10 = session.query(Departments).filter(Departments.dep_name=='销售部')
sales = qset10.first()
print(sales)
session.delete(sales)


# 确认
session.commit()
```





