class Product:
    def __init__(self, id, name, price, stock):
        self._id = id
        self._name = name
        self._price = price
        self._stock = stock

    def update_stock(self, new_stock):
        self._stock = new_stock

    def display_information(self):
        print("---------------")
        print(f'Product ID: {self._id}\nProduct Name: {self._name}\nPrice: {self._price}\nStock: {self._stock} ')