#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import sys

#To Do: make it cyclic.
#Caesar Cipher

available_actions = ["encode", "decode"]

def encode(word, key):
    result = ""
    for c in word:
        result += chr(ord(c) + key)
    return result

def decode(word, key):
    result = ""
    for c in word:
        result += chr(ord(c) - key)
    return result

current_action = "encode"

while current_action in available_actions:
    current_action = input("do you want to encode or decode?")
    if current_action not in available_actions:
        print("exiting, available actions: ", available_actions)
        sys.exit()
    word = input("Enter the word: ")
    key = int(input("Enter the key: "))
    if current_action == "encode":
        print(encode(word, key))
    elif current_action == "decode":
        print(decode(word, key))