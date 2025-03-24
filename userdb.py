import os
import math
import pymysql
import pymysql.cursors

def store(user,answers):
    try:
        mydb=pymysql.connect(host=os.getenv("MYSQLHOST"),user=os.getenv("MYSQLUSER"), passwd=os.getenv("MYSQLPASSWORD"), database=os.getenv("MYSQLDATABASE"),cursorclass=pymysql.cursors.Cursor)
        with mydb.cursor() as cursor:
            cursor.execute("insert into users values ('"+("%s,"*48)+"%s""');",user,*answers)
        mydb.close()
    except Exception as e:
        print("Error: ", e)

def retrieve(user):
    try:
        mydb=pymysql.connect(host=os.getenv("MYSQLHOST"),user=os.getenv("MYSQLUSER"), passwd=os.getenv("MYSQLPASSWORD"), database=os.getenv("MYSQLDATABASE"),cursorclass=pymysql.cursors.Cursor)
        with mydb.cursor() as cursor:
            cursor.execute("select * from users where uid='%s'",user)
            data = cursor.fetchall()
        mydb.close()
        print(data)
        return data
    except Exception as e:
        print("Error: ", e)