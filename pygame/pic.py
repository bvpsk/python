import pygame
screen = pygame.display.set_mode((1000,600))
pic=pygame.image.load("batman.png")
screen.blit(pic,(0,0))
pygame.display.flip()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
