from random import randint
money=1000
while money>0:
    print('你总共有%d'%money)
    need_to_go=False
    while True:
        debt=int(input('请下注'))
        if 0<debt<=money:
            break
    first=randint(1,6)+randint(1,6)
    print('玩家摇出了%d'%first)
    if first==7 or first==11:
        print('玩家胜')
        money+=debt
    elif first==3 or first==2 or first==12:
        print('庄家胜')
        money-=debt
    else:
        need_to_go=True
        
    while need_to_go==True:
        need_to_go=False
        print('继续游戏')
        second=randint(1,6)+randint(1,6)
        print('玩家摇出了%d'%second)
        if second==7:
            print('庄家胜')
            money-=debt
        elif second==first:
            print('玩家胜')
            money+=debt
        else:
            need_to_go=True
print('你已经输掉所有资金')
        