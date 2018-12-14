import pygame
from time import sleep
from random import randint as r
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('keyboard controlled sphere')
ball = pygame.image.load("ball.png")
back = pygame.image.load("bounceback.png")
green = pygame.image.load("green.png")
red = pygame.image.load("red.png")
img=pygame.image.load("back.png")
pygame.font.init()
myfont = pygame.font.SysFont("Luminari",200,italic=True)
label = myfont.render("BOUNCE",1,(255,0,100))
change = green
class Button:
    def __init__(self,pic,back,label,picc):
        self.pic=pic
        self.picc=picc
        self.back = back
        self.label = label
    def clicked(self):
        screen.blit(self.back,(0,0))
        screen.blit(self.pic,(500,300))
        screen.blit(self.label,(200,100))
        pygame.display.flip()
        sleep(0.1)
    def show(self):
        screen.blit(self.back,(0,0))
        screen.blit(self.label,(200,100))
        screen.blit(self.picc,(500,300))
        pygame.display.flip()
but=Button(red,img,label,green)
initial = 1
class Circle:
    def __init__(self,(x,y),ball,cho,choi):
        self.x=x
        self.y=y
        self.size=100
        self.ball = ball
        self.width=self.size
        self.speed = 5
        self.mode = cho
        self.model = choi
    def display(self):
        screen.blit(self.ball,(int(self.x),int(self.y)))
    def move(self,mode):
        self.mode = mode
    #def movel(self,model):
#        self.model = model
    def ment(self):
        if self.mode == 'nw':
            self.y-=self.speed
            self.x-=self.speed
            if (self.y)<=0:
                self.mode = 'sw'
            if (self.x)<=0:
                self.mode = 'ne'
        if self.mode == 'ne':
            self.y-=self.speed
            self.x+=self.speed
            if (self.x+100)>=1000:
                self.mode = 'nw'
            if self.y<=0:
                self.mode = 'se'
        if self.mode == 'sw':
            self.y+=self.speed
            self.x-=self.speed
            if (self.x)<=0:
                self.mode = 'se'
            if (self.y+100)>=600:
                self.mode = 'nw'
        if self.mode == 'se':
            self.y+=self.speed
            self.x+=self.speed
            if (self.x+100)>=1000:
                self.mode = 'sw'
            if (self.y+100)>=600:
                self.mode = 'ne'
        if self.mode == 'a':
            self.y-=self.speed
            if (self.y)<=0:
                self.mode = 'b'
        if self.mode == 'b':
            self.y+=self.speed
            if (self.y+100)>=600:
                self.mode = 'a'
        if self.mode == 'c':         #model() here
            self.x-=self.speed
            if (self.x)<=0:
                self.mode = 'd'
        if self.mode == 'd':          #model() here
            self.x+=self.speed
            if (self.x+100)>=1000:
                self.mode = 'c'
ch=r(1,2)
che=r(3,4)
b=r(51,549)
if ch == 1:
    cho = 'a'
if ch == 2:
    cho = 'b'
if che == 3:
    choi = 'c'
if che == 4:
    choi = 'd'
a=Circle((b,b),ball,cho,choi)
run =True
while run:
    if initial ==1:
        but.show()
    else:
        screen.blit(back,(0,0))
        a.ment()
        a.display()
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mx,my) = pygame.mouse.get_pos()
            if mx>=500 and mx<=550:
                if my>=300 and my<=350:
                    initial+=1
                    but.clicked()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                a.move('a')
            if event.key == pygame.K_s:
                a.move('b')
            if event.key == pygame.K_a:
                a.move('c')
 #               a.movel('c')
            if event.key == pygame.K_d:
                a.move('d')
                #a.movel('d')
            if event.key == pygame.K_q:
                a.move('nw')
            if event.key == pygame.K_e:
                a.move('ne')
            if event.key == pygame.K_z:
                a.move('sw')
            if event.key == pygame.K_c:
                a.move('se')
pygame.quit()
