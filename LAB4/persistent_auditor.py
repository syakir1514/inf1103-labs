


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

load_inventory()
