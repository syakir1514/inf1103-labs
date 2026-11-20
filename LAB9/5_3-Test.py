from main import load_products
from Inventory import Inventory
from Supplier import Supplier

supplier = Supplier("S001", "Razer", "razer@razer.com")
load_products("products.csv", Inventory(), supplier)