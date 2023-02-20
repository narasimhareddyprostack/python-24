import mysql.connector
dbcon = mysql.connector.connect(host="localhost", user="root",password="root", database="dbproduct")

if dbcon !='None':
    print("Connection Success")
else:
    print("Failure")
