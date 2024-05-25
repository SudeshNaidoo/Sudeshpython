import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('music2.db')
 
# cursor object
cursor_obj = connection_obj.cursor()

#drop table if already exist
#cursor_obj.execute('DROP TABLE IF EXISTS')

#create table
table = """ CREATE TABLE MUSIC (UserName VARCHAR(25) NOT NULL,
Password VARCHAR(25) NOT NULL,
UserID INTEGER (8) );"""

cursor_obj.execute(table)

print("Table is Ready")
# Close the connection
connection_obj.close()
