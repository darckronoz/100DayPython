#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import random

##Guess the number

number_to_guess = random.randint(1,100)
print("I'm thinking of a number between 1 and 100 \n")
difficulty = input("Choose a difficulty:  Type 'easy' or 'hard': \n")

def main():
    attempts = 10 if difficulty == 'easy' else 5
    print(f"Difficulty {difficulty} set, you have {attempts} attempts \n")
    while attempts > 0:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == number_to_guess:
            print("You guessed the number!")
            return
        tip = "Too low" if guess < number_to_guess else "Too high"
        print(f"{tip}, Try again.")
        attempts -= 1
    print(f"you lose you didnt guess the number :( \n the number was {number_to_guess}")

main()