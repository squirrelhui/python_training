from urllib import request
import sys

def download(html, fname):
    url = request.urlopen(html)
    with open(fname, 'wb') as fobj:
        while 1:
            data = url.read(4096)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    download(sys.argv[1], sys.argv[2])