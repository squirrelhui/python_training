import  paramiko

def rcmd(host, user, passwd, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('\033[32;1m[%s] OUT:\n%s' % (host, out.decode()))
    if err:
        print('[%s] ERR:\n%s' % (host, err.decode()))

    ssh.close()

if __name__ == '__main__':
    rcmd('192.168.1.10', 'root', 'a', 'id root; id zhangsan')