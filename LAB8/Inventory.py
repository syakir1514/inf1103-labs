from Product import Product

class Inventory:
    def __init__(self):
        self._inventory: list[Product] = []

    def add_product(self, product:Product):
        self._inventory.append(product)

    def rm_product(self, product_id:str):
        for product in self._inventory:
            if product._id == product_id:
                self._inventory.remove(product)
                return True
        return False

    def find_product(self, product_id: str) -> Product | None:
        for product in self._inventory:
            if product._id == product_id:
                self._inventory.remove(product)
                return product
        return None


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
        if len(self._inventory) == 0:
            print("No records found")
            return
        for product in self._inventory:
            product.display_information()
