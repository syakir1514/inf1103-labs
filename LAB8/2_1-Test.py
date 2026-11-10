from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct


supplier = Supplier("S001", "Razer", "razer@razer.com")

physical = PhysicalProduct("P001", "Keyboard", 50.0, 30, supplier, 0.2)
digital = DigitalProduct("D001", "Game", 100.0, 20, supplier, 1000)

del supplier

physical.display_information()
digital.display_information()



