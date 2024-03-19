#importerar saker
import Game_over
import os




key = 0

#fixar clear 
clear = lambda: os.system('cls')
clear()

#första funktionen 
def situationchoice():
    #en innästlad funktion :=)
    def outside():
        clear()
        print("You are standing outside at a crossroad and are looking around. what would you like to do?")
        choice1_outside = input("1:Go back home\n2:To The castle\n3:To the forestn\n")
        match choice1_outside:
            case "1":
                    Home()
            case "2":
                clear()
                print("You went to the castle")
                Castle()
            case "3":
                    clear()
                    print("You went to the forest")
                    Forest()
            case _:
                    clear()
                    print("Invalid argument....")
        return outside       
    #som ni ser är detta de olika platserna som man kan gå till. det blir en indirekt loop vilket är bra?
    def Castle():
        clear()
        print("You stand infront of a big castle, infront of you there is a guard standig in your way")
        choice2_Castle = input("1:Go back\n2:Talk to the guard\n3:punch the Guard\n")
        match choice2_Castle:
            case "1":
                    clear()
                    outside()
            case "2":
                clear()
                Talk_Guard()
            case "3":
                    clear()
                    Punch_Guard()
            case _:
                    clear()
                    print("Invalid argument....")
                  
        return Castle

    def Forest():
         clear()
         print("You stand before the big scary forest")
         return Forest
    
    def Home():
        clear()
        print("You are home")
        clear()
        Home = input("You are at your house, What would you like to do?\n\n1:Exit house\n2:Kill yourself\n")
        match Home:
                case "1":
                    clear()
                    print("You exited your house")
                    outside()
                case "2":
                    clear()
                    print("You commited no life :(")
                    Game_over.Game_End()
                    exit
                case _:
                    clear()
                    print("Invalid input....Exiting game")
                    exit
        return Home

    def Talk_Guard():
          clear()
          if key == 1:
                print("You are welcome into the castle! Thank you for slaying the beast!")
          else:
                print("You can not enter before you have slain the beast in the Forest")
                Castle()
          return Talk_Guard
    
    def Punch_Guard():
          clear()
          print("You punched the guard")
          print(f"'The Guard puches you back'\n\n dont be silly")
          punch_again =input("Would you like to punch him again? y/n")
          
          
          return Punch_Guard

    return situationchoice, outside, Castle, Forest, Home, Talk_Guard, Punch_Guard









