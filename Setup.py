import os
import UserClassSecure
import MusicClassSecure

os.system('clear' if os.name == 'posix' else 'cls')
print('Setting up Sudeshs Music App')
print('Create the Database')
if os.path.exists("music.db"):
    print('An older version of the Database exists')
    print('Deleting music.db')
    os.remove("music.db")
else:
    print('Existing Database file does not exist, lets continue')

print('Setting up Music Table')
MusicClassSecure.initialise()

print('Setting up Users Table')
UserClassSecure.initialise()



print('Creating admin user')



