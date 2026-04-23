#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import time
#Pomodoro GUI using Tkinter.

from tkinter import *

window = Tk()
window.title("Pomodoro :D")
window.geometry("500x500")
bg_pic = PhotoImage(file="tomate.png")
background_label = Label(window, image=bg_pic)
background_label.place(x=0, y=0)

timer = Label()

timer.place(x=230, y=250)

work_sections = 4
minutes = 0
seconds = 0
keep_going = True

def count_interval(mins):
    global seconds, minutes
    for minute in range(mins):
        if keep_going:
            time.sleep(1)
            pass_one_second()
            timer["text"] = f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
            window.update()
        else:
            window.update()
            return

def pass_one_second():
    global seconds, minutes
    seconds += 1
    if seconds > 59:
        minutes += 1
        seconds = 0

def start_pomodoro():
    window.update()
    global minutes, keep_going
    keep_going = True
    for _ in range(work_sections):
        count_interval(2)
        minutes = 0
        window.lift()
        count_interval(1)
        minutes = 0
    count_interval(2)
    minutes = 0

def reset_pomodoro():
    window.update()
    global minutes, seconds, keep_going
    keep_going = False
    minutes = 0
    seconds = 0
    timer["text"] = f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    window.update()

timer["text"] = f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
start_button = Button(command=start_pomodoro, text="start")
start_button.place(x=120, y=350)
reset_button = Button(command=reset_pomodoro, text="reset")
reset_button.place(x=340, y=350)

window.mainloop()