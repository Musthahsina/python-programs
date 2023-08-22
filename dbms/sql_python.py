import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="Sina#@97",port= 3306)
print(mydb)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE maypython")
mycursor.execute("use maypython")
# mycursor.execute("create table students(name varchar(250),age int,roll_num int)")
# sql="insert into students (name,age,roll_num)values(%s,%s,%s)"
# val=("Jerry",15,20)
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [('Peter',16,21),('Amy',15,20),('Hannah',14,20)]
# mycursor.executemany(sql,val)
# mydb.commit()

print(mycursor.rowcount,"record inserted")


"""

SQL INNER JOIN 
----------------

The INNER JOIN keyword selects records that have matching values in both tables.

INNER JOIN Syntax
------------------

SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;

"""
