#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha


#A labyrinth solving algorithm?...
import random

robot = "String representing a robot object haha :D"

maze = "string representing a maze that the robot can be on haha :D"

#boolean representing that the robot has reached x and y on the goal of the maze :D
win_condition = False

wall_in_front_of_robot = False

def move_forwards():
    print("Moving Forward")

def turn_right():
    print("Turning Right")

def check_possible_paths():


def validate_wall():
    global wall_in_front_of_robot
    if random.randint(0, 4) == 3:
        wall_in_front_of_robot = False
    else:
        wall_in_front_of_robot = True

while not win_condition:
    #simulating that the robot found the way?
    if random.randint(0, 100) == 27:
        win_condition = True
    
    validate_wall()
    while wall_in_front_of_robot:
        turn_right()
    move_forwards()

