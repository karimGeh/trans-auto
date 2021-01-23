import psycopg2 as postgres
import psycopg2.extras 


class DatabaseConnection :
    DB_HOST = "localhost"
    DB_NAME = "transauto"
    DB_USER = "postgres"
    DB_PASS = "K@r##mG&h@d1"
    def __init__(self):
        self.connection =  postgres.connect(dbname=self.DB_NAME, 
                                            user=self.DB_USER, 
                                            password=self.DB_PASS, 
                                            host=self.DB_HOST)
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    #!  CRUD functionality for RFID
    #?      Create NEW CARD    
    def CreateRFID(self, code:str, x:int, y:int):
        self.cursor.execute("INSERT INTO rfid_cards (code, x ,y) VALUES('{}',{},{});".format(code,x,y))
        self.commit()
    
    #?      Read by code CARD
    def ReadRFIDbyCode(self, code:str):
        self.cursor.execute("SELECT * FROM rfid_cards WHERE code='{}';".format(code))
        return self.cursor.fetchone()
    
    #?      Read by position CARD
    def ReadRFIDbyCode(self, x:int, y:int):
        self.cursor.execute("SELECT * FROM rfid_cards WHERE x={} AND y={};".format(x,y))
        return self.cursor.fetchone()
    
    #?      Read All CARDs
    def ReadAllRFID(self):
        self.cursor.execute("SELECT * FROM rfid_cards;")
        return self.cursor.fetchall()
    
    #?      UPDATE CARD    
    def UpdateRFID(self, code:str, x:int, y:int):
        self.cursor.execute("UPDATE rfid_cards SET  x={} y={} WHERE code='{}';".format(x,y,code))
        self.commit()
    
    #?      Delete CARD    
    def DeleteRFID(self, code:str):
        self.cursor.execute("DELETE FROM rfid_cards WHERE code='{}';".format(code))
        self.commit()

    #!  CRUD functionality for links
    #?      Create NEW link    
    def CreateLINK(self, id1:int, id2:int):
        self.cursor.execute("INSERT INTO links (first_end , second_end) VALUES({},{});".format(id1,id2))
        self.commit()
    
    
    #?      Read by end links
    def ReadLINKbyEnd(self, idEnd:int):
        self.cursor.execute("SELECT * FROM links WHERE first_end={} OR second_end={};".format(idEnd,idEnd))
        return self.cursor.fetchall()
    
    #?      Read All Links
    def ReadAllLINK(self):
        self.cursor.execute("SELECT * FROM links;")
        return self.cursor.fetchall()
    
    #?      UPDATE links    
    def UpdateLINK(self,ID:int, id1:int, id2:int):
        self.cursor.execute("UPDATE links SET  first_end={} second_end={} WHERE id={};".format(id1,id2,ID))
        self.commit()
    
    #?      Delete links    
    def DeleteLINK(self,ID:int):
        self.cursor.execute("DELETE FROM links WHERE id={};".format(ID))
        self.commit()
    


    def commit(self):
        self.connection.commit()

    def close(self):
        #close cursor and connection 
        self.cursor.close()
        self.connection.close()