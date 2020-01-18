import paramiko
import sys
import getpass
import os
import threading

def rcmd(host, user, passwd, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)
    stdin, stout, sterr = ssh.exec_command(command)
    out = stout.read()
    err = sterr.read()
    if out:
        print('%s out: %s' % (host, out.decode()) )
    if err:
        print('%s out: %s' % (host, err.decode()))

    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: %s ipfile 'command'" % sys.argv[0])
    if not os.path.exists(sys.argv[1]):
        print('%s is not extsis')

    ipfile = sys.argv[1]
    cmds = sys.argv[2]
    passwd = getpass.getpass
    with open(ipfile, 'rb') as fobj:
        for line in fobj:
            ip = line.strip()

        t = threading.Thread(target=rcmd, args=(ip, 'root', passwd, cmds))
        t.start()