import sqlite3  ######## step 1
class dbFunctions :
    def createMembersTable (self ):
            #############  Step2
            conn = sqlite3.connect('test.db')  # database name, in sqlite3 : if test.db does not exist, it will be created
            
            sql = "CREATE TABLE members " 
            sql = sql + " ( m_ID INTEGER PRIMARY KEY AUTOINCREMENT, "  
            sql = sql + " memberName text, memberPW text) "
#            print (sql)
            
            #############  Step3
            conn.execute(sql)
            print ( "table sucessfully created")
            
            #############  Step4
            conn.close()
    
    def insertMember (self , name, pw):
            ###########  step2
            conn = sqlite3.connect('test.db')  # database name, in sqlite3 : if test.db does not exist, it will be created
            
            sqlinsert  = "insert into members " 
            sqlcolumns = " ( memberName , memberPW  ) "  
            sqlvalues  = " values ( ?, ?) "
            sql = sqlinsert + sqlcolumns + sqlvalues
#            print (sql )
            
            conn.execute(sql, (name, pw, ) ) #############  Step3 
            conn.commit() ############   Step 4 ( only for insert , update , delete)
            
            print ( "Registration successful") 
            conn.close()  #############  Step5
    
    def findMember (self , name, pw):
            ###########  step2
            conn = sqlite3.connect('test.db')  # database name, in sqlite3 : if test.db does not exist, it will be created
            loggedin = 'n'
            sql1 = "select memberName , memberPW from members " 
            sql2 = " where  memberName = ? and  memberPW = ? "  
            sql = sql1 + sql2
#            print (sql )
        
            mydata = conn.execute(sql, (name, pw, ))  #############  Step3
            for row in mydata :
                loggedin = 'y'
                
            conn.close()  #############  Step5
            return loggedin
    
    def findNeither (self , name ):
            ###########  step2
            conn = sqlite3.connect('test.db')  # database name, in sqlite3 : if test.db does not exist, it will be created
            register = 'y'
            sql1 = "select memberName , memberPW from members " 
            sql2 = " where  memberName = ?  "  
            sql = sql1 + sql2
#            print (sql )
        
            mydata = conn.execute(sql, (name,))  #############  Step3
            for row in mydata :
                register = 'n'
                
            conn.close()  #############  Step5
            return register
    
    def updateMember (self , oldname, newname):
            ###########  step2
            conn = sqlite3.connect('test.db')  # database name, in sqlite3 : if test.db does not exist, it will be created
            
            sqlinsert  = " update members " 
            sqlcolumns = " set  memberName = ? "  
            sqlvalues  = " where memberName = ? "
            sql = sqlinsert + sqlcolumns + sqlvalues
#            print (sql )
            
            conn.execute(sql, (newname, oldname, ) ) #############  Step3 
            conn.commit() ############   Step 4 ( only for insert , update , delete)
            
            print ( "success") 
            conn.close()  #############  Step5
            
    def deleteMember (self , name):
            ###########  step2
            conn = sqlite3.connect('test.db')  # database name, in sqlite3 : if test.db does not exist, it will be created
            
            sql1  = " delete from members "   
            sql2  = " where memberName = ? "
            sql   = sql1 + sql2 
#            print (sql )
            
            conn.execute(sql, (name, ) ) #############  Step3 
            conn.commit() ############   Step 4 ( only for insert , update , delete)
            
            print ( "success") 
            conn.close()  #############  Step5
        
    def printMembers(self):
        ###########  step2
        conn  = sqlite3.connect('test.db')  # database name, in sqlite3 : if test.db does not exist, it will be created
        sql  = "select m_ID , memberName , memberPW  from members "  
        print (sql)
        
        mydata = conn.execute(sql)  #############  Step3
        for row in mydata :
            print(row)
        
        print ( "success") 
        conn.close()    #############  Step5