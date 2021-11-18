import os
import random
import string
import math
import sqlite3 as lite
con=lite.connect('Dicedrake.db')
cur=con.cursor()
#setting up the connection to the associated database for all of the stored information reguarding accounts and content that need be accessed.
def diceroll():
    y = str(input("What would you like to roll? (No spaces, eg:1d20): "))
    x = y.split('+')
    total = 0
    index=0
    for d in x:

        if 'd' in x[index]:
            subtotal = 0
            n = d.split('d')
            numb = int(n[0])
            max = int(n[1])
            for i in range(numb):
                num = random.randint(1,max)
                subtotal += num
                print(num)
        else:
            subtotal=int(x[index])
        total += subtotal
        index += 1
    print(total)
    x = input("REDO?")
    if x =='y':
        main()
    if x == 'n':
        mainMenu()
#this will be accessed via the virtual tabletop. my aim is to create a separate gui for it. 
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
    return arrStats
#this is for the players that wish to allow lower stat scores in their game, with the lowest possible being a score of three, a massive handicap
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
    return arrStats
#this is the exact same as statroll() however it limits the handicap provided to unlucky players by not allowing ones.
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
#creates a directory for each user on that client
def createAccount():
    global username
    username = input("What would you like your username to be?")
    global password
    password = input("What would you like your password to be?")
    os.mkdir('./'+username+'/')
    cur.execute("INSERT INTO Accounts (Username, Password) VALUES (?, ?)",
            (username, password))
    con.commit()
 #writes an account for a new user
def logIn():
    global username
    username = input("Username:")
    password = input("Password:")
    PFound = False
    for x in cur.execute("SELECT Password FROM Accounts WHERE Username='"+(username)+"'"):
        if x[0]== password:
            PFound = True
    if PFound == True:
        print("Logged in!")
        mainMenu()
    if PFound == False:
        print("Wrong!")
        startup()
#allows people to log in through the database. if they get it wrong they get sent back to the startup menu
def startUp():
    SorL = input("Would you like to sign in [S] or log in [L] now?")
    if SorL == 'S'or SorL == 's':
        createAccount()
    if SorL == 'L'or SorL == 'l':
        logIn()
#boots the program
def characterCreator():
    CName = input("What is your character's name? ")
    Race = input("What is your character's race? ")
    numClass = int(input("How man classes does your character have? "))
    abilityScores =statroll()
    c1 = charInfo(CName,Race,numClass,abilityScores)
    for i in range(c1.noclass):
        className = input("What is your class? ")
        classLevel = int(input("What level is your class? "))
        c1.add_class([className, classLevel])
    Prof = c1.proficiencybonus()
    dirName = (username+'/'+CName)
    os.makedirs(dirName)
    f = open(username+'/'+CName+'/'+CName+'sheetp1.txt', 'x')
    mainMenu()
    #for creating characters, still a work in progress but I am working on it
def characterEditor():
    print ("section incomplete")
    mainMenu()
def characterViewer():
    print ("section incomplete")
    mainMenu()
def gameBoard():
    diceroll()
    mainMenu()
def mainMenu():
    actionCS = str(input('''Main Menu:
                            Create new character [C]
                            View existing characters[V]
                            Edit a character[E]
                            Open virtual tabletop [P]
                            Quit[Q]'''))
    if actionCS == 'c' or actionCS == 'C':
        characterCreator()
    if actionCS == 'v' or actionCS == 'V':
        print("in progress")
    if actionCS == 'e' or actionCS == 'E':
        print("in progress")
    if actionCS == 'p' or actionCS == 'P':
        gameBoard()
    if actionCS == 'q' or actionCS == 'Q':
        quit()
    #the main menu
startUp()
