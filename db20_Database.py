# DDL : create table, drop table, alter table add columns etc
# DML : insert records, update record , delete record  +++++!!! conn.commit() otherwise data will be lost
# select queries : extract data 

import sqlite3
class dbfunctions :
    
        
    def testfunction(self):
        #your code here
        return 'hello world'
    
    
    def createTableReg(self):
        conn = sqlite3.connect('test.db')  # database name, in sqlite3 : if test.db does not exist, it will be created
        try : 
            conn.execute("CREATE TABLE customerRegistration (c_ID  int, name text, email text, pw text, age int, salary real);")
            print ( "table sucessfully created")
        except :
            print ( "table already exists")
    
        conn.close()
        
    
    
    def insertRecordsReg2(self, c_ID, name , email , pw , age ):
        conn = sqlite3.connect('test.db')
        inserts = "insert into customerRegistration "
        fields = "(c_ID, name , email , pw , age  ) "
        values = " values (?,?,?,?,?,?) "
        query = inserts + fields + values
        conn.execute( query, (c_ID, name , email , pw , age ) )
        conn.commit()  # insert , update and delete
        conn.close()
        
    def insertRecordsReg(self):
        conn = sqlite3.connect('test.db')
        conn.execute("insert into customerRegistration (c_ID, name , email , pw , age , salary ) values (34,'Mary', 'm@gmail.com','123',21, 1000.0);")
        conn.execute("insert into customerRegistration (c_ID, name , email , pw , age , salary ) values (38,'Paula','p@gmail.com','123',22, 2000.0);")
        conn.execute("insert into customerRegistration (c_ID, name , email , pw , age , salary ) values (41,'Anton','a@gmail.com','123',23, 3000.0);")
        conn.commit()  # insert , update and delete
        conn.close()
    
    
    
    def updateRecords (self):
        conn = sqlite3.connect('test.db')
        conn.execute("update customerRegistration set name='Pauline' where name = 'Mary' ")
        conn.commit()
        conn.close()
        
    def deleteRecords(self):
        conn = sqlite3.connect('test.db')
        conn.execute("delete from customerRegistration where name = 'Pauline' ")
        conn.commit()
        conn.close()
        
    def showRecords(self): 
        conn = sqlite3.connect('test.db')
        mydata = conn.execute("select c_ID, name , email , pw , age , salary from customerRegistration  order by name ")
        print('Display result set of the select clause')
        for row in mydata:
            print(row)
        conn.close()
    
    def showRecords2(self, firstname, c_ID): 
        conn = sqlite3.connect('test.db')
        selects = "select  c_ID, name, email, pw, age, salary "
        froms   = "from customerRegistration "
        wheres  = "where name = ? and c_ID = ? "
        orderby = "order by name "
        query   = selects + froms + wheres + orderby
#        print ( query )
        mydata  = conn.execute(query, (firstname, c_ID, ))
        print('Display result set of the select clause')
        var = 'not found'
        for row in mydata:
            print(row[1], 'has a salary of',  row[5] )
            var =  row[3]
        conn.close()
        return var
        
        # input parameters : name
        # execute must save the pw in a variable password
        # the return value is that variable password

    
