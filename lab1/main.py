import sys
import pygame
import t1

pygame.init()

screen = pygame.display.set_mode((1200, 800))
color = (255, 255, 255)
screen.fill(color)

t1.task11(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
