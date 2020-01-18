# create / retrieve / update / delete
from dbconn import Students, emp, Session

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
# qset10 = session.query(Departments).filter(Departments.dep_name=='销售部')
# sales = qset10.first()
# print(sales)
# session.delete(sales)
u1 = emp(
    empno=1009, ename='曾阿牛', job='董事长',
    hiredate='2001-11-17',sal=50000,deptno=10,
)

u2 = emp(
    empno=1004, ename='刘备', job='经理', mgr=1009,
    hiredate=2001-4-2,sal=29750,COMM='',deptno=20,
)

u3 = emp(
    empno=1006, ename='关羽', job='经理', mgr=1009,
    hiredate=2001-5-1,sal=28500,COMM='',deptno=30,
)

u4 = emp(
    empno=1007, ename='张飞', job='经理', mgr=1009,
    hiredate=2001-9-1,sal=24500,COMM='',deptno=10,
)

u5 = emp(
    empno=1008, ename='诸葛亮', job='分析师', mgr=1004,
    hiredate=2007-4-19,sal=30000,COMM='',deptno=20,
)

u6 = emp(
    empno=1013, ename='庞统', job='分析师', mgr=1004,
    hiredate=2001-12-3,sal=30000,COMM='',deptno=20,
)

u7 = emp(
    empno=1002, ename='黛绮丝', job='销售员', mgr=1006,
    hiredate=2001-2-20,sal=16000,COMM=3000,deptno=30,
)

u8 = emp(
    empno=1003, ename='殷天正', job='销售员', mgr=1006,
    hiredate=2001-2-22,sal=12500,COMM=5000,deptno=30,
)

u9 = emp(
    empno=1005, ename='谢逊', job='销售员', mgr=1006,
    hiredate=2001-9-28,sal=12500,COMM=14000,deptno=30,
)

u10 = emp(
    empno=1010, ename='韦一笑', job='销售员', mgr=1006,
    hiredate=2001-9-8,sal=15000,COMM=0,deptno=30,
)

u11 = emp(
    empno=1012, ename='程普', job='文员', mgr=1006,
    hiredate=2001-12-3,sal=9500,COMM='',deptno=30,
)

u12 = emp(
    empno=1014, ename='黄盖', job='文员', mgr=1007,
    hiredate=2002-1-23,sal=13000,COMM='',deptno=10,
)

u13 = emp(
    empno=1011, ename='周泰', job='文员', mgr=1008,
    hiredate=2007-5-23,sal=11000,COMM='',deptno=20,
)

session.add_all([u1])
# session.add_all([u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12, u13])

# 确认
session.commit()

# 关闭
session.close()
