import random
import pygame
from settings import BrickData

BLACKK = (0, 0, 0)

__color__ = [
    RED, GREEN, BLUE, YELLOW, PURPLE, PINK, LIGHTBLUE, WHITE, BLACK] = [
        (227, 48, 48), (97, 204, 61), (63, 89, 235), (209, 166, 46),
        (151, 66, 255), (230, 34, 230), (29, 219, 197), (227, 209, 209), (40, 40, 40)]
nColors = len(__color__)

class Brick(pygame.sprite.Sprite):
    def __init__(self, width=BrickData.sizeX-BrickData.margin, height=BrickData.sizeY-BrickData.margin):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACKK)
        self.image.set_colorkey(BLACKK)
        self.color = __color__[random.randint(0, nColors-1)]

        pygame.draw.rect(self.image, self.color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def pick_random_color(self):
        self.color = __color__[random.randint(0, nColors-1)]
