import colorama
from colorama import Fore, Back, Style
import math

def error404notfound():
    print(Fore.RED + Back.BLACK + "ERROR 404: NOT FOUND")

def circlemath():
    _1to4 = input(Fore.BLUE + Back.WHITE + "What do you already have Radius:Diameter:Circumfrance:Area; ")
    #Radius Math
    if _1to4.lower() == "radius" or _1to4.lower() == "r":
        radius =  input(Fore.BLUE + "What is the Radius: ")
        print("Radius: " + str(radius))
        diameter = int(radius) * 2
        print("Diameter: " + str(diameter))
        print("Circumference: " + str((float(radius) * 2) * math.pi))
        print("Area: " + str(math.pi * float(radius) * float(radius)))
    #Diameter Math
    if _1to4.lower() == "diameter" or _1to4.lower() == "d":
        diameter =  input(Fore.BLUE + "What is the Diameter: ")
        print(Fore.GREEN + "Radius: " + str(int(float(diameter) / 2)))
        print(Fore.GREEN + "Diameter: " + str(diameter))
        print(Fore.GREEN + "Circumference: " + str((math.pi * float(diameter))))
        radius = float(((float(diameter)) / 2))
        print(Fore.GREEN + "Area: " + str(math.pi * radius * radius))

    #Circumfrance Math
        
    if _1to4.lower() == "circumfrance" or _1to4.lower() == "c":
        circumfrance =  float(input(Fore.BLUE + "What is the Circumfrance: "))
        diameter = circumfrance / math.pi
        radius = diameter / 2
        print(Fore.GREEN + "Radius: " + str(radius))
        print(Fore.GREEN + "Diameter: " + str(diameter))
        print(Fore.GREEN + "Circumference: " + str(circumfrance))
        print(Fore.GREEN + "Area: " + str(math.pi * float(radius) * float(radius)))

    #Area Math
        
    if _1to4.lower() == "area" or _1to4.lower() == "a":
        area =  float(input(Fore.BLUE + "What is the Area: "))
        radius = math.sqrt(area / math.pi)
        diameter = radius + radius
        print(Fore.GREEN + "Radius: " + str(radius))
        print(Fore.GREEN + "Diameter: " + str(diameter))
        print(Fore.GREEN + "Circumference: " + str(math.pi * float(diameter)))
        print(Fore.GREEN + "Area: " + str(area))

    #error 404 NOT FOUND
    else:
        error404notfound()
    
    #end

def normalcalculator():
    userproblem = input(Fore.CYAN + Back.BLACK + "What is the math equation: " + Fore.GREEN + Back.WHITE + Fore.RED + Back.BLACK)
    print(eval(userproblem))

while True:
    mathtype = input(Fore.BLACK + Back.WHITE + "What type of math are you trying to do\n1.Normal Calculator\n2.Geomotry\n type 2.1 for Circle Calculation\n")
    if mathtype == "1":
        normalcalculator()
    elif mathtype == "2.1":
        circlemath()