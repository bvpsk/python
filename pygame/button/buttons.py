import pygame
from time import sleep
screen = pygame.display.set_mode((1000,600))
run = True
green = pygame.image.load("green.png")
red = pygame.image.load("red.png")
img=pygame.image.load("back.png")
imgg=pygame.image.load("background.png")
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
b=Button(red,img,label,green)
initial = 1
while run:
    if initial == 1:
        b.show()
    else:
        screen.blit(imgg,(0,0))
        pygame.display.flip()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mx,my) = pygame.mouse.get_pos()
            if mx>=500 and mx<=550:
                if my>=300 and my<=350:
                    initial+=1
                    b.clicked()
pygame.quit()
