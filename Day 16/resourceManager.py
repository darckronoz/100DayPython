from product import Product

class ResourceManager:
    def __init__(self, water, milk, coffee):
        self.water = water
        self.milk = milk
        self.coffee = coffee

    def validate_resources(self, product: Product):
        for ingredient in product.ingredients:
            if getattr(self, ingredient.name) < ingredient.amount:
                return False
        return True

    def consume_resources(self, product: Product):
        for ingredient in product.ingredients:
            match ingredient.name:
                case "water":
                    self.water -= ingredient.amount
                case "milk":
                    self.milk -= ingredient.amount
                case "coffee":
                    self.coffee -= ingredient.amount
