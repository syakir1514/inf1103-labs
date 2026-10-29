class Product:
    def __init__(self, id, name, price, stock):
        self._id = id
        self._name = name
        self._price = price
        self._stock = stock

    def update_stock(self, quantity):
        self.__stock = self.__stock + quantity

    def display_information(self):
        print(f'Product ID: {self._id}\n Product Name: {self._name}\n Price: {self._price} Stock: {self._stock} ')