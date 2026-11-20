from Orderline import Orderline
from Product import Product

class Order():
    def __init__(self, order_id:str) -> None:
        self._order_id = order_id
        self._order_lines: list[Orderline] = []

    def add_order_line(self, product:Product, quantity:int) -> None:
        order_line = Orderline(product, quantity)
        self._order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        for line in self._order_lines:
            total += line.calculate_subtotal()
        return total

    def display_all(self) -> str:
        for line in self._order_lines:
            line.display()
        print(f'Total: {self.calculate_total()}')

        

            
