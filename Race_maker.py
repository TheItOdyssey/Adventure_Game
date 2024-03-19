import os
from Stats import *


clear = lambda: os.system('cls')
clear()




def pick_race():
    print("Please choose your race:")
    race = input("1:Human\n2:Orc\n3:Leopold\n")
    if race == "1":

        clear()
        race = human

    elif race == "2":

        clear()
        race = Orc
        
    elif race == "3":

        clear()
        race = Leopold
        
    return race

ChosenRace = pick_race