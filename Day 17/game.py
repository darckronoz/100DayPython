from question import Question

class Game:
    def __init__(self, question_bank: list[Question], score):
        self.question_bank = question_bank
        self.score = score

    def start_game(self):
        while len(self.question_bank) > 0:
            current = self.question_bank.pop()
            print(current.text)
            user_answer = input("\n True or false? \n")
            if user_answer.lower() == current.answer.lower():
                self.score += 1
                print(f"Correct! The score is {self.score}.")
            else:
                print(f"Incorrect! it's {current.answer}!!"
                      f"\n The score is {self.score}.")
        print(f"you have finished the game!!, final score is {self.score}.")
