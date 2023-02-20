import mysql.connector
dbcon = mysql.connector.connect(host="localhost", user="root",password="root", database="dbproduct")

if dbcon !='None':
    print("Connection Success")
    dbcursor = dbcon.cursor()
else:
    print("Failure")


dbcursor.execute("SELECT * FROM user")

print(type(dbcursor))
for row in dbcursor:
    print(row)

dbcursor.close()
dbcon.close()