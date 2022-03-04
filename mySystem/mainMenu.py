
from mySystem import *
def menu():
    while True:
        print("******************** Main menu **********************")
        choice = input("1 - Login\n2 - Register\n3 - Enter any key to exit.\n>> ")
        print("*****************************************************")
        if choice == '1':
            newUser = login()
            if newUser:
                chooseOption(newUser)
        elif choice == '2':
            regUser()
        else:
            exit()

menu()