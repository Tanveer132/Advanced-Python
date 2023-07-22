import mysql.connector
#Assume the MySQL server is running on 'localhost', database name is 'mydb' and user is 'root'
con = mysql.connector.connect(host="localhost", user="root", password="", database="mydb")
cur = con.cursor()

cur.execute('SELECT increase_by_100(%s)', [10])
print(cur.fetchone())

#Closing curson and connection to avoid collision with other connections which are using same database
cur.close()
con.close()