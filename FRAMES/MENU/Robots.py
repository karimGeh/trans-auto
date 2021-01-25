import pygame as pg
import serial
import sys

sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')

from FRAMES.MENU.AddRobot import AddRobot
from components.RobotCard import RobotCard
from components.IconButton2 import IconButton2
from components.Label import Label
from components.TextInput import TextInput
from components.SubmitButton import SubmitButton

class Robots :
    def __init__(self,screen,x,y,w,h):
        self.State = {
            "AddRobot":False,
        }
        self.redColor = '#C72026'
        self.grayColor = '#1D1D1D'
        self.ListOfRobots = [] 
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.frame = pg.Rect(x, y, w, h)
        self.fontH2 = pg.font.Font(None, 50)
        self.fontH3 = pg.font.Font(None, 30)
        self.fontH4 = pg.font.Font(None, 25)
        self.fontP = pg.font.Font(None, 20)

        self.Title = Label(60,25,self.fontH3,text='Conected Robot',textColor=pg.Color(self.grayColor))
        self.Add   = IconButton2(300,
                                20,
                                30,
                                30,
                                icon = "add24.png",
                                bgColor=pg.Color('#848F8B'), 
                                border_thikness=1, 
                                border_radius=10,
                                nextFunc=self.AddRobotMenu)
        
        self.ADDRobot = AddRobot(self.screen,self.State,x,y,w,h,self.AddRobotFunction)
        



    def AddRobotMenu(self):
        self.State['AddRobot']  = True

    def AddRobotFunction(self,COMPORT):
        try:
            connection = serial.Serial(COMPORT, 9600)
            robot = RobotCard(connection,self.ListOfRobots,COMPORT)
            self.ListOfRobots.append(robot)
        except Exception as e:
            print("Unexpected error:", e)
            print("ERROR CONNECTING TO THIS DEVICE")
            return

    def handleEvent(self,event):
        if(self.State['AddRobot']):
            self.ADDRobot.handleEvent(event)
            return
        
        self.Add.handleEvent(event)


    def draw(self):
        if(self.State['AddRobot']):
            self.ADDRobot.draw()
            return
        pg.draw.rect(self.screen, "#DDDDDD", self.frame, 0, 0)

        
        self.Title.draw(self.screen)        
        self.Add.draw(self.screen)

        # print(len(self.ListOfRobots))
        for robot in self.ListOfRobots :
            robot.draw(self.screen)