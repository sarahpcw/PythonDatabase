# -*- coding: utf-8 -*-
import sqlite3
#############   CREATE A movies TABLE
conn = sqlite3.connect('test.db')  # database name, in sqlite3 : if test.db does not exist, it will be created
try : 
    conn.execute("CREATE TABLE movieprogram (day text, moviename text );")
    print ("table sucessfully created")
except :
    print ("table exists already")

conn.close()
################## inserting records from txt file
conn = sqlite3.connect('test.db')  #########
filename = "C:\\Users\\u\\.spyder-py3\\3W-Webinar\\movies4.txt"
finput = open(filename, "r" ) 
for line in finput : 
    # insert every line to the database
    mylist = line.split(',')
    print(mylist)
    conn.execute("insert into movieprogram (day, moviename ) values ( ?,? )", (mylist[0], mylist[1],) )
    conn.commit()
finput.close() 
 
print('Display result set of the select clause')
mydata = conn.execute("select day, moviename from movieprogram ")
for row in mydata:
    print ( row )   
conn.close()





import sqlite3

conn = sqlite3.connect('test.db')
print("drop table")
conn.execute("drop table customerRegistrations")
conn.close()




#############   CREATE A TABLE
conn = sqlite3.connect('test.db')
conn.execute("drop table customerRegistrations ")
conn.commit()
conn.close()


#############  get the pw 3 x
def getpw(count, loggedin):
    while ( count < 3 and  loggedin == 'n'):
            pw   = input("Enter your password ")
            count +=1
            loggedin = db.findMember ( name, pw)
            if loggedin == 'y' :
                print("Connected " , name, pw)
    return count, loggedin
#############  Step1

from db20_database_begin_Lib import dbFunctions

db = dbFunctions()

"""
ask the end user for the name and password
loggedin = y
if both was found successfull login  

register = y
if none was found register, call insert function

wrongpw = y
if name was found but not the password, try again 3 x
"""
from db20_database_begin_Lib import dbFunctions

db = dbFunctions()
db.printMembers()
count = 0

name = input("Enter your name ")
pw   = input("Enter your password ")

count +=1

loggedin = 'n'

loggedin = db.findMember(name,pw )
if loggedin == 'y' :
    print("Connected ", name, pw)
else : 
    register = db.findNeither(name)
    if register == 'y' :
        db.insertMember(name,pw)
    else :  # log in
#        while ( count < 3 and  loggedin == 'n'):
#            pw   = input("Enter your password ")
#            count +=1
#            loggedin = db.findMember ( name, pw)
#            if loggedin == 'y' :
#                print("Connected " , name, pw)
        count, loggedin = getpw(count, loggedin)
        if count >= 3 and loggedin == 'n':
            print ("you have been blocked")
        
    












    









#############   INSERT RECORDS INTO A DATABASE
conn = sqlite3.connect('test.db')
conn.execute("insert into customerRegistrations (name , email , pw ) values ('Mary', 'm@gmail.com','123');")
conn.execute("insert into customerRegistrations ( name , email , pw ) values ('Helen','h@gmail.com','345');")
conn.execute("insert into customerRegistrations (name , email , pw ) values ('Chris','c@gmail.com','979');")
conn.commit()
conn.close()

#############   PRINT A TABLE
conn = sqlite3.connect('test.db')
print('Display result set of the select clause')
mydata = conn.execute("select * from customerRegistrations ")
for row in mydata:
    print ( row )   
conn.close()


