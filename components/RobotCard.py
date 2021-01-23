import pygame as pg
import serial

import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')


class RobotCard:
    """
    this is a icon input
    """

    def __init__(self, connection,ListOfRobots):

        self.connection = connection
        self.ListOfRobots = ListOfRobots
        self.width = 260
        self.height = 100
        self.x = 50 + 20
        self.y = len(ListOfRobots)*110

        self.rect = pg.Rect(x, y, width, height)



    def handleEvent(self, event ):
        pass



    def draw(self, screen):
        if self.connection.in_waiting:
            self.currentPosition = str(self.connection.readline().decode('ascii'))
        pg.draw.rect(screen, '#A6606D', self.rect, 1, 20)
                     
