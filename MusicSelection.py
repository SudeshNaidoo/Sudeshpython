import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('MusicSelection.db')
 
# cursor object
cursor_obj = connection_obj.cursor()

#drop table if already exist
#cursor_obj.execute('DROP TABLE IF EXISTS')

#create table
table = """ CREATE TABLE MUSIC (MusicID INTEGER(25) NOT NULL,
MusicName CHAR(25) NOT NULL,
MusicLyrics CHAR (255), MusicScore INTEGER(25), MusicType CHAR(20), UserId INTEGER(25), CreationDate INTEGER(08), ModDate INTEGER(8) );"""

cursor_obj.execute(table)

print("Table is Ready")
# Close the connection
connection_obj.close()