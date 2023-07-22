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

#Committing the changes
con.commit()

#Fetching methods to get countable rows from selected data
cur.execute("SELECT * FROM Computer")
print(cur.fetchone())
print("fetchmany method \n",cur.fetchmany())
print("fetchmany(2) method \n",cur.fetchmany(2))
print("fetchall method \n",cur.fetchall())

#Closing curson and connection to avoid collision with other connections which are using same database
cur.close()
con.close()
