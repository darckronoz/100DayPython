from coin import Coin

class MoneyModule:
    def __init__(self, money):
        self.money = money

    def validate_money(self, cost):
        # Entering the money can be improved but as this will in theory came from 1 of
        # the machine sensors then it does not matter :D
        user_money = input(
            f"Cost: {cost}\n Insert coins\n QUANTITY:COINTYPE, eg 4:quarter,2:dimes,1:nickel,1:pennies\n").split(",")
        total_money = float(0)
        for coins in user_money:
            count = int(coins.split(":")[0])
            amount = Coin[coins.split(":")[1].upper()].value
            total_money += amount * count
        if total_money > cost:
            print(f"take your change: ${total_money - cost}")
        elif total_money < cost:
            print(f"not enough money")
        return total_money >= cost