
import sqlite3
conn = sqlite3.connect('user.db')
cur = conn.cursor()

# UserClass.py
class User_class:

    def add(self,a,b):
        return a
    
def method():
    print("OUTPUT")


def add(userid,password):

    insert_query = "INSERT INTO Users (USERNAME, PASSWORD) VALUES (?, ?)"
    conn.execute(insert_query, (userid, password))
    conn.commit()
    #conn.close()
    

    print('Added User '+ userid)


def view(userid):
    cur.execute('select * from users where userid = '+userid)
    rows = cur.fetchall()

    for row in rows:
        print(row)


def verify(username,password):
    cur.execute('select * from Users where USERNAME = ? and PASSWORD = ?',(username,password))
    rows = cur.fetchall()

    for row in rows:
        return 'Y'
    
    return 'N'

    


def viewAll():
    cur.execute('select * from users')
    rows = cur.fetchall()

    for row in rows:
        print(row)


def initialise():
    conn.execute('''DROP TABLE Users''')
    conn.execute('''CREATE TABLE Users(
                    USERNAME TEXT,
                    PASSWORD TEXT,
                    USERID INTEGER PRIMARY KEY);''')
    
	

    

