import pygame as pg
import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')


from components.IconButton import IconButton

from components.Label import Label
from components.TextInput import TextInput
from components.SubmitButton import SubmitButton

class RemoveCardWin :
    def __init__(self,screen,state,x,y,w,h,updateFunc,connectionToDatabase):
        self.redColor = '#C72026'
        self.grayColor = '#1D1D1D'
        self.screen = screen
        self.connectionToDatabase =connectionToDatabase
        self.updateFunc = updateFunc
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.frame = pg.Rect(x, y, w, h)
        
        self.fontH2 = pg.font.Font(None, 50)
        self.fontH3 = pg.font.Font(None, 30)
        self.fontH4 = pg.font.Font(None, 25)
        self.fontP = pg.font.Font(None, 20)


        self.Title = Label(60,20,self.fontH3,text='Remove Card from Map',textColor=pg.Color(self.grayColor))
        
        self.idLabel = Label(60,50,self.fontH4,text='id :',textColor=pg.Color(self.redColor))
        self.idInput = TextInput(90,50,100,30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,activeColor=self.redColor,inactiveColor=self.grayColor)
        
        self.posLabel = Label(60,100,self.fontP,text='Position :',textColor=pg.Color(self.grayColor))

        self.Xlabel = Label(60,125,self.fontH3,text='X',textColor=pg.Color(self.redColor))
        self.Xinput = TextInput(90,120,100,30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,activeColor=self.redColor,inactiveColor=self.grayColor)
        
        self.YLabel = Label(60,165,self.fontH3,text='Y',textColor=pg.Color(self.redColor))
        self.Yinput = TextInput(90,160,100,30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,activeColor=self.redColor,inactiveColor=self.grayColor)
        
        self.addButton = SubmitButton(60, 200,200,30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,bgColor=self.grayColor,text='Remove Card')



    def draw(self):
        pg.draw.rect(self.screen, "#DDDDDD", self.frame,
                     0, 0)
        self.idInput.draw(self.screen)
        self.Xinput.draw(self.screen)
        self.Yinput.draw(self.screen)

        self.Title.draw(self.screen)
        self.idLabel.draw(self.screen)
        self.posLabel.draw(self.screen)
        self.Xlabel.draw(self.screen)
        self.YLabel.draw(self.screen)
        self.addButton.draw(self.screen)

    def handleSubmit(self):
        id = self.idInput.text.strip()
        x = self.Xinput.text
        y = self.Yinput.text

        if (
            not (str(x) and str(y)) and not (str(id))
        ):
            print('conditions not satisfied')
            return 

        
        Cards = self.connectionToDatabase.ReadAllRFID()
        Links = self.connectionToDatabase.ReadAllLINK()
        
        if  all( str(card['id']) != str(id) for card in Cards) :
            print('card does not exist')
            return

        if any( str(id) in [str(link['first_end']), str(link['second_end'])] for link in Links):
            print('card cant be removed for links purposes')
            return
        
        for card in Cards :
            if str(card['id']) == str(id) :
                self.connectionToDatabase.DeleteRFID(card['code'])
                break
            
            if str(card['x']) == str(x) and str(card['y']) == str(y) :
                self.connectionToDatabase.DeleteRFID(card['code'])
                break
            

        self.idInput.updateText('')
        self.Xinput.updateText('')
        self.Yinput.updateText('')
        self.updateFunc()




    def handleEvent(self,event):
        self.idInput.handleEvent(event)
        self.Xinput.handleEvent(event)
        self.Yinput.handleEvent(event)
        self.addButton.handleEvent(event,self.handleSubmit,True)