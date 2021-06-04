import sqlite3
# setup data
conn = sqlite3.connect('test.db')

selects = "select * "
froms   = "from customers "
orderby = "order by name "
query = selects + froms + orderby

# process
mydata = conn.execute(query) 

# results and output
for line in mydata:
    # code
    print(line)

conn.close()

# setting up the data
finput = open("C:\\Users\\u\\.spyder-py3\\Stu_LondonFeb25\\movies4.csv", "r" ) 
 
for line in finput : 
    print (line)
 
finput.close()