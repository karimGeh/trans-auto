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

        self.Map = Map(self.screen,50 ,0,screen_width-50,screen_height,self.connectionToDatabase)

        #? MENU

        self.RobotsMenu = Robots(self.screen,50 ,0,300,screen_height )
        self.MapsMenu = Maps(self.screen,50 ,0,300,screen_height,self.Map.update,self.connectionToDatabase )
        self.PathsMenu = Paths(self.screen,50 ,0,300,screen_height )
        self.SettingsMenu = Settings(self.screen,50 ,0,300,screen_height )



    def draw(self) :
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.Map.draw()
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
            self.RobotsMenu.draw()
        if(self.STATE["settings"]):
            self.RobotsMenu.draw()
        

    def handleEvent(self,event) :
        self.robot.handleEvent(event,50,350)
        self.paths.handleEvent(event,50,350)
        self.map.handleEvent(event,50,350)
        self.settings.handleEvent(event,50,350)
        self.Map.handleEvent(event)
        if(self.STATE["robot"]):
            self.RobotsMenu.handleEvent(event)
        if(self.STATE["mapCustomize"]):
            self.MapsMenu.handleEvent(event)
        if(self.STATE["paths"]):
            self.RobotsMenu.handleEvent(event)
        if(self.STATE["settings"]):
            self.RobotsMenu.handleEvent(event)