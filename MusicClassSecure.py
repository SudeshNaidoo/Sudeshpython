
import datetime
from pysqlitecipher import sqlitewrapper
import hashlib


currentDateTime = datetime.datetime.now()

obj = sqlitewrapper.SqliteCipher (dataBasePath="music.db" ,checkSameThread=False , password='keypassword123456')


# MusicClassSecure.py
class MusicClassSecure:

    def add(self,a,b):
        return a
    
def method():
    print("OUTPUT")


def add(UserName,MusicName , MusicLyrics, MusicScore, MusicType,MusicDataPath):
    
    ## Adds music data to the 'music' table in the database
    ##used md5 hashing from Hash library
    md5_hash = hashlib.md5()
    

    with open(MusicDataPath, 'rb') as file:
        while True:
            chunk = file.read(8192)  # Read 8 KB at a time

            if not chunk:
                break
            md5_hash.update(chunk)
        
        MusicData = file.read()


    MusicCheckSum = md5_hash.hexdigest()

    insertList = [MusicName,MusicLyrics,MusicScore,MusicType,UserName,currentDateTime,MusicData,MusicCheckSum]
    obj.insertIntoTable('music' , insertList , commit = True)
    print('Record inserted successfully - File CheckSum is : '+MusicCheckSum)
    
    ##Prints data from the 'music' table based on the username provided.
    ##    dataarray (list): List of music records.
    ##    username (str): Username or 'ALL' to display all records.
def printTableData(dataarray,username):

    if username == 'ALL':
        #Print header for all records
        print(dataarray[0][0].ljust(5,' ')+dataarray[0][1].ljust(30,' ')+dataarray[0][2].ljust(50,' ')+dataarray[0][3].ljust(12,' ')+dataarray[0][8].ljust(36,' ')+dataarray[0][5].ljust(10,' '))
    else:
        #print header for specific user
        print(dataarray[0][0].ljust(5,' ')+dataarray[0][1].ljust(30,' ')+dataarray[0][2].ljust(50,' ')+dataarray[0][3].ljust(12,' ')+dataarray[0][8].ljust(36,' '))
        
    for v in dataarray[1]:
        if username == 'ALL':
              #print data for all  records
              print(str(v[0]).ljust(5,' ')+v[1].ljust(30,' ')+str(v[2]).ljust(50,' ')+str(v[3]).ljust(12,' ')+str(v[8]).ljust(36,' ')+str(v[5]).ljust(10,' '))
        else:
              #print data for specific user
              if v[5] == username:
                  print(str(v[0]).ljust(5,' ')+v[1].ljust(30,' ')+str(v[2]).ljust(50,' ')+str(v[3]).ljust(12,' ')+str(v[8]).ljust(36,' '))

                  
        
          

          

def view(username):
    #Prints music records for a specific user.
    #username (str): Username or 'ALL' to display all records.
    printTableData(
    obj.getDataFromTable('music' , raiseConversionError = True , omitID = False),username)

 ##Prints data from the “music” table based on the username provided

def viewAll():
    #Prints all music records
    printTableData(
    obj.getDataFromTable('music' , raiseConversionError = True , omitID = False),'ALL')

def delete(id):
    #Deletes a record from the 'music' table by ID
    obj.deleteDataInTable(tableName='music',iDValue=id)

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
        ['CreationDate','char'],
        ['MusicData','blob'],
        ['MusicCheckSum','char']]
        
        obj.createTable('music' , colList, makeSecure=True , commit=True)
