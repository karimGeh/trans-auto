import pygame as pg
import sys
sys.path.insert(
    1, 'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')

try:
    from components.TextInput import TextInput
    from components.PasswordInput import PasswordInput
    from components.Label import Label
    from components.SubmitButton import SubmitButton
except:
    print('Something went wrong')


class LandingPage:
    USERNAME = "Admin"
    PASSWORD = "Admin"

    def __init__(self, screen, nextFunc):
        self.nextFunc = nextFunc
        self.redColor = '#C72026'
        self.grayColor = '#1D1D1D'

        self.screen = screen
        self.screen_w = screen.get_width()
        self.screen_h = screen.get_height()
        self.LogoImg = pg.image.load("./assets/logo.png")
        self.LogoX = ((self.screen_w/2) - self.LogoImg.get_width())//2
        self.LogoY = ((self.screen_h) - self.LogoImg.get_height())//2

        self.fontText = pg.font.Font(None, 25)

        self.fontTitle = pg.font.Font(None, 60)
        self.Title = Label(0, 100, self.fontTitle, text='LOGIN',
                           textColor=pg.Color(self.redColor))
        self.Title.x = self.screen_w/2 + \
            ((self.screen_w/2) - self.Title.getTextWidth())//2

        # ? Username
        self.fontUsername = pg.font.Font(None, 20)
        self.UsernameX = 600
        self.UsernameY = 250

        self.Username = Label(self.UsernameX, self.UsernameY + 5, self.fontUsername,
                              text='USERNAME :', textColor=pg.Color(self.grayColor))
        self.username = TextInput(self.UsernameX, self.UsernameY, 200, 30, self.fontText, border_radius=5,
                                  border_thikness=2, activeColor=self.redColor, inactiveColor=self.grayColor)

        # ? Password
        self.fontPassword = pg.font.Font(None, 20)
        self.PasswordX = 600
        self.PasswordY = self.UsernameY + 50

        self.Password = Label(self.PasswordX, self.PasswordY + 5, self.fontPassword,
                              text='PASSWORD :', textColor=pg.Color(self.grayColor))
        self.password = PasswordInput(self.PasswordX, self.PasswordY, 200, 30, self.fontText,
                                      border_radius=5, border_thikness=2, activeColor=self.redColor, inactiveColor=self.grayColor)

        self.password.rect.x = self.PasswordX + \
            max(self.Password.getTextWidth(), self.Username.getTextWidth()) + 10
        self.username.rect.x = self.UsernameX + \
            max(self.Password.getTextWidth(), self.Username.getTextWidth()) + 10

        # ? Submit Button

        self.fontSubmitButton = pg.font.Font(None, 20)
        self.SubmitButtonX = self.screen_w/2 + ((self.screen_w/2) - 200)//2
        self.SubmitButtonY = self.UsernameY + 100
        self.SubmitButton = SubmitButton(self.SubmitButtonX, self.SubmitButtonY, 200, 30, self.fontText,
                                         border_radius=5, border_thikness=0, textColor=self.redColor, bgColor=self.grayColor, text='LOGIN')

    def draw(self):
        self.screen.blit(self.LogoImg, (self.LogoX, self.LogoY))
        self.Title.draw(self.screen)
        self.username.draw(self.screen)
        self.password.draw(self.screen)
        self.Username.draw(self.screen)
        self.Password.draw(self.screen)
        self.SubmitButton.draw(self.screen)

    def handleEvent(self, event):
        self.username.handleEvent(event)
        self.password.handleEvent(event)
        self.SubmitButton.handleEvent(event,
                                      self.nextFunc,
                                      self.username.text == self.USERNAME and self.password.text == self.PASSWORD
                                      )
