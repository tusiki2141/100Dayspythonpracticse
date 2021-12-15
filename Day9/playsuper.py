from abc import ABCMeta,abstractmethod
import abc
from random import randint,randrange

class Fighter(object,metaclass=ABCMeta):
    """战斗者"""
    __slots__=('_name','_hp')

    def __init__(self,name,hp):
        """初始化方法"""
        self._name=name
        self._hp=hp
    
    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self,hp):
        self._hp=hp if hp>=0 else 0

    @property
    def alive(self):
        return self._hp>0

    @abstractmethod
    def attack(self):
        """攻击"""
        pass

class Ultraman(Fighter):

    __solts__=('_name','_hp','_mp')

    def __init__(self,name,hp,mp):
        super().__init__(name,hp) #super().__init__是指调用父类方法
        self._mp=mp
    
    def attack(self,other):
        other.hp-=randint(15,25)

    def huge_attack(self,other):
        """必杀技"""
        if self._mp>=50:
            self._mp-=50
            injury=other.hp*3//4
            injury=injury if injury>=50 else 50
            other.hp-=injury
            return True
        else:
            self.attack(other)
            return False
    
    def magic_attack(self,others):
        """魔法攻击"""
        if self._mp>=20:
            self._mp-=20
            for temp in others:
                if temp.alive:
                    temp.hp-=randint(10,15)
            return True
        else:
            return False
    
    def resume(self):
        """恢复魔法值"""
        incr_point=randint(1,10)
        self._mp+=incr_point
        return incr_point

    def __str__(self):
        return '~~~%s凹凸曼~~~\n'%self.name +\
            '生命值：%d\n'%self._hp + \
            '魔法值：%d\n'%self._mp
    
class Moster(Fighter):

    __slots__=('_name','_hp')

    def attack(self,other):
        other.hp-=randint(10,20)
    
    def __str__(self):
        return '~~~%s小怪兽~~~\n'%self.name +\
            '生命值：%d\n'%self._hp
    
def is_any_alive(mosters):
    for moster in mosters:
        if moster.alive>0:
            return True
    return False
    
def select_alive_one(mosters):
    mosters_len=len(mosters)
    while True:
        index=randrange(mosters_len)
        moster=mosters[index]
        if moster.alive>0:
            return moster
    
def display_info(ultraman,mosters):
    """显示凹凸曼和小怪兽信息"""
    print(ultraman)
    for moster in mosters:
        print(moster,end='')

def main():
    u=Ultraman('A',1000,120)
    m1=Moster('B',250)
    m2=Moster('C',500)
    m3=Moster('D',750)
    ms=[m1,m2,m3]
    fight_round=1
    while u.alive and is_any_alive(ms):
        print('=============第%02d回合============'%fight_round)
        m=select_alive_one(ms)    ##选中一只怪兽
        skill=randint(1,10)
        if skill<=6:
            print('%s对%s使用普通攻击'%(u.name,m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点'%(u.name,u.resume()))
        elif skill<=9:
            if u.magic_attack(ms):
                print('%s对%s使用魔法攻击'%(u.name,m.name))
            else:
                print('%s使用魔法攻击失败'%u.name)
        else:
            if u.huge_attack(m):
                print('%s使用了必杀技'%u.name)
            else:
                print('%s使用了普通打击'%u.name)
                print('%s魔法值恢复了%d'%(u.name,u.resume()))
        if m.alive>0:
            print('%s反击了%s'%(m.name,u.name))
            m.attack(u)
        display_info(u,ms)
        fight_round+=1
    print('\n================战斗结束！==========')
    if u.alive>0:
        print('%s凹凸曼胜利了'%u.name)
    else:
        print('小怪兽胜利了')
if __name__=='__main__':
    main()
    