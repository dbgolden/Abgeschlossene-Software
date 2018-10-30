#© by dbgolden - 2018


#import
from colorama import init, Fore, Style

import os
import sys
import math
import time



init()
#Logo/Banner
print (Fore.LIGHTRED_EX + "####################################################")
print ("####################################################")
print (Fore.LIGHTBLUE_EX +"####### Willkommen im DB-Dev Taschenrechner. #######")
print ("####################################################")
print (Fore.LIGHTWHITE_EX +"####################################################")   



#Choose Menu
print (Fore.LIGHTGREEN_EX + '''
    Wähle deine Rechenart aus:
    
    \n\t + Addieren ist \t\t
    \n\t - Subtrahieren ist \t\t
    \n\t * Multiplizieren ist \t\t
    \n\t / Dividiren ist \t\t

    ''')
#Enter your Choose
sume = input(">>>: ")
#Enter your Nummber
x = input("Gebe deine Erste Zahl ein: ")
y = input("Gebe deine Zweite Zahl ein: ")

#Calculat +
if (sume == "+"): 
    print (Fore.LIGHTBLUE_EX + "Das Ergebnis ist: ", int(x) + int(y))

    time.sleep(2) #Time Sleep is to get a slower Reading in the Consol
#Calculat -
elif (sume == "-"): 
    print (Fore.LIGHTRED_EX + "Das Ergebnis ist: ", int(x) - int(y))
    
    time.sleep(2)
#Calculat * 
elif (sume == "*"): 
    print (Fore.LIGHTMAGENTA_EX + "Das Ergebnis ist: ", int(x) * int(y))

    time.sleep(2)
#Calculat /
elif (sume == "/"): 
    print (Fore.BLUE + "Das Ergebnis ist: ", int(x) / int(y))
    time.sleep(2)
#Print if it wrong
else:
    print ("Eingabe ist falsch....")
#Restart or Exit the Software
input ("Möchtest du den Rechner neustarten y/n:  ")
if ("y"):
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
elif ("n"):
    sys.exit(0)