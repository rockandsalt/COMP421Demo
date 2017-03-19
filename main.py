# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 15:28:29 2017

@author: marc
"""
import tkinter as tk
import UI

def main():
    root = tk.Tk()
    initUI = UI.dbGUI(root)
    root.mainloop()
        

if(__name__=="__main__"):
    main()
