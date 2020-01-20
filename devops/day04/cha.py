from dbconn import Students, emp, Session
from sqlalchemy import select, func, Integer, Table, Column, MetaData

session = Session()

# num1:
print('第1题：')
print('%-5s %-10s' % ('id', '学生名称'))
qset1 = session.query(Students)
for data in qset1:
    print('%-5s %-10s' % (data.id, data.name))
print('*' * 38)

# num2:
print('第2题：')
print('%3s:%-3s' % ('学生名称', '语文'))
qset2 = session.query(Students)
for data in qset2:
    print('%3s:%3s' % (data.name, data.chinese))
print('*' * 38)

# num3:
print('第3题：')
print('工作岗位:')
qset3 = session.query(emp.job).distinct().all()
for data in qset3:
    print('%s' % data)
print('*' * 38)

# num4:
print('第4题：')
print('%3s %-3s' % ('学生名称', '总分(+10特长分)'))
qset4 = session.query(Students)
for data in qset4:
    zf = data.chinese + data.english + data.math +10
    print('%3s %-3s' % (data.name, zf))
print('*' * 38)

# num5:
print('第5题：')
print('%3s %-3s' % ('学生名称', '总分'))
qset5 = session.query(Students).filter(Students.name=='张小明')
for data in qset5:
    zf = data.chinese + data.english + data.math
    print('%3s:%3s' % (data.name, zf))
print('*' * 38)

# num6:
print('第6题：')
print('%3s %-3s' % ('学生名称', '英语'))
qset6 = session.query(Students).filter(Students.english>=90)
for data in qset6:
    print('%3s:%3s' % (data.name, data.english))
print('*' * 38)

# num7:
print('第7题：')
print('%3s %-3s' % ('学生名称', '总分'))
qset7 = session.query(Students).filter(Students.chinese + Students.english + Students.math >=200)
for data in qset7:
    zf = data.chinese + data.english + data.math
    print('%3s:%3s' % (data.name, zf))
print('*' * 38)

# num8:
print('第8题：')
print('%3s %-3s' % ('学生名称', '数学'))
qset8 = session.query(Students).filter(Students.math.in_([89,90,91]))
for data in qset8:
    print('%3s:%3s' % (data.name, data.math))
print('*' * 38)

# num9:
print('第9题：')
print('%3s %-3s' % ('学生名称', '英语'))
qset9 = session.query(Students).filter(Students.english>79).filter(Students.english<91)
for data in qset9:
    print('%3s:%3s' % (data.name, data.english))
print('*' * 38)

# num10:
print('第10题：')
print('%3s %-3s' % ('学生名称', '总分'))
qset10 = session.query(Students).filter(Students.name.like('李%'))
for data in qset10:
    zf = data.chinese + data.english + data.math
    print('%3s:%3s' % (data.name, zf))
print('*' * 38)

# num11:
print('第11题：')
print('%3s %-3s' % ('学生名称', '总分'))
qset11 = session.query(Students).filter(Students.name.like('%李'))
for data in qset11:
    zf = data.chinese + data.english + data.math
    print('%3s:%3s' % (data.name, zf))
print('*' * 38)

# num12:
print('第12题：')
print('学生名称')
qset12 = session.query(Students).filter(Students.name.like('李_'))
for data in qset12:
        print(data.name)
print('*' * 38)

# num13:
print('第13题：')
print('学生名称')
qset13 = session.query(Students).filter(Students.name.like('李_'))
for data in qset13:
        print(data.name)
print('*' * 38)

# num14:
print('第14题：')
print('%3s %-3s' % ('学生名称', '总分'))
qset14 = session.query(Students).filter(Students.name.like('%李%'))
for data in qset14:
    zf = data.chinese + data.english + data.math
    print('%3s:%3s' % (data.name, zf))
print('*' * 38)

# num15:
print('第15题：')
print('%3s %-3s' % ('学生名称', '总分'))
qset15 = session.query(Students).filter(Students.name.like('李__'))
for data in qset15:
    zf = data.chinese + data.english + data.math
    print('%3s:%3s' % (data.name, zf))
print('*' * 38)

# num16:
print('第16题：')
print('%3s %-3s' % ('学生名称', '数学'))
qset16 = session.query(Students).order_by(-Students.math).all()
for data in qset16:
    print('%3s:%3s' % (data.name, data.math))
print('*' * 38)

