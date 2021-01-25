import pygame as pg
import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')


from components.IconButton2 import IconButton2

from components.Label import Label
from components.TextInput import TextInput
from components.SubmitButton import SubmitButton

class AddPath :
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


        self.Title = Label(60,20,self.fontH3,text='Add Path',textColor=pg.Color(self.grayColor))
        self.back   = IconButton2(300,
                                20,
                                30,
                                30,
                                icon = "back.png",
                                bgColor=pg.Color('#848F8B'), 
                                border_thikness=1, 
                                border_radius=10,
                                nextFunc=self.backFunction)
        self.Codelabel = Label(60, 70,self.fontH3,text='Code :',textColor=pg.Color(self.redColor))
        self.Codeinput = TextInput(75, 100, 250, self.h - 200 ,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,activeColor=self.redColor,inactiveColor=self.grayColor)
        
       
        self.addButton = SubmitButton(75, self.h - 50, 250, 30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,bgColor=self.grayColor,text='Execute The Path')



    def backFunction(self):
        self.ArgState['AddPath'] = False 

    def handleSubmit(self,*args):
        if self.submitFunction : 
            self.submitFunction(self.Codeinput.text,*args)

    def draw(self):
        pg.draw.rect(self.screen, "#DDDDDD", self.frame,
                     0, 0)
        self.Title.draw(self.screen)
        self.back.draw(self.screen)
        self.Codelabel.draw(self.screen)
        self.Codeinput.draw(self.screen)
        self.addButton.draw(self.screen)
                             

    def handleEvent(self,event,*args):
        self.back.handleEvent(event)
        self.Codeinput.handleEvent(event)
        self.addButton.handleEvent(event,self.handleSubmit,True,*args)
        