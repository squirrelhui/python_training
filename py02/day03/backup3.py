import os
import tarfile
import hashlib
import pickle
from time import strftime

def check_md5(fname):
    m = hashlib.md5()

    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

def full_backup():
    fname = os.path.basename(src)
    fname = '%s_full_%s.tar.gz' %

def incr_backup():

if __name__ == '__main__':
    src = '/tmp/nsd1908/security'
    dst = '/tmp/nsd1908/backup'
    md5file = '/tmp/nsd1908/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)