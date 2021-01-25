import pygame as pg
import os

from DATABASE.DatabaseConnection import DatabaseConnection

from pages.LandingPage import LandingPage 
from pages.Dashboard import Dashboard 


os.environ['SDL_VIDEO_CENTERED'] = '1'

#! connecting to database
connectionToDatabase = DatabaseConnection()

#! initialize the game
pg.init()


info = pg.display.Info()
screen_width,screen_height = info.current_w,info.current_h

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
dashboard = Dashboard(screen,nextFunc,screen_width,screen_height,connectionToDatabase)
running = True

FRAMES = [frame1,dashboard]
currentFrame = 1


while running:
    screen.fill((255, 255, 255))
    

    for e in pg.event.get():
        FRAMES[currentFrame].handleEvent(e)
        
        if e.type == pg.QUIT:
            running = False

    
    FRAMES[currentFrame].draw()
    pg.display.update()
    pg.time.Clock().tick(60)



