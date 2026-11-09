from Product import Product
from CanBeShipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, id, name, price, stock, weight):
        super().__init__(id, name, price, stock)
        self._medium = "physical"
        self._weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self._weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return self._weight * 5.0

#test
def test():
    physical_1 = PhysicalProduct(
        id = "P001",
        name = "Guitar",
        price = 100.0,
        stock = 10,
        weight = 2.5
    )

    physical_2 = PhysicalProduct(
        id = "P002",
        name = "Table",
        price = 50.0,
        stock = 5,
        weight = 12.0
    )

    physical_1.display_information()
    print(physical_1.get_fulfilment_info())
    print(f"Shipping cost: $ {physical_1.calculate_shipping_cost()}")

    physical_2.display_information()
    print(physical_2.get_fulfilment_info())
    print(f"Shipping cost: $ {physical_2.calculate_shipping_cost()}")

