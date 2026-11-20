from Orderline import Orderline
from Product import Product
from LAB9.discount_strategy.DiscountStrategy import DiscountStrategy
from LAB9.discount_strategy.NoDiscount import NoDiscount


class Order():
    def __init__(self, order_id:str, discount:DiscountStrategy | None = None) -> None:
        self._order_id = order_id
        self._order_lines: list[Orderline] = []
        self._discount = discount or NoDiscount()

    def set_discount(self, discount:DiscountStrategy) -> None:
        self._discount = discount

    def add_order_line(self, product:Product, quantity:int) -> None:
        order_line = Orderline(product, quantity)
        self._order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        for line in self._order_lines:
            total += line.calculate_subtotal()
        return self._discount.apply(total)

    def display_all(self) -> str:
        for line in self._order_lines:
            line.display()
        print(f'Total: {self.calculate_total()}')

        

            
