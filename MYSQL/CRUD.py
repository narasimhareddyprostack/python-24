import mysql.connector
try:
    dbcon = mysql.connector.connect(host="localhost", user="root",password="root", database="pydb")
    dbcursor = dbcon.cursor()
    
    dbcursor.execute("create table employeeOne(id int, name varchar(32), email varchar(32), salary int)")
    print("Table Created")

except DatabaseError  as err:
    print('Unable to Establish Connection')
    print(err)