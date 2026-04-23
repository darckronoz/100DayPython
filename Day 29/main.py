#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import random
#Password manager...
#I won't be putting much effort on the pretty UI part as I need speeeeeed

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("password manager")
window.minsize(400, 300)
window.config(padx=20, pady=20)
lock_image = Canvas(window, width=200, height=200)
lock_photo = PhotoImage(file="lock.png")
lock_image.create_image(100, 100, image=lock_photo)
lock_image.grid(row=0, column=1, columnspan=2)

website_label = Label(window, text="Website: ")
website_input = Entry(window, width=35)

username_label = Label(window, text="uername: ")
username_input = Entry(window, width=35)

password_label = Label(window, text="password: ")
password_input = Entry(window, width=21)

def clean_fields():
    password_input.delete(0, END)
    username_input.delete(0, END)
    website_input.delete(0, END)

def generate_password():
    result = []
    result+=([str(n) for n in random.choices(range(0,9), k=6)])
    result+=([str(chr(n)) for n in random.choices(range(65,122), k=6)])
    result+=([str(chr(n)) for n in random.choices(range(91,96), k=6)])
    random.shuffle(result)
    password_input.delete(0, END)
    password_input.insert(0, ''.join(result))

def save_password():
    user = username_input.get()
    website = website_input.get()
    password = password_input.get()
    row_to_save = ' | '.join([user, website, password])+'\n'
    with open('not_open.txt', 'a') as file:
        file.write(row_to_save)
    messagebox.showinfo("Password Saved", "Password has been saved")
    clean_fields()

generate_pass_button = Button(text="Generate Password", command=generate_password)
save_pass_button = Button(text="Save", width=36, command=save_password)

website_label.grid(row=2, column=0)
website_input.grid(row=2, column=1, columnspan=2)

username_label.grid(row=3, column=0)
username_input.grid(row=3, column=1, columnspan=2)

password_label.grid(row=4, column=0)
password_input.grid(row=4, column=1)

generate_pass_button.grid(row=4, column=2)
save_pass_button.grid(row=5, column=1, columnspan=2)

window.mainloop()