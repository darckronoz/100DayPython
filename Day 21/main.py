#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import turtle
from turtle import Turtle, Screen

#Pong!
#I will not use oop here to try and speed up coding this one.
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!!")

ceiling = Turtle()
ceiling.shape("square")
ceiling.color("white")
ceiling.penup()
ceiling.turtlesize(stretch_len=40, stretch_wid=0.5)
floor = ceiling.clone()

ceiling.goto(0, 290)
floor.goto(0, -290)

painter = Turtle()
player_one_trainer = Turtle()
player_one_trainer.color("white")
player_one_trainer.hideturtle()

player_two_trainer = Turtle()
player_two_trainer.penup()
player_two_trainer.color("white")
player_two_trainer.hideturtle()

player_one = Turtle()
player_one_score = 0

player_one.shape("square")
player_one.color("white")
player_one.setheading(90)
player_one.penup()
player_one.turtlesize(stretch_len=5, stretch_wid=0.5)
player_one.goto(-350, 0)

player_two = player_one.clone()
player_two_score = 0
player_two.goto(350, 0)

painter.color("white")
painter.penup()
painter.hideturtle()
painter.teleport(0, 300)
painter.setheading(270)
for i in range(30):
    painter.pendown()
    painter.forward(10)
    painter.penup()
    painter.forward(10)

ball = Turtle()
bouncing = False
ball.penup()
ball.shape("square")
ball.color("white")

player_one_trainer.penup()
player_one_trainer.goto(120,150)

player_one_trainer.write("0", align="right", font=("Terminal", 100, "bold"))

player_two_trainer.goto(-120,150)
player_two_trainer.write("0", align="left", font=("Terminal", 100, "bold"))

def play_game():
    ball_move()
    evaluate_ball_hit()
    evaluate_score()
    screen.ontimer(play_game, 5)
    screen.update()

def move_player_one_up():
    player_one.forward(40)

def move_player_one_down():
    player_one.backward(40)

def move_player_two_up():
    player_two.forward(40)

def move_player_two_down():
    player_two.backward(40)

def player_one_scored():
    global player_one_score
    player_one_score += 1
    player_one_trainer.clear()
    player_one_trainer.penup()
    player_one_trainer.goto(120, 150)
    player_one_trainer.write(f"{player_one_score}", align="right", font=("Terminal", 100, "bold"))
    ball.goto(0, 0)
    ball.setheading(160)

def player_two_scored():
    global player_two_score
    player_two_score += 1
    player_two_trainer.clear()
    player_two_trainer.penup()
    player_two_trainer.goto(-120, 150)
    player_two_trainer.write(f"{player_two_score}", align="left", font=("Terminal", 100, "bold"))
    ball.goto(0, 0)
    ball.setheading(160)

def ball_move():
    ball.forward(5)

def bounce_vertically():
    angle_in = ball.heading()
    ball.setheading(360-angle_in)

def bounce_horizontally():
    ball.speed(10)
    angle_in = ball.heading()
    ball.setheading(180 - angle_in)
    ball.forward(10)

def evaluate_ball_hit():
    (player_one_x, player_one_y) = player_one.position()
    (player_two_x, player_two_y) = player_two.position()
    (ball_x, ball_y) = ball.position()
    if int(ball_x) < -345 and int(ball_y) in range(int(player_one_y) - 40, int(player_one_y) + 40):
        bounce_horizontally()
        ball.speed(6)
    elif int(ball_x) > 345 and int(ball_y) in range(int(player_two_y) - 40, int(player_two_y) + 40):
        bounce_horizontally()
        ball.speed(6)
    elif ball_y > 287 or ball_y < -287:
        bounce_vertically()


def evaluate_score():
    (ball_x, ball_y) = ball.position()
    if ball_x > 400:
        player_two_scored()
    elif ball_x < -400:
        player_one_scored()

screen.onkeypress(move_player_one_up ,"w")
screen.onkeypress(move_player_two_up ,"u")
screen.onkeypress(move_player_one_down ,"s")
screen.onkeypress(move_player_two_down ,"j")

screen.tracer(0,0)
ball.setheading(160)
play_game()
screen.listen()
screen.exitonclick()
screen.mainloop()

