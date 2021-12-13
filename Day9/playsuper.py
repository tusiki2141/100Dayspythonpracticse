from abc import ABCMeta,abstractmethod
import abc
from random import randint,randrange

class Fighter(object,metaclass=ABCMeta):
    """战斗者"""
    __slots__=('name','hp')

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
    
    def magic_attack(self.others):
        """魔法攻击"""
        if self.mp>=20:
            self.mp-=20
            for temp in others:
                if temp.alive:
                    temp.hp-=randint(10,15)
            return True
        else:
            return False
    
    def resume(self):
        """恢复魔法值"""
        incr_point=randint(1,10)
        self.mp+=incr_point
        return incr_point

    def __str__(self):
        return '~~~%s凹凸曼~~~\n'%self.name +\
            '生命值：%d\n'%self._hp + \
            '魔法值：%d\n'%self._mp
    
class Moster(Fighter):

    __slots__=('_name','_hp')

    def __init__(self, name, hp):
        super().__init__(name,hp)
    
    def attack(self,other):
        other.hp-=randint(10,20)
    
    def __str__(self) -> str:
        return '~~~%s小怪兽~~~\n'%self.name +\
            '生命值：%d\n'%self._hp
    
    def is_any_alive(mosters):
        for moster in mosters:
            if moster.alive>0:
                return True
        return False
    
    def selec_alive_one(mosters):
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
    

    