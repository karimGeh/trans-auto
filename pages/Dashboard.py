import pygame as pg
import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')


from components.IconButton import IconButton
from FRAMES.MENU.Robots import Robots
from FRAMES.MENU.Maps import Maps
from FRAMES.MENU.Paths import Paths
from FRAMES.MENU.Settings import Settings
from FRAMES.MAP.Map import Map


class Dashboard :
    MENU_WIDTH=50
    ICON_WIDTH=40
    def __init__(self, screen, nextFunc ,screen_width,screen_height,connectionToDatabase):
        self.STATE = {
            "robot":False,
            "paths":False,
            "mapCustomize":False,
            "settings":False,
        }

        self.connectionToDatabase = connectionToDatabase
        self.nextFunc  = nextFunc
        self.redColor  = '#C72026'
        self.grayColor = '#1D1D1D'

        self.screen = screen
        self.screen_w = screen.get_width()
        self.screen_h = screen.get_height()

        self.robot = IconButton(int((self.MENU_WIDTH - self.ICON_WIDTH) / 2),
                                10,
                                self.ICON_WIDTH,
                                self.ICON_WIDTH,
                                icon = "robotIcon.png",
                                bgColor=pg.Color('#848F8B'), 
                                border_thikness=2, 
                                border_radius=10,
                                State = self.STATE,
                                key='robot' )

        self.paths = IconButton(int((self.MENU_WIDTH - self.ICON_WIDTH) / 2),
                                60,
                                self.ICON_WIDTH,
                                self.ICON_WIDTH,
                                icon = "pathway.png",
                                bgColor=pg.Color('#848F8B'), 
                                border_thikness=2, 
                                border_radius=10,
                                State = self.STATE,
                                key='paths' )

        self.map = IconButton(int((self.MENU_WIDTH - self.ICON_WIDTH) / 2),
                                110,
                                self.ICON_WIDTH,
                                self.ICON_WIDTH,
                                icon = "map.png",
                                bgColor=pg.Color('#848F8B'), 
                                border_thikness=2, 
                                border_radius=10,
                                State = self.STATE,
                                key='mapCustomize' )

        self.settings = IconButton(int((self.MENU_WIDTH - self.ICON_WIDTH) / 2),
                                screen_height - self.ICON_WIDTH - 10,
                                self.ICON_WIDTH,
                                self.ICON_WIDTH,
                                icon = "settings.png",
                                bgColor=pg.Color('#848F8B'), 
                                border_thikness=2, 
                                border_radius=10,
                                State = self.STATE,
                                key='settings' )

        self.side_menu = pg.Rect(0, 0, self.MENU_WIDTH, screen_height)

        #? MAP

        self.TheMap = Map(self.screen,50 ,0,screen_width-50,screen_height,self.connectionToDatabase)

        #? MENU

        self.RobotsMenu = Robots(self.screen,50 ,0,300,screen_height )
        self.MapsMenu = Maps(self.screen,50 ,0,300,screen_height,self.TheMap.update,self.connectionToDatabase )
        self.PathsMenu = Paths(self.screen,50 ,0,300,screen_height )
        self.SettingsMenu = Settings(self.screen,50 ,0,300,screen_height )



    def draw(self) :
        for robot in self.RobotsMenu.ListOfRobots :
            if robot.connection.in_waiting:
                cardCode = str(robot.connection.readline().decode('ascii'))
                print(cardCode)
                if robot.id not in self.PathsMenu.PATHS :
                    print("no path available")
                    break
                for card in self.TheMap.Cards :
                    # print('card',card['code'])
                    # print(all( int(card['code'].split()[i]) == int(cardCode.split()[i]) for i in range(4)  ))
                    if all( int(card['code'].split()[i]) == int(cardCode.split()[i]) for i in range(4)  ) :
                        for command in self.PathsMenu.PATHS[robot.id][1:]:
                            print(command)
                            if int(command.split()[0]) == int(card['id']) :
                                print(command.split()[1])
                                robot.connection.write(bytearray(command.split()[1], "utf8"))
                                if command.split()[1] =='A' :
                                    self.PathsMenu.PATHS.pop(robot.id)
                                return 
                        
                

        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.TheMap.draw()
        pg.draw.rect(self.screen,'#C6C5CA', self.side_menu,0)
        
        self.robot.draw(self.screen)
        self.paths.draw(self.screen)
        self.map.draw(self.screen)
        self.settings.draw(self.screen)
        
        if(self.STATE["robot"]):
            self.RobotsMenu.draw()
        if(self.STATE["mapCustomize"]):
            self.MapsMenu.draw()
        if(self.STATE["paths"]):
            self.PathsMenu.draw()
        if(self.STATE["settings"]):
            self.Settings.draw()
        

    def handleEvent(self,event) :
        self.robot.handleEvent(event,50,350)
        self.paths.handleEvent(event,50,350)
        self.map.handleEvent(event,50,350)
        self.settings.handleEvent(event,50,350)
        if not any(self.STATE[menu] for menu in self.STATE):
            self.TheMap.handleEvent(event)
        if(self.STATE["robot"]):
            self.RobotsMenu.handleEvent(event)
        if(self.STATE["mapCustomize"]):
            self.MapsMenu.handleEvent(event)
        if(self.STATE["paths"]):
            self.PathsMenu.handleEvent(event,self.RobotsMenu.ListOfRobots,self.TheMap.Cards)
        if(self.STATE["settings"]):
            self.Settings.handleEvent(event)