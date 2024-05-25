import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('admin.db')
 
# cursor object
cursor_obj = connection_obj.cursor()

#drop table if already exist
#cursor_obj.execute('DROP TABLE IF EXISTS')

#create table
table = """ CREATE TABLE ADMIN (UserName VARCHAR(25) NOT NULL,
Password VARCHAR(25) NOT NULL,
UserID INTEGER (8) );"""

cursor_obj.execute(table)

print("Table is Ready")

#access control
#specify the host
host='localhost',

#specify root account
user='root',

# password for root admin account
password='1234',

#default port for MySQl is 3306
port=3306

# Close the connection
connection_obj.close()

