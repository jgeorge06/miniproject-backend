import os
import pymysql
import pymysql.cursors

riasec = ["R", "I", "A", "S", "E", "C"]

def store(user, answers):
    try:
        mydb = pymysql.connect(
            host=os.getenv("MYSQLHOST"),
            user=os.getenv("MYSQLUSER"),
            passwd=os.getenv("MYSQLPASSWORD"),
            database=os.getenv("MYSQLDATABASE"),
            cursorclass=pymysql.cursors.Cursor
        )
        with mydb.cursor() as cursor:
            if not retrieve(user):
                cursor.execute("INSERT INTO users (uid) VALUES (%s);", (user,))
            for i in range(48):
                column = riasec[i // 8] + str((i % 8) + 1)
                query = "UPDATE users SET {}=%s WHERE uid=%s;".format(column)
                cursor.execute(query, (answers[i], user))

        mydb.commit()
        mydb.close()
    except Exception as e:
        print("Error: ",e)

def retrieve(user):
    try:
        mydb = pymysql.connect(
            host=os.getenv("MYSQLHOST"),
            user=os.getenv("MYSQLUSER"),
            passwd=os.getenv("MYSQLPASSWORD"),
            database=os.getenv("MYSQLDATABASE"),
            cursorclass=pymysql.cursors.Cursor
        )
        with mydb.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE uid = %s;", (user,))
            print (cursor)
            data = cursor.fetchall()
            print(data)
        mydb.close()
        return data
    except Exception as e:
        print("Error: ",e)
        return []
