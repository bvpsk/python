import pygame
from pygame.locals import *
screen=pygame.display.set_mode((1000,600))
back = pygame.image.load("batman.png")
col=(0,255,0)
run = True
while run:
    screen.blit(back,(0,0))
    pygame.draw.rect(screen,col,(140,90,100,50))
    pygame.font.init()
    myfont = pygame.font.SysFont('Courier',35)
    label = myfont.render("kumar", 1, (255,255,0))
    screen.blit(label, (150, 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if col == (0,255,0):
                    col = (255,0,0)
                else:
                    col = (0,255,0)
pygame.quit()
