#create variable 'inventory' and set it to 0
inventory = 0
failed_entries = 0
deliveries_done = 0

''' function handles prompt, input validation,
 and returns a valid int or 'quit' signal'''
def get_valid_input():
    global failed_entries
    while True:
        _input = input("Enter a stock quantity for a delivery or 'quit' to exit: ")
        if _input.isdigit():
            return int(_input)
        elif _input.lower() == 'quit':
            return 'quit'
        else:
            print("ERROR: Invalid input. Please enter a valid stock quantity for a delivery or 'quit' to exit.")
            failed_entries += 1
        
''' function calculates the new total and returns it'''
def process_delivery(current_total, new_value):
    return current_total + new_value

''' function takes a delivery amount and returns 10%'''
def calculate_tax(amount):
    return amount * 0.1

''' function generates and prints report of total units processed and failed attempts'''
def generate_report(total_units, failed_attempts):
    print(f"Total units processed: {total_units}")
    print(f"Failed attempts: {failed_attempts}")


while True:
    _input = get_valid_input()

    if _input == 'quit':
        generate_report(inventory, failed_entries)
        break   

    #Updates inventory by adding the new delivery amount
    inventory = process_delivery(inventory, _input)
    
    tax = calculate_tax(_input)
    deliveries_done += 1


