import pygame as pg


class Label:
    """
    this is a Title/text
    """

    def __init__(self, x, y, font, text='',textColor=pg.Color('#000000')):

        self.x = x
        self.y = y
        self.text = text

        #!  Colors
        self.textColor = textColor
        self.font = font
        self.Text_screen = self.font.render(self.text, True, self.textColor)


    def updateText(self, text: str):
        self.text = text
        self.Text_screen = self.font.render(self.text, True, self.textColor)
    
    def getTextWidth(self):
        return self.Text_screen.get_width()
    
    def draw(self, screen):
        screen.blit(self.Text_screen, (self.x, self.y))
