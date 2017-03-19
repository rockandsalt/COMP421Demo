# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 15:28:29 2017

@author: marc
"""
import psycopg2


def main():
    conn = psycopg2.connect('dbname=cs421 user=cs421g19 password=mSKUc"UK+9 host=comp421.cs.mcgill.ca')
    cur = conn.cursor()
    
    cur.close()
        
    


if(__name__=="__main__"):
    main()
