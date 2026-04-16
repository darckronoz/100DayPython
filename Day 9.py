#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import os

#Silent bid program.
print("""                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`""")
print("Welcome to the secret auction program. \n")
another_player = True
players = {}
while another_player:
    player = input("\n What is your name?: ")
    bid = int(input("\n What is your bid? $ "))
    players[bid] = player
    keep_playing = input("\n Are there any other bidders? Type 'yes' or 'no': ")
    another_player = True if keep_playing == 'yes' else False
    os.system("cls" if os.name == "nt" else  "clear")

winner_bid = max(players.keys())
print(f"\n The winner is {players[winner_bid]}! with a bid of: {winner_bid}")

