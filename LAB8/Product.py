from abc import ABC, abstractmethod
from Supplier import Supplier

class Product(ABC):
    def __init__(self, id:str, name:str, price:float, stock:int, supplier: Supplier):
        self._id = id
        self._name = name
        self._price = price
        self._stock = stock
        self._supplier = supplier

    def update_stock(self, new_stock):
        self._stock = new_stock

    def display_information(self):
        print(f'''
----------------------
Product ID: {self._id}
Product Name: {self._name}
Price: {self._price}
Stock: {self._stock}''')
    
    def display_supplier(self):
        print(f'''
-----Supplier Info-----
Supplier ID: {self._supplier._id}
Supplier Name: {self._supplier._name}
Supplier Contact: {self._supplier._email}
-----------------------
        ''')


    @abstractmethod
    def get_fulfilment_info(self):
        pass
