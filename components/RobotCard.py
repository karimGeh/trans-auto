import pygame as pg
import serial

import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')

from components.Label import Label

class RobotCard:
    """
    this is a icon input
    """

    def __init__(self, connection,ListOfRobots,Port):
        self.position = None
        self.id = Port[-1]
        self.redColor = '#C72026'
        self.grayColor = '#1D1D1D'
        self.greenColor = '#80FF00'
        self.whiteColor = '#ffffff'
        self.connection = connection
        self.ListOfRobots = ListOfRobots
        self.width = 260
        self.height = 70
        self.x = 50 + 20
        self.y = len(ListOfRobots)*110 + 70

        self.icon = pg.image.load("./assets/robot.png")
        self.icon = pg.transform.scale(self.icon, (40, 40))

        self.fontH2 = pg.font.Font(None, 50)
        self.fontH3 = pg.font.Font(None, 30)
        self.fontH4 = pg.font.Font(None, 25)
        self.fontP = pg.font.Font(None, 20)
        
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)


        self.Status = Label(self.x +70, self.y + 10,self.fontH3,text='Conected',textColor=pg.Color(self.greenColor))
        self.IdLabel = Label(self.x +70, self.y + 35,self.fontP,text=self.id,textColor=pg.Color(self.whiteColor))
        self.PortLabel = Label(self.x +70, self.y + 50,self.fontP,text='Port : COM' + str(self.id),textColor=pg.Color(self.whiteColor))


    def handleEvent(self, event ):
        pass



    def draw(self, screen):
        pg.draw.rect(screen, '#002040', self.rect,0, 20)
        screen.blit(self.icon,(self.x+10,self.y+ (self.height - 32)//2))
        self.Status.draw(screen)
        self.IdLabel.draw(screen)
        self.PortLabel.draw(screen)
                     
