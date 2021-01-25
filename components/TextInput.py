import pygame as pg


class TextInput:
    """
    this is a text input
    """

    def __init__(self, x, y, width, height, font, text='', inactiveColor=pg.Color('#000000'), activeColor=pg.Color('#00FF00'), textColor=pg.Color('#000000'), border_thikness=1, border_radius=0):

        self.width = width
        self.height = height
        self.text = text
        self.rect = pg.Rect(x, y, width, height)
        self.active = False

        #!  Colors
        self.activeColor = activeColor
        self.textColor = textColor
        self.inactiveColor = inactiveColor
        self.font = font
        self.txt_surface = self.font.render(text, True, self.textColor)

        #! box sdts
        self.border_thikness = border_thikness
        self.border_radius = border_radius

    def handleEvent(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        self.textColor = self.activeColor if self.active else self.inactiveColor
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_KP_ENTER or event.key == 13 :
                    self.text += '\n'
                    return
                if event.key == pg.K_RETURN or event.key == pg.K_ESCAPE:
                    pass
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
        self.txt_surface = self.font.render(
            self.text, True, self.textColor)

    def updateText(self, text: str):
        self.text = text

    def draw(self, screen):
        lines = self.text.splitlines()
        for i, l in enumerate(lines):
            screen.blit(self.font.render(l, True, self.textColor), (self.rect.x+5, self.rect.y+5 + 10*i))
        pg.draw.rect(screen, self.textColor, self.rect,
                     self.border_thikness, self.border_radius)
