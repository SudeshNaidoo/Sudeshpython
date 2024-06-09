import os
import UserClassSecure
import MusicClassSecure

os.system('clear' if os.name == 'posix' else 'cls')

print('Setting up Sudeshs Music App')


print('Setting up Music Table')
MusicClassSecure.initialise()

print('Setting up Users Table')
UserClassSecure.initialise()



print('Creating admin user')
UserClassSecure.add(Username='AdminUser',Password='12345abcde',AdminFlag='Y')

print('Creating users user')
UserClassSecure.add(Username='Sudesh',Password='12345Sudesh',AdminFlag='N')
UserClassSecure.add(Username='Deva',Password='12345Deva',AdminFlag='N')
UserClassSecure.add(Username='Liza',Password='12345Liza',AdminFlag='N')

print('Uploading some Test Data for Demo purposes')

MusicClassSecure.add(UserName='Sudesh',MusicName='TestSong1',MusicLyrics='Lyrics1',MusicScore='10',MusicType='Pop',MusicDataPath='TestMusic.mp3')
MusicClassSecure.add(UserName='Sudesh',MusicName='TestSong2',MusicLyrics='Lyrics2',MusicScore='8',MusicType='Rock',MusicDataPath='TestMusic.mp3')
MusicClassSecure.add(UserName='Deva',MusicName='TestSong3',MusicLyrics='Lyrics3',MusicScore='6',MusicType='Amapiano',MusicDataPath='TestMusic.mp3')
MusicClassSecure.add(UserName='Liza',MusicName='TestSong4',MusicLyrics='Lyrics4',MusicScore='4',MusicType='Jazz',MusicDataPath='TestMusic.mp3')
MusicClassSecure.add(UserName='Liza',MusicName='TestSong5',MusicLyrics='Lyrics5',MusicScore='2',MusicType='HipHop',MusicDataPath='TestMusic.mp3')

#UserClassSecure.viewAll()
print('To start Sudeshs Music App - please run MainProg.py')

#print('Check if admin - Sudesh '+ UserClassSecure.isAdmin(username='Sudesh'))
#print('Check if admin - Admin '+ UserClassSecure.isAdmin(username='AdminUser'))


