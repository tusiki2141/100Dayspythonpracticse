from time import sleep
from threading import Thread

class Account(object):

    def __init__(self):
        self._balance=0

    def deposit(self,money):
        new_balance=self._balance + money
        sleep(0.1)
        self._balance=new_balance

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __ini__(self,account,money):
        super().__init__()
        self._account=account
        self._money=money
    
    def run(self):
        self._account.deposit(self._money)

def main():
    account=Account()
    threads=[]
    for _ in range(100):
        t=AddMoneyThread(account,1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    print('Account%s Totoal balance is %d'%(account,account.balance))

if __name__=='__main__':
    main()