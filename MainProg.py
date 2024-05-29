import UserClass
import os


User = UserClass.User_class

#UserClass.initialise()

#UserClass.add('Sudesh','123456')

def MainMenu():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('++++++++++++++++++++++++++')
    print('+Welcome to Music Library+')
    print('++++++++++++++++++++++++++')
    print()
    print()
    print('1 - View Your Music')
    print('2 - View All Music')
    print('3 - Delete Your Music')
    print('4 - Upload Your Music')
    print()
    

    

#UserClass.viewAll()
username = input("Please enter your Username : ")
password = input("Please enter your Password : ")


if UserClass.verify(username,password) == "Y":
    MainMenu()
else:
    print("IMPOSTER!!!")


    
    
