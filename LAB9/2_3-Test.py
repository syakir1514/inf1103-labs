from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from Order import Order
from discount_strategy.BulkDiscount import BulkDiscount
from discount_strategy.PercentageDiscount import PercentageDiscount

supplier = Supplier("S001", "Razer", "razer@razer.com")
keyboard = PhysicalProduct("P001", "Keyboard", 50.0, 30, supplier, 0.2)

# Five keyboards at 50.00 each give a subtotal of 250.00.
default_order = Order("O001")
default_order.add_order_line(keyboard, 5)

total = default_order.calculate_total()
print(f"No discount: {total:.2f}")
assert total == 250.0, f"Expected 250.00, got {total:.2f}"

# Pass a bulk discount when creating the order.
order = Order("O002", discount=BulkDiscount(200, 20))
order.add_order_line(keyboard, 5)

total = order.calculate_total()
print(f"Bulk discount: {total:.2f}")
assert total == 230.0, f"Expected 230.00, got {total:.2f}"

# Change the strategy on the same order, without changing its lines.
order.set_discount(PercentageDiscount(10))

total = order.calculate_total()
print(f"Percentage discount: {total:.2f}")
assert total == 225.0, f"Expected 225.00, got {total:.2f}"

print("All Step 2.3 checks passed.")