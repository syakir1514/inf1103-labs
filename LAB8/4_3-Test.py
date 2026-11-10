from Order import Order
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier

supplier = Supplier("S001", "Razer", "razer@razer.com")

product1 = PhysicalProduct("P001", "Keyboard", 50.0, 30, supplier, 0.2)
product2 = DigitalProduct("D001", "Game", 100.0, 20, supplier, 1000)

order1 = Order("O001")
order1.add_order_line(product1, 10)
order1.add_order_line(product2, 2)
print("order1 displaying:")
order1.display_all()

order2 = Order("O002")
order2.add_order_line(product1, 10)
order2.add_order_line(product2, 2)
print("order2 displaying:")
order2.display_all()

line1 = order1._order_lines[0]
line2 = order2._order_lines[0]
print("Same OrderLine object?", line1 is line2)
print("Same Product object?", line1._product is line2._product)

del order1
print("order1 deleted")

print("order2 displaying:")
order2.display_all()

print("product1 displaying:")
product1.display_information()