# num17:
print('第17题：')
print('%3s:%-2s:%-2s:%-2s' % ('学生名称', '数学', '语文', '英语'))
qset17 = session.query(Students).order_by(-Students.math).order_by(-Students.chinese).all()
for data in qset17:
    print('%3s:%3s:%3s:%3s' % (data.name, data.math, data.chinese, data.english))
print('*' * 38)

# num18:
print('第18题：')
print('%3s:%-3s' % ('学生名称', '总分'))
qset18 = session.query(Students).order_by(-(Students.chinese + Students.english + Students.math))
for data in qset18:
    zf = data.chinese + data.english + data.math
    print('%3s:%3s' % (data.name, zf))
print('*' * 38)

# num19:
print('第19题：')
print('%3s %-3s' % ('学生名称', '总分'))
qset19 = session.query(Students).filter(Students.name.like('李%')).order_by(-(Students.chinese + Students.english + Students.math))
for data in qset19:
    zf = data.chinese + data.english + data.math
    print('%3s:%3s' % (data.name, zf))
print('*' * 38)

# num20:
print('第20题：')
qset20 = session.query(func.count(Students.name)).first()
print('班级中共有%s个学生' % qset20)
print('*' * 38)
# num21:
print('第21题：')
qset21 = session.query(func.count(Students.name)).filter(Students.math>80).first()
print('班级中共有%s个学生数学成绩大于80分' % qset21)
print('*' * 38)
# num22:
print('第22题：')
qset22 = session.query(func.count(Students.name)).filter(Students.chinese + Students.english + Students.math >250).first()
print('班级中共有%s个学生总成绩大于250分' % qset22)
print('*' * 38)

# num23:
print('第23题：')
qset23 = session.query(func.sum(Students.math)).first()
print('班级中共所有学生的数学总成绩为%s分' % qset23)
print('*' * 38)

# num24:
print('第24题：')
qset91 = session.query(func.sum(Students.chinese)).first()
qset92 = session.query(func.sum(Students.english)).first()
print('班级中共所有学生的语文总成绩为%s分' % qset91)
print('班级中共所有学生的英语总成绩为%s分' % qset92)
print('班级中共所有学生的数学总成绩为%s分' % qset23)
print('*' * 38)

# num25:
print('第25题：')
zcj = qset91[0] + qset92[0] + qset23[0]
print('班级中共所有学生的各科成绩总和为%s分' % zcj)
print('*' * 38)

# num26:
print('第26题：')
qset26 = session.query(func.avg(Students.chinese)).first()
print('班级中共所有学生的语文成绩的平均分为%s分' % qset26)
print('*' * 38)

# num27:
print('第27题：')
qset27 = session.query(func.avg(Students.chinese+Students.english+Students.math)).first()
print('班级中共所有学生的总成绩的平均分为%s分' % qset27)
print('*' * 38)

# num28:
print('第28题：')
qset28 = session.query(func.max(Students.math)).first()
print('班级中共所有学生的数学成绩最高分数为%s分' % qset28)
qset93 = session.query(func.min(Students.math)).first()
print('班级中共所有学生的数学成绩最低分数为%s分' % qset93)
print('*' * 38)

# num29:
print('第29题：')
qset29 = session.query(func.count(emp.ename)).filter(emp.job=='销售员').filter(emp.sal>15000).first()
print('公司中销售员岗位中共有%s个工资大于15000' % qset29)
qset100 = session.query(func.count(emp.ename)).filter(emp.job=='经理').filter(emp.sal>15000).first()
print('公司中经理岗位中共有%s个工资大于15000' % qset100)
qset101 = session.query(func.count(emp.ename)).filter(emp.job=='分析师').filter(emp.sal>15000).first()
print('公司中分析师岗位中共有%s个工资大于15000' % qset101)
qset102 = session.query(func.count(emp.ename)).filter(emp.job=='董事长').filter(emp.sal>15000).first()
print('公司中董事长岗位中共有%s个工资大于15000' % qset102)
qset103 = session.query(func.count(emp.ename)).filter(emp.job=='文员').filter(emp.sal>15000).first()
print('公司中文员岗位中共有%s个工资大于15000' % qset103)
print('*' * 38)

# num30:
print('第30题：')
res = session.query(emp.job).group_by(emp.job).all()

qset30 = session.query(func.count(emp.job)).filter(emp.sal>15000).group_by(emp.job).all()
for data in qset30:
     print(data)


print('*' * 38)

# 确认
session.commit()


# 确认
session.commit()

# 关闭
session.close()