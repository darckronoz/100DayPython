#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import sys
from time import sleep

#Coffee Machine...
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
            "ingredients": {
                "water": 200,
                "coffee": 24,
                "milk": 150,
            },
            "cost": 2.5
        },
    "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0
        },
}

machine_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins_values = {
    "quarter": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

money = 0

def turn_off():
    print("turning off")
    sys.exit()

def print_report():
    print(f"""
    Report:
        Water: {machine_resources["water"]}ml
        Milk: {machine_resources["milk"]}ml
        Coffee: {machine_resources["coffee"]}g
        Money: ${money}
    """)
    start()

def validate_resources(product):
    for ingredient in product["ingredients"].keys():
        if product["ingredients"][ingredient] > machine_resources[ingredient]:
            return False
    return True

def validate_money(cost):
    #The enter of the money can be improved but as this will in theory came from 1 of
    #the machine sensors then it does not matter :D
    user_money = input(f"Cost: {cost}\n Insert coins\n QUANTITY:COINTYPE, eg 4:quarter,2:dimes,1:nickel,1:pennies").split(",")
    total_money = float(0)
    for coins in user_money:
        count = int(coins.split(":")[0])
        amount = coins_values[coins.split(":")[1]]
        total_money += amount*count
    if total_money > cost:
        print(f"take your change: ${total_money-cost}")
    elif total_money < cost:
        print(f"not enough money")
    return total_money>=cost

def prepare_product(user_command):
    global money, machine_resources
    product = MENU[user_command]
    if validate_resources(product):
        if validate_money(product["cost"]):
            money += product["cost"]
            print(f"preparing: {user_command}")
            for ingredient in product["ingredients"].keys():
                machine_resources[ingredient] -= product["ingredients"][ingredient]
            sleep(1)
            print(f"Here is you {user_command}. Enjoy!")
            start()
        else:
            print("Money refunded.")
            start()
    else:
        print("Not enough resources")
        start()

def start():
    user_command = input("What would you like? (espresso/latte/cappucino) \n")
    match user_command:
        case "report":
            print_report()
        case "off":
            turn_off()
        case "espresso" | "latte" | "capuccino":
            prepare_product(user_command)
        case _:
            print("incorrect command, restarting...")
            start()

start()
