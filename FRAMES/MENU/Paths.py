import pygame as pg
import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')


from FRAMES.MENU.AddPath import AddPath

from components.IconButton2 import IconButton2
from components.Label import Label
from components.TextInput import TextInput
from components.SubmitButton import SubmitButton

class Paths :
    def __init__(self,screen,x,y,w,h):
        self.PATHS = {}
        
        self.State = {
            "AddPath":False,
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
        self.fontH4 = pg.font.Font(None, 25)
        self.fontP = pg.font.Font(None, 20)


        self.Title = Label(60,25,self.fontH3,text='Current Paths',textColor=pg.Color(self.grayColor))
        self.Add   = IconButton2(300,
                                20,
                                30,
                                30,
                                icon = "add24.png",
                                bgColor=pg.Color('#848F8B'), 
                                border_thikness=1, 
                                border_radius=10,
                                nextFunc=self.AddPathMenu)
        self.ADDPath = AddPath(self.screen,self.State,x,y,w,h,self.AddPathFunction)




    def AddPathMenu(self):
        self.State['AddPath']  = True

    def AddPathFunction(self,CODE,ListOfAvailableRobots,ListOfAvailableCards):
        # print(ListOfAvailableRobots)
        ListCommands = CODE.splitlines()
        if not len(ListCommands) :
            return
        
        if any(len(commandLine.split()) != 2 for commandLine in ListCommands):
            print('SYNTAXE ERROR')
            return


        if ListCommands[0].split()[0] != "ROBOT" or any(commandLine.split()[1] not in ['R','L','N','S'] for commandLine in ListCommands[1:-1]):
            print('SYNTAXE ERROR')
            return


        if all(str(robot.id) != str(ListCommands[0].split()[1]) for robot in ListOfAvailableRobots) :
            print("ROBOT " + ListCommands[0].split()[1] + " not found")
            return 

        ListOfAvailableCards = map(lambda card : card['id'],ListOfAvailableCards)

        if any( int(command.split()[0]) not in ListOfAvailableCards for command in ListCommands[1:-1]) :
            print("A CARD ID NOT IN MAP")
            return 
        
        if ListCommands[0].split()[1] in self.PATHS :
            print("ROBOT CURRENTLY IN A PATH")
            return 
        
        for r in ListOfAvailableRobots :
            if str(r.id) == ListCommands[0].split()[1] :
                robot = r
                break
        # robot = filter(lambda robot : str(robot.id) == ListCommands[0].split()[1], ListOfAvailableRobots)

        self.PATHS[robot.id] = ListCommands

        robot.connection.write(bytearray(str("B"), "utf8"))


          

        

    def handleEvent(self,event,*args):
        if(self.State['AddPath']):
            self.ADDPath.handleEvent(event,*args)
            return
        
        self.Add.handleEvent(event)

    def draw(self):
        if(self.State['AddPath']):
            self.ADDPath.draw()
            return

        pg.draw.rect(self.screen, "#DDDDDD", self.frame,
                     0, 0)
        self.Title.draw(self.screen)        
        self.Add.draw(self.screen)