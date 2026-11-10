from Product import Product

class Orderline():
    def __init__(self, product:Product, quantity:int):
        self._product = product
        self._quantity = quantity

    def calculate_subtotal0(self) -> float:
        return self._product._price * self._quantity