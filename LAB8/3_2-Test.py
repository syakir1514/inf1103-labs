from Inventory import Inventory
from PhysicalProduct import PhysicalProduct
from Supplier import Supplier

supplier = Supplier("S001", "Razer", "razer@razer.com")

product1 = PhysicalProduct("P001", "Keyboard", 50.0, 30, supplier, 0.2)

inventoryA = Inventory()
inventoryA.add_product(product1)
print("inventoryA display:")
inventoryA.display_all()
inventoryA.rm_product("P001")
print("product1 display after removing from inventoryA:")
product1.display_information()
inventoryB = Inventory()
inventoryB.add_product(product1)
print("inventoryB display:")
inventoryB.display_all()

