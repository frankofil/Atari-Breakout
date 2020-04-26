import sys
from random import randint
import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick
import features
from settings import (scr_size, FPS, bgColor, PaddleData, BallData, BrickData)

#Useful colors
RED = (255, 0, 0)
GREEN = (97, 204, 61)
BLUE = (71, 159, 214)
WHITE = (227, 209, 209)
BLACK = (0, 0, 0)
GRAY = (60, 60, 60)
YELLOW = (255, 255, 0)

lives = 3
score = 0

def hearts(screen, i):
    heartMargin = 18
    if i == 3:
        pygame.draw.circle(screen, RED, [587, heartMargin], 8)
        pygame.draw.circle(screen, RED, [566, heartMargin], 8)
        pygame.draw.circle(screen, RED, [545, heartMargin], 8)
    elif i == 2:
        pygame.draw.circle(screen, RED, [587, heartMargin], 8)
        pygame.draw.circle(screen, RED, [566, heartMargin], 8)
    elif i == 1:
        pygame.draw.circle(screen, RED, [587, heartMargin], 8)


def main():
    pygame.init()

    #screen
    screen = pygame.display.set_mode(scr_size) #creating screen
    pygame.display.set_caption('Breakout')
    clock = pygame.time.Clock()

    all_sprites_list = pygame.sprite.Group()

    global lives
    global score
    counter = 0
    gameOver = False

    #countdown
    screen.fill(bgColor)
    features.countdown(screen, 3)
    screen.fill(bgColor)
    features.countdown(screen, 2)
    screen.fill(bgColor)
    features.countdown(screen, 1)

    screen.fill(bgColor)

    #Create the Paddle
    paddle = Paddle()
    paddle.rect.x = PaddleData.x
    paddle.rect.y = PaddleData.y

    #Create a ball
    ball = Ball(2*BallData.radius, 2*BallData.radius)
    ball.rect.x = BallData.center[0] - BallData.radius
    ball.rect.y = BallData.center[1] - BallData.radius

    #Create bricks
    all_brick = pygame.sprite.Group()
    for y in range(BrickData.columns):
        for x in range(0, scr_size[0], int(BrickData.sizeX)):
            brick = Brick()
            brick.rect.x = x + BrickData.margin
            brick.rect.y = int(BrickData.sizeY) * (y + BrickData.topMarginLayer) + BrickData.margin
            all_sprites_list.add(brick)
            all_brick.add(brick)

    all_sprites_list.add(paddle)
    all_sprites_list.add(ball)

    while not gameOver:
        #Changing colors every 5 seconds
        counter += 1
        #if counter == FPS*colorChange:
         #   counter = 0
          #  nBricks = len(bricks)
           # for i in range(nBricks):
            #    bricks[i].pick_random_color()

        #Handling user input
        for event in pygame.event.get(): #getting all events like keypress, mouseclick, etc
            if event.type == pygame.QUIT:
                gameOver = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.moveLeft()
        if keys[pygame.K_RIGHT]:
            paddle.moveRight()


        ball.walls()
        if ball.bottom_line():
            lives -= 1
            if lives == 0:
                screen.fill(bgColor)
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, BLACK)
                screen.blit(text, (130, 130))

                font = pygame.font.Font(None, 60)
                text = font.render("Score: " + str(score), 1, BLACK)
                screen.blit(text, (180, 210))
                pygame.display.flip()
                counterEnd = 0
                while counterEnd <= 150:
                    counterEnd += 1
                    for event in pygame.event.get(): #getting all events like keypress, mouseclick, etc
                        if event.type == pygame.QUIT:
                            pygame.quit() #quitting pygame
                            sys.exit() #quitting our program
                    clock.tick(FPS)
                gameOver = True
                pygame.quit() #quitting pygame
                sys.exit()
            main()

        #Collision with Paddle
        if paddle.rect.colliderect(ball.rect):
            if ball.movement[1] < 0:
                ball.movement[1] *= -1

        #Collision with bricks
        brick_collison_list = pygame.sprite.spritecollide(ball, all_brick, False)
        for brick in brick_collison_list:
            if ball.movement[1] > 0:
                ball.movement[1] *= -1
            if brick.color == (40, 40, 40):
                score += 100
                ball.speed += 1
                paddle.speed += 1
            else:
                score += 20
            brick.kill()
            if len(all_brick) == 0:
                score += 500

                screen.fill(bgColor)
                font = pygame.font.Font(None, 74)
                text = font.render("LEVEL COMPLETE", 1, BLACK)
                screen.blit(text, (135, 165))

                font = pygame.font.Font(None, 60)
                text = font.render("Score: " + str(score), 1, BLACK)
                screen.blit(text, (215, 250))

                while counterEnd <= 150:
                    counterEnd += 1
                    for event in pygame.event.get(): #getting all events like keypress, mouseclick, etc
                        if event.type == pygame.QUIT:
                            pygame.quit() #quitting pygame
                            sys.exit() #quitting our program
                    clock.tick(FPS)

                main()

        all_sprites_list.update()
        #Drawing code
        screen.fill(bgColor)
        hearts(screen, lives)
        #Score
        font = pygame.font.Font(None, 40)
        text = font.render(str(score), 1, WHITE)
        screen.blit(text, (20, 7))
        #All sprites
        all_sprites_list.draw(screen)
        pygame.draw.line(screen, WHITE, [0, 35], [800, 35], 2)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit() #quitting pygame
    sys.exit() #quitting our program


if __name__ == '__main__':
    main()