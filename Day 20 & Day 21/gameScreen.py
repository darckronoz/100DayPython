from random import random, randint
from time import sleep
from turtle import Turtle
from snake import Snake

writer = Turtle()
food = Turtle()
score = 0

class GameScreen:
    def __init__(self, screen, param_snake: Snake):
        self.screen = screen
        self.snake = param_snake
        self.set_up_screen()

    def set_up_screen(self):
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        writer.color("white")
        writer.hideturtle()
        writer.teleport(0, 295)
        writer.write("Snake Game", move=False, align='center', font=('Arial', 12, 'normal'))
        writer.teleport(-295, -295)
        writer.write("Score: 0", move=False, align='right', font=('Arial', 12, 'normal'))
        food.color("red")
        food.shape("circle")
        food.penup()
        food.teleport(randint(-300, 300), randint(-300, 300))


    def move_food(self):
        food.teleport(randint(-300, 300), randint(-300, 300))

    def increase_score(self):
        global score
        score += 1
        writer.teleport(-288, -285)
        writer.color("black")
        writer.dot(40)
        writer.teleport(-299, -295)
        writer.color("white")
        writer.write(str(score), move=False, align='center', font=('Arial', 12, 'normal'))

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
        self.screen.clear()
        writer.goto(0,0)
        writer.color("red")
        writer.write(f"You lose :C, score: {score}", move=False, align='center', font=('Arial', 50, 'normal'))