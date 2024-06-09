import UserClassSecure
import MusicClassSecure
import os


def header():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('+                                                            Welcome to Music Library                                                            +')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print()
    print()
    
def MainMenu(username):
    
    header()
    print('1 - View Your Music')
    print('2 - Delete Your Music')
    print('3 - Upload Your Music')
    if UserClassSecure.isAdmin(username=username) == 'Y':
        print('4 - View All Music')
    print('9 - Exit')
    print()
    
    menuinput = input("Please choose an option : ")

    match menuinput:
        case '1':
            ViewYourMusic(username)
        case '2':
            DeleteYourMusic(username);
        case '3':
            UploadYourMusic(username)
        case '4':
            ViewAllMusic(username)
        case '9':
            os.system('clear' if os.name == 'posix' else 'cls')
            exit
            
    

def UploadYourMusic(username):
    header()
    musicname = input("Music Name : ")
    musiclyrics = input("Music Lyrics : ")
    musicscore = input("Music Score : ")
    musictype = input("Music Type : ")
    musicdatapath = input("Please share the location of your music : ")

    #MusicClass.view(username)
    #MusicClass.initialise()
    MusicClassSecure.add(UserName=username,MusicName=musicname,MusicLyrics=musiclyrics,MusicScore=musicscore,MusicType=musictype,MusicDataPath=musicdatapath)
    print()
    dummyinput = input('Press enter')
    MainMenu(username)


def DeleteYourMusic(username):
    header()
    MusicClassSecure.view(username=username)
    print()
    deleteID = input("Please enter the ID of the song you want to delete: ")
    if len(deleteID) > 0 : 
        MusicClassSecure.delete(id=deleteID)
    header()
    MusicClassSecure.view(username=username)
    print()
    dummyinput = input('Press enter to continue')
    MainMenu(username)
    


def ViewYourMusic(username):
    header()
    #MusicClass.view(username)
    #MusicClass.initialise()
    MusicClassSecure.view(username)
    print()
    dummyinput = input("Press enter to continue")
    MainMenu(username)

def ViewAllMusic(username):
    header()
    #MusicClass.view(username)
    #MusicClass.initialise()
    MusicClassSecure.viewAll()
    dummyinput = input("Press enter to continue")
    MainMenu(username)
    

header()

username = input("Please enter your Username : ")
password = input("Please enter your Password : ")



if UserClassSecure.verify(username,password) == "Y":
    MainMenu(username=username)
else:
    print("IMPOSTER!!!")
    dummyinput = input("Press enter to exit")
    print('Good Bye!')


    
    
