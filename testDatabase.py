import sqlite3
#
#conn = sqlite3.connect('test.db')
#conn.execute("CREATE TABLE customers (c_ID  int, name text, age int, address text, salary real);")
#conn.close()

#conn = sqlite3.connect('test.db')
#conn.execute("CREATE TABLE orders (Order_ID  int, c_ID int, orderamount real);")
#conn.close()

#conn = sqlite3.connect('test.db')
#conn.execute("insert into orders (Order_ID, c_ID, orderamount) values (1, 25, 100) ;")
#conn.execute("insert into orders (Order_ID, c_ID, orderamount) values (2, 25, 200) ;")
#conn.execute("insert into orders (Order_ID, c_ID, orderamount) values (3, 25, 300) ;")
#conn.commit()
#conn.close()

#
#conn = sqlite3.connect('test.db')
#conn.execute("insert into customers(c_ID, name, age , salary) values (25,'Peter',10,1000.0);")
#conn.execute("insert into customers(c_ID, name,age ,address, salary ) values (26,'John',20,'Bristol',2000.0);")
#conn.execute("insert into customers(c_ID, name,age ,address, salary ) values (27,'Paul',30,'Leeds',3000.0);")
#conn.execute("insert into customers(c_ID, name,age ,address, salary ) values (26,'Pauline',20,'Brighton',2500.0);")
#conn.execute("insert into customers(c_ID, name,age ,address, salary ) values (27,'Jenny',30,'Leeds',3500.0);")
#conn.commit()
#conn.close()

conn = sqlite3.connect('test.db')

# select name, age, salary from customers
# select name , age, salary, salary * 1.1  from customers  

### aggregate queries and group by
# select count (*) from customers
# select sum(salary) , count(*) from customers where salary > 2000
# select age, count(*), sum(salary) , avg(salary)  from customers group by age

### joins
# select name, age, orderamount from customers inner join orders on customers.c_ID = orders.c_ID
# select customers.c_ID , name , sum(orderamount )  
        #from customers inner join orders on customers.c_ID = orders.c_ID
        #group by customers.c_ID, name"

select = "select customers.c_ID , name ,   sum(orderamount )  "
fromstatement = "from customers inner join orders on customers.c_ID = orders.c_ID  "
where = ""
groupby = "group by customers.c_ID, name "
orderby = ""

query = select + fromstatement  + where + groupby + orderby
print (query)
print('Display result set of the select clause')
mydata = conn.execute(query)
for row in mydata:
    print ( row )   
conn.close()


"""
# how many people have a salary over 2000
# how many people are on the database
# what is the total salary
"""


