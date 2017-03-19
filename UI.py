# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:15:22 2017

@author: marc
"""

import tkinter as tk


class dbGUI(tk.Frame):
    
    def __init__(self,root):
        self.root = root
        root.title("COMP421 Demo")
        
        
        n = tk.ttk.Notebook(root)
        
        f0 = tk.Frame(n, width = 200, height = 200)
        f1 = tk.Frame(n, width = 200, height=200)
        f2 = tk.Frame(n, width=200, height=200)
        
        n.add(f0, text = "DB")
        n.add(f1, text="member")
        n.add(f2, text = "Plans")
        
        connectDB = tk.ttk.Button(f0, text = "Connect DB")
        DisconnectDB = tk.ttk.Button(f0, text = "Disconnect")
        
        connectDB.grid(column = 0)
        DisconnectDB.grid(column = 0)   
        
        
        n.pack(fill = tk.X)
        

if __name__ == "__main__":
        root = tk.Tk()
        UI = dbGUI(root)
        root.mainloop()