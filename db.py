# -*- coding: utf-8 -*-

import psycopg2
from psycopg2 import sql
import sys
import datetime
from tabulate import tabulate

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
            query = "INSERT INTO Classes (Cname,CFrequency,CFirstDAY, Ctime, CDuration, CMaxEnroll, CRoom, TaughtBy) VALUES (%(cname)s,%(cfreq)s,%(cfirday)s,%(ctime)s,%(cdur)s,%(cmax)s,%(croom)s,%(taught)s);"
            self.cursor.execute(query,{'cname': Cname, 'cfreq': CFrequency, 'cfirday': CFirstDAY, 'ctime': CTime, 'cdur': CDuration, 'cmax': CMaxEnroll, 'croom': CRoom, 'taught': TaughtBy})
        except Exception as e:
            print('*** Class Inerstion Failed %r'%(e))
            sys.exit(1)
    def searchMember(self, attribute, value):
        try:
            query = sql.SQL( "SELECT * FROM Members WHERE {} = %s ;").format(sql.Identifier(attribute))
            self.cursor.execute(query, [value])
            headers = ['mid', 'mname', 'HouseNum', 'Street', 'City', 'PostalCode','phone', 'regidate']
            
            self.prettyprintConsole(self.cursor.fetchall(),headers)           
        except Exception as e:
            print('*** Search Failed %r'%(e))
            sys.exit(1)

    def addPlan(self, name, cost, freq):
        try:
            query = "INSERT INTO Plans (pname, cost, payment_frequency) VALUES (%s,%s,%s);"
            self.cursor.execute(query, (name,cost,freq))
            print("Insert Success")
        except Exception as e:
            print('*** Plan insertion failed %r'%(e))
            sys.exit(1)
            
    def modifyMember(self, attribute, value, ID):
        try:
            query = sql.SQL("UPDATE Members SET {} = %s WHERE mid = %s").format(sql.Identifier(attribute))
            self.cursor.execute(query, [value,ID])
            print("Modification Success")
        except Exception as e:
            print('*** Member Modification failed %r'%(e))
            sys.exit(1)
    def getPlan(self):
        try:
            query = "SELECT pname FROM Plans;"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print('*** error fetching plans %r'%(e))
            sys.exit(1)
    def addMembership(self,ID,pname):
        try:
            query = "INSERT INTO Memberships (mid,pname,pregidate) VALUES (%s,%s,%s);"
            self.cursor.execute(query, [ID,pname,datetime.datetime.today()])
            print("Membership Added")
        except Exception as e:
            print('*** error adding MemberShip plans %r'%(e))
            
    def prettyprintConsole(self,Result, Header):
         print(tabulate(Result, headers = Header))


    def addInstructor(self, inName):
        try:
            query = "INSERT INTO Instructors (instructorname) VALUES (%(inName)s);"
            self.cursor.execute(query, {'inName': inName})
            print("Insert Success")
        except Exception as e:
            print('*** Instructor Insertion FailedL %r' % (e))
            sys.exit(1)

