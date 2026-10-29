
class Product:
    def __init___(self, ID, name, price, stock):
        self.__product_id = ID
        self.__product_name = name
        self.__product_price = price
        self.__stock = stock

    def update_stock(self, quantity):
        pass

    def display_information(self):
        print(f'Product ID: {self.__product_id}\n Product Name: {self.__product_name}\n Price: {self.__product_price} Stock: {self.__stock} ')