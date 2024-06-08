
import datetime
from pysqlitecipher import sqlitewrapper
import hashlib


currentDateTime = datetime.datetime.now()

obj = sqlitewrapper.SqliteCipher (dataBasePath="music.db" ,checkSameThread=False , password='keypassword123456')


# UserClassSecure.py
class UserClassSecure:

    def add(self,a,b):
        return a
    
def method():
    print("OUTPUT")

def hash_password(username, password):

    SudeshsSpecialSalt = 'SaltyIsntThis'
    combined_string = f"{username}:{password}:{SudeshsSpecialSalt}"
    #print(combined_string)
    
    hashed = hashlib.sha512(combined_string.encode()).hexdigest()
    #print(hashed)
    
    return hashed

def add(Username, Password):

    hashedPassword = hash_password(username=Username,password=Password)
    insertList = [Username,hashedPassword]
    obj.insertIntoTable('user' , insertList , commit = True)
    print('Record inserted successfully')
    


def printTableData(dataarray,username):
    if username == 'ALL':
        print(dataarray[0][0].ljust(5,' ')+dataarray[0][1].ljust(30,' ')+dataarray[0][2].ljust(200,' '))
    else:
        print(dataarray[0][0].ljust(5,' ')+dataarray[0][1].ljust(30,' '))
        
    for v in dataarray[1]:
        if username == 'ALL':
              print(str(v[0]).ljust(5,' ')+v[1].ljust(30,' ')+str(v[2]).ljust(200,' '))
        else:
              if v[1] == username:
                  print(str(v[0]).ljust(5,' ')+v[1].ljust(30,' '))

                      
        
          
def verify(username,password):
    dataarray = obj.getDataFromTable('user' , raiseConversionError = True , omitID = False)
    for v in dataarray[1]:
        if v[1] == username and v[2] == hash_password(username=username,password=password):
            return 'Y'
        else:
            return 'N'
        

          
		


def view(username):
    printTableData(
    obj.getDataFromTable('user' , raiseConversionError = True , omitID = False),username)



def viewAll():
    printTableData(
    obj.getDataFromTable('user' , raiseConversionError = True , omitID = False),'ALL')




def initialise():

    colList = [
	['Username', 'int' ] ,
	['Password' , 'char' ],
    ['Admin','char']
    ]    

    obj.createTable('user' , colList, makeSecure=True , commit=True)

    