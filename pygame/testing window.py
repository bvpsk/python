import pygame
from random import randint as r
import math
screen = pygame.display.set_mode((1000,600))
background=(255,255,255)
pygame.display.set_caption('circles')
class Circle:
    def __init__(self,(x,y),size,(r,b,ye)):
        self.x=x
        self.y=y
        self.size=size
        self.r=r
        self.b=b
        self.ye=ye
        self.thickness=5
        self.speed = 0.01
        self.angle = 0
    def display(self):
        pygame.draw.circle(screen,(self.r,self.b,self.ye),(int(self.x),int(self.y)),self.size,self.thickness)
    def move(self):
        self.x+=0.1
        self.y-=0.1

        
listt=[]
for n in range(60):
    ax=r(0,1000)
    ay=r(0,600)
    asi=r(5,50)
    ar=r(0,255)
    ab=r(0,255)
    aye=r(0,255)
    listt.append(Circle((ax,ay),asi,(ar,ab,aye)))

running = True
while running:
    screen.fill(background)
    for ob in listt:
        ob.move()
        ob.display()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
pygame.quit()
