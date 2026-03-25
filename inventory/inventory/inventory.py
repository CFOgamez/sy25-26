#Carters personal inventory manager with dictionaries
inventory = {}

print("\nOptions: [1] Add, [2] Remove, [3] List, [4] Exit")
option = input("Choose an option (1-4): ")

while option != "4":
    if option == "1":
        item = input("Enter item name to add: ")
        quantity = int(input("Enter quantity: "))
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
        print(f"Added {quantity} of {item}.")
   
    if option == "2":
        item = input("Enter item name to remove: ")
        quantity = int(input("Enter quantity: "))
        if item in inventory and inventory[item] >= quantity:
            inventory[item] -= quantity
            print(f"Removed {quantity} of {item}.")
            if inventory[item] == 0:
                del inventory[item]
        else:
            print("Not enough items to remove or item does not exist.")
        
    if option == "3":
        print("Current Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")

    print("\nOptions: [1] Add, [2] Remove, [3] List, [4] Exit")
    option = input("Choose an option (1-4): ")
