from random import randint
import pygame
from settings import BallData, scr_size

BLACK = (0, 0, 0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, width, height, color=BallData.color):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        while True:
            self.movement = [randint(-1, 1), -1]
            if self.movement[0] != 0:
                break

        self.speed = BallData.speed

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.movement[0] * self.speed
        self.rect.y -= self.movement[1] * self.speed

    def walls(self):
        if self.rect.x + 2 * BallData.radius >= scr_size[0] or self.rect.x <= 0:
            self.movement[0] *= -1
        if self.rect.y < 37:
            self.movement[1] *= -1

    def bottom_line(self):
        if self.rect.y + 2 * BallData.radius > scr_size[1]:
            return True
            