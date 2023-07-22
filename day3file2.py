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


list_of_ids = [1001,1002,1003,1004]
for id in list_of_ids:
    #Binding parameters increase fetching performance
    cur.execute("SELECT * FROM Computer WHERE idComputer=%(c_id)s", {"c_id":id} )
    for idComputer,Make,MYear in cur:
        print(Make,idComputer)

#Exception Handling 
try:
    param = 1005
    query = "delete from iComputer where idComputer="+str(param)
    cur.execute(query)    #Binding parameters
    con.commit()
    #Select query
    cur.execute("SELECT * FROM Computer")
    for row in cur:
        print(row)
except mysql.connector.ProgrammingError as e:
    print(e)
finally:
    cur.close()
    con.close()