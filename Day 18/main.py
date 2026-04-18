#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import math
import random
#this is the first one I have to stop and watch because I have never
#worked with python to make GUI
from turtle import Turtle, Screen
import colorgram

turtle = Turtle()
turtle.color("orange")

def reset():
    turtle.clear()
    turtle.teleport(0,0)

#the way I found
#dash line
for i in range(6):
    turtle.forward(20)
    (x, y) = turtle.pos()
    turtle.teleport(x + 20, y)

#intended was using penup and pendown

#draw triangle, square, pentagon, hexagon, heptagon, nonagon, and decagon.
reset()

#triangle
turtle.color("blue")
turtle.begin_fill()
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.end_fill()

reset()
#square
turtle.color("red")
turtle.begin_fill()
for i in range(3):
    turtle.forward(50)
    turtle.right(90)
turtle.forward(50)
turtle.end_fill()

reset()
#pentagon
turtle.color("black")
turtle.begin_fill()
for i in range(4):
    turtle.forward(50)
    turtle.right(72)
turtle.forward(50)
turtle.end_fill()

reset()

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    turtle.color(R, G, B)

def move_to_center(sides,l, angle):
    constant = 0.25*(sides+2)
    perimeter = sides*l
    radius = perimeter/(math.pi*2)
    turtle.right(angle*(constant))
    turtle.forward(radius)
    #turtle.right(angle)

#I found the patern!, its 360 divided by the number of sides of the shape
def draw_shape(sides):
    angles = 360/sides
    longitud = (angles*math.pi*1.5)/5
    for _ in range(sides-1):
        turtle.forward(longitud)
        turtle.right(longitud)
    turtle.forward(longitud)

def draw_outher_circle(sides):
    angles = 360 / sides
    longitud = (angles * math.pi)/2
    for _ in range(sides - 1):
        turtle.forward(longitud)
        turtle.right(angles)
    turtle.forward(longitud)
    move_to_center(sides, longitud, angles)
    draw_shape(15)

# i Just started experimenting with circles haha
# for _ in range(30):
#     draw_outher_circle(9)
#     draw_outher_circle(9)

colors = colorgram.extract("dots.jpg", 10)
for c in colors:
    print(type(c.rgb.r))

screen = Screen()
screen.colormode(255)

def move_forward_without_drawing(distance):
    turtle.penup()
    turtle.forward(distance)
    turtle.pendown()

def select_random_color():
    color = random.choice(colors).rgb
    turtle.color((color))

reset()
turtle.setheading(0)
turtle.heading()
turtle.teleport(-350,-300)
for _ in range(21):
    for _ in range(23):
        select_random_color()
        turtle.dot(20)
        move_forward_without_drawing(30)
    turtle.dot(20)
    if turtle.pos()[0] > 0:
        turtle.setheading(90)
        turtle.heading()
        move_forward_without_drawing(30)
        turtle.setheading(180)
        turtle.heading()
    else:
        turtle.setheading(90)
        turtle.heading()
        move_forward_without_drawing(30)
        turtle.setheading(0)
        turtle.heading()

#Un desastre pero terminado el experimento con turtle.

screen.exitonclick()