from ProductFactory import ProductFactory
from Supplier import Supplier

supplier = Supplier("S001", "Razer", "razer@razer.com")
ProductFactory.create("service", "P001", "Installation", 30.0, 5, supplier)
