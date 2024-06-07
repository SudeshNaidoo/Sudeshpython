import sqlite3
import datetime
from pysqlitecipher import sqlitewrapper



conn = sqlite3.connect('user.db')
cur = conn.cursor()

currentDateTime = datetime.datetime.now()


# make the object 

#obj = sqlitewrapper.SqliteCipher (dataBasePath="pysqlitecipher.db" ,checkSameThread=False , password='keypassword123456')
#colList = [
	#['music', 'CHAR' ] ,
#	['whatever' , 'int' ] ,
#]

## created table hash out after creation
##obj.createTable('testtable' , colList, makeSecure=True , commit=True)

##def printTableData(dataarray):
	#print(dataarray[0][0].ljust(4,' ')+dataarray[0][1].ljust(10,' ')+dataarray[0][2].ljust(10,' '))
	#for v in dataarray[1]:
	#	print(str(v[0]).ljust(4,' ')+v[1].ljust(10,' ')+str(v[2]).ljust(10,' '))



	
#insertList = ['musictest', 89]
#obj.insertIntoTable('testtable' , insertList , commit = True)

#printTableData(
#obj.getDataFromTable('testtable' , raiseConversionError = True , omitID = False))

#obj.deleteDataInTable('testtable' , 0 , commit= True , raiseError= True , updateId = True)

#print(
#obj.getDataFromTable('testtable' , raiseConversionError = True , omitID = False))

##obj.getDataFromTable(tableName , raiseConversionError = True , omitID = False)


##obj.updateInTable(tableName , iDValue ,colName , colValue , commit = True , raiseError = True)
###obj.changePassword(newPass)

# MusicClass.py
#class Music_class:

   ## def add(self,a,b):
     #   return a
    
#def method():
   # print("OUTPUT")


#def add(USERNAME,MusicName , MusicLyrics, MusicScore, MusicType):

    #insert_query = "INSERT INTO Music (USERNAME,MusicName , MusicLyrics, MusicScore, MusicType, CreationDate, ModDate) VALUES (?, ?, ?, ?, ?, ? ,?)"
    #conn.execute(insert_query, (USERNAME,MusicName , MusicLyrics, MusicScore, MusicType, currentDateTime, currentDateTime))
    #conn.commit()
    #conn.close()
    #viewAll()
    


#def view(username):
    #cur.execute('select * from Music where USERNAME = ?',(username,))
    #rows = cur.fetchall()

    #for row in rows:
       # print(row)


##def verify(username,password):
  ##  cur.execute('select * from Users where USERNAME = ? and PASSWORD = ?',(username,password))
  ##  rows = cur.fetchall()

   ### for row in rows:
    ##    return 'Y'
    
  ##  return 'N'

    


#def viewAll():
    #cur.execute('select * from Music')
    #rows = cur.fetchall()
    #print('Viewing all Music')
    #print()
    #for row in rows:
       # print(row)
    #conn.close()


def initialise():

    ##insecure table creation 
    ##conn.execute('''DROP TABLE Music''')
    ##conn.execute(""" CREATE TABLE Music (MusicID INTEGER PRIMARY KEY,
##MusicName CHAR(25) NOT NULL,
##MusicLyrics CHAR (255), MusicScore INTEGER(25), MusicType CHAR(20), USERNAME INTEGER, CreationDate TIMESTAMP, ModDate TIMESTAMP);""");


# make the object 

 obj = sqlitewrapper.SqliteCipher (dataBasePath="music.db" ,checkSameThread=False , password='keypassword123456')
colList = [
	['MusicName', 'CHAR' ],
	['MusicLyrics' , 'CHAR' ],
    ['MusicScore', 'INT'],
    ['MusicType', 'CHAR'],
    ['USERNAME','INT'],
    ['CreationDate', 'TIMESTAMP'],
    ['MusicID', 'INT PRIMARY KEY'],
    ['ModDate', 'TIMESTAMP']

]

## created table hashed out after creation
##obj.createTable('music' , colList, makeSecure=True , commit=True)

#Secure Table creation
#obj.createTable('Music' , colList, makeSecure=True , commit=True)
#colList = [
#	['MusicName', 'CHAR' ],
#	['MusicLyrics' , 'CHAR' ],
 #   ['MusicScore', 'INT'],
 #   ['MusicType', 'CHAR'],
 #   ['USERNAME','INT'],
 #   ['CreationDate', 'TIMESTAMP'],
 #   ['MusicID', 'INT PRIMARY KEY'],
 #   ['ModDate', 'TIMESTAMP']
#
 #    ]
    
    #Encrypt music table DB
obj = sqlitewrapper.SqliteCipher (dataBasePath="MusicDBSecure.db" ,checkSameThread=False , password='keypassword123456')
colList = [
	['MusicName', 'CHAR' ],
	['MusicLyrics' , 'CHAR' ],
    ['MusicScore', 'INT'],
    ['MusicType', 'CHAR'],
    ['USERNAME','INT'],
    ['CreationDate', 'TIMESTAMP'],
    ['MusicID', 'INT PRIMARY KEY'],
    ['ModDate', 'TIMESTAMP']

     ]
    
def printTableData(dataarray):
        print(dataarray[0][0].ljust(4,' ')+dataarray[0][1].ljust(10,' ')+dataarray[0][2].ljust(10,' ')+dataarray[0][3].ljust(10,' ')+dataarray[0][4].ljust(10,' '))
        for v in dataarray[1]: 
            print(dataarray[0][0].ljust(4,' ')+dataarray[0][1].ljust(10,' ')+dataarray[0][2].ljust(10,' ')+dataarray[0][3].ljust(10,' ')+dataarray[0][4].ljust(10,' '))

            #test insert list 
		
insertList = ['Mr Bombastic', 'lyrics', 10, 'pop', 1234567]
obj.insertIntoTable('Music' , insertList , commit = True)
    
printTableData(
obj.getDataFromTable('Music' , raiseConversionError = True , omitID = False))
    
#obj.deleteDataInTable('Music' , 0 , commit= True , raiseError= True , updateId = True)



