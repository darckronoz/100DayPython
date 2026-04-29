import html
import sys
import tkinter as tk

from click import command


class Gui:
    def __init__(self, screen):
        self.false_button = None
        self.true_button = None
        self.question_canva = None
        self.screen = screen
        self.question_label = None
        self.score = 0
        self.score_label = None

    def start_game(self, next_question, first_question):
        self.screen.title("QUIZ")
        self.question_canva = tk.Canvas(width=300, height=300)
        buttons_canvas = tk.Canvas(width=300, height=150)
        self.question_canva.grid(row=0, column=0)
        buttons_canvas.grid(row=1, column=0)
        self.score_label = tk.Label(self.screen, text=f"Score: {self.score}")
        self.score_label.grid(row=2, column=0)
        self.true_button = tk.Button(buttons_canvas, text="true", command=lambda: next_question("True"))
        self.false_button = tk.Button(buttons_canvas, text="false", command=lambda: next_question("False"))
        self.true_button.grid(row=0, column=0)
        self.false_button.grid(row=0, column=1)
        self.question_label = tk.Label(self.question_canva)
        self.question_label.grid(row=0, column=0)
        self.display_question(first_question, 1)

    def display_question(self, question, number):
        self.question_label.config(text=f"Question number {number}!: {html.unescape(question)}")

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def evaluate_question(self, correct_answer, answer):
        if correct_answer == answer:
            self.score += 1
            self.update_score()

    def display_finish(self, total_questions):
        self.question_label.config(text=f"Finished! final score: {self.score}")
        self.score_label.config(text=f"{total_questions-self.score} Wrong Answers!")
        self.false_button.config(command=lambda: {sys.exit(0)})
        self.true_button.config(command=lambda: {sys.exit(0)})




