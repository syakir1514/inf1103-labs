
class Product:
    def __init__(self, ID, name, price, stock):
        self._id = ID
        self._name = name
        self._price = price
        self._stock = stock

    def update_stock(self, quantity):
        self.__stock = self.__stock + quantity

    def display_information(self):
        print(f'Product ID: {self._id}\n Product Name: {self._name}\n Price: {self._price} Stock: {self._stock} ')

class Inventory:
    def __init__(self):
        self._inventory = []

    def add_product(self, product):
        self._inventory.append(product)

    def search_product(self, search_type, search_filter):
        for product in self._inventory: 
            if search_type == "id":
                if product._id == search_filter:
                    product.display_information()
                    return
            elif search_type == "name":
                if product._name == search_filter:
                    product.display_information()
                    return

    def display_all(self):
        for product in self._inventory:
            product.display_information()
        



