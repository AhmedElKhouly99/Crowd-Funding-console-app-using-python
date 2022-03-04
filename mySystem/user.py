from mySystem import *
import json



class User:
    userCount = 0
    allUsers = dict()
    def __init__(self, email, password, fname = "", lname = "", phone = ""):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.phone = phone
        User.userCount +=1
        self.id = User.userCount
        uDic = {"fname":self.fname, "lname":self.lname, "email":self.email, "password":self.password, "phone":self.phone}
        User.allUsers[f"{self.email}"] = uDic



def addUser(email, password, fname = "", lname = "", phone = ""):
    getUsers()
    for u in User.allUsers.keys():
        if str(u) ==email:
            print("User already exist!!!")
            return False
    u = User(email, password, fname, lname, phone)
    addUsers()
    getUsers()
    del u
    return True

def getUser(email, password):
    getUsers()
    for u in User.allUsers.keys():
        if str(u) == email and User.allUsers[u]["password"] == password:
            l = (u, f"{User.allUsers[u]['fname']} {User.allUsers[u]['lname']}")
            return l
            # break
    return False

def getUsers():
    try:
        with open('users.txt', 'r') as readUsers:
            User.allUsers = json.load(readUsers)
            User.userCount = len(User.allUsers)
    except Exception as e:
        print(f"Error : {e}")



def addUsers():
    try:
        with open('users.txt', 'w') as readUsers:
            json.dump(User.allUsers, readUsers)
    except Exception as e:
        print(f"Error : {e}")


