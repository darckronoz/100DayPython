#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha

#Unit converter program with TKinter

import tkinter

window = tkinter.Tk()
window.title("COP to USD")
window.minsize(200, 100)
window.config(padx=50, pady=50)

cop_label = tkinter.Label(window, text="COP: ")
usd_label = tkinter.Label(window, text="USD: ")
cop_input = tkinter.Entry(width=8)
usd_result = tkinter.Label(window)

#unlimited positional args
def my_sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(my_sum(1,2,3,4,5,6,7,7))

#unlimited key word args
def calculate(**kwargs):
    result = 0
    if kwargs.__contains__("operator"):
        if kwargs["operator"] == "+":
            for n in kwargs["value"]:
                result += n
        if kwargs["operator"] == "*":
            result = 1
            for n in kwargs["value"]:
                result *= n
    return result

print(calculate(operator="*", value=[1,2,3,4,5,6,7,7]))
print(calculate(operator="+", value=[1,2,3,4,5,6,7,7]))


def convert_cop_to_usd():
    cop_value = cop_input.get()
    usd_result["text"] = f"{float(cop_value) * float(0.00028)}"

cop_label.grid(row=0, column=0)
cop_input.grid(row=0, column=1)
usd_label.grid(row=1, column=0)
usd_result.grid(row=1, column=1)

convert_button = tkinter.Button(text="convert", command=convert_cop_to_usd)

convert_button.grid(row=2, column=1)

window.mainloop()