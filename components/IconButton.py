import pygame as pg

import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')


class IconButton:
    """
    this is a icon input
    """

    def __init__(self, x, y, width, height,State={},key='', icon="logo.png", textColor=pg.Color('#000000'), bgColor=pg.Color('#FFFFFF'), border_thikness=0, border_radius=0):

        self.width = width
        self.height = height
        self.rect = pg.Rect(x, y, width, height)
        self.active = False
        self.icon = pg.image.load("./assets/" + icon)

        #!  Colors
        self.buttonColor = bgColor
        self.x = x
        self.y = y

        self.State = State
        self.key=key

        #! box sdts
        self.border_thikness = border_thikness
        self.border_radius = border_radius

    def handleEvent(self, event , wm ,w):
        

        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.State[self.key] = not self.State[self.key] 
            elif wm> event.pos[0] or event.pos[0] > w :
                self.State[self.key] = False
                
        

    def draw(self, screen):
        pg.draw.rect(screen, self.buttonColor, self.rect,
                     self.border_thikness, self.border_radius)
        screen.blit(self.icon,(self.x+4,self.y+4))
                     
