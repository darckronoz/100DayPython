#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import sys

print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=\"\"_;=.______________|_____________________|_______
|                   |  ,-\"_,=\"\"     `\"=.|                  |
|___________________|__\"=._o`\"-._        `\"=.______________|___________________
          |                `\"=._o`\"=._      _`\"=._                     |
 _________|_____________________:=._o \"=._.\"_.-=\"'\"=.__________________|_______
|                   |    __.--\" , ; `\"=._o.\" ,-\"\"\"-._ \".   |
|___________________|_._\"  ,. .` ` `` ,  `\"-._\"-._   \". '__|___________________
          |           |o`\"=._` , \"` `; .\". ,  \"-._\"-._; ;              |
 _________|___________| ;`-.o`\"=._; .\" ` '`.\"\\` . \"-._ /_______________|_______
|                   | |o;    `\"-.o`\"=._``  '` \" ,__.--o;   |
|___________________|_| ;     (#) `-.o `\"=.`_.--\"_o.-; ;___|___________________
____/______/______/___|o;._    \"      `\".o|o_.--\"    ;o;____/______/______/____
/______/______/______/_\"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_
____/______/______/______/______/_____\"=.o|o_.--\"\"___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
""")

print("""Welcome to Treasure Island. 
Your mission is to find the treasure. 
You're at a cross road. Where do you want to go?""")
way_to_go = input("\t\tType \"left\" or \"right\"\n")
if way_to_go == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    way_to_go = input("\t\tType \"wait\" to wait for a boat. Type \"swim\" to swim across. \n")
    if way_to_go == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        way_to_go = input("\tOne red, one yellos and one blue. Which colour do you choose?\n")
        if way_to_go == "red" or way_to_go == "blue":
            print("It's a room full of fire. Game Over.")
            sys.exit()
        elif way_to_go == "yellow":
            print("You found the treasure. You win!")
            sys.exit()
    else:
        print("You got attacked by an angry trout. Game Over.")
        sys.exit()
else:
    print("You fell into a hole. Game Over.")
    sys.exit()