import paramiko
import sys
import getpass
import os
import threading

def rcmd(host, user, passwd, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('\033[32;1m[%s] OUT:\n%s\033[0m' % (host, out.decode()))
    if err:
        print('\033[31;1m[%s] ERR:\n%s\033[0m' % (host, err.decode()))

    ssh.close()

if __name__ == '__main__':
    #rcmd('192.168.1.10', 'root', 'a', 'id root; id zhangsan')
    if len(sys.argv) != 3:
        print("Usage:%s ipfile 'commands'"% sys.argv[0])
        exit(1)
    if not os.path.exists(sys.argv[1]):
        print('%s is not exists!' % sys.argv[1])
        exit(2)
    ipflie = sys.argv[1]
    cmds = sys.argv[2]
    passwd = getpass.getpass()
    with open(ipflie, 'rb') as fobj:
        for line in fobj:
            ip = line.strip()
            #rcmd(ip, 'root', passwd, cmds)
            t = threading.Thread(target=rcmd, args=(ip, 'root', passwd, cmds))
            t.start()