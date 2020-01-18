from sqlalchemy import create_engine, Column, INTEGER, String, ForeignKey, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建连接到数据库的引擎
engine = create_engine(
    # mysql+pymysql://用户名：密码@服务器/数据库？参数
    'mysql+pymysql://mysql:123qqq...A@192.168.1.10/tedu1908?charset=utf8', encoding='utf8',
    # echo=True # 在屏幕上输出日志
)


# 创建一个会话类，用于客户端到服务器的会话连接
Session = sessionmaker(bind=engine)


# 创建实体类（与表关联的类）的基类
Base = declarative_base()

# 创建实体类
class Departments(Base):
    __tablename__ = 'departments' # 定义库中关联的表
    dep_id = Column(INTEGER, primary_key=True)
    dep_name = Column(String(20), unique=True)

    def __str__(self):
        return '[%s: %s]' % (self.dep_id, self.dep_name)

class employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(INTEGER, primary_key=True)
    emp_name = Column(String(20))
    email = Column(String(50))
    dep_id = Column(INTEGER, ForeignKey('departments.dep_id'))

class salary(Base):
    __tablename__ = 'salary'
    sal_id = Column(INTEGER, primary_key=True)
    date = Column(DATE)
    emp_id = Column(INTEGER, ForeignKey('employees.emp_id'))
    basic = Column(INTEGER)
    awards = Column(INTEGER)

if __name__ == '__main__':
    #如果库中没有相关的表则创建，如果已存在，只是映射，不会再创建一遍
    Base.metadata.create_all(engine)