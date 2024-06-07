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

obj = sqlitewrapper.SqliteCipher (dataBasePath="MusicSecure.db" ,checkSameThread=False , password='keypassword123456')
colList = [
	['MusicID', 'INT' ] ,
	['MusicName' , 'INT' ] ,
	['MusicLyrics' ,'CHAR'],
	['MusicScore' , 'INT'],
	['MusicType' ,'CHAR' ],
	['UserID', 'INT'],
	['CreationDate', 'INT'],
	['ModDate', 'INT']
	
]

## created table # out after creation
##obj.createTable('testtable2' , colList, makeSecure=True , commit=True)

def printTableData(dataarray):
	print(dataarray[0][0].ljust(4,' ')+dataarray[0][1].ljust(10,' ')+dataarray[0][2].ljust(10,' ')+dataarray[0][3].ljust(5,' ')+dataarray[0][4].ljust(10,' ')+dataarray[0][5].ljust(10,' ')+dataarray[0][2].ljust(10,' ')+dataarray[0][2].ljust(10,' '))
	for v in dataarray[1]:
		print(str(v[0]).ljust(4,' ')+str(v[1]).ljust(10,' ')+str(v[2]).ljust(10,' ')(v[3]).ljust(10,' ')(v[4]).ljust(10,' ')+str(v[5]).ljust(10,' ')+str(v[6]).ljust(10,' ')+str(v[7]).ljust(10,' '))



insertList = [1, 67 ,'ooh lalala ',9,'popular',9,2014,2024]
obj.insertIntoTable('testtable2' , insertList , commit = True)

printTableData(
obj.getDataFromTable('testtable2' , raiseConversionError = True , omitID = False))

#obj.deleteDataInTable('testtable1' , 0 , commit= True , raiseError= True , updateId = True)

#print(
#obj.getDataFromTable('testtable1' , raiseConversionError = True , omitID = False))

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
