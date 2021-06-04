# -*- coding: utf-8 -*-
import sqlite3

############## Update a record
conn = sqlite3.connect('test.db')
conn.execute("update customerRegistration set salary = 1800   where name = 'Mary'")
conn.commit()
conn.close()

############## Delete a record
conn = sqlite3.connect('test.db')
conn.execute("delete from customerRegistration  where name = 'Anton'")
conn.commit()
conn.close()


############## print all records
conn = sqlite3.connect('test.db')
print('Display result set of the select clause')
mydata = conn.execute("select c_ID, name, age , salary from customerRegistration order by c_ID")
for row in mydata:
    print ( row )   
conn.close()


