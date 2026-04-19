#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import random
#Turtle with event listeners
#Turtle race
import turtle
from time import sleep
from turtle import Turtle, Screen

colors = ["red", "blue", "black", "green", "orange", "purple"]

turtle_list = []

def create_turtles():
    for c in colors:
        sleep(0.2)
        turtle_racer = Turtle()
        turtle_racer.shape("turtle")
        turtle_racer.color(c)
        turtle_racer.speed(0)
        turtle_racer.penup()
        turtle_list.append(turtle_racer)

create_turtles()
screen = Screen()

def place_turtles():
    position = -50
    for t in turtle_list:
        sleep(0.2)
        t.teleport(-350, position)
        position += 30

def race():
    place_turtles()
    user_bet = screen.textinput("Who do you think will win?", "Input a color: ")
    first = turtle_list[0]
    while first.pos()[0] < 350:
        for t in turtle_list:
             t.forward(random.randint(10,50))
        for t in turtle_list:
            if t.pos()[0] > first.pos()[0]:
                first = t
    winner = first.color()[0]
    print(f"The Winner is: the {winner} turtle!!")
    if user_bet == winner:
        print("You Won!")
    else:
        print("You Lost!")

race()
screen.exitonclick()