
import datetime
from pysqlitecipher import sqlitewrapper


currentDateTime = datetime.datetime.now()

obj = sqlitewrapper.SqliteCipher (dataBasePath="music.db" ,checkSameThread=False , password='keypassword123456')


# MusicClassSecure.py
class MusicClassSecure:

    def add(self,a,b):
        return a
    
def method():
    print("OUTPUT")


def add(USERNAME,MusicName , MusicLyrics, MusicScore, MusicType):

    insert_query = "INSERT INTO Music (USERNAME,MusicName , MusicLyrics, MusicScore, MusicType, CreationDate, ModDate) VALUES (?, ?, ?, ?, ?, ? ,?)"

    viewAll()
    


def view(username):
    #cur.execute('select * from Music where USERNAME = ?',(username,))
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
    #cur.execute('select * from Music')
    rows = cur.fetchall()
    print('Viewing all Music')
    print()
    for row in rows:
        print(row)
    #conn.close()


def initialise():
#        conn.execute(""" CREATE TABLE Music (MusicID INTEGER PRIMARY KEY,
#MusicName CHAR(25) NOT NULL,
#MusicLyrics CHAR (255), MusicScore INTEGER(25), MusicType CHAR(20), USERNAME INTEGER, CreationDate TIMESTAMP, ModDate TIMESTAMP);""");

    colList = [
	['MusicID', 'int' ] ,
	['MusicName' , 'char' ],
    ['MusicLyrics','char'],
    ['MusicScore','int'],
    ['MusicType','char'],
    ['UserName','int'],
    ['CreationDate','char']]
    
    obj.createTable('music' , colList, makeSecure=True , commit=True)