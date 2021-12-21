from enum import Enum,unique
from math import radians, sqrt
from random import randint

import pygame
from pygame import color
from pygame import math
from pygame.draw import circle

@unique
class Color(Enum):
    """颜色"""

    RED=(255,0,0)
    GREEN=(0,255,0)
    BLUE=(0,0,255)
    BLACK=(0,0,0)
    WHITE=(255,255,255)
    GRAY=(242,242,242)

    @staticmethod
    def random_color():
        """获得随机颜色"""
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        return(r,g,b)
class Ball(object):
    """球"""
    def __init__(self,x,y,radius,sx,sy,color=Color.RED):
        """初始化方法"""
        self.x=x
        self.y=y
        self.radius=radius
        self.sx=sx
        self.sy=sy
        self.color=color
        self.alive=True

    def move(self,screen):
        """移动"""
        self.x+=self.sx
        self.y+=self.sy
        if self.x-self.radius<=0 or \
                self.x+self.radius>=screen.get_width():
            self.sx=-self.sx
        if self.y-self.radius<=0 or \
                self.y+self.radius>=screen.get_height():
            self.sy=-self.sy
    
    def eat(self,other):
        """吃其他球"""
        if self.alive and other.alive and self !=other:
            dx,dy=self.x-other.x, self.y-other.y
            distance=sqrt(dx**2+dy**2)
            if distance<self.radius>other.radius \
                    and self.radius>other.radius:
                other.alive=False
                self.radius=self.radius+int(other.radius*0.146)

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)

def main():
    #定义用来装所有球的容器
    balls=[]
    #初始化导入的pygame中的模块
    pygame.init
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption('大球吃小球')
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            #处理鼠标事件
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                #获得点击鼠标位置
                x,y=event.pos
                radius=randint(10,100)
                sx,sy=randint(-10,10),randint(-10,10)
                color=Color.random_color()
                #在点击鼠标的位置创建一个球
                ball=Ball(x,y,radius,sx,sy,color)
                balls.append(ball)
        screen.fill((255,255,255))
        #取出容器中的球
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        #每隔50毫秒就改变球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            #检测有没有吃到其他球
            for other in balls:
                ball.eat(other)
if __name__=='__main__':
    main()


