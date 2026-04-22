from random import random, randint
from time import sleep
from turtle import Turtle
from snake import Snake

score_writer = Turtle()
writer = Turtle()
food = Turtle()
score = 0

class GameScreen:
    def __init__(self, screen, param_snake: Snake, highscore):
        self.screen = screen
        self.snake = param_snake
        self.highscore = highscore
        self.set_up_screen()


    def set_up_screen(self):
        global score_writer
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        writer.color("white")
        writer.hideturtle()
        writer.teleport(0, 295)
        writer.write("Snake Game", move=False, align='center', font=('Arial', 12, 'normal'))
        score_writer.hideturtle()
        score_writer.color("white")
        score_writer.teleport(-295, -295)
        score_writer.write("Score: 0", move=False, align='right', font=('Arial', 12, 'normal'))
        score_writer.teleport(-100, -295)
        score_writer.write(f"High score: {self.highscore}", move=False, align='right', font=('Arial', 12, 'normal'))
        food.color("red")
        food.shape("circle")
        food.penup()
        food.teleport(randint(-300, 300), randint(-300, 300))


    def move_food(self):
        food.teleport(randint(-300, 300), randint(-300, 300))

    def increase_score(self):
        global score
        score += 1
        score_writer.clear()
        score_writer.teleport(-295, -295)
        score_writer.write(f"Score: {score}", move=False, align='center', font=('Arial', 12, 'normal'))
        if score >= self.highscore:
            self.highscore = score
        score_writer.teleport(-100, -295)
        score_writer.write(f"High score: {self.highscore}", move=False, align='right', font=('Arial', 12, 'normal'))

    def evaluate_dead(self):
        (x,y) = self.snake.get_position()
        if x >= 360 or x <= -360 or y >= 300 or y <= -300:
            return True
        else:
            return False

    def evaluate_eat(self):
        (snake_x, snake_y) = self.snake.get_position()
        (food_x, food_y) = food.position()

        if int(snake_x) in range(int(food_x) - 20, int(food_x) + 20) and int(snake_y) in range(int(food_y) - 20, int(food_y) + 20):
            self.move_food()
            self.increase_score()
            self.snake.increase_length()

    def display_lose_screen(self):
        if score >= self.highscore:
            with open("score.txt", "w") as file:
                file.write(str(score))
        self.screen.clear()
        writer.goto(0,0)
        writer.color("red")
        writer.write(f"You lose :C, score: {score}", move=False, align='center', font=('Arial', 50, 'normal'))