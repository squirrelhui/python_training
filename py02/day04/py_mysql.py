import pymysql

# 建立到数据库的连接
conn = pymysql.connect(
    host ='192.168.1.10', port=3306,
    user='mysql', passwd='123qqq...A',
    db='nsd1908', charset='utf8'
)

# 创建游标，它就像文件对象一样
cur = conn.cursor()

# 编写SQL语句
mk_dep = """CREATE TABLE departments(dep_id INT, dep_name VARCHAR(50), PRIMARY KEY(dep_id))
"""
mk_emp = """CREATE TABLE employees(
emp_id INT, emp_name VARCHAR(20), email VARCHAR(20), dep_id INT, 
PRIMARY KEY (emp_id),
FOREIGN KEY (dep_id) REFERENCES  departments(dep_id)
)
"""
mk_sal = """CREATE TABLE salary(
id INT, date DATE, emp_id INT, basic INT, awards INT,
PRIMARY KEY(id),
FOREIGN KEY(emp_id) REFERENCES  employees(emp_id))
"""

# 执行SQL语句
# cur.execute(mk_dep)
# cur.execute(mk_emp)
# cur.execute(mk_sal)

#添加记录
# insert1 = 'INSERT INTO departments VALUES(%s, %s) '
# cur.executemany(insert1, [(1, '人事部'), (2, '运维部'), (3, '开发部'), (4, '财务部')])

# update1 = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
# cur.execute(update1, ('人力资源部', '人事部'))

# delete1 = 'DELETE FROM departments WHERE dep_name=%s'
# cur.execute(delete1, ('运维部',))

# select1 = 'SELECT * FROM departments'
# cur.execute(select1)
# result1 = cur.fetchone()
# print(result1)
# print('*' * 30)
# result2 = cur.fetchmany(2)
# print(result2)
# print('*' * 30)
# result3 = cur.fetchall()
# print(result3)


# 确认
conn.commit()

# 关闭游标、关闭连接
cur.close()
conn.close()