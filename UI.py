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
        f4 = tk.Frame(n, width = 200, height = 200)
        
        #a tab and name
        n.add(f0, text = "DB")
        n.add(f1, text="member")
        n.add(f2, text = "Plans")
        n.add(f3, text = "Classes")
        n.add(f4, text = "Instructor")
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
        
        FindMemberL = ttk.Label(f1, text = "Search Member by attribute")
        self.FindMember = ttk.Entry(f1)
        attributeLabel = ttk.Label(f1,text = "Attribute : ")
        valueLabel = ttk.Label(f1,text = "Value: ")
        searchedAttribute =  tk.StringVar()
        MAttributeComboBox = ttk.Combobox(f1,textvariable = searchedAttribute)
        MAttributeComboBox['values'] = ('mid','mname','housenum','street','city', 'postalcode','phone')
        
        searchButton = ttk.Button(f1, text = "search", command = lambda : self.searchMember(MAttributeComboBox.get(), self.FindMember.get()))
        
        ModifyMemberL = ttk.Label(f1, text = "Modify Member")
        MemberIDToModL = ttk.Label(f1, text = "ID: ")
        MemberIDToMod = ttk.Entry(f1)
        MemberToModAttributeL = ttk.Label(f1,text = "Attribute : ")
        MemberToModValueL = ttk.Label(f1,text = "Value: ")
        MemberToModValue = ttk.Entry(f1)
        MemberToModAttribute =  tk.StringVar()
        MModAttributeComboBox = ttk.Combobox(f1,textvariable = MemberToModAttribute)
        MModAttributeComboBox['values'] = ('mname','housenum','street','city', 'postalcode','phone')
        
        ModifyButton = ttk.Button(f1, text = "Modify", command = lambda : self.modifyMember(MemberIDToMod.get(),MModAttributeComboBox.get(), MemberToModValue.get()))        
        
        AddPlanL = ttk.Label(f1, text = "Add Plan to member")
        AddPlanIDL = ttk.Label(f1, text = "ID: ")
        AddPlanID = ttk.Entry(f1)
        self.PlanComboBox = ttk.Combobox(f1)
        self.fillPlan()
        AddPlanToMB = ttk.Button(f1, text = "add Plan", command = lambda: self.addMembership(AddPlanID.get(), self.PlanComboBox.get()))
        
        
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
        
        AddMemberButton.grid(column = 1 , row = 7,padx=5, pady=5)
        
        FindMemberL.grid(column = 0, row = 8, padx = 5, pady = 5)
        
        attributeLabel.grid(column = 0, row = 9)
        MAttributeComboBox.grid(column =1, row = 9 )
        valueLabel.grid(column = 2 , row = 9)
        self.FindMember.grid(column = 3, row = 9)
        searchButton.grid(column = 0, row =10)
        
        ModifyMemberL.grid(column = 0 , row= 11, padx = 5, pady = 5)
        MemberIDToModL.grid(column = 0, row = 12)
        MemberIDToMod.grid(column = 1 , row = 12)
        MemberToModAttributeL.grid(column = 2, row = 12)
        MModAttributeComboBox.grid(column = 3, row = 12)
        MemberToModValueL.grid(column = 4 , row = 12)
        MemberToModValue.grid(column = 5, row =12)
        ModifyButton.grid(column = 0 , row = 13, padx = 5, pady=5)
        
        AddPlanL.grid(column = 0 , row = 14, padx=5, pady= 5)
        AddPlanIDL.grid(column = 0 , row = 15)
        AddPlanID.grid(column = 1 ,row = 15 )
        self.PlanComboBox.grid(column = 2 , row = 15)
        AddPlanToMB.grid(column =0 , row = 16, padx = 5, pady =5)
        

        #Plan Entry
        CreatePlanLabel = ttk.Label(f2, text = "Create Plan")
        pNameLabel = ttk.Label(f2, text = "Name")
        costLabel = ttk.Label(f2, text = "Cost")
        PlanFreqLabel = ttk.Label(f2, text = "payment frequency")
        AddPlanButton = ttk.Button(f2, text = "add Plan", command = self.addPlan)
        
        self.PlanNameEntryBox = ttk.Entry(f2)
        self.PlanCostEntryBox = ttk.Entry(f2)
        self.PlanPFreqEntryBox = ttk.Entry(f2)

        #Plan Grid
        CreatePlanLabel.grid(column = 0, row = 0,padx=5, pady=5) 
        pNameLabel.grid(column = 0, row =1,padx=5, pady=5)
        costLabel.grid(column = 1, row = 1,padx=5, pady=5)
        PlanFreqLabel.grid(column = 2 , row = 1, padx=5, pady=5)
        

        self.PlanNameEntryBox.grid(column = 0, row =2)
        self.PlanCostEntryBox.grid(column =1, row = 2)
        self.PlanPFreqEntryBox.grid(column = 2, row = 2)
        AddPlanButton.grid(column = 0 , row =3)
        

        AddClassesButton.grid(column = 4, row = 0)

    #instructor entry

        self.var = tk.StringVar()

        instructorNameL = ttk.Label(f4, text="Instructor Name")
        self.instructorName = ttk.Entry(f4)
        msg = ttk.Label(f4, textvariable=self.var, font="Helvetica 10 italic")

        AddInstructorButton = ttk.Button(f4, text="Add", command=self.addInstructorCallback)

        # class grid

        instructorNameL.grid(column=0, row=0)
        self.instructorName.grid(column=0, row=1)

        AddInstructorButton.grid(column=1, row=1)
        msg.grid(column=2, row=1)



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
        else:
            self.database.addMember(name,houseNum, houseStreet, City, HousePhone, PostCode)

    def close_window(self): 
        self.root.destroy()
    
    def searchMember(self,attribute,value):
        if(attribute and value):
            self.database.searchMember(attribute,value)

    def addInstructorCallback(self):
        iname = self.instructorName.get()

        if(not iname):
            print ("Please add Instructor Name")
            self.var.set("Please add Instructor Name!")
        else:
            self.database.addInstructor(iname)
            self.var.set("Instructor Added!")

        
    def addPlan(self):
        name = self.PlanNameEntryBox.get()
        cost = self.PlanCostEntryBox.get()
        freq = self.PlanPFreqEntryBox.get()
        
        if(name and cost and freq):
            self.database.addPlan(name, cost, freq)
        else:
            print("some input are empty")
    def modifyMember(self,ID,attribute,value):
        if(ID, attribute, value):
            self.database.modifyMember(attribute,value,ID)
           
    def fillPlan(self):
        PlanList = self.database.getPlan() 
        self.PlanComboBox['values'] = PlanList 
         
    def addMembership(self, ID , pname):
        self.database.addMembership(ID,pname)
        

if __name__ == "__main__":
    root = tk.Tk()
    UI = dbGUI(root)
    root.mainloop()
