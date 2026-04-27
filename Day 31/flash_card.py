import datetime
import json

from known_word import KnownWord

class FlashCard:
    def __init__(self, filename):
        self.filename = filename

    def evaluate_word(self, rank, know: bool):
        last_studied = datetime.datetime.now().strftime("%d/%m/%Y")
        with open(self.filename, 'r') as f:
            data = json.load(f)
        known_words = data["known"]
        indexes = [i for i, obj in enumerate(known_words) if obj["rank"] == rank]
        if len(indexes) > 0:
            index = indexes[0]
            if know:
                known_words[index]["score"] += 1
            elif known_words[index]["score"] > 0 and not know:
                known_words[index]["score"] -= 1
            known_words[index]["last_studied"] = last_studied
        else:
            if know:
                known_words.append({"rank": rank, "score": 1, "last_studied": last_studied})
            else:
                known_words.append({"rank": rank, "score": 0, "last_studied": last_studied})
        result = {"known" : known_words}
        with open(self.filename, "w+") as f:
            json.dump(result, f)







