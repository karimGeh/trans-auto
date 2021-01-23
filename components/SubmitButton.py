import pygame as pg


class SubmitButton:
    """
    this is a text input
    """

    def __init__(self, x, y, width, height, font, text='', textColor=pg.Color('#000000'), bgColor=pg.Color('#00FF00'), border_thikness=0, border_radius=0):

        self.width = width
        self.height = height
        self.text = text
        self.rect = pg.Rect(x, y, width, height)
        self.active = False

        #!  Colors
        # self.activeColor = activeColor
        # self.inactiveColor = inactiveColor
        self.textColor = textColor
        self.buttonColor = bgColor
        self.font = font
        self.txt_surface = self.font.render(text, True, self.textColor)

        #! box sdts
        self.border_thikness = border_thikness
        self.border_radius = border_radius

    def handleEvent(self, event , nextFunc , argument):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and argument:
                nextFunc()
                return
            elif self.rect.collidepoint(event.pos) and not argument:
                return
                

    def updateText(self, text: str):
        self.text = text

    def draw(self, screen):
        pg.draw.rect(screen, self.buttonColor, self.rect,
                     self.border_thikness, self.border_radius)
        screen.blit(self.txt_surface, (self.rect.x+(self.width-self.txt_surface.get_width())//2, self.rect.y+(self.height-self.txt_surface.get_height())//2))
