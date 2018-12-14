import pygame
from random import randint as r
screen = pygame.display.set_mode((600,600))
back = (255,255,255)
run = True
while run:
    screen.fill(back)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x=r(0,255)
            y=r(0,255)
            z=r(0,255)
            back = (x,y,z)
pygame.quit()
