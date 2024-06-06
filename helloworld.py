
import sqlite3
from pysqlitecipher import sqlitewrapper
## this is for testing
##class obj:
	###def _init_(self,tableName ,colList, insertList, iDValue, colName, colValue, newPass ):
	#	self.tableName = tableName
	##	self.colList = colList
		#self.insertList = insertList
	#	self.iDValue = iDValue
		#self.colName = colName
		#self.colValue = colValue
		#self.newPass = newPass


# make the object 

obj = sqlitewrapper.SqliteCipher (dataBasePath="pysqlitecipher.db" ,checkSameThread=False , password='keypassword123456')
colList = [
	['music', 'CHAR' ] ,
	['whatever' , 'int' ] ,
]

## created table # out after creation
##obj.createTable('testtable' , colList, makeSecure=True , commit=True)

def printTableData(dataarray):
	print(dataarray[0][0].ljust(4,' ')+dataarray[0][1].ljust(10,' ')+dataarray[0][2].ljust(10,' '))
	for v in dataarray[1]:
		print(str(v[0]).ljust(4,' ')+v[1].ljust(10,' ')+str(v[2]).ljust(10,' '))



	
insertList = ['musictest', 89]
obj.insertIntoTable('testtable' , insertList , commit = True)

printTableData(
obj.getDataFromTable('testtable' , raiseConversionError = True , omitID = False))

obj.deleteDataInTable('testtable' , 0 , commit= True , raiseError= True , updateId = True)

print(
obj.getDataFromTable('testtable' , raiseConversionError = True , omitID = False))

##obj.getDataFromTable(tableName , raiseConversionError = True , omitID = False)


##obj.updateInTable(tableName , iDValue ,colName , colValue , commit = True , raiseError = True)
###obj.changePassword(newPass)



#try:
#
#	# Connect to DB and create a cursor
#	sqliteConnection = sqlite3.connect('sql.db')
##	print('DB Init')
#
#	# Write a query and execute it with cursor
#	query = 'select sqlite_version();'
#	cursor.execute(query)

	# Fetch and output result
##	result = cursor.fetchall()
	#print('SQLite Version is {}'.format(result))

	# Close the cursor
	#cursor.close()



