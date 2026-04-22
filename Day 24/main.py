#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha

#congratulations letter template

import shutil

names = ["cris", "juan", "pepe", "juana", "pepa", "cristina"]

for name in names:
    file_name = f"./congrats_{name}.txt"
    shutil.copy("congrats_name.txt", file_name)
    with open(file_name, "r") as file:
        lines = file.readlines()
    lines[1] = f'Dear {name}\n'
    with open(file_name, "w") as file:
        file.writelines(lines)


