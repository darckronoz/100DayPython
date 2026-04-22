#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import random

#Turtle crossing the road.

from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "violet"]


screen = Screen()
screen.tracer(0,0)

cars_quantity = 15
cars = []

for i in range(cars_quantity):
    t = Turtle()
    t.shape("square")
    t.turtlesize(1, 2)
    t.speed(1)
    t.color(random.choice(colors))
    t.penup()
    t.goto(random.randint(-300, 900), random.randint(-250, 250))
    t.setheading(180)
    cars.append(t)

player = Turtle()
player.shape("turtle")
player.color("black")
player.penup()
player.goto(0,-290)
player.setheading(90)

def move_player_up():
    player.forward(20)

def move_player_down():
    player.backward(20)

score_writer = Turtle()

movement_counter = 0
level = 1

def increase_level():
    global level
    level += 1
    score_writer.clear()
    score_writer.write(f"level: {level}", align="center", font=("Terminal", 20, "bold"))
    player.goto(0,-290)
    move_cars()

def move_cars():
    for car in cars:
        car.forward(5)
        if player.distance(car.pos()) < 10:
            score_writer.clear()
            score_writer.write(f"you lose :( level: {level}", align="center", font=("Terminal", 20, "bold"))
            return
        if car.xcor() < -300:
            car.goto(310,random.randint(-250, 250))
    if player.ycor() > 270:
        increase_level()

    screen.ontimer(move_cars, 80-level)
    screen.update()

score_writer.hideturtle()
score_writer.teleport(0,0)
score_writer.write(f"level: {level}", align="center", font=("Terminal", 20, "bold"))

#it's funny
move_cars()

screen.onkey(move_player_up, "w")
screen.onkey(move_player_down, "s")

screen.setup(width=800, height=600)
screen.listen()
screen.exitonclick()