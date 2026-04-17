import sys
from time import sleep
from resourceManager import ResourceManager
from moneyModule import MoneyModule
from menu import Menu

class CoffeeMachine:

    def __init__(self, resources: ResourceManager, money_module: MoneyModule, menu: Menu):
        self.machine_resources = resources
        self.money_module = money_module
        self.menu = menu

    def turn_off(self):
        print("turning off")
        sys.exit()

    def print_report(self):
        print(f"""
        Report:
            Water: {self.machine_resources.water}ml
            Milk: {self.machine_resources.milk}ml
            Coffee: {self.machine_resources.coffee}g
            Money: ${self.money_module.money}
        """)
        self.start()

    def prepare_product(self, user_command):
        product = self.menu.get_product_by_name(user_command)
        if product is not None:
            if self.machine_resources.validate_resources(product):
                if self.money_module.validate_money(product.cost):
                    self.money_module.money += product.cost
                    print(f"preparing: {user_command}")
                    self.machine_resources.consume_resources(product)
                    sleep(1)
                    print(f"Here is you {user_command}. Enjoy!")
                    self.start()
                else:
                    print("Money refunded.")
                    self.start()
            else:
                print("Not enough resources")
                self.start()
        print("ERROR: product not found.")
        self.start()

    def start(self):
        user_command = input("What would you like? (espresso/latte/cappucino) \n")
        match user_command:
            case "report":
                self.print_report()
            case "off":
                self.turn_off()
            case "espresso" | "latte" | "capuccino":
                self.prepare_product(user_command)
            case _:
                print("incorrect command, restarting...")
                self.start()