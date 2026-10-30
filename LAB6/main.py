import json
import inventory_class
import product_class

# search for file named 'inventory.txt'; if none is found, create it.
def load_inventory(inventory_obj):
    print ("Loading Inventory\nPlease Wait...")
    try:
        with open('inventory.json', 'r') as file:    # try to open the file in read mode
            loaded_data = json.load(file)
            for item in loaded_data:
                new_product = product_class.Product(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"]
                )
                inventory_obj.add_product(new_product)
        print ("Inventory Loaded")

    except FileNotFoundError:                       # expect a failure if the file is not found
        print ("No previous inventory found\nCreating new invetory.json file")
        with open('inventory.json', 'w') as file:    # creates the file in write mode
            json.dump([], file)
        print ("New invetory.json file created")
    return

def save_inventory(inventory_obj):
    json_list = []
    for product in inventory_obj._inventory:
        product_dict = {
            "id": product._id,
            "name": product._name,
            "price": product._price,
            "stock": product._stock
        }
        json_list.append(product_dict)

    with open('inventory.json', 'w') as file:
        json.dump(json_list, file, indent=4)
                          

def startup():
    print("---------------")
    print("Welcome to Inventory Management System")
    print("---------------")

    inventory1 = inventory_class.Inventory()                         #creates new inventory object
    load_inventory(inventory1)
    main_menu(inventory1)
    
def quit():
    print("---------------")
    print("Exiting Inventory Management System\nGoodbye!")
    print("---------------")


def main_menu(inventory1):
    while True:
        print("\nInventory Management System\nMain Menu\n")
        print("1. Display all products")
        print("2. Add a product")
        print("3. Seach for a product")
        print("4. Update stock")
        print("5. Save inventory")
        print("Q. Quit")

        main_input = input("Enter your choice with numbers or Q:")

        if main_input == "1":
            inventory1.display_all()

        elif main_input == "2":
            print("Add a New Product\n")
            new_id = input("Enter Product ID: ")
            new_name = input("Enter Product Name: ")
            new_price = float(input("Enter Price: "))
            new_stock = int(input("Enter Stock Quantity: "))
            
            new_product = product_class.Product(new_id, new_name, new_price, new_stock)
            
            inventory1.add_product(new_product)
            
            print(f"\nSuccess! {new_id}: {new_name} has been added to the inventory.")

        elif main_input == "3":
            print("Search for a Product\n")
            search_type = input("Search by: 1: Product ID, 2: Name:")
            if search_type == "1":
                input_id = input("Enter product id:")
                for product in inventory1._inventory:
                    if product._id == input_id:
                        product.display_information()
            elif search_type == "2":
                input_name = input("Enter product name: ")
                for product in inventory1._inventory:
                    if product._name == input_name:
                        product.display_information()

        elif main_input == "4":
            print("Update stock\n")
            search_type = input("Update by: 1: Product ID, 2: Name:")
            if search_type == "1":
                input_id = input("Enter product id:")
                for product in inventory1._inventory:
                    if input_id == product._id:
                        new_stock = int(input(f"Product {product._id}:{product._name} found. Enter new total stock number:"))
                        product.update_stock(new_stock)
                        print(f"Stock for {product._id}:{product._name} updated. New stock: {product._stock}")
            if search_type == "2":
                input_name = input("Enter product name:")
                for product in inventory1._inventory:
                    if input_name == product._name:
                        new_stock = int(input(f"Product {product._id}:{product._name} found. Enter new total stock number:"))
                        product.update_stock(new_stock)
                        print(f"Stock for {product._id}:{product._name} updated. New stock: {product._stock}")
                                
        elif main_input == "5":
            save_inventory(inventory1)
            print("\nInventory Saved Successfully")

        elif main_input.lower() == "q":
            quit()
            break

startup()