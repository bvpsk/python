import pygame
screen = pygame.display.set_mode((1000,600))
back = (255,255,255)
run = True
class Circles:
    def __init__(self,(x,y)):
        self.x = x
        self.y = y
    
while run:
    screen.fill(back)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
