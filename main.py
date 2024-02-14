import colorama
from colorama import Fore, Back, Style
import math
from sympy import symbols, Eq, solve
import keyboard
import os
import time

def clear_console():
    os.system('cls') 

def keyclear():
    time.sleep(0.5)
    print("press enter to go back")
    keyboard.wait('enter')
    clear_console()

def commands():
    print(Fore.BLUE + Back.BLACK + "commands:")
    print(Fore.RED + Back.BLACK + "exit: this command exits the program")
    print(Fore.RED + Back.BLACK + "cls: this command clears the console to clean it up")
    print(Fore.BLUE + Back.BLACK + "1 - this opens the normal calculator")
    print(Fore.BLUE + Back.BLACK + "2 - This is the value for Geomotry")
    print(Fore.BLUE + Back.BLACK + "    2.1 - This is the value for finding the radius:diameter:circumfrence:area of a circle")
    print(Fore.BLUE + Back.BLACK + "3 - This is the command for Algabra:COMING SOON:")
    print(Fore.BLUE + Back.BLACK + "    3.1 - This is the command for Algabra that is like this x + 7 = 30:COMING SOON:")
    print(Fore.BLUE + Back.BLACK + "    3.2 - This is the command for Algabra that is like this 3x + 7 = 30:COMING SOON:")

def error404notfound():
    print(Fore.RED + Back.BLACK + "ERROR 404: NOT FOUND")

def circlemath():
    _1to4 = input(Fore.BLUE + Back.BLACK + "What do you already have Radius:Diameter:Circumfrance:Area; " + Back.BLACK + Fore.BLUE)
    #Radius Math
    if _1to4.lower() == "radius" or _1to4.lower() == "r":
        radius =  input(Fore.BLUE + "What is the Radius: " + Back.BLACK + Fore.BLUE)
        print("Radius: " + str(radius))
        diameter = int(radius) * 2
        print("Diameter: " + str(diameter))
        print("Circumference: " + str((float(radius) * 2) * math.pi))
        print("Area: " + str(math.pi * float(radius) * float(radius)))
        keyclear()

    #Diameter Math
    if _1to4.lower() == "diameter" or _1to4.lower() == "d":
        diameter =  input(Fore.BLUE + "What is the Diameter: " + Back.BLACK + Fore.BLUE)
        print(Fore.GREEN + "Radius: " + str(int(float(diameter) / 2)))
        print(Fore.GREEN + "Diameter: " + str(diameter))
        print(Fore.GREEN + "Circumference: " + str((math.pi * float(diameter))))
        radius = float(((float(diameter)) / 2))
        print(Fore.GREEN + "Area: " + str(math.pi * radius * radius))
        keyclear()

    #Circumfrance Math
        
    if _1to4.lower() == "circumfrance" or _1to4.lower() == "c":
        circumfrance =  float(input(Fore.BLUE + "What is the Circumfrance: " + Back.BLACK + Fore.BLUE))
        diameter = circumfrance / math.pi
        radius = diameter / 2
        print(Fore.GREEN + "Radius: " + str(radius))
        print(Fore.GREEN + "Diameter: " + str(diameter))
        print(Fore.GREEN + "Circumference: " + str(circumfrance))
        print(Fore.GREEN + "Area: " + str(math.pi * float(radius) * float(radius)))
        keyclear()

    #Area Math
        
    if _1to4.lower() == "area" or _1to4.lower() == "a":
        area =  float(input(Fore.BLUE + "What is the Area: " + Back.BLACK + Fore.BLUE))
        radius = math.sqrt(area / math.pi)
        diameter = radius + radius
        print(Fore.GREEN + "Radius: " + str(radius))
        print(Fore.GREEN + "Diameter: " + str(diameter))
        print(Fore.GREEN + "Circumference: " + str(math.pi * float(diameter)))
        print(Fore.GREEN + "Area: " + str(area))
        keyclear()


    #error 404 NOT FOUND
    else:
        error404notfound()
    
    #end

def normalcalculator():
    try:
        userproblem = input(Fore.CYAN + Back.BLACK + "What is the math equation: " + Back.BLACK + Fore.BLUE)
        print(eval(userproblem))
        keyclear()
    except:
        print(Fore.RED + "You can not type characters/letters if this is not what happended email me at\n" + Fore.LIGHTYELLOW_EX +"evanrunnercontact@gmail.com" + Fore.GREEN)




clear_console()
while True:
    #Normal Calculator
    mathtype = input(Fore.BLACK + Back.BLACK + "What type of math are you trying to do\nType help for all the different calculators\n" + Fore.GREEN + Back.BLACK + "We support Algabra | Geomotry | Normal Calculator\n" + Fore.RED + "THESE ARE NOT COMMANDS DO HELP FOR CALCULATOR COMMANDS\n" + Fore.CYAN)
    
        #\\\\\\\\\\\\\\\\\\\Commands/////////////////
    
    #Help Command
        
    if mathtype.lower() == "help":
        commands()
        keyclear()

    #Exit Command
    elif mathtype.lower() == "exit":
        break
        sys.exit()

    if mathtype.lower() == "cls":
        clear_console()
    
    if mathtype == "1":
        normalcalculator()
    #Geomotry
    if mathtype == "2":
        print(Fore.GREEN + Back.BLACK + "type one of the specifacations such as 2.1 or 2.2")
    elif mathtype == "2.1":
        circlemath()
    #Algebra
    if mathtype == "3":
        print(Fore.GREEN + Back.BLACK + "type one of the specifacations such as 3.1 or 3.2:COMING SOON:")
    elif mathtype == "3.1":
        error404notfound()

