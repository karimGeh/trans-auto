import pygame as pg
import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')


from components.IconButton import IconButton

from components.Label import Label
from components.TextInput import TextInput
from components.SubmitButton import SubmitButton

class AddCardWin :
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


        self.Title = Label(60,20,self.fontH3,text='Add Card To Map',textColor=pg.Color(self.grayColor))
        
        self.codeLabel = Label(60,50,self.fontH4,text='Code de la cart :',textColor=pg.Color(self.redColor))
        self.codeInput = TextInput(60,80,200,30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,activeColor=self.redColor,inactiveColor=self.grayColor)
        
        self.posLabel = Label(60,150,self.fontP,text='Position :',textColor=pg.Color(self.grayColor))

        self.Xlabel = Label(60,175,self.fontH3,text='X',textColor=pg.Color(self.redColor))
        self.Xinput = TextInput(80,170,200,30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,activeColor=self.redColor,inactiveColor=self.grayColor)
        
        self.YLabel = Label(60,215,self.fontH3,text='Y',textColor=pg.Color(self.redColor))
        self.Yinput = TextInput(80,210,200,30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,activeColor=self.redColor,inactiveColor=self.grayColor)
        
        self.addButton = SubmitButton(60, 250,200,30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,bgColor=self.grayColor,text='Add Card')



    def draw(self):
        pg.draw.rect(self.screen, "#DDDDDD", self.frame,
                     0, 0)
        self.codeInput.draw(self.screen)
        self.Xinput.draw(self.screen)
        self.Yinput.draw(self.screen)

        self.Title.draw(self.screen)
        self.codeLabel.draw(self.screen)
        self.posLabel.draw(self.screen)
        self.Xlabel.draw(self.screen)
        self.YLabel.draw(self.screen)
        self.addButton.draw(self.screen)

    def handleSubmit(self):
        code = self.codeInput.text.strip()
        x = int(self.Xinput.text)
        y = int(self.Yinput.text)

        if (
            not (str(x) and str(y) and 
            all(0<len(i) and len(i)<4 for i in code.split() ))
        ):
            print('conditions not satisfied ')
            return 

        
        Cards = self.connectionToDatabase.ReadAllRFID()
        
        if any( card['code'] == code for card in Cards) :
            print('card already existing')
            return

        if any( (int(card['x']) == x and int(card['y']) == y ) for card in Cards):
            print('position already occupied')
            return
        
        self.connectionToDatabase.CreateRFID(code,int(x),int(y))
        self.codeInput.updateText('')
        self.Xinput.updateText('')
        self.Yinput.updateText('')
        self.updateFunc()




    def handleEvent(self,event):
        self.codeInput.handleEvent(event)
        self.Xinput.handleEvent(event)
        self.Yinput.handleEvent(event)
        self.addButton.handleEvent(event,self.handleSubmit,True)