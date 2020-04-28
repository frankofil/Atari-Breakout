#colors
GREEN = (97, 204, 61)
BLUE = (71, 159, 214)
WHITE = (227, 209, 209)
GRAY = (55, 55, 55)

#screen
scr_size = (width, height) = (600, 400)
FPS = 50
bgColor = GRAY
colorChange = 4 #in sec

#Paddle data
class PaddleData:
    sizeX = 80
    sizeY = 13
    x = int((width-sizeX)/2)
    y = int(height-height/8)
    color = BLUE
    speed = 5

#Brick data
class BrickData:
    nBricks = 12
    margin = 2
    columns = 6
    topMarginLayer = 3
    sizeX = width/nBricks
    sizeY = height/3/columns - margin
    color = GREEN

#Ball data
class BallData:
    radius = 8
    center = [int((width-radius)/2), int(2*height/4)]
    color = WHITE
    speed = PaddleData.speed - 2
