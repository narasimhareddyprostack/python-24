import mysql.connector

dbcon = mysql.connector.connect(host="localhost", user="root",password="root", database="dbproduct")
dbcursor = dbcon.cursor()
dbcursor.execute('select *from user')

for row in dbcursor:
    print('Emp Id: {} and Emp Name'.format(row[0], row[4]))
    print()
    print()

dbcursor.close()
dbcon.close()