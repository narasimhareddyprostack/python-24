import mysql.connector

dbcon = mysql.connector.connect(host="localhost", user="root", password="root" ,database="pydb")
dbcursor = dbcon.cursor()

#sql= "update employeeone set name='Rahul Gandhi' where id=101"
sql = "select * from employeeone"
dbcursor.execute(sql)

#dbcon.commit()

for row in dbcursor:
    print(row)


dbcursor.close()
dbcon.close()