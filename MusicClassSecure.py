
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


def add(UserName,MusicName , MusicLyrics, MusicScore, MusicType):
    insertList = [MusicName,MusicLyrics,MusicScore,MusicType,UserName,currentDateTime]
    obj.insertIntoTable('music' , insertList , commit = True)
    viewAll()
    


def view(username):
    #cur.execute('select * from Music where USERNAME = ?',(username,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

def printTableData(dataarray):
	print(dataarray[0][0].ljust(4,' ')+dataarray[0][1].ljust(10,' ')+dataarray[0][2].ljust(10,' '))
	for v in dataarray[1]:
		print(str(v[0]).ljust(4,' ')+v[1].ljust(10,' ')+str(v[2]).ljust(10,' '))


def viewAll():
    printTableData(
    obj.getDataFromTable('music' , raiseConversionError = True , omitID = False))


def initialise():

    if obj.checkTableExist('music'):
        print('Table already exists - ignoring')
    else:    
        colList = [
        ['MusicName' , 'char' ],
        ['MusicLyrics','char'],
        ['MusicScore','int'],
        ['MusicType','char'],
        ['UserName','int'],
        ['CreationDate','char']]
        
        obj.createTable('music' , colList, makeSecure=True , commit=True)
