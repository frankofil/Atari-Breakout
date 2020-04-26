import pygame
from settings import PaddleData, scr_size

BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color=PaddleData.color, width=PaddleData.sizeX, height=PaddleData.sizeY):
        #Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        self.speed = PaddleData.speed

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def moveLeft(self):
        self.rect.x -= self.speed
        #Check that you are not going too far (off the screen)
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self):
        self.rect.x += self.speed
        #Check that you are not going too far (off the screen)
        if self.rect.x + PaddleData.sizeX > scr_size[0]:
            self.rect.x = scr_size[0] - PaddleData.sizeX
