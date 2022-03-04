from user import *
import re

def regUser():
    while True:
        fname = input("Please enter your first name : ")
        if fname.isalpha():
            break
        else:
            print("Invalid input !!")
    while True:
        lname = input("Please enter your last name : ")
        if lname.isalpha():
            break
        else:
            print("Invalid input !!")
    while True:
        email = input("Please enter your email : ")
        if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            break
        else:
            print("Invalid email !!")
    while True:
        password = input("Please enter a password : ")
        conPass = input("Confirm password : ")
        if password == conPass and len(password)>=8:
            break
        else:
            print("Incorrect Password !!")
    while True:
        phone = input("Please enter your phone number : ")
        if re.fullmatch(r'\b01[0-9]{9}\b', phone):
            break
        else:
            print("Invalid phone number !!")
    if not addUser(email, password, fname, lname, phone):
        print("Email already exists !!")
    else:
        print("******************Register is done successfully***********************")

