from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from Product import Product

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())

supplier = Supplier("S001", "Razer", "razer@razer.com")

physical = PhysicalProduct("P001", "Keyboard", 50.0, 30, supplier, 0.2)
digital = DigitalProduct("D001", "Game", 100.0, 20, supplier, 1000)

inventory1 = Inventory()
inventory1.add_product(physical)
inventory1.add_product(digital)
inventory1.display_all()

show_product_details(physical)
show_product_details(digital)




