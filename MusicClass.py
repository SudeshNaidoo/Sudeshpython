
import sqlite3
conn = sqlite3.connect('user.db')
cur = conn.cursor()

# MusicClass.py
class Music_class:

    def add(self,a,b):
        return a
    
def method():
    print("OUTPUT")


def add(USERNAME,MusicName ,MusicID, MusicLyrics, MusicScore, MusicType, CreationDate, ModDate):

    insert_query = "INSERT INTO Music (USERNAME,MusicName ,MusicID, MusicLyrics, MusicScore, MusicType, CreationDate, ModDate) VALUES (?, ?, ?, ?, ?, ? ,? ,?)"
    conn.execute(insert_query, (USERNAME,MusicName ,MusicID, MusicLyrics, MusicScore, MusicType, CreationDate, ModDate))
    conn.commit()
    #conn.close()
    

    print('Added User '+ USERNAME)


def view(USERNAME):
    cur.execute('select * from Music where USERNAME = '+USERNAME)
    rows = cur.fetchall()

    for row in rows:
        print(row)


##def verify(username,password):
  ##  cur.execute('select * from Users where USERNAME = ? and PASSWORD = ?',(username,password))
  ##  rows = cur.fetchall()

   ### for row in rows:
    ##    return 'Y'
    
  ##  return 'N'

    


def viewAll():
    cur.execute('select * from Music')
    rows = cur.fetchall()

    for row in rows:
        print(row)


def initialise():
    conn.execute('''DROP TABLE Music''')
    conn.execute(""" CREATE TABLE MUSIC (MusicID INTEGER PRIMARY KEY,
MusicName CHAR(25) NOT NULL,
MusicLyrics CHAR (255), MusicScore INTEGER(25), MusicType CHAR(20), USERNAME INTEGER, CreationDate INTEGER(08), ModDate INTEGER(8) );""");
    
	


