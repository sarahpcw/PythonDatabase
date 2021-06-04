#################  open the connection
import sqlite3


#############   CREATE A user TABLE
def createTable():
    conn = sqlite3.connect('test.db')  # database name, in sqlite3 : if test.db does not exist, it will be created
    try : 
        conn.execute("CREATE TABLE userfiles (username text, password text, fullname text );")
        print ("table sucessfully created")
    except :
        print ("table exists already")
    conn.close()

def insertUser():
    conn = sqlite3.connect('test.db')  # database name, in sqlite3 : if test.db does not exist, it will be created
    
    em   = input("Please enter your email")
    pw   = input("Please enter your pw")
    fullname = input("Please enter your full name")
    
    conn.execute("insert into userfiles (username, password, fullname ) values ( ?,?,? )", (em, pw, fullname,) )
    conn.commit()
    conn.close()

def insertMLBPlayer(em, pw, fullname):
#    print ( "INSERTING" , em, pw, fullname)
    conn = sqlite3.connect('test.db')  # database name, in sqlite3 : if test.db does not exist, it will be create
    conn.execute("insert into userfiles (username, password, fullname ) values ( ?,?,? )", (em, pw, fullname,) )
    conn.commit()
    conn.close()
    
def readMLBPlayers ():  #################  read the database table 
    count = 0
    conn = sqlite3.connect('test.db')
    print('Display result set of the select clause')
    mydata = conn.execute("select username, password, fullname from userfiles ")
    for row in mydata:
        count += 1
        print (row,"COUNT " , count)
    conn.close()


def createPW (mylist):
    init_1 = mylist[2]
    init_1 = init_1[0]
    pos    = mylist[2].find(" ")
    init_2 = mylist[2]
    init_2 = init_2[pos+1]
    nr = str(random.randint(10000,90000)) # integer
    pw = init_1.upper()+init_2.lower()+"$"+nr
    return pw
    
def validatePw():
    conn = sqlite3.connect('test.db')  # database name, in sqlite3 : if test.db does not exist, it will be created
    em   = input("Please enter your email ")
    pw   = input("Please enter your pw ")
    selects = "select username, password, fullname from userfiles "
    wheres =  "where username = ? and password =? "
    query = selects + wheres
    mydata = conn.execute(query , (em, pw,) )
    count = 0
    for row in mydata:
        count += 1
        print (row,"  Successful Login" )
    if count == 0:
        print ( "invalid username or password")
    conn.close()
########################################################
### get the data
import pandas as pd
import random
path     = 'C:\\Users\\u\\.spyder-py3\\3W-Webinar\\'
filename = path + 'MLBPlayerSalaries.xlsx'
fcsv     = path + 'MLBPlayerSalaries.csv'
df = pd.read_excel(filename)
print(df.shape)
df.to_csv(fcsv)
############ create the table
createTable()


### read the csv file and create username and password
finput = open(fcsv, "r" ) 
count = 0
for line in finput : 
    count +=1 
    mylist = line.split(',')  #  ['1','234','353453','iuoq', 'fjpwjefpw']
    username = mylist[2].replace(' ','_')+"@mlb.com"
    pw = createPW(mylist)
    if count == 1:
        print (username, pw)
    elif count < 10 : 
        print (pw)
        insertMLBPlayer(username, pw, mylist[2])
    else:
        break
    ## create the email: name+surname concatenates + @ + mlb.com (replace ' ' with '_' )
    ## create a pw: initals + $ + a randomnumber between 0 and 100  count += 1
print ( 'Record Count', count)
finput.close()
###### print the records
readMLBPlayers()
###### validate the password
validatePw()
