import json

import pandas as pd

class FrenchDict:
    def __init__(self, csv_file: str, exclude_file):
        self.df = pd.read_csv(csv_file)
        self.exclude_file = exclude_file

    def get_known_words(self, score):
        with open(self.exclude_file, "r") as file:
            known_words = json.load(file)["known"]
        return [word["rank"] for word in known_words if word["score"] >= score]

    def get_new_and_known_words(self, count):
        exclude = self.get_known_words(10)
        return [
            row[1]["rank"]
            for row in self.df.iterrows()
            if row[1]["rank"] not in exclude
        ][:count]

    def get_new_words(self, count):
        exclude = self.get_known_words(5)
        return [
            row[1]["rank"]
            for row in self.df.iterrows()
            if row[1]["rank"] not in exclude
        ][:count]

    def get_word(self, rank):
        return self.df.query('rank == @rank').to_dict("records")[0]