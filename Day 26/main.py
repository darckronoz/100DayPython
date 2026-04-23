#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha

#List comprehension.

# numbers = [1,2,3]
# new_list = [n+1 for n in numbers]
# name = "cristhian"
# new_name = [l.upper() for l in name]
# doubled_numbers = [n*2 for n in range(1,5)]
# names = ["juan", "carlos", "camilo", "juan", "carlos", "camila"]
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)

#NATO Alphabet
import pandas as pd

nato_dataframe = pd.read_csv("data.csv")
nato_dictionary = {row[1].letter:row[1].nato for row in nato_dataframe.iterrows()}

#a more "pandas way" for doing this is using zip and dict

# zip creates a tuple element by element, and dict creates a dictionary from a list of tuples
nato_dictionary_two = dict(zip(nato_dataframe["letter"], nato_dataframe["nato"]))
#print(nato_dictionary_two)
name = input("Enter your name: ")

print([nato_dictionary[letter.upper()] for letter in name if letter.upper() in nato_dictionary])