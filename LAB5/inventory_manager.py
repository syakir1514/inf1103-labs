import json


def initialise():
    print("===========================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("===========================")
    load_inventory()
    menu()

def load_inventory():
    try:
        with open('inventory.json', 'r') as file:
            print("inventory.json found.")
            print("Inventory loaded successfully.")
            pass
    except FileNotFoundError:
        with open('inventory.json', 'w') as file:
            json.dump([], file, indent=4)
            print("inventory.json file created.")
            pass

def display_products():
    with open('inventory.json', 'r') as file:
        inventory = json.load(file)
        if not inventory:
            print("No products found in the inventory.")
            return
        else:
            print("\nCurrent Inventory")
            print("------------------")
            for product in inventory:
                print(f"ID: {product['id']} | Name: {product['name']} | Price: {product['price']} | Stock: {product['stock']}")

def add_product():
    with open('inventory.json', 'r') as file:
        inventory = json.load(file)
    new_product = {}
    print ("\nAdd New Product")
    new_product['id'] = input("Product ID: ")
    new_product['name'] = input("Product Name: ")
    new_product['price'] = float(input("Product Price: "))
    new_product['stock'] = int(input("Product Stock: "))
    inventory.append(new_product)
    with open('inventory.json', 'w') as file:
        json.dump(inventory, file, indent=4)
    print("Product added successfully!")

def update_stock():
    with open('inventory.json', 'r') as file:
        inventory = json.load(file)
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    for product in inventory:
        if product['id'] == product_id:
            print()
            print("Product Found:")
            print(f'Name: {product['name']}')
            print(f'Current Stock: {product['stock']}')
            print()
            new_stock = int(input("New Stock Quantity: "))
            product['stock'] = new_stock
            with open('inventory.json', 'w') as file:
                json.dump(inventory, file, indent=4)
            print("Stock updated successfully!")
            return
    print("Product not found.")

def search_product():
    with open('inventory.json', 'r') as file:
        inventory = json.load(file)
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    for product in inventory:
        if product['id'] == product_id:
            print()
            print("Product Found:")
            print("----------------")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")   
            print(f"Price: {product['price']}")
            print(f"Stock: {product['stock']}")
            print("----------------")
            return
    print("Product not found.")

def save_inventory():
    with open('inventory.json', 'r') as file:
        inventory = json.load(file)
    with open('inventory.json', 'w') as file:
        json.dump(inventory, file, indent=4)
    print("Inventory saved successfully!")

def menu():
    while True:
        print("\n----------MENU----------")
        print("1. Display All Products")
        print("2. Add New Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("-------------------------")
        choice = input("Enter option: ")

        if choice == '1':
            display_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            update_stock()
        elif choice == '4':
            search_product()
        elif choice == '5':
            save_inventory()
        elif choice == '6':
            print("Saving inventory before exit...")
            save_inventory()
            print("Inventory saved successfully.")
            print()
            print("Thank you for using the Inventory Management System.")
            print("Program Terminated.")
            break


initialise()