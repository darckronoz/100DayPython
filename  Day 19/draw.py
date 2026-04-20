#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha

#Turtle with event listeners
#draw with turtle and the arrow on the keyboard
import turtle

def move_forward():
    turtle.forward(20)

def move_backwards():
    turtle.forward(-20)

def turn_left():
    turtle.left(20)

def turn_right():
    turtle.right(20)

screen = turtle.Screen()
screen.setup(width=800, height=600)

screen.onkey(move_forward, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

screen.listen()
screen.exitonclick()