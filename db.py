# -*- coding: utf-8 -*-

import psycopg2
import sys

class db():
    
    
    def __init__(self, sshport, port):
        self.SSH_Port = sshport
        self.Port = port
          
    def connectdb(self):
        try:
            conn = psycopg2.connect(dbname="cs421", user="cs421g19", password='mSKUc"UK+9', host = "localhost")
                           
        except Exception as e:
            print('*** DB failed to connect; %r'%(e))
            sys.exit(1)
        