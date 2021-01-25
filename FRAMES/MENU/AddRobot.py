import pygame as pg
import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')


from components.IconButton2 import IconButton2

from components.Label import Label
from components.TextInput import TextInput
from components.SubmitButton import SubmitButton

class AddRobot :
    def __init__(self,screen,state,x,y,w,h,submitFunction):
        self.ArgState = state
        self.redColor = '#C72026'
        self.grayColor = '#1D1D1D'
        self.screen = screen
        self.submitFunction =submitFunction
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.frame = pg.Rect(x, y, w, h)
        
        self.fontH2 = pg.font.Font(None, 50)
        self.fontH3 = pg.font.Font(None, 30)
        self.fontH4 = pg.font.Font(None, 25)
        self.fontP = pg.font.Font(None, 20)


        self.Title = Label(60,20,self.fontH3,text='Add Robot',textColor=pg.Color(self.grayColor))
        self.back   = IconButton2(300,
                                20,
                                30,
                                30,
                                icon = "back.png",
                                bgColor=pg.Color('#848F8B'), 
                                border_thikness=1, 
                                border_radius=10,
                                nextFunc=self.backFunction)
        self.Portlabel = Label(60, 70,self.fontH3,text='Port :',textColor=pg.Color(self.redColor))
        self.Portinput = TextInput(150, 70, 100, 30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,activeColor=self.redColor,inactiveColor=self.grayColor)
        
       
        self.addButton = SubmitButton(60, 150, 200, 30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,bgColor=self.grayColor,text='Connect To Robot')



    def backFunction(self):
        self.ArgState['AddRobot'] = False 

    def handleSubmit(self):
        if self.submitFunction : 
            self.submitFunction(self.Portinput.text)

    def draw(self):
        pg.draw.rect(self.screen, "#DDDDDD", self.frame,
                     0, 0)
        self.Title.draw(self.screen)
        self.back.draw(self.screen)
        self.Portlabel.draw(self.screen)
        self.Portinput.draw(self.screen)
        self.addButton.draw(self.screen)
                             

    def handleEvent(self,event):
        self.back.handleEvent(event)
        self.Portinput.handleEvent(event)
        self.addButton.handleEvent(event,self.handleSubmit,True)
        