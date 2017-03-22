# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:15:22 2017

@author: marc
"""

import tkinter as tk
from tkinter import ttk
import db

class dbGUI(tk.Frame):
    
    def __init__(self,root):
        #Master canvas
        self.root = root
        root.title("COMP421 Demo")
        
        #Creates the tab master object
        n = ttk.Notebook(root)
        
        #assign a canvas each individual small tab
        f0 = tk.Frame(n, width = 200, height = 200)
        f1 = tk.Frame(n, width = 200, height = 200)
        f2 = tk.Frame(n, width = 200, height = 200)
        f3 = tk.Frame(n, width = 200, height = 200)
        
        #a tab and name
        n.add(f0, text = "DB")
        n.add(f1, text="member")
        n.add(f2, text = "Plans")
        n.add(f3, text = "Classes")
        
        self.database = db.db()
        
        DisconnectDB = ttk.Button(f0, text = "Disconnect", command = self.database.disconnectdb)
        InitDB = ttk.Button(f0, text = "Init DB", command = self.database.initTable)
        Quit = ttk.Button(f0, text = "quit", command = self.close_window)        
        
        DisconnectDB.grid(column = 0)
        InitDB.grid(column = 0)
        Quit.grid(column = 0)

	#member Entrys

        MemberNameL = ttk.Label(f1, text = "Name")
        self.MemberName = ttk.Entry(f1)
        
        MemberAddressL = ttk.Label(f1, text = "Address")
        MemberAddressHouseNumL = ttk.Label(f1, text = "house #")
        self.MemberAddressHouseNum = ttk.Entry(f1)
        
        MemberAddressHouseStreetL = ttk.Label(f1, text = "Street")
        self.MemberAddressHouseStreet = ttk.Entry(f1)
        
        MemberAddressHouseCityL = ttk.Label(f1, text = "City")
        self.MemberAddressHouseCity = ttk.Entry(f1)
        
        MemberAddressHousePostCodeL = ttk.Label(f1, text = "Postal Code")
        self.MemberAddressHousePostCode = ttk.Entry(f1)
        
        MemberPhoneL = ttk.Label(f1, text = "Phone")
        self.MemberPhone = ttk.Entry(f1)
    
        AddMemberButton = ttk.Button(f1, text ="Add", command = self.addMemCallback)        
        
	#member grid

        MemberNameL.grid(column =0 , row = 0)
        self.MemberName.grid(column = 0 , row = 1)
        
        MemberAddressL.grid(column = 0 ,row =2)
        MemberAddressHouseNumL.grid(column = 0 ,row =3)
        self.MemberAddressHouseNum.grid(column = 0 , row = 4)
        MemberAddressHouseStreetL.grid(column = 1, row = 3)
        self.MemberAddressHouseStreet.grid(column = 1, row =4)
        MemberAddressHouseCityL.grid(column = 2, row = 3)
        self.MemberAddressHouseCity.grid(column = 2, row = 4)        
        MemberAddressHousePostCodeL.grid(column = 3 , row = 3)
        self.MemberAddressHousePostCode.grid(column = 3 , row = 4)
        
        MemberPhoneL.grid(column = 1, row = 0)
        self.MemberPhone.grid(column = 1 , row = 1)
        
        AddMemberButton.grid(column = 1 , row = 7)


        	#class entrys
        
        classNameL = ttk.Label(f3, text = "Class Name")
        self.className = ttk.Entry(f3)
        
        classFreqL = ttk.Label(f3, text = "Frequency")
        self.classFreq = ttk.Entry(f3)
        
        classFirDayL = ttk.Label(f3, text = "First Day")
        self.classFirDay = ttk.Entry(f3)
        
        classTimeL = ttk.Label(f3, text = "Time")
        self.classTime = ttk.Entry(f3)
        
        classDurL = ttk.Label(f3, text = "Duration")
        self.classDur = ttk.Entry(f3)
        
        cmaxEnrollL = ttk.Label(f3, text = "Max Enrollment")
        self.cmaxEnroll = ttk.Entry(f3)
        
        cRoomL = ttk.Label(f3, text = "Room Number")
        self.cRoom = ttk.Entry(f3)
        
        cTaughtL = ttk.Label(f3, text = "Taught by")
        self.cTaught = ttk.Entry(f3)
        
        AddClassesButton = ttk.Button(f3,text = "Add", command = self.addClassCallback)
        	
        #class grid
        
        classNameL.grid(column =0 , row = 0)
        self.className.grid(column = 0 , row = 1)
        classFreqL.grid(column =0 , row = 2)
        self.classFreq.grid(column = 0 , row = 3)
        
        classFirDayL.grid(column =1 , row = 0)
        self.classFirDay.grid(column = 1 , row = 1)
        classTimeL.grid(column =1 , row = 2)
        self.classTime.grid(column = 1 , row = 3)
        
        classDurL.grid(column =2 , row = 0)
        self.classDur.grid(column = 2 , row = 1)
        cmaxEnrollL.grid(column =2 , row = 2)
        self.cmaxEnroll.grid(column = 2 , row = 3)
        
        cRoomL.grid(column =3 , row = 0)
        self.cRoom.grid(column = 3 , row = 1)
        cTaughtL.grid(column =3 , row = 2)
        self.cTaught.grid(column = 3 , row = 3)
        
        AddClassesButton.grid(column = 4, row = 0)
        


	#packing 

	
        n.pack(fill = tk.X)
        
    def addMemCallback(self):
        name = self.MemberName.get()
        houseNum = self.MemberAddressHouseNum.get()
        houseStreet = self.MemberAddressHouseStreet.get()
        PostCode= self.MemberAddressHousePostCode.get()
        HousePhone = self.MemberPhone.get()
        City = self.MemberAddressHouseCity.get()
        
        if(not name and not houseNum and not houseStreet and not PostCode and not HousePhone and not City):
            print("Some Input are Empty") 
        
        self.database.addMember(name,houseNum, houseStreet, City, HousePhone, PostCode)


    def addClassCallback(self):
        cname = self.className.get()
        cfreq = self.classFreq.get()
        cfirday = self.classFirDay.get()
        ctime = self.classTime.get()
        cdur = self.classDur.get()
        cmax = self.cmaxEnroll.get()
        croom = self.cRoom.get()
        ctaughtby = self.cTaught.get()

        if(not cname and not cfreq and not cfirday and not ctime and not cdur and not cmax and not croom and not ctaughtby):
            print ("Some Inputs are Empty!")

        self.database.addClass(cname,cfreq,cfirday,cdur,cmax,croom,ctaughtby)

    def close_window(self): 
        self.root.destroy()   

         
         
         
    

if __name__ == "__main__":
        root = tk.Tk()
        UI = dbGUI(root)
        root.mainloop()
