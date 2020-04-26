#colors
__color__ = [red, green, blue, yellow, black, white, gray] = [(255, 0, 0), (97, 204, 61), (71, 159, 214), (255, 255, 0), (0, 0, 0), (227, 209, 209), (60, 60, 60)]

#screen
scr_size = (width, height) = (600, 400)
FPS = 50
bgColor = gray
colorChange = 5

#Paddle data
class PaddleData:
    sizeX = 80
    sizeY = 13
    x = (width-sizeX)/2
    y = height-height/8
    color = blue
    speed = 5

#Brick data
class BrickData:
    nBricks = 12
    margin = 2
    columns = 6
    topMarginLayer = 3
    sizeX = width/nBricks
    sizeY = height/3/columns - margin
    color = green

#Ball data
class BallData:
    radius = 8
    center = [int((width-radius)/2), int(2*height/3)]
    color = white
    speed = PaddleData.speed - 2
