import UserClass
import MusicClass
import os


User = UserClass.User_class
Music = MusicClass.Music_class


#UserClass.initialise()
#MusicClass.initialise()

#UserClass.add('Sudesh','123456')

def MainMenu(username):
    os.system('clear' if os.name == 'posix' else 'cls')
    print('++++++++++++++++++++++++++')
    print('+Welcome to Music Library+')
    print('++++++++++++++++++++++++++')
    print()
    print()
    print('1 - View Your Music')
    print('2 - Delete Your Music')
    print('3 - Upload Your Music')
    print('4 - View All Music')
    print('9 - Exit')
    print()
    
    menuinput = input("Please choose an option : ")

    match menuinput:
        case '1':
            ViewYourMusic(username)
        case '2':
            MainMenu(username);
        case '3':
            UploadYourMusic(username)
        case '4':
            ViewAllMusic(username)
        case '9':
            exit
            


def UploadYourMusic(username):
    print('++++++++++++++++++++++++++')
    print('+Welcome to Music Library+')
    print('++++++++++++++++++++++++++')
    print()
    print()
    musicname = input("Music Name : ")
    musiclyrics = input("Music Lyrics : ")
    musicscore = input("Music Score : ")
    musictype = input("Music Type : ")

    #MusicClass.view(username)
    #MusicClass.initialise()
    MusicClass.add(username, musicname, musiclyrics, musicscore, musictype)
    MusicClass.viewAll()
    dummyinput = input('Press enter')
    MainMenu(username)


    


def ViewYourMusic(username):
    print('++++++++++++++++++++++++++')
    print('+Welcome to Music Library+')
    print('++++++++++++++++++++++++++')
    print()
    print()
    #MusicClass.view(username)
    #MusicClass.initialise()
    MusicClass.view(username)
    dummyinput = input("Press enter to continue")
    MainMenu(username)

def ViewAllMusic(username):
    print('++++++++++++++++++++++++++')
    print('+Welcome to Music Library+')
    print('++++++++++++++++++++++++++')
    print()
    print()
    #MusicClass.view(username)
    #MusicClass.initialise()
    MusicClass.viewAll()
    dummyinput = input("Press enter to continue")
    MainMenu(username)
    
    ##def f(x):
    ##match x:
    ##    case 'a':
    ##        return 1
    ##    case 'b':
    ##        return 2
    ##    case _:
    #3        return 0   # 0 is the default case if x is not found

    

#UserClass.viewAll()

username = input("Please enter your Username : ")
##password = input("Please enter your Password : ")


MainMenu(username)
##if UserClass.verify(username,password) == "Y":
##    MainMenu()
##else:
##    print("IMPOSTER!!!")


    
    
