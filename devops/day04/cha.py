from dbconn import Students, emp, Session

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
qset1 = session.query(Students)
for data in qset1:
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
print('第3题：')
print('%3s %-3s %-3s %-3s ' % ('学生名称', '语文', '英语', '数学'))



# 确认
session.commit()

# 关闭
session.close()