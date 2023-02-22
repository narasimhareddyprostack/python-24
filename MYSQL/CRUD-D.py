import mysql.connector
dbcon = mysql.connector.connect(host="localhost", user="root", password="root" ,database="pydb")
dbcursor = dbcon.cursor()

sqld="DELETE FROM employeeone where id=101"
dbcursor.execute(sqld)
dbcon.commit()

dbcursor.close()
dbcon.close()
