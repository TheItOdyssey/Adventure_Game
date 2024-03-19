
#Imports av de andra modulerna samt os för att kunna använda clear
import os
import Race_maker
import Game_over
import Stations
from Stations import *
from Stations import situationchoice

#funktionen för att kunna navända clear
clear = lambda: os.system('cls')
clear()

situation_choice = situationchoice()

#Detta samlar de olika funktionerna från den andra modulen vilket är innästlade i varandra? i dunno tbh skrev lite skit och det funkade, tar man bort detta fuckas allt
situationchoice_func, outside_func, castle_func, forest_func, home_func, talk_guard_func, punch_guard_func = situationchoice()

#Starting shit
print("Welcome to The Adventure of niggaland")
start_exit = input("1: Start Game\n2: Exit\n")
clear()

#Intro, tydligen funkar detta inte helt? kan inte trycka 2 vilket är weird
if start_exit == "1":
    clear()
    print("Welcome to Niggaland")
elif start_exit == "2":
    exit()
else: 
    exit()

#Making your race and picking difficulty
race = Race_maker.pick_race()
print(f"You picked {race}")
clear()

#Basen för att starta spelet. vet inte ens ifall detta behövs? kan egentligen bara kalla på funktionen home ju men jag är lat....
Home = input("You are at your house, What would you like to do?\n1:Exit house\n2:Kill yourself\n")
#en fin match statement istället för en så kallad switch. Kanske bara skall användas när det är mer än 3 val.....
match Home:
    case "1":
        clear()
        print("You exited your house")
        outside_func()
    case "2":
        clear()
        print("You commited no life :(")
        Game_over.Game_End()
        exit()
    case _:
        clear()
        print("Invalid input....Exiting game")
        exit()


