from user import *
from mySystem import *
def login():
    while True:
        print("*********************** Login **************************")
        email = input("Please enter your email : ")
        password = input("Please enter your password : ")
        newUser = getUser(email, password)
        if newUser:
            print("*********************** Login is done successfully **************************")
            return newUser
        else:
            print("Icorrect email or password")
            return False

# login()