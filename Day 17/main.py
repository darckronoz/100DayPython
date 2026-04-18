#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha

from question import Question
from data import question_data
from game import Game

def main():
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question["text"], question["answer"]))
    game = Game(question_bank, 0)
    game.start_game()

if __name__ == "__main__":
    main()