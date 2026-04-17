from dataclasses import dataclass
from product import Product

@dataclass
class Menu:
    products: list[Product]

    def get_product_by_name(self, name: str) -> Product|None:
        for product in self.products:
            if product.name == name:
                return product
        return None

