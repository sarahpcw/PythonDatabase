# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 08:19:06 2021

@author: u
"""
from db20_Database import dbfunctions

class db20_rundb (dbfunctions) :
    
    db = dbfunctions() 
    ##################
    message = db.testfunction()
    print (message)
    ##################
    db.createTableReg()  # function call
    db.insertRecordsReg()
    db.updateRecords()
    db.deleteRecords()
    db.showRecords()
    password = db.showRecords2('Chris', 36)
    print ( password)
    
    
    """
    ask the enduser for name and id
    then find his password
    run showrecords2() to extract his record, and save his password in a variable
    return his password
    
    ask him for his password
    if he gives the correct , print ("continue")
    otherwise he can try 3 times
    if after 3 times he did not enter the correct password, print ("Your accounts is blocked")
    """
