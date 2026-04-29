#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import os
import tkinter as tk

from dotenv import load_dotenv
from questions import Questions
from gui import Gui
#store this token on the

screen = tk.Tk()

load_dotenv()

question_number = int(input("How many questions fo you want?:\n"))
difficulty = input("Select your difficulty Type 'easy', 'medium' or 'hard':\n")

Questions = Questions(difficulty, question_number)

def main(token=os.getenv('QUIZ_TOKEN')):
    response,status_code = Questions.get_questions(token)
    if status_code == 200:
        if response["response_code"] == 3 or response["response_code"] == 4:
            token = Questions.generate_token()
            main(token)
        else:
            current = 0
            window = Gui(screen)
            screen.lift()
            questions = response["results"]
            def next_question(answer):
                nonlocal current
                window.evaluate_question(questions[current]["correct_answer"], answer)
                current += 1
                if current == len(questions):
                    window.display_finish(len(questions))
                else:
                    window.display_question(questions[current]["question"], current+1)
            window.start_game(next_question, questions[current]["question"])

    screen.mainloop()

if __name__ == "__main__":
    main()