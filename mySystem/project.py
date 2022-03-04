import json

class Project:
    proCount = 0
    allPro = dict()
    def __init__(self, email, title, details, ttarget, start, end):
        self.title = title
        self.details = details
        self.ttarget = ttarget
        self.start = start
        self.end = end
        Project.proCount += 1
        pDic = {'title':self.title, 'details':self.details, 'ttarget':self.ttarget, 'start':self.start,'end':self.end}
        Project.allPro[f"{Project.proCount}:{email}"] = pDic

def addPro(email, title, details, ttarget, start, end):
    getAllPro()
    p = Project(email, title, details, ttarget, start, end)
    addAllPro()
    getAllPro()
    del p
    return True

def editPro(id,email, title, details, ttarget, start, end):
    getAllPro()
    Project.allPro[f"{id}:{email}"] = {'title': title, 'details':details, 'ttarget': ttarget, 'start':start, 'end':end}
    addAllPro()
    getAllPro()

def deletePro(id):
    getAllPro()
    Project.allPro.pop(id)
    addAllPro()
    getAllPro()


def getAllPro():
    try:
        with open('projects.txt', 'r') as readpro:
            Project.allPro = json.load(readpro)
            Project.proCount = list(Project.allPro.keys())[-1]
            Project.proCount = int(str(Project.proCount).split(":")[0])
            # Project.proCount = len(Project.allPro)
    except Exception as e:
        print(f"Error : {e} line1111111111111111111")

def addAllPro():
    try:
        with open('projects.txt', 'w') as readPro:
            json.dump(Project.allPro, readPro)
    except Exception as e:
        print(f"Error : {e}")

def viewAll():
    print("********************************* All Projects **********************************")
    getAllPro()
    for u in Project.allPro.keys():
        print(f"{(str(u).split(':'))[0]}:{Project.allPro[u]}")

def ownerPro(newUser):
    print(f"********************************* {newUser[1]} Projects **********************************")
    getAllPro()
    for u in Project.allPro.keys():
        if str(u).endswith(newUser[0]):
            print(f"{(str(u).split(':'))[0]}:{Project.allPro[u]}")


def searchPro(col, value):
    getAllPro()
    for u in Project.allPro.keys():
        if Project.allPro[u][col] == value:
            print(f"{(str(u).split(':'))[0]}:{Project.allPro[u]}")



