import pygame as pg
import sys
sys.path.insert(1,'C:\\Users\\karim\\OneDrive\\Documents\\Code\\PYTHON\\trans-auto')


from components.IconButton2 import IconButton2

class Map :
    def __init__(self,screen,x,y,w,h,connectionToDatabase):
        
        self.connectionToDatabase = connectionToDatabase
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.offsetX = w/2
        self.offsetY = h/2
        self.offsetXTemp = 0
        self.offsetYTemp = 0
        self.zoomCard = 1
        
        self.fontP = pg.font.Font(None, 15)
        
        self.ZoomIn = IconButton2(w - 90,
                                h - 50,
                                40,
                                40,
                                icon = "plus.png",
                                bgColor=pg.Color('#848F8B'), 
                                border_thikness=1, 
                                border_radius=10,
                                nextFunc=self.ZoomInFunc)
        self.ZoomOut = IconButton2(w - 40,
                                h - 50,
                                40,
                                40,
                                icon = "minus.png",
                                bgColor=pg.Color('#848F8B'), 
                                border_thikness=1, 
                                border_radius=10,
                                nextFunc=self.ZoomOutFunc)

        self.Cards = self.connectionToDatabase.ReadAllRFID()
        self.Links = self.connectionToDatabase.ReadAllLINK()

        self.graphicCards = {}
        self.graphicLinks = {}
        for card in self.Cards:
            self.graphicCards[card['id']] = {
                                                'id':card['id'],
                                                'code':card['code'],
                                                'x': card['x'],
                                                'y': (self.h-card['y']),
                                            }
        for link in self.Links:
            self.graphicLinks[link['id']] = {
                                                'id': link['id'],
                                                'id1': link['first_end'],
                                                'id2': link['second_end'],
                                            }
        self.frame = pg.Rect(x, y, w, h)



        #! MAP MOVE AND ZOOM VARIABLE
        self.down = False
        self.up = True
        self.positionDown = (0,0)
        self.zoom = 1

        # for l in self.graphicLinks :
        #     print(l)
        # for l in self.graphicCards :
        #     print(l)

        # print(self.graphicLinks)

    def ZoomInFunc(self):
        if  self.zoom < 4:
            self.zoom += 0.1

    def ZoomOutFunc(self):
        if  self.zoom >0.1:
            self.zoom -= 0.1

    def update(self):
        self.Cards = self.connectionToDatabase.ReadAllRFID()
        self.Links = self.connectionToDatabase.ReadAllLINK()
        for card in self.Cards:
            self.graphicCards[card['id']] = {
                                                'id':card['id'],
                                                'code':card['code'],
                                                'x': card['x'],
                                                'y': (self.h-card['y']),
                                            }
        for link in self.Links:
            self.graphicLinks[link['id']] = {
                                                'id': link['id'],
                                                'id1': link['first_end'],
                                                'id2': link['second_end'],
                                            }
    
    def draw(self , ListOfRobots):
        
        pg.draw.rect(self.screen, "#ffffff", self.frame,
                     0, 0)
        for link in self.Links:
            x1 = int(self.graphicCards[link['first_end']]['x'] * self.zoom + self.offsetX)
            y1 = int((self.graphicCards[link['first_end']]['y']- self.h) * self.zoom + self.h - self.offsetY)
            x2 = int(self.graphicCards[link['second_end']]['x'] * self.zoom + self.offsetX)
            y2 = int((self.graphicCards[link['second_end']]['y'] - self.h) * self.zoom + self.h - self.offsetY)
            pg.draw.line(self.screen,'#000000',(x1,y1),(x2,y2),int(2 * self.zoom))


        for card in self.Cards:
            x = self.graphicCards[card['id']]['x'] * self.zoom + self.offsetX
            y = (self.graphicCards[card['id']]['y'] - self.h) * self.zoom + self.h - self.offsetY
            pg.draw.circle(self.screen,'#dd0000',(x,y),int(5*self.zoom))
            self.screen.blit(
                self.fontP.render(
                                    '{} ({}, {})'.format(card['id'], card['x'], card['y']),
                                    True,
                                    pg.Color('#000000')
                                ),
                (x + 10 , y + 10)
            )
        for robot in ListOfRobots :
            if robot.position :
                x = robot.position[0] * self.zoom + self.offsetX
                y = -1 * robot.position[1] * self.zoom + self.h - self.offsetY
                pg.draw.circle(self.screen, '#00dd00', (x,y), int(4 * self.zoom))


        self.ZoomIn.draw(self.screen)
        self.ZoomOut.draw(self.screen)

    def handleEvent(self,event):
        # print("type : ",event.type,event.type == pg.KEYDOWN)
        # print("zoom : " ,self.zoom)
        self.ZoomIn.handleEvent(event)
        self.ZoomOut.handleEvent(event)
        if event.type == pg.KEYDOWN:
            # print("key",event.key)
            keys = pg.key.get_pressed()  #checking pressed keys
            if  (keys[pg.K_PLUS] or keys[pg.K_KP_PLUS] ) and self.zoom < 4:
                self.zoom += 0.1
            elif (keys[pg.K_MINUS] or keys[pg.K_KP_MINUS] ) and self.zoom > 0.2:
                self.zoom -= 0.1
            else:
                pass
                # Re-render the text.

        if event.type == pg.MOUSEBUTTONDOWN:
            if self.frame.collidepoint(event.pos):
                self.down = True
                self.up = False
                self.positionDown = event.pos
                self.offsetXTemp = self.offsetX 
                self.offsetYTemp = self.offsetY

            
        if event.type == pg.MOUSEBUTTONUP:
            if self.frame.collidepoint(event.pos):
                self.down = False
                self.up = True
                self.offsetXTemp = self.offsetX 
                self.offsetYTemp = self.offsetY

        if event.type == pg.MOUSEMOTION and self.down and not self.up :
            self.offsetX = self.offsetXTemp - (self.positionDown[0] - event.pos[0])
            self.offsetY = self.offsetYTemp + (self.positionDown[1] - event.pos[1])
