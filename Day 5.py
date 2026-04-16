#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import random
from random import shuffle

#password generator

letters_quantity = int(input("How many letters would you like in your password?\n"))
symbols_quantity = int(input("How many symbols would you like?\n"))
numbers_quantity = int(input("How many numbers would you like?\n"))
characters_list = []

for _ in range(letters_quantity):
    coin_flip = random.randint(1, 2)
    if coin_flip == 1:
        characters_list.append(str(chr(random.randint(65,90))))
    else:
        characters_list.append(str(chr(random.randint(97,122))))

for _ in range(symbols_quantity):
    characters_list.append(str(chr(random.randint(37, 47))))

for _ in range(numbers_quantity):
    characters_list.append(str(random.randint(0,1)))



print(characters_list)
shuffle(characters_list)
print(characters_list)
print(f"Your password is: {"".join(characters_list)}")