from concurrent.futures import thread
from random import randint
from threading import Thread
from time import time,sleep

def download(filename):
    print('开始下载%s......'%filename)
    time_to_download=randint(3,6)
    sleep(time_to_download)
    print('%s下载完成，耗时%d秒'%(filename,time_to_download))

def main():
    start=time()
    t1=Thread(target=download,args=('python.pdf',))
    t1.start()
    t2=Thread(target=download,args=('moive.mp4',))
    t2.start()
    t1.join()
    t2.join()
    end=time()
    print('总共耗时%.2f'%(end-start))

if __name__=='__main__':
    main()