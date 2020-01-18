from dbconn import Students, emp, Session

session = Session()

# u1 = emp(
#     empno=1009, ename='曾阿牛', job='董事长',
#     hiredate='2001-11-17',sal=50000.00,deptno=10,
# )
#
# u2 = emp(
#     empno=1004, ename='刘备', job='经理', mgr=1009,
#     hiredate='2001-4-2',sal=29750.00,deptno=20,
# )
#
# u3 = emp(
#     empno=1006, ename='关羽', job='经理', mgr=1009,
#     hiredate='2001-5-1',sal=28500.00,deptno=30,
# )
#
# u4 = emp(
#     empno=1007, ename='张飞', job='经理', mgr=1009,
#     hiredate='2001-9-1',sal=24500.00,deptno=10,
# )
#
# u5 = emp(
#     empno=1008, ename='诸葛亮', job='分析师', mgr=1004,
#     hiredate='2007-4-19',sal=30000.00,deptno=20,
# )
#
# u6 = emp(
#     empno=1013, ename='庞统', job='分析师', mgr=1004,
#     hiredate='2001-12-3',sal=30000.00,deptno=20,
# )
#
# u7 = emp(
#     empno=1002, ename='黛绮丝', job='销售员', mgr=1006,
#     hiredate='2001-2-20',sal=16000.00,COMM=3000.00,deptno=30,
# )
#
# u8 = emp(
#     empno=1003, ename='殷天正', job='销售员', mgr=1006,
#     hiredate='2001-2-22',sal=12500.00,COMM=5000.00,deptno=30,
# )
#
# u9 = emp(
#     empno=1005, ename='谢逊', job='销售员', mgr=1006,
#     hiredate='2001-9-28',sal=12500.00,COMM=14000.00,deptno=30,
# )
#
# u10 = emp(
#     empno=1010, ename='韦一笑', job='销售员', mgr=1006,
#     hiredate='2001-9-8',sal=15000.00,COMM=0.00,deptno=30,
# )
#
# u11 = emp(
#     empno=1012, ename='程普', job='文员', mgr=1006,
#     hiredate='2001-12-3',sal=9500.00,deptno=30,
# )
#
# u12 = emp(
#     empno=1014, ename='黄盖', job='文员', mgr=1007,
#     hiredate='2002-1-23',sal=13000.00,deptno=10,
# )
#
# u13 = emp(
#     empno=1011, ename='周泰', job='文员', mgr=1008,
#     hiredate='2007-5-23',sal=11000.00,deptno=20,
# )
#
# session.add_all([u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12, u13])


s1 = Students(name='张小明', chinese=89, english=98, math=90)
s2 = Students(name='李进', chinese=67, english=98, math=89)
s3 = Students(name='王五', chinese=87, english=78, math=77)
s4 = Students(name='李一', chinese=88, english=98, math=90)
s5 = Students(name='李来财', chinese=82, english=84, math=67)
s6 = Students(name='张进宝', chinese=55, english=85, math=45)
s7 = Students(name='黄蓉', chinese=85, english=75, math=80)
s8 = Students(name='张一李', chinese=75, english=65, math=30)
s9 = Students(name='何李', chinese=75, english=65, math=90)
s10 = Students(name='单', chinese=75, english=65, math=30)
s11 = Students(name='jack', chinese=75, english=65, math=40)
s12 = Students(name='marry', chinese=75, english=65, math=60)
session.add_all([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12])



# 确认
session.commit()

# 关闭
session.close()
