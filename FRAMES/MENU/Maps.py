import pygame as pg
# import tkinter as tk
import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')

from components.IconButton import IconButton
from components.SubmitButton import SubmitButton
from components.Label import Label


from FRAMES.MENU.AddCardWin import AddCardWin
from FRAMES.MENU.RemoveCardWin import RemoveCardWin
from FRAMES.MENU.AddLinkWin import AddLinkWin
from FRAMES.MENU.RemoveLinkWin import RemoveLinkWin

class Maps :
    def __init__(self,screen,x,y,w,h,updateFunc,connectionToDatabase):
        self.State  ={
            'AC':False,
            'RC':False,
            'AL':False,
            'RL':False,
        }
        self.redColor = '#C72026'
        self.grayColor = '#1D1D1D'

        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.frame = pg.Rect(x, y, w, h)


        self.fontH2 = pg.font.Font(None, 50)
        self.fontH3 = pg.font.Font(None, 30)
        self.fontP = pg.font.Font(None, 20)


        self.Title = Label(60,20,self.fontH3,text='Customize Map',textColor=pg.Color(self.grayColor))
        
        self.LinksLabel = Label(60,50,self.fontH3,text='Links :',textColor=pg.Color(self.redColor))
        self.AddLink = SubmitButton(60,80,200,30,self.fontP,border_radius=5,border_thikness=0,textColor=self.redColor,bgColor=self.grayColor,text='Add Link')
        self.RemoveLink = SubmitButton(60,120,200,30,self.fontP,border_radius=5,border_thikness=0,textColor=self.redColor,bgColor=self.grayColor,text='Remove Link')
    
        self.CardsLabel = Label(60,200,self.fontH3,text='Cards :',textColor=pg.Color(self.redColor))
        self.AddCard = SubmitButton(60,230,200,30,self.fontP,border_radius=5,border_thikness=0,textColor=self.redColor,bgColor=self.grayColor,text='Add Card')
        self.RemoveCard = SubmitButton(60,270,200,30,self.fontP,border_radius=5,border_thikness=0,textColor=self.redColor,bgColor=self.grayColor,text='Remove Card')
    

        #! windows tkinter
        

        self.AC = AddCardWin(self.screen,self.State,x,y,w,h,updateFunc,connectionToDatabase) 
        self.RC = RemoveCardWin(self.screen,self.State,x,y,w,h) 
        self.AL = AddLinkWin(self.screen,self.State,x,y,w,h) 
        self.RL = RemoveLinkWin(self.screen,self.State,x,y,w,h) 
    

    def ACButtonsFunc(self):
       self.State  ={
            'AC':True,
            'RC':False,
            'AL':False,
            'RL':False,
        }
    def RCButtonsFunc(self):
       self.State  ={
            'AC':False,
            'RC':True,
            'AL':False,
            'RL':False,
        }
    def ALButtonsFunc(self):
       self.State  ={
            'AC':False,
            'RC':False,
            'AL':True,
            'RL':False,
        }
    def RLButtonsFunc(self):
       self.State  ={
            'AC':False,
            'RC':False,
            'AL':False,
            'RL':True,
        }
    

    def draw(self):
        pg.draw.rect(self.screen, "#DDDDDD", self.frame,
                     0, 0)

        self.Title.draw(self.screen)

        self.LinksLabel.draw(self.screen)
        self.AddLink.draw(self.screen)
        self.RemoveLink.draw(self.screen)
        
        self.CardsLabel.draw(self.screen)
        self.AddCard.draw(self.screen)
        self.RemoveCard.draw(self.screen)

        if self.State['AC'] :
            self.AC.draw()
        if self.State['RC'] :
            self.RC.draw()
        if self.State['AL'] :
            self.AL.draw()
        if self.State['RL'] :
            self.RL.draw()

    def handleEvent(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if not self.frame.collidepoint(event.pos):
                self.State  =   {
                                    'AC':False,
                                    'RC':False,
                                    'AL':False,
                                    'RL':False,
                                }

        if self.State['AC'] :
            self.AC.handleEvent(event)
            return
        if self.State['RC'] :
            self.RC.handleEvent(event)
            return
        if self.State['AL'] :
            self.AL.handleEvent(event)
            return
        if self.State['RL'] :
            self.RL.handleEvent(event)
            return

        self.AddCard.handleEvent(event,self.ACButtonsFunc ,True)
        self.AddLink.handleEvent(event,self.RCButtonsFunc ,True)
        
        self.RemoveCard.handleEvent(event,self.ALButtonsFunc ,True)
        self.RemoveLink.handleEvent(event,self.RLButtonsFunc ,True)