import MusicClassSecure
import UserClassSecure

#UserClassSecure.initialise()
#UserClassSecure.add(Username='User1',Password='User1Pa$$word',AdminFlag='N')
#
# UserClassSecure.add(Username='User2',Password='User2Pa$$word',AdminFlag='N')
print(UserClassSecure.verify(username='User2',password='User2Pa$$word'))

UserClassSecure.viewAll()
#UserClassSecure.view('test')
#print(UserClassSecure.verify(username='test',password='password1'))

#MusicClassSecure.initialise()
#MusicClassSecure.add(UserName='Python',MusicName='Baba Shark',MusicLyrics='Do do do',MusicScore=1,MusicType='Shit',MusicDataPath='/Users/rooshenra/Downloads/TheSpokenWord.mp3')
#MusicClassSecure.view('Python')
#MusicClassSecure.viewAll()
#MusicClassSecure.delete(1)
#MusicClassSecure.viewAll()


