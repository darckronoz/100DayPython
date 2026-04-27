#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import json
import sys
#flash card app, but I am running out of time D:

import tkinter as tk
from tkinter import messagebox

from known_word import KnownWord
from flash_card import FlashCard
from french_dict import FrenchDict
frenchWords = FrenchDict("5000_wordlist_french.csv", "known_words.json")
flash_cards = FlashCard("known_words.json")
window = tk.Tk()
front = tk.Canvas(width=200, height=200)

french_word = tk.Label(front, text="")
french_phrase = tk.Label(front, text="")

back = tk.Canvas(width=200, height=200)
english_word = tk.Label(back, text="")
english_phrase = tk.Label(back, text="")

french_face = True
session_words = []
current_word = 0

def flip_current_card():
    global french_face
    print("trying to flip ", french_face)
    if french_face:
        front.pack_forget()
        back.pack()
        french_face = False
    else:
        back.pack_forget()
        front.pack()
        french_face = True

def end_session():
    tk.messagebox.showinfo("session finished!", "You have finished your study session for today.")
    window.destroy()
    sys.exit()

def next_word(known):
    global current_word
    if current_word < len(session_words)-1:
        flash_cards.evaluate_word(current_word, known)
        current_word += 1
        show_flash_card(frenchWords.get_word(session_words[current_word]))
    else:
        end_session()

know_button = tk.Button(text="Got It!", command=lambda: next_word(True))
dont_know_button = tk.Button(text="Repeat", command=lambda: next_word(False))
flip_card_button = tk.Button(text="Flip Card", command=flip_current_card)

def show_flash_card(word):
    global french_face
    fr_phrase = word["phrase_fr"]
    fr_word = word["word_fr"]
    en_phrase = word["phrase_en"]
    en_word = word["word_en"]

    french_word.config(text=fr_word)
    french_phrase.config(text=fr_phrase)

    french_word.pack()
    french_phrase.pack()
    front.pack()
    french_face = True

    english_word.config(text=en_word)
    english_phrase.config(text=en_phrase)
    english_word.pack()
    english_phrase.pack()

def main():
    global session_words
    #this can be changed for UI obv
    session_type = input("What kind of session you want? type 'remember' or 'new': \n")
    word_count = int(input("How many words do you want to study?: \n"))

    know_button.pack()
    dont_know_button.pack()
    flip_card_button.pack()

    if session_type == "remember":
        session_words = frenchWords.get_new_words(word_count)
    else:
        session_words = frenchWords.get_new_and_known_words(word_count)
    show_flash_card(frenchWords.get_word(session_words[current_word]))

    window.mainloop()

if __name__ == "__main__":
    main()





