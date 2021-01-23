import pygame as pg

import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')


class IconButton2:
    """
    this is a icon input
    """

    def __init__(self, x, y, width, height,nextFunc, icon="logo.png", textColor=pg.Color('#000000'), bgColor=pg.Color('#FFFFFF'), border_thikness=0, border_radius=0):

        self.width = width
        self.height = height
        self.rect = pg.Rect(x, y, width, height)
        self.active = False
        self.icon = pg.image.load("./assets/" + icon)

        #!  Colors
        self.buttonColor = bgColor
        self.x = x
        self.y = y

        self.nextFunc = nextFunc

        #! box sdts
        self.border_thikness = border_thikness
        self.border_radius = border_radius

    def handleEvent(self, event):
        

        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.nextFunc :
                    self.nextFunc()
                
        

    def draw(self, screen):
        pg.draw.rect(screen, self.buttonColor, self.rect,
                     self.border_thikness, self.border_radius)
        screen.blit(self.icon,(self.x+4,self.y+4))
                     
