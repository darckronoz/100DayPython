#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import random
import sys
from time import sleep

#Blackjack

#Clubs=+  Diamonds=^ Hearts=# Spades=-
cards = {
    "1+": 11,
    "2+": 2,
    "3+": 3,
    "4+": 4,
    "5+": 5,
    "6+": 6,
    "7+": 7,
    "8+": 8,
    "9+": 9,
    "10+": 10,
    "11+": 10,
    "12+": 10,
    "13+": 10,
    "1^": 11,
    "2^": 2,
    "3^": 3,
    "4^": 4,
    "5^": 5,
    "6^": 6,
    "7^": 7,
    "8^": 8,
    "9^": 9,
    "10^": 10,
    "11^": 10,
    "12^": 10,
    "13^": 10,
    "1#": 11,
    "2#": 2,
    "3#": 3,
    "4#": 4,
    "5#": 5,
    "6#": 6,
    "7#": 7,
    "8#": 8,
    "9#": 9,
    "10#": 10,
    "11#": 10,
    "12#": 10,
    "13#": 10,
    "1-": 11,
    "2-": 2,
    "3-": 3,
    "4-": 4,
    "5-": 5,
    "6-": 6,
    "7-": 7,
    "8-": 8,
    "9-": 9,
    "10-": 10,
    "11-": 10,
    "12-": 10,
    "13-": 10,
}

deck = []

def fill_deck():
    for card in cards.keys():
        deck.append(card)
    random.shuffle(deck)

def main():
    play = input("21 BlackJack (card counting simulator B).) \n Wanna play? Type 'yes' or 'no'. ")
    if play.lower() == "yes":
        play_game()
    else:
        print("\n :) Bye. \n")
        sys.exit()

def get_card():
    global deck
    print(len(deck))
    return cards[deck.pop()]

def evaluate_game(computers_game, players_game):
    global deck
    sleep(0.5)
    if sum(players_game) == 21:
        print("You have 21! \n")
    sleep(0.5)
    print(f"Dealers game: {computers_game}")
    if sum(computers_game) == 21:
        sleep(0.5)
        print(f"House wins, you lose.\n Dealers game: {computers_game} Your game: {players_game} \n")
        return []
    while sum(computers_game) < sum(players_game):
            sleep(0.5)
            computers_game.append(get_card())
            print(f"Dealers game: {computers_game}")
    if sum(computers_game) > 21:
        print("Dealer bust, You Win")
    elif sum(computers_game) > sum(players_game):
        print(f"House wins, you lose.\n Dealers game: {computers_game} Your game: {players_game} \n")
    return []


def convert_players_decision(question):
    decision = input(f"{question} Type yes or no").lower()
    return True if decision == "yes" else False

def player_hit(player_game):
    global deck
    sleep(0.5)
    player_game.append(get_card())
    print(f"Your game: {player_game} = {sum(player_game)}")
    if sum(player_game) > 21:
        print("You bust, The house wins. \n")
        return []
    elif not convert_players_decision("Do you want another card?"):
        return player_game
    player_hit(player_game)
    return []


#def player_split(player_game): v2
    #global deck v2

def player_double(player_game):
    global deck
    sleep(0.5)
    player_game.append(get_card())
    print(f"Your game: {player_game} = {sum(player_game)}")
    if sum(player_game) > 21:
        print("You bust, The house wins. \n")
        return []
    return player_game

def play_hand():
    global deck
    player_game = []
    computers_game = []
    player_game.append(get_card())
    player_game.append(get_card())
    computers_game.append(get_card())
    computers_game.append(get_card())
    print(f"Your game: {player_game}")
    if sum(player_game) == 21:
        evaluate_game(computers_game, player_game)
        return convert_players_decision("Do you want to keep playing?")
    sleep(0.5)
    print(f"Dealer: {computers_game[0]}")
    player_play = input("What do you wanna do?: \n hit, stand, double or split?")
    match player_play:
        case "hit":
            player_game = player_hit(player_game)
        case "stand":
            player_game = evaluate_game(computers_game, player_game)
        case "double":
            player_game = player_double(player_game)
        #case "split": v2
            #player_game = player_split(player_game) v2
        case _:
            return False
    if len(player_game) > 0:
        evaluate_game(computers_game, player_game)
    return convert_players_decision("Do you want to keep playing?")


def play_game():
    global deck
    print("shuffling deck...")
    fill_deck()
    keep_playing = True
    while len(deck) > 4 and keep_playing:
        keep_playing = play_hand()

main()
