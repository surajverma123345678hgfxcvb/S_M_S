import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Suraj@123",
  database="student_sms"
)
mycursor = mydb.cursor()

mycursor.execute("create table student_form( f_name VARCHAR(50) NOT NULL, l_name VARCHAR(50) NOT NULL, course VARCHAR(30) NOT NULL, subject VARCHAR(50) NOT NULL, year Int(10) NOT NULL, age Int(10) NOT NULL, gender char(10) NOT NULL, birth DATE NOT NULL, contact VARCHAR(15) NOT NULL, email VARCHAR(100) NOT NULL, PRIMARY KEY ( contact ) );")