# -*- coding: utf-8 -*-

import psycopg2
import sys
import datetime

class db():
    
    
    def __init__(self):
        self.SSH_Port = 22
        try:
            self.conn = psycopg2.connect(dbname="cs421", user="cs421g19", password='mSKUc"UK+9', 
                                         host = "comp421.cs.mcgill.ca")
            self.conn.autocommit = True                             
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
            print(self.cursor.query)
        except Exception as e:
            print('*** DB failed to initialise: %r'%(e))
            sys.exit(1)
            
    def addMember(self, mname, houseNum, street, city, phone, postalCode):
        try:
            query = "INSERT INTO Members (mname, HouseNum, Street, City, phone,PostalCode , regidate) VALUES (%(name)s,%(hNum)s,%(st)s,%(city)s,%(phone)s,%(pCode)s, %(rDate)s);"
            self.cursor.execute(query, 
                {'name': mname,'city':city, 'hNum': houseNum, 'st':street, 'phone':phone, 'pCode':postalCode, 'rDate': datetime.datetime.today()})
            print("Insert Success")
        except Exception as e:
            print('*** Member Insertion FailedL %r'%(e))
            sys.exit(1)

    def addClass(self, Cname, CFrequency, CFirstDAY, CTime, CDuration, CMaxEnroll, CRoom, TaughtBy):
        try:
            query = "INSERT INTO Classes VALUES (%(cname)s,%(cfreq)s,%(cfirday)s,%(ctime)s,%(cdur)s,%(cmax)s,%(croom)s,%(taught)s);"
            self.cursor.execute(query,{'cname': Cname, 'cfreq': CFrequency, 'cfirday': CFirstDAY, 'ctime': CTime, 'cdur': CDuration, 'cmax': CMaxEnroll, 'croom': CRoom, 'taught': TaughtBy})
        except Exception as e:
            print('*** Class Inerstion Failed %r'%(e))
            sys.exit(1)
    def searchMember(self, attribute, value):
        try:
            query = "SELECT * FROM Members WHERE (%s) = (%s)"
            self.cursor.execute(query, (attribute,value))
            print(self.cursor.fetchmany())            
        except Exception as e:
            print('*** Search Failed %r'%(e))
            sys.exit(1)