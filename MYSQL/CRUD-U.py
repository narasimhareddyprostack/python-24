import mysql.connector
try:
    dbcon = mysql.connector.connect(host="localhost", user="root",password="root", database="pydb")
    dbcursor = dbcon.cursor()
    
    dbcursor.execute("insert into employeeone(id, name, email, salary) values(104, 'Surya', 'Surya@gmail.com', 155000)")
    print("Data Inserted")

    dbcon.commit()

    dbcursor.close()
    dbcon.close()
    
except DatabaseError  as err:
    print('Unable to Establish Connection')
    print(err)


