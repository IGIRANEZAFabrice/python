import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database ="testdb")

mycursor = mydb.cursor()

sqlformula = "INSERT INTO students (name, age) VALUES (%s, %s)"
students = [("Eulade", 21),
            ("Kevin", 22),
            ("Eugen", 18),
            ("Aimee", 21),
            ("Foustin", 19),
            ]

mycursor.execute("SELECT age FROM students")
myresult = mycursor.fetchall()

for row in myresult:
    print(row)
