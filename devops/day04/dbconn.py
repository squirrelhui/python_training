from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, DECIMAL, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建连接到数据库的引擎
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器/数据库?参数
    'mysql+pymysql://mysql:123qqq...A@139.159.200.182/lianxi?charset=utf8',
    encoding='utf8',
    # echo=True  # 在屏幕上输出日志
)

# 创建一个会话类，用于客户端到服务器的会话连接
Session = sessionmaker(bind=engine)

# 创建实体类（与表关联的类）的基类
Base = declarative_base()

# 创建实体类
# class Departments(Base):
#     __tablename__ = 'departments'  # 定义库中关联的表
#     dep_id = Column(Integer, primary_key=True)
#     dep_name = Column(String(20), unique=True)
#
#     def __str__(self):
#         return "[%s: %s]" % (self.dep_id, self.dep_name)
#
# class Employees(Base):
#     __tablename__ = 'employees'
#     emp_id = Column(Integer, primary_key=True)
#     emp_name = Column(String(20))
#     email = Column(String(50))
#     dep_id = Column(Integer, ForeignKey('departments.dep_id'))
#
# class Salary(Base):
#     __tablename__ = 'salary'
#     id = Column(Integer, primary_key=True)
#     date = Column(Date)
#     emp_id = Column(Integer, ForeignKey('employees.emp_id'))
#     basic = Column(Integer)
#     awards = Column(Integer)

class emp(Base):
    __tablename__ = 'emp'
    empno = Column(Integer, primary_key=True)
    ename = Column(String(50))
    job = Column(String(50))
    mgr = Column(Integer, index=True)
    hiredate = Column(Date)
    sal = Column(DECIMAL(7, 2))
    COMM = Column(DECIMAL(7, 2))
    deptno = Column(Integer)

class Students(Base):
    __tablename__ = 'Students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    chinese = Column(FLOAT)
    english = Column(FLOAT)
    math = Column(FLOAT)

if __name__ == '__main__':
    # 如果库中没有相关的表则创建，如果已存在，只是映射，不会再创建一遍
    Base.metadata.create_all(engine)
