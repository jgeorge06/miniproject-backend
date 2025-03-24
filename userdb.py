import os
import math
import pymysql
import pymysql.cursors

riasec=["RIASEC"]
def store(user,answers):
    try:
        mydb=pymysql.connect(host=os.getenv("MYSQLHOST"),user=os.getenv("MYSQLUSER"), passwd=os.getenv("MYSQLPASSWORD"), database=os.getenv("MYSQLDATABASE"),cursorclass=pymysql.cursors.Cursor)
        with mydb.cursor() as cursor:
            if retrieve(user)==[]:
                cursor.execute("insert into users (uid) values ('%s');",user)
                for i in range(48):
                    column=riasec[48/i]+str((48%i)+1)
                    cursor.execute("update users set %s=%s where uid='%s';" ,column,answers[48],user)
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