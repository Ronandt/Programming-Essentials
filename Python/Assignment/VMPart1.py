import sys
inventory = {'IM': {'description': 'Iced Milo', 'price': 1.5, 'quantity': 30},
             'IC': {'description': 'Iced Coffee', 'price': 1.5, 'quantity': 40},
             'CC': {'description': 'Coca Cola', 'price': 1.3, 'quantity': 50},
             'HM': {'description': 'Hot Milo', 'price': 1.2, 'quantity': 20},
             'HC': {'description': 'Hot Coffee', 'price': 1.2, 'quantity': 0},
             '1P': {'description': '100 Plus', 'price': 1.1, 'quantity': 50}}
vendor = input("Are you a vendor (Y/N)? ").upper().strip()
if vendor not in ["Y", "N"]:
    print("Please input correctly!")
    sys.exit()
print("Welcome to ABC Vending Machine.\nSelect from following choices to continue: ")
def add_drink_type(drink_id, description, price, quantity):
    inventory[drink_id] = {'description': description, 'price': price, 'quantity': quantity}
    print(inventory)

def replenish_drink(drink_id, quantity):
    

menu, record, paid = {
    "IM": 1.5,
    "HM": 1.2,
    "IC": 1.5,
    "HC": 1.2,
    "1P": 1.1,
    "CC": 1.3
}, [], [0]
if vendor == "N":
    print("IM. Iced Milo (S$1.5)\nHM. Hot Milo (S$1.2)\nIC. Iced Coffee (S$1.5)\nHC. Hot Coffee (S$1.2)\n1P. 100 Plus (S$1.1)\nCC. Coca Cola (S$1.3)\n0. Exit / Payment")
    number = 0
    while 1:
        try:
            choice = input("Enter choice: ").upper().strip()
            if choice == "0": break
            check = menu[choice]
            number = int(input("No. of drinks selected = "))
            record.append(check * number)
        except KeyError:
            print("Invalid option")
        except ValueError:
            print("Please input the proper number of drinks!")
    print("Please pay: $%.2f" % sum(record)), print("Indicate your payment:")
    cancel = "N"
    while cancel == "N":
        money_sequence = 20
        for x in range(3):
            money_sequence //= 2
            while 1:
                try:
                    paid.append(int(input(f"Enter no. of ${money_sequence} notes: ")) * money_sequence)
                    break
                except ValueError:
                    print("Please input the proper number of notes!")
            if sum(paid) >= sum(record):
                print("Please collect your change: $%.2f" % (sum(paid) - sum(record)))
                print("Drinks paid. Thank you.")
                sys.exit()
        if sum(paid) - sum(record) < 0:
            print("Not enough to pay for the drinks\nTake back your cash!")
            while 1:
                cancel = input("Do you want to cancel the purchase? Y/N: ").upper().strip()
                if cancel == "Y":
                    print("Purchase is cancelled. Thank you.")
                    sys.exit()
                elif cancel not in ["Y", "N"]:
                    print("Not a proper confirmation!")
                    continue
                paid.clear()
                break
elif vendor == "Y":
    print("1. Add Drink Type\n2. Replenish Drink\n0. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        while 1:
            drinkid = input("Enter drink id: ").upper().strip()
            if drinkid in inventory:
                print("Drink id exists!")
                continue
            break
        add_drink_type(drinkid, input("Enter description of drink: ").strip(), float(input("Enter price: $")), int(input("Enter quantity: ")))
    elif choice == 2:
        for x in inventory:
            print(f"{x}. {inventory[x]['description']} (${inventory[x]['price']}) " + "\t" + f"Qty: {str(inventory[x]['quantity']) * (inventory[x]['quantity'] >= 1)}" + "***out of stock***" * (inventory[x]['quantity'] <= 0))