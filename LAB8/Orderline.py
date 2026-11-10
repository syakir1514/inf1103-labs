from Product import Product

class Orderline():
    def __init__(self, product:Product, quantity:int) -> None:
        self._product = product
        self._quantity = quantity

    def calculate_subtotal(self) -> float:
        return self._product._price * self._quantity

    def display(self) -> str:
        print(f'Product Name: {self._product._name}     | Quantity: {self._quantity}    | Subtotal: {self.calculate_subtotal()}')