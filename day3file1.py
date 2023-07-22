import mysql.connector
#Assume the MySQL server is running on 'localhost', database name is 'mydb' and user is 'root'
con = mysql.connector.connect(host="localhost", user="root", password="", database="mydb")
cur = con.cursor()

#executing query
cur.execute("truncate table Computer")
cur.execute("INSERT INTO Computer VALUES (1001,'Dell','2015')")
cur.execute("INSERT INTO Computer VALUES (1002,'Dell','2013')")
cur.execute("INSERT INTO Computer VALUES (1003,'Lenovo','2018')")
cur.execute("INSERT INTO Computer VALUES (1004,'Apple','2020')")
cur.execute("INSERT INTO Computer VALUES (1005,'Apache','2022')")
print(f"inserting into table = {cur.rowcount}")

#Delete operation
param = 1005
cur.execute("delete from Computer where idComputer="+str(param))
print("deleting into table =",cur.rowcount)

#Committing the changes
con.commit()

#Select query
cur.execute("SELECT * FROM Computer")
for row in cur:
    print(row)
    print(row[1],row[2])

#Closing curson and connection to avoid collision with other connections which are using same database
cur.close()
con.close()

