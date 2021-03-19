import time
import random

dice = [1,2,3,4,5,6]

roll_again = 'yes'

while roll_again == 'yes' or roll_again == 'y':
    print('Rolling the dice again... ')

    time.sleep(0.8) ## pause
    print('the values are... ')
    time.sleep(0.6) ##pause

    
#   First dice #
    
    if random.choice(dice) == 6:             ##prints the image 6  opens file
            adicefile=open('Dice6.txt','r')
            dices = adicefile.read()
            print(dices)
            adicefile.close()#Closesfile

    elif random.choice(dice) == 5:             ##prints the image 5 opens file
            bdicefile=open('Dice5.txt','r')
            dices = bdicefile.read()
            print(dices)
            bdicefile.close()#Closesfile
            
    elif random.choice(dice) == 4:             ##prints the image 4 opens file
            cdicefile=open('Dice4.txt','r')
            dices = cdicefile.read()
            print(dices)
            cdicefile.close() #Closesfile
            
    elif random.choice(dice) == 3:              ##prints the image 3 opens file
            cdicefile=open('Dice3.txt','r')
            dices = cdicefile.read()
            print(dices)
            cdicefile.close()#Closesfile
            
    elif random.choice(dice) == 2:             ##prints the image 2 opens file
            ddicefile=open('Dice2.txt','r')
            dices = ddicefile.read()
            print(dices)
            ddicefile.close()#Closesfile
    else:
        #random.choice(dice) == 1:              ##prints the image 1 opens file 
            edicefile=open('Dice1.txt','r')
            dices = edicefile.read()
            print(dices)
            edicefile.close()#Closesfile
    #else:
        #print('I DIDNT HAVE ENOUGH TIME TO FINISH OR THINK IT THROUGH :( ')
######
    time.sleep(0.5)

    ######## Second dice #################
    if random.choice(dice) == 6:             ##prints the image 6 opens file
            aadicefile=open('Dice6.txt','r')
            dices = aadicefile.read()
            print(dices)
            aadicefile.close() #Closesfile

    elif random.choice(dice) == 5:             ##prints the image 5 opens file
            abdicefile=open('Dice5.txt','r')
            dices = abdicefile.read()
            print(dices)
            abdicefile.close()#Closesfile
            
    elif random.choice(dice) == 4:             ##prints the image 4 opens file
            acdicefile=open('Dice4.txt','r')
            dices = acdicefile.read()
            print(dices)
            acdicefile.close() #Closesfile
            
    elif random.choice(dice) == 3:              ##prints the image 3 opens file
            acdicefile=open('Dice3.txt','r')
            dices = acdicefile.read()
            print(dices)
            acdicefile.close()#Closesfile
            
    elif random.choice(dice) == 2:             ##prints the image 2 opens file
            addicefile=open('Dice2.txt','r')
            dices = addicefile.read()
            print(dices)
            addicefile.close()#Closesfile
    else:
        #random.choice(dice) == 1:              ##prints the image 1 opens file
            aedicefile=open('Dice1.txt','r')
            dices = aedicefile.read()
            print(dices)
            aedicefile.close()#Closesfile
    #else:
        #print('I DIDNT HAVE ENOUGH TIME TO FINISH OR THINK IT THROUGH :( ')
    time.sleep(0.6)
    roll_again= input('Roll the dice again ? (yes~y)')

    
