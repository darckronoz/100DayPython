#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import sys
#Rock Paper Scisssor.
from random import randint

# Rock
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper_art ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
art_picker = {
    0: rock_art,
    1: paper_art,
    2: scissors_art,
}
user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_pick = randint(0,2)

if user_pick not in [0,1,2]:
    print("you can only choose between 0 and 2 \n you lose :(((((")
    sys.exit()

print("You picked", art_picker[user_pick])
print("Computer picked: ", art_picker[computer_pick])

if user_pick == computer_pick:
    print("its a Draw!")

if user_pick == 0 and computer_pick == 2:
    print("You win!")
elif user_pick == 1 and computer_pick == 0:
    print("You win!")
elif user_pick == 2 and computer_pick == 1:
    print("You win!")
else:
    print("You lose :(")