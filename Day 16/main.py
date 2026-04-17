##Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
from enum import Enum

#coffee machine with oop.
from coffeeMachine import CoffeeMachine
from resourceManager import ResourceManager
from moneyModule import MoneyModule
from menu import Menu
from product import Product
from ingredient import Ingredient

#I just modified the original to be OOP, there's much room to improve here
#however, next day!
def main():
    products: list[Product] = [
                            Product("espresso",
                                [Ingredient("water", 50),
                                Ingredient("coffee", 18)],
                                1.5),
                            Product("latte",
                                [Ingredient("water", 200),
                                Ingredient("coffee", 24),
                                Ingredient("milk", 150)],
                                2.5),
                            Product("cappuccino",
                                [Ingredient("water", 250),
                                Ingredient("coffee", 100),
                                Ingredient("milk", 24)],
                                3.0)]

    m = Menu(products)
    rm = ResourceManager(300,200,100)
    mm = MoneyModule(0)
    coffee_machine = CoffeeMachine(rm, mm, m)
    coffee_machine.start()

if __name__ == "__main__":
    main()
