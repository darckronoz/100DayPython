#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha

import sys

# a calculator xd

print("this is a python calculatoooor haha! \n")

def perform_operation(a, b, symbol):
    match symbol:
        case "+":
            return a+b
        case "*":
            return a*b
        case "/":
            return a/b
        case "-":
            return a-b
        case _:
            return 0

def kill():
    print("killing!!!")
    sys.exit(0)

use_previous_result = False
selection = ""
result = 0

def get_inputs():
    user_symbol = input("Whats the operation: -, +, * or / \n")
    user_number = int(input("What is the second number? \n"))
    return user_symbol, user_number

functions = {
    "kill": kill
}

while selection != "exit":
    if use_previous_result:
        print("previous result: ", result)
        first_number = result
    else:
        first_number = int(input("What is the first number? \n"))
    inputs = get_inputs()
    operation = inputs[0]
    second_number = inputs[1]
    result = perform_operation(first_number, second_number, operation)
    print(f"result: {result} \n")
    selection = input("Use result for the next operation? Type 'yes', 'no' or 'exit': \n")
    use_previous_result = True if selection == "yes" else False
    #functions[selection]() if selection == "kill" else lambda: None
    #updated to
    functions.get(selection, lambda: None)()







