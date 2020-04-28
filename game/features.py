import sys
import pygame
from settings import scr_size

pygame.init()
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
FPS = 50

def countdown(screen, i):
    count = FPS
    while count > 0:
        for event in pygame.event.get(): #getting all events like keypress, mouseclick, etc
            if event.type == pygame.QUIT:
                pygame.quit() #quitting pygame
                sys.exit() #quitting our program

        number = pygame.font.Font('freesansbold.ttf', 100)
        text = number.render(str(i), True, BLACK)
        textRect = text.get_rect()
        textRect.center = (scr_size[0]/2, scr_size[1]/2)
        screen.blit(text, textRect)

        pygame.display.update()
        clock.tick(FPS)

        count -= 1
