import json
import inventory_class
import product_class

# search for file named 'inventory.txt'; if none is found, create it.
def load_inventory():
    try:
        with open('inventory.txt', 'r') as file:    # try to open the file in read mode
            print("Current Orders:")
            print()
            print(file.read())
            print()
    except FileNotFoundError:                       # expect a failure if the file is not found
        with open('inventory.txt', 'w') as file:    # creates the file in write mode
            pass
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
                          
    return 


def startup():
    print("---------------")
    print("Welcome to Inventory Management System")
    print("---------------")
    load_inventory()
    
    

def quit():
    print("---------------")
    print("Exiting Inventory Management System\nGoodbye!")
    print("---------------")

def main_menu():

    return