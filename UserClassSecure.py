
import datetime
from pysqlitecipher import sqlitewrapper
import hashlib

# Get the current date and time
currentDateTime = datetime.datetime.now()

#Initialize the SQLite database with encryption
obj = sqlitewrapper.SqliteCipher (dataBasePath="music.db" ,checkSameThread=False , password='keypassword123456')


# UserClassSecure.py
class UserClassSecure:

    def add(self,a,b):
        return a
    
def method():
    print("OUTPUT")

def hash_password(username, password):
#Hashes the password using a special salt.

    SudeshsSpecialSalt = 'SaltyIsntThis'
    combined_string = f"{username}:{password}:{SudeshsSpecialSalt}"
    #print(combined_string) with salt
    
    hashed = hashlib.sha512(combined_string.encode()).hexdigest()
    #print(hashed)
    
    return hashed

def add(Username, Password,AdminFlag):
# Adds a user record to the 'user' table in the database.
    hashedPassword = hash_password(username=Username,password=Password)
    insertList = [Username,hashedPassword,AdminFlag]
    obj.insertIntoTable('user' , insertList , commit = True)
    print('Record inserted successfully')
    


def printTableData(dataarray,username):
    # Prints data from the 'user' table based on the username provided.
    if username == 'ALL':
        print(dataarray[0][0].ljust(5,' ')+dataarray[0][1].ljust(30,' ')+dataarray[0][2].ljust(200,' ')+dataarray[0][3].ljust(7,' '))
    else:
        print(dataarray[0][0].ljust(5,' ')+dataarray[0][1].ljust(30,' '))
        
    for v in dataarray[1]:
        if username == 'ALL':
           # Print data for all records
              print(str(v[0]).ljust(5,' ')+v[1].ljust(30,' ')+str(v[2]).ljust(200,' ')+str(v[3]).ljust(7,' '))
        else:
               # Print data for specific user
              if v[1] == username:
                  print(str(v[0]).ljust(5,' ')+v[1].ljust(30,' '))

                      
        
          
def verify(username,password):
    # Verifies the user's credentials.
    dataarray = obj.getDataFromTable('user' , raiseConversionError = True , omitID = False)
    for v in dataarray[1]:
        if v[1] == username:
            if v[2] == hash_password(username=username,password=password):
                return 'Y'
    return 'N'
        

def isAdmin(username):
    #Checks if the user is an admin.
    dataarray = obj.getDataFromTable('user' , raiseConversionError = True , omitID = False)
    for v in dataarray[1]:
        if v[1] == username:
            if v[3] == 'Y':
                return 'Y'
    return 'N'
          
		


def view(username):
    # Prints user records for a specific user.
    printTableData(
    obj.getDataFromTable('user' , raiseConversionError = True , omitID = False),username)



def viewAll():
    #Prints all user records.
    printTableData(
    obj.getDataFromTable('user' , raiseConversionError = True , omitID = False),'ALL')

  
    

def initialise():
#Initializes the 'user'
    colList = [
	['Username', 'int' ] ,
	['Password' , 'char' ],
    ['Admin','char']
    ]    

    obj.createTable('user' , colList, makeSecure=True , commit=True)

  # Initializes the 'CheckIfTableIsSecure' table
  #  check_table_colList = [
  #      # Define your columns here (e.g., ['Column1', 'datatype'], ['Column2', 'datatype'], ...)
  #      # Example:
  #      ['Username', 'int'],
  #      ['Password', 'char'],
  #      ['Admin', 'char']
  #  ]
  #  
  #  obj.createTable('CheckIfTableIsSecure', check_table_colList, makeSecure=True, commit=True)

