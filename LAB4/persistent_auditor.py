


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

def make_new_entry():
    
    with open('inventory.txt', 'r') as file:                    #open the file in read mode
        last_order_number = file.read().splitlines()[-1][:4]    #read file, split into lines, get the first 4 char
        if not last_order_number.isdigit():                     #if it's not a digit, means first entry.
            new_order_number = 1001                             #start with 1001 for first entry
        else:
            new_order_number = int(last_order_number) + 1       #new order number is +1 from last
    new_entry = [new_order_number]                              #new list with order number
    new_entry.append(input("Enter Product Name: "))             #ask, and add to end of list
    new_entry.append(input("Enter Quantity: "))                 #ask, and add to end of list
    return new_entry

def save_inventory(new_entry):
    with open('inventory.txt', 'a') as file:                    #open file in append mode
        file.write(f"\n{new_entry}")                            #write new entry
    return 

    
load_inventory()
new_entry = make_new_entry()
new_entry_str = f"{new_entry[0]}, {new_entry[1]}, {new_entry[2]}"
save_inventory(new_entry_str)

print()
print("New Order Added:")
print(new_entry_str)
print()
print("Order successfully saved to inventory.txt")

