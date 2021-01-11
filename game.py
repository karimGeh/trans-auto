import pygame as pg

from components.TextInput import TextInput
from pages.LandingPage import LandingPage 


#! initialize the game
pg.init()


#! create screen
screen = pg.display.set_mode((1000, 600))
icon = pg.image.load("./assets/logo.jpg")


pg.display.set_caption("Trans-Auto")
pg.display.set_icon(icon)



def nextFunc():
    global currentFrame
    currentFrame += 1


#! Game Loop

frame1 = LandingPage(screen,nextFunc)
running = True

FRAMES = [frame1]
currentFrame = 0

while running:
    screen.fill((255, 255, 255))

    for e in pg.event.get():
        frame1.handleEvent(e)
        if e.type == pg.QUIT:
            running = False

    
    FRAMES[currentFrame].draw()
    pg.display.update()



