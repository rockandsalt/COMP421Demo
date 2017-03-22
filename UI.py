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
        self.root = root
        root.title("COMP421 Demo")
        
        
        n = ttk.Notebook(root)
        
        f0 = tk.Frame(n, width = 200, height = 200)
        f1 = tk.Frame(n, width = 200, height=200)
        f2 = tk.Frame(n, width=200, height=200)
        
        n.add(f0, text = "DB")
        n.add(f1, text="member")
        n.add(f2, text = "Plans")
        
        self.database = db.db()
        
        DisconnectDB = ttk.Button(f0, text = "Disconnect", command = self.database.disconnectdb)
        InitDB = ttk.Button(f0, text = "Init DB", command = self.database.initTable)
        
        DisconnectDB.grid(column = 0)
        InitDB.grid(column = 0)
        
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
    
        AddMemberButton = ttk.Button(f1, text ="Add", command = self.addMemCallback )        
        
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
        
        n.pack(fill = tk.X)
        
    def addMemCallback(self):
        name = self.MemberName.get()
        houseNum = self.MemberAddressHouseHum.get()
        houseStreet = self.MemberAddressHouseStreet.get()
        PostCode= self.MemberAddressHousePostCode.get()
        HousePhone = self.MemberPhone.get()
        City = self.MemberAddressHouseCity.get()
        
        if(not name and not houseNum and not houseStreet and not PostCode and not HousePhone and not City):
            print("Some Input are Empty") 
        
        self.database.addMember(name,houseNum, houseStreet, City, HousePhone, PostCode)
        
        
        

         
         
         
    

if __name__ == "__main__":
        root = tk.Tk()
        UI = dbGUI(root)
        root.mainloop()