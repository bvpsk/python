import pygame
import math
from random import randint as r
screen = pygame.display.set_mode((1000,600))
back=(255,255,255)
pygame.display.set_caption("SPHERES")
class Circle:
    def __init__(self,(x,y),color,size,soo,sorr,speed):
        self.x=x
        self.y=y
        self.color=color
        self.size=size
        self.thickness=self.size
        self.speed = speed
        self.xto = soo
        self.yto = sorr
        self.prevx =0
        self.prevy = 0
    def display(self):
        pygame.draw.circle(screen,self.color,(int(self.x),int(self.y)),self.size,self.thickness)
    def move(self):
        self.prevx = self.x
        self.prevy = self.y
        if (self.x)-self.size <= 0:
            self.xto = 'a'
        if (self.x)+self.size >= 1000:
            self.xto = 'b'
        if (self.y)-self.size <= 0:
            self.yto = 'c'
        if (self.y)+self.size >= 600:
            self.yto = 'd'
        if self.xto == 'a':
            self.x+=self.speed
        if self.xto == 'b':
            self.x-=self.speed
        if self.yto == 'c':
            self.y+=self.speed
        if self.yto == 'd':
            self.y-=self.speed
    def collide(self,be):
        dx=self.x - be.x
        dy = self.y - be.y
        dox = self.x - self.prevx
        doy = self.y - self.prevy
        dotx = be.x - be.prevx
        doty = be.y - be.prevy
        pro = math.hypot(dx,dy)
        if pro <= self.size + be.size:
            if dox < 0 and doy > 0:
                if dotx < 0 and doty > 0:
                    be.xto = 'a'
                    be.yto = 'd'
                if dotx > 0 and doty < 0:
                    self.xto = 'a'
                    self.yto = 'd'
                    be.xto = 'b'
                    be.yto = 'c'
                if dotx < 0 and doty < 0:
                    self.yto = 'd'
                    be.yto = 'c'
                if dotx > 0 and doty > 0:
                    self.xto = 'a'
                    be.xto = 'b'
            if dox > 0 and doy < 0:
                if dotx > 0 and doty < 0:
                    be.xto = 'b'
                    be.yto = 'c'
                if dotx < 0 and doty > 0:
                    self.xto = 'b'
                    self.yto = 'c'
                    be.xto = 'a'
                    be.yto = 'd'
                if dotx > 0 and doty > 0:
                    self.yto = 'c'
                    be.yto = 'd'
                if dotx < 0 and doty < 0:
                    self.xto = 'b'
                    be.xto = 'a'
            if dox > 0 and doy > 0:
                if dotx > 0 and doty > 0:
                    be.xto = 'b'
                    be.yto = 'd'
                if dotx < 0 and doty < 0:
                    self.xto = 'b'
                    self.yto = 'd'
                    be.xto = 'a'
                    be.yto = 'c'
                if dotx > 0 and doty < 0:
                    self.yto = 'd'
                    be.yto = 'c'
                if dotx < 0 and doty > 0:
                    self.xto = 'b'
                    be.xto = 'a'
            if dox < 0 and doy < 0:
                if dotx < 0 and doty < 0:
                    be.xto = 'a'
                    be.yto = 'c'
                if dotx > 0 and doty > 0:
                    self.xto = 'a'
                    self.yto = 'c'
                    be.xto = 'b'
                    be.yto = 'd'
                if dotx > 0 and doty < 0:
                    self.xto = 'a'
                    be.xto = 'b'
                if dotx < 0 and doty > 0:
                    self.yto = 'c'
                    be.yto = 'd'
            
 

col1=(0,0,255)
col2=(255,0,0)
col3=(0,255,0)
col4=(255,0,255)
x=r(51,249)
y=r(151,459)
z=r(251,559)
w=r(351,669)
so=r(1,2)
sor=r(3,4)
if so == 1:
    soo = 'a'
if so == 2:
    soo = 'b'
if sor == 3:
    sorr = 'c'
if sor == 4:
    sorr = 'd'

sooo=r(1,2)
sorrr=r(3,4)
if sooo == 1:
    soooo = 'a'
if sooo == 2:
    soooo = 'b'
if sorrr == 3:
    sorry = 'c'
if sorrr == 4:
    sorry = 'd'

some=r(1,2)
sort=r(3,4)
if some == 1:
    soup = 'a'
if some == 2:
    soup = 'b'
if sort == 3:
    story = 'c'
if sort == 4:
    story = 'd'

somu=r(1,2)
sorting=r(3,4)
if somu == 1:
    full = 'a'
if somu == 2:
    full = 'b'
if sorting == 3:
    half = 'c'
if sorting == 4:
    half = 'd'
a=Circle((y,y),col1,50,soo,sorr,8)
b=Circle((x,x),col2,40,soooo,sorry,8)
c=Circle((z,z),col3,80,soup,story,4)
d=Circle((w,w),col4,30,full,half,5)
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            p=r(0,255)
            q=r(0,255)
            s=r(0,255)
            back = (p,q,s)
    screen.fill(back)
    a.collide(b)
 #   a.collide(c)
#    a.collide(d)
    b.collide(a)
#    b.collide(c)
#    b.collide(d)
 #  c.collide(a)
 #   c.collide(d)
 #   d.collide(a)
#    d.collide(b)
#    d.collide(c)
    a.move()
    b.move()
#    c.move()
#    d.move()
    a.display()
    b.display()
#    c.display()
#    d.display()
    pygame.display.flip()
pygame.quit()
