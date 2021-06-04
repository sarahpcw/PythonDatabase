import sqlite3

class dbfunctions:
# library of functions
    
    def printmessage(self):  #def is to define a function
        print("hello world")
    
    def createemessage(self):  #def is to define a function
        msg = "Hello new world"
        return msg

    def updatemessage(self, name):  #def is to define a function
        msg = "Hello " + name
        return msg
        
    def createTable(self):
        conn = sqlite3.connect('test.db')  # usercode, password
        conn.execute("CREATE TABLE customers (c_ID int, name text, age int, address text, salary real)")
        conn.close()
    
    def insertRecords(self, col1,col2):
        conn = sqlite3.connect('test.db')
        conn.execute("insert into customers (c_ID, name, age ,address, salary ) values (40,?,10,?,1000.0)", (col1,col2,))
#        conn.execute("insert into customers(c_ID, name,age ,address, salary ) values (41,'Molly',20,'Bristol',2000.0);")
#        conn.execute("insert into customers(c_ID, name,age ,address, salary ) values (42,'Paul',30,'Leeds',3000.0);")
        conn.commit()
        conn.close()
    
    def updateRecords (self):
        conn = sqlite3.connect('test.db')
        conn.execute("update customers set name='Frederik' where name = 'Molly'")
        conn.commit()
        conn.close()
        
    def deleteRecords(self):
        conn = sqlite3.connect('test.db')
        conn.execute("delete from customers where c_ID = 41")
#        conn.execute("delete from customers where c_ID = 31")
#        conn.execute("delete from customers where c_ID = 28")
        conn.commit()
        conn.close()
        
    def showRecords(self): 
        conn = sqlite3.connect('test.db')
        mydata = conn.execute("select c_ID, name,age ,address, salary from customers order by name ")
        print('Display result set of the select clause')
        for row in mydata:
            print( row )
        conn.close()
        
    def showRecords2(self, city): 
        conn = sqlite3.connect('test.db')
        selects = "select c_ID, name, age, address, salary "
        froms   = "from customers "
        wheres  = "where address = ? "
        orders  = "order by name"
        q = selects + froms + wheres + orders  
        mydata = conn.execute(q , (city,) )
        print('Display result set of the select clause')
        for row in mydata:
            print(row[0],row[1],row[2],row[3],row[4] )
        conn.close()