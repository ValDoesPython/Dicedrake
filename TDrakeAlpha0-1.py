import os
import random
import string
import math
import sqlite3 as lite
UandP = "UandP.txt"
con=lite.connect('Dicedrake.db')
cur=con.cursor()
def diceroll():
    y = str(input("What would you like to roll? (No spaces, eg:1d20): "))
    x = y.split('+')
    total = 0
    for d in x:
        subtotal = 0
        n = d.split('d')
        numb = int(n[0])
        max = int(n[1])
        lodice = []
        for i in range(numb):
            num = random.randint(1,max)
            subtotal += num
        
        total += subtotal
    print(total)
    x = input("REDO?")
    if x =='y':
        main()
    if x == 'n':
        exit()
def statroll():
    arrStats=[0,0,0,0,0,0]
    for i in range (6):
        arrRoll=[0,0,0,0]
        for r in range (4):
            num = random.randint(1,6)
            arrRoll[r-1]=num
        arrRoll.remove(min(arrRoll))
        stat=arrRoll[0]+arrRoll[1]+arrRoll[2]
        arrStats[i-1]=stat
    print (arrStats)
def statrollheroic():
    arrStats=[0,0,0,0,0,0]
    for i in range (6):
        arrRoll=[0,0,0,0]
        for r in range (4):
            num = random.randint(1,6)
            arrRoll[r-1]=num
        arrRoll.remove(min(arrRoll))
        stat=arrRoll[0]+arrRoll[1]+arrRoll[2]
        arrStats[i-1]=stat
    print (arrStats)

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def createAccount():
    global username
    username = input("What would you like your username to be?")
    global password
    password = input("What would you like your password to be?")
    os.mkdir('./'+username+'/')
    f = open(UandP, 'a+')
    f.write(username+", ")
    f.write(password+"\n")
    f.close()
    cur.execute("INSERT INTO Accounts (Username, Password) values (?, ?)",
            (username, password))
    con.commit()


def logIn():
    f = open("UandP.txt", "r")
    names=[line.strip() for line in open('UandP.txt')]
    global username
    username = input("Username:")
    password = input("Password:")
    UFound = False
    PFound = False
    for n in names:
        UFound = False
        PFound = False
        x = n.split(', ')
        if x[0] ==username:
            UFound = True
        if x[1] == password:
            PFound = True
        if UFound == True and PFound == True:
            print("Logged in!")
            characterCreator()
    if UFound == False or PFound == False:
        print("Wrong!")

def startUp():
    SorL = input("Would you like to sign in [S] or log in [L] now?")
    if SorL == 'S'or SorL == 's':
        createAccount()
        logIn()
    if SorL == 'L'or SorL == 'l':
        logIn()

def characterCreator():
    actionCS = str(input("Would you like to create [C], view [V] or edit [E] a character?"))
    if actionCS == 'c' or actionCS == 'C':
        CName = input("What is your character's name? ")
        Race = input("What is your character's race? ")
        numClass = int(input("How man classes does your character have? "))
        abilityScores = [10,10,10,10,10,10]
        c1 = charInfo(CName,Race,numClass,abilityScores)
        for i in range(c1.noclass):
            className = input("What is your class? ")
            classLevel = int(input("What level is your class? "))
            c1.add_class([className, classLevel])
        Prof = c1.proficiencybonus()

        #c1 = charInfo(CName,Race,numClass,abilityScores)
        dirName = (username+'/'+CName)
        os.makedirs(dirName)
        f = open(username+'/'+CName+'/'+CName+'sheetp1.txt', 'x')

def gameBoard():
    #I am not sure where to go from here, personally I want to get it on a working board but chances are it will not.
    quit()
startUp()

