import wget
import os
import re
def get_patt(fname, patt, charset='utf8'):
    '用于在文件中找到相关的模式'
    result = []
    cpatt = re.compile(patt)
    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                result.append(m.group())

    return result

if __name__ == '__main__':
    url = 'http://www.sina.com'
    down_dir = '/tmp/sina'
    fname = '/tmp/sina/sina.html'
    img_patt = '(http|https)://[\w./-]+.(jpg|jpeg|png|gif)'


    #下载目录不存在则创建
    if not os.path.exists(down_dir):
        os.mkdir(down_dir)
    if not os.path.exists(fname):
        wget.download(url, fname)

    img_list = get_patt(fname, img_patt)  # 取得图片url列表

    for img_url in img_list:
        wget.download(img_url, down_dir)
