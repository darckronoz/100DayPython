#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha

#pandas...
import pandas as pd
from turtle import Turtle, Screen

data = pd.read_csv("data.csv")
data_with_no_country = data.drop('country', axis = 1)
data_with_no_country[['x', 'y']] = data_with_no_country['location'].str.split('-', n = 1, expand = True)
data_with_no_country = data_with_no_country.drop('location', axis = 1)

print(data_with_no_country.head())

screen = Screen()
screen.setup(width=500, height=673)
screen.bgpic("map.jpg")
screen.tracer(0,0)
department_writer = Turtle()
department_writer.hideturtle()

def write_department(name, x, y):
    department_writer.teleport(x, y)
    department_writer.write(name, align='center', font=('Arial', 10, 'normal'))

def start_game():
    guess = screen.textinput("Departamento", "Escribe un departamento")
    department = data_with_no_country[data_with_no_country['name'] == guess]
    if not department.empty:
        write_department(department.name.array[0], float(department.x.array[0]), float(department.y.array[0]))
    screen.ontimer(start_game, 100)

start_game()

screen.exitonclick()


