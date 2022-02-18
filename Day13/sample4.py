from fileinput import filename
from random import randint
from threading import Thread
from time import time, sleep

class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename=filename

    def run(self):
        print('start download %s.....'%self._filename)
        time_to_download=randint(3,5)
        sleep(time_to_download)
        print('%s was download completed, it cost%.2f'%(self._filename,time_to_download))

def main():
    start=time()
    t1=DownloadTask('Python.pdf')
    t1.start()
    t2=DownloadTask('Costsin.avi')
    t2.start()
    t1.join()
    t2.join()
    end=time()
    print('Total cost %.2f to download all files'%(end-start))

if __name__=='__main__':
    main()