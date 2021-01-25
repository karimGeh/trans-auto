import pygame as pg
import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')


from components.IconButton import IconButton

from components.Label import Label
from components.TextInput import TextInput
from components.SubmitButton import SubmitButton

class AddLinkWin :
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


        self.Title = Label(60,20,self.fontH3,text='Add Link To Map',textColor=pg.Color(self.grayColor))
        
        self.descLabel = Label(60, 50,self.fontP,text='ID of CARDS :',textColor=pg.Color(self.grayColor))

        self.Id1label = Label(60, 70,self.fontH3,text='ID 1',textColor=pg.Color(self.redColor))
        self.Id1input = TextInput(100, 70, 100, 30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,activeColor=self.redColor,inactiveColor=self.grayColor)
        
        self.Id2Label = Label(60, 110,self.fontH3,text='ID 2',textColor=pg.Color(self.redColor))
        self.Id2input = TextInput(100, 110, 100, 30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,activeColor=self.redColor,inactiveColor=self.grayColor)
        
        self.addButton = SubmitButton(60, 150, 200, 30,self.fontP,border_radius=5,border_thikness=2,textColor=self.redColor,bgColor=self.grayColor,text='Add Link')



    def draw(self):
        pg.draw.rect(self.screen, "#DDDDDD", self.frame,
                     0, 0)
        
        self.Id1label.draw(self.screen)
        self.Id1input.draw(self.screen)

        self.Id2Label.draw(self.screen)
        self.Id2input.draw(self.screen)

        self.Title.draw(self.screen)
        self.descLabel.draw(self.screen)
        self.addButton.draw(self.screen)

    def handleSubmit(self):
        id1 = int(self.Id1input.text)
        id2 = int(self.Id2input.text)

        if (
            not (str(id1) and str(id2))
        ):
            print('conditions not satisfied ')
            return 

        Cards = self.connectionToDatabase.ReadAllRFID()
        Links = self.connectionToDatabase.ReadAllLINK()

        graphicCards = {}
        
        for card in Cards:
            graphicCards[card['id']] =  {
                                            'id':card['id'],
                                            'code':card['code'],
                                            'x': card['x'],
                                            'y': card['y'],
                                        }
                                        
        if id1 not in graphicCards or id2 not in graphicCards or id1 == id2:
            print('one of your ids does not exist in the database')
            return 
        
        if graphicCards[id1]['x'] != graphicCards[id2]['x'] and graphicCards[id1]['y'] != graphicCards[id2]['y'] :
            print('you can not link those two cards for geometrique reasons')
            return

        if (
            any( link["first_end"] == id1 and link["second_end"] == id2 for link in Links) or
            any( link["first_end"] == id2 and link["second_end"] == id1 for link in Links)
        ) :
            print("link already exist")
            return
        
        self.connectionToDatabase.CreateLINK(id1,id2)
        self.Id1input.updateText('')
        self.Id2input.updateText('')
        self.updateFunc()



    def handleEvent(self,event):
        self.Id1input.handleEvent(event)
        self.Id2input.handleEvent(event)
        self.addButton.handleEvent(event,self.handleSubmit,True)