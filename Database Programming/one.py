import mysql.connector

dbcon=mysql.connector.connect(host='localhost', user='root', password='root')

if dbcon !='None':
    print("Connection Established")
else:
    print("Connection Failed")