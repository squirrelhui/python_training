import  time
import subprocess
import os

def ping(host):

    result = subprocess.run('ping -c2 %s &> /dev/null' % host, shell=True)

    if result.returncode == 0:
        print('%s :up' % host)

    else:
        print('%s: down' % host)


if __name__ == '__main__':
    ips = [' 176.121.202.%s' % i for i in range(1, 255)]
    print((time.ctime()))
    for ip in ips:
        ret_val = os.fork()
        if not ret_val:
            ping(ip)
            exit()
    print(time.ctime())
