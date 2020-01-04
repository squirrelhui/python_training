import sys
import subprocess
from randpass2 import randpass

def add_user(user, passwd, fname):
    result = subprocess.run('id %s &> /dev/null' % user , shell=True)
    if result.returncode == 0:
        print('用户已存在')
        return

    subprocess.run('useradd %s' % user, shell=True)
    subprocess.run('echo %s | passwd --stdin %s' % (user, passwd), shell=True)

    info = """username: %s
password: %s
""" % (user, passwd)

    with open(fname) as fobj:
        fobj.write(info)

if __name__ == '__main__':
    user = sys.argv[1]
    fname = sys.argv[2]
    passwd = randpass()
    add_user(user, passwd, fname)