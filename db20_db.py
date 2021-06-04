"""
SQLite is a C library that provides a lightweight disk-based database that doesn’t require a 
separate server process and allows accessing the database using a nonstandard variant of the 
SQL query language. Some applications can use SQLite for internal data storage. 
It’s also possible to prototype an application using SQLite and then port the code to a larger 
database such as PostgreSQL or Oracle.  
http://www.sqlite.org  
https://docs.python.org/3.4/library/sqlite3.html 


ask name and password from enduser
foundNamePw = call showrecords2 

if the return value  foundNamePw = found then print "found!"
else foundName = call  showrecords3 



"""

from db20_Database import dbfunctions  #from filename import classname

db = dbfunctions()    #create an on object or instance of the class

#db.createTable()
#db.insertRecordsReg() 
#db.deleteRecords()

var = db.showRecords2("Walter",35)
print (var)
# get values from end=user
# insert a record into the database using the user input
c_ID = int(input ("Enter your id: "))
name = input ("what is your name ") 
email = input ("Enter your email address: ")
pw  = input ("Enter your password: ") 
age  = int ( input ("Enter your age: " ) ) 
#salary = float ( input ("Enter your salary: " ))
db.insertRecordsReg2( c_ID, name , email , pw , age )
db.showRecords()