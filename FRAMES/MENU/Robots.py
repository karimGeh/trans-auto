import pygame as pg
import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')


from components.RobotCard import RobotCard

class Robots :
    def __init__(self,screen,x,y,w,h):
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.frame = pg.Rect(x, y, w, h)

        self.ListOfRobots = []

    def AddRobot(self,COMPORT):
        try:
            connection = serial.Serial(COMPORT, 9600)
            robot = RobotCard(connection,ListOfRobots)
            ListOfRobots.append(robot)
        except :
            print("ERROR CONNECTING TO THIS DEVICE")
            return

    def draw(self):
        pg.draw.rect(self.screen, "#DDDDDD", self.frame, 0, 0)
        for robot in self.ListOfRobots :
            robot.draw()