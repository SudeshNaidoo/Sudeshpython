
import sqlite3

try:

	# Connect to DB and create a cursor
	sqliteConnection = sqlite3.connect('sql.db')
	cursor = sqliteConnection.cursor()
	print('DB Init')

	# Write a query and execute it with cursor
	query = 'select sqlite_version();'
	cursor.execute(query)

	# Fetch and output result
	result = cursor.fetchall()
	print('SQLite Version is {}'.format(result))

	# Close the cursor
	cursor.close()

# Handle errors
except sqlite3.Error as error:
	print('Error occurred - ', error)

# Close DB Connection irrespective of success
# or failure
finally:

	if sqliteConnection:
		sqliteConnection.close()
		print('SQLite Connection closed')

import sqlite3

#create connection to DB
cnt = sqlite3.connect('user.db')

# create User class table
cnt.execute('''CREATE TABLE Users(
USERNAME TEXT,
PASSWORD TEXT,
USERID INTEGER);''')

#Open file in read mode
#read image as bianary data in variable
##fileh = open('/C:\Users\Admin\Documents\GitHub\Sudeshpython\Screenshot1.png','rb')
##img = fileh.read()

#insert tuples for realtion
###was not created --need method ?
##cnt.execute('''verify(UserId)

connection = sqlite3.connect('users.db')
#add to Users table manually
connection.execute('INSERT INTO users.db VALUES(Sudesh, abc123456, 1)')
connection.execute('INSERT INTO users.db VALUES (TEST, pwd123, 2)')
connection.execute('INSERT INTO users.db VALUES (TESTer, pwd1234, 3)')

print('All data in users table\n')

# create a cousor object for select query
cursor = connection.execute('SELECT * from users')

#display all data from table
for row in cursor:
	print(row)

#create class method
class User_class:
	
	def _init_(Self,Verify, Add, DeleteOwnMusic, View, ModOwnMusic, ModifyGenre ):
		Self.Verify = Verify
		Self.Add = Add
		Self.DeleteOwnMusic = DeleteOwnMusic
		Self.View = View
		Self.ModifyOwnMusic = ModOwnMusic
		Self.ModifyGenre = ModifyGenre

    ##@classmethod
    ##def Add(self, name, birthYear):
       ## return cls(name, date.today().year - birthYear)

 #create Music_class
class Music_class:
	def _init_(self,Play ,Download, Upload, Modify):
		self.Play = Play
		self.Download = Download
		self.Upload = Upload
		self.Modify = Modify
