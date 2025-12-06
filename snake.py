import pygame

import random
import time
pygame.mixer.init()
pygame.init()
#genrate colors
White=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

#create variables
width=626
hight=313
start_x=45
start_y=45
size=15
update_x=0
update_y=0
FPS=5
snakelen=1
list=[]

def music1():
    pygame.mixer.music.load("alien.mp3.wav")
    pygame.mixer.music.play()

def snake_length(list,size):
    for XnY in list:
        pygame.draw.rect(gameWindow, green, [XnY[0], XnY[1], size, size])
gameWindow=pygame.display.set_mode((width,hight))

pygame.display.set_caption("My Game")

gameClose=False

clk=pygame.time.Clock()

food_x=round(random.randrange(0,width-size)/15.0)*15.0
food_y=round(random.randrange(0,hight-size)/15.0)*15.0
font = pygame.font.SysFont(None,50)
background=pygame.image.load("my.png")
icon=pygame.image.load("icons.jpg")
pygame.display.set_icon(icon)

def msg_txt(msg,color):
    screen_text=font.render(msg,True,color)
    gameWindow.blit(screen_text,[width/3,hight/2])

while not gameClose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameClose=True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                update_x=+15
                update_y=0

            if event.key == pygame.K_LEFT:
                update_x=-15
                update_y=0

            if event.key == pygame.K_UP:
                update_y=-15
                update_x=0

            if event.key == pygame.K_DOWN:
                update_y=+15
                update_x=0

    start_x+=update_x
    start_y+=update_y
    gameWindow.blit(background,[0,0])

    if start_x > width-12 or start_y > hight-12 or width+start_x < width or hight+start_y < hight:
        gameClose=True
    pygame.draw.rect(gameWindow, red, [food_x, food_y, size, size])
    pygame.draw.rect(gameWindow, green, [start_x, start_y, size, size])

    if start_x == food_x and start_y == food_y:
        food_x = round(random.randrange(0, width-size)/15.0)*15.0
        food_y = round(random.randrange(0, hight-size)/15.0)*15.0
        snakelen=snakelen+1
    music1()
    snake_length(list,size)
    head=[]
    head.append(start_x)
    head.append(start_y)
    list.append(head)
    if len(list)==snakelen:
        del list[0]

    pygame.display.update()

    clk.tick(FPS)
msg_txt("Game over",red)
pygame.display.update()
time.sleep(5)

pygame.display.quit()

quit()