#create variable 'inventory' and set it to 0
inventory = 0
failed_entries = 0

#continuous loop asking user to enter a stock quantity, until the user types quit
while True:
    #promtps user for input
    inv_input = input("Enter a stock quantity or 'quit' to exit: ")
    #checks if input is a digit, rejects negative and non numbers
    if inv_input.isdigit():
        inventory += int(inv_input)
        if inventory > 500:
            print("Inventory limit exceeded. Cannot add more stock.")
            print("Total units processed:", inventory)
            print ("Total Failed/Rejected Entries:", failed_entries)
            break
    elif inv_input.lower() == 'quit':
        print("Total units processed:", inventory)
        print ("Total Failed/Rejected Entries:", failed_entries)
        break
    else:
        failed_entries += 1
        print("ERROR:Invalid input.")
        