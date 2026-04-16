#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import random
import sys

# hangman

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
 / \\ |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

word = random.choice(words)
guess = [""] * len(word)
tries = 0
max_tries = len(HANGMANPICS)

def get_letter_positions(letter):
    positions = []
    for x in range(len(word)):
        if letter == word[x]:
            positions.append(x)
    return positions

def add_letter_to_guess(letter):
    global guess
    positions = get_letter_positions(letter)
    for p in positions:
        guess[p] = letter

while tries < max_tries:
    if word == "".join(guess):
        print("You win! word:", word)
        sys.exit(0)
    print(HANGMANPICS[tries])
    print(guess)
    try_letter = input("Enter a letter: \n")
    if try_letter in word:
        add_letter_to_guess(try_letter)
        print("Correct!: ")
    else:
        tries += 1
        print("wrong! remaining tries: ", max_tries-tries)

print("You lose haha haha you are so bad")
print("word: ", word)
