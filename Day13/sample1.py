from random import randint
from time import time,sleep

def download_task(filename):
    print('开始下载%s___'%filename)
    time_to_download=randint(5,10)
    sleep(time_to_download)
    print('%s下载w完成！耗费了%d秒'%(filename,time_to_download))

def main():
    start=time()
    download_task('Python从0到弃坑.pdf')
    download_task('tokyo hot.avi')
    end=time()
    print('总共耗时%.2f秒'%(end-start))

if __name__=='__main__':
    main()
