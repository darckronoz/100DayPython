import time
import requests
import os
from dotenv import set_key

class Questions:
    def __init__(self, difficulty, question_number):
        self.difficulty = difficulty
        self.question_number = question_number

    def generate_token(self):
        print("Generando nuevo token... (espere 5 segundos)")
        response = requests.get("https://opentdb.com/api_token.php?command=request")
        set_key(".env", "QUIZ_TOKEN", response.json()["token"])
        time.sleep(6)
        print("obteniendo preguntas nuevamente...")
        return response.json()["token"]

    def get_questions(self, token):
        response = requests.get(
            f"https://opentdb.com/api.php?amount={self.question_number}&difficulty={self.difficulty}&type=boolean&token={token}")
        return response.json(), response.status_code