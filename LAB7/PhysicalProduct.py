from Product import Product

class PhysicalProduct(Product):
    def __init__(self, id, name, price, stock, weight):
        super().__init__(id, name, price, stock)
        self._weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self._weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

#test
physical_product = PhysicalProduct(
    id = "P001",
    name = "Guitar",
    price = 100.0,
    stock = 10,
    weight = 2.5
)
physical_product.display_information()