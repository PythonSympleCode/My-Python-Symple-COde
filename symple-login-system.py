
import getpass
import os

os.system('cls')

welcome = ("    Symple Login System")
print("")
print(welcome)
print("")


username = input ("Username : ")
password = getpass.getpass(prompt='Password : ')

user = ('Bumi1234')
passw = ('bumi123')


import os

os.system('cls')


from tqdm import tqdm
from time import sleep

for i in tqdm(range(100),desc = "Equalize Account:",unit = "",position = 2):
    sleep(0.10)


print("")
print("Loading Complete")
print("")

os.system('cls')


if username in user:

    os.system('cls')
    print("    Equalized Account Data")

    print("")
    print("Username Correct!")
    print("")

else:

    os.system('cls')
    print("    Equalized Account Data")

    print("")
    print("Username Incorrect!")
    print("")

if password in passw:

    print("")
    print("Password Correct!")
    print("")

else:
    print("")
    print("Password Incorrect!")
    print("")
