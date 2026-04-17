from typing import NamedTuple
from ingredient import Ingredient

class Product(NamedTuple):
    name: str
    ingredients: list[Ingredient]
    cost: float