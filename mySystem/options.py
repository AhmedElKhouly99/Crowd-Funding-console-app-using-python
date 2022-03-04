import datetime
import re
import time

from project import *

def createProject(email):
    while True:
        print(f"************************** Create project ****************************")
        title = input("Please enter the project title : ")
        if title.isalpha():
            break
        else:
            print("Ivalid title !!")
    while True:
        details = input("Please enter project details : ")
        if details != "":
            break
        else:
            print("You have to enter details !!")

    while True:
        ttarget = input("Please enter the total target : ")
        if ttarget.isdigit():
            break
        else:
            print("Total target must be digits !!")

    while True:
        # start = input('Enter the start date in YYYY-MM-DD format')
        start = str((datetime.datetime.now()).strftime("%Y-%m-%d"))
        s = time.strptime(start, "%Y-%m-%d")
        end = input('Enter the end date in yyyy-mm-dd format : ')
        if re.fullmatch(r'\b[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}\b', end):
            try:
                d = time.strptime(end, '%Y-%m-%d')
                if not d <= s:
                    break
                else:
                    print("End date must be later than start date !!")
            except Exception:
                print("Invalid date !!")
        else:
            print("Invalid date !!")

    addPro(email,title,details,ttarget,start,end)
    print("*************** Project is created successfully ! ***************")



def edit(newUser):
    print(f"************************** Edit project ****************************")
    ownerPro(newUser)
    id = input("Enter project id to edit : ")
    if id.isdigit() and f"{id}:{newUser[0]}" in Project.allPro.keys():
        start = Project.allPro[f"{id}:{newUser[0]}"]["start"]
        while True:
            title = input("Please enter the project title : ")
            if title.isalpha():
                break
            else:
                print("Ivalid title !!")
        while True:
            details = input("Please enter project details : ")
            if details != "":
                break
            else:
                print("You have to enter details !!")

        while True:
            ttarget = input("Please enter the total target : ")
            if ttarget.isdigit():
                break
            else:
                print("Total target must be digits !!")

        while True:
            s = time.strptime(start, "%Y-%m-%d")
            end = input('Enter the end date in dd-mm-yyyy format : ')
            if re.fullmatch(r'\b[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}\b', end):
                d = time.strptime(end, '%Y-%m-%d')
                if not d <= s:
                    break
                else:
                    print("End date must be later than start date !!")
            else:
                print("Invalid date !!")
        editPro(id, newUser[0], title, details, ttarget, start, end)
        print("*************** Project is Update successfully ! ***************")
    else:
        print("Invalid id !!")


def search():
    while True:
        print(f"************************** Search project ****************************")
        col = input("Enter field name you wants to search by:\n1 - Title\n2 - details\n3 - Total target\n4 - Start date\n5 - End date\n6 - Back\n>> ")
        if col == "1":
            val = input("Enter its value : ")
            if val.isalpha():
                searchPro("title", val)
            else:
                print("Invalid value !!")
        elif col == "2":
            val = input("Enter its value : ")
            if val.isalpha():
                searchPro("details", val)
            else:
                print("Invalid value !!")
        elif col == "3":
            val = input("Enter its value : ")
            if val.isdigit():
                searchPro("ttarget", val)
            else:
                print("Invalid value !!")
        elif col == "4":
            val = input("Enter its value : ")
            searchPro("start", val)
        elif col == "5":
            val = input("Enter its value : ")
            searchPro("end", val)
        else:
            break





def delete(newUser):
    print(f"************************** Delete ****************************")
    ownerPro(newUser)
    id = input("Enter project id to edit : ")
    if id.isdigit() and f"{id}:{newUser[0]}" in Project.allPro.keys():
        deletePro(f"{id}:{newUser[0]}")
        print("*************** Project is Delete successfully ! ***************")
    else:
        print("Invalid id !!")



def chooseOption(newUser):
    while True:
        print(f"************************** {newUser[1]} ****************************")
        choice = input("1 - Create project fund raise campaign\n2 - view all projects\n3 - Edit project\n4 - Delete project\n5 - Search for a project\n6 - Back\n>> ")
        if choice == "1":
            createProject(newUser[0])
        elif choice == "2":
            viewAll()
        elif choice == "3":
            edit(newUser)
        elif choice == "4":
            delete(newUser)
        elif choice == "5":
            search()
        else:
            break
