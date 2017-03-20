# -*- coding: utf-8 -*-

import psycopg2
import sys

class db():
    
    
    def __init__(self):
        self.SSH_Port = 22
        try:
            self.conn = psycopg2.connect(dbname="cs421", user="cs421g19", password='mSKUc"UK+9', 
                                         host = "comp421.cs.mcgill.ca")
            self.cursor = self.conn.cursor()
            print("db connection successful")               
        except Exception as e:
            print('*** DB failed to connect; %r'%(e))
            sys.exit(1)
             
    def disconnectdb(self):
        try:
            self.cursor.close()
            self.conn.close()
            print("db disconnect successful")
        
        except Exception as e:
            print('*** DB failed to connect; %r'%(e))
            sys.exit(1)
    
    
    def initTable(self):
        try:
            self.cursor.execute(open("projectsetup.sql", "r").read())
            self.conn.commit()
            print(self.cursor.query)
        except Exception as e:
            print('*** DB failed to initialise: %r'%(e))
            sys.exit(1)