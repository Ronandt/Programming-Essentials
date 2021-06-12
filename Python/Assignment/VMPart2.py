# Author Declan Isaac Kuok
# Admin Number: 212803T
inventory = {'IM': {'description': 'Iced Milo', 'price': 1.5, 'quantity': 30},
             'HM': {'description': 'Hot Milo', 'price': 1.2, 'quantity': 20},
             'IC': {'description': 'Iced Coffee', 'price': 1.5, 'quantity': 40},
             'HC': {'description': 'Hot Coffee', 'price': 1.2, 'quantity': 0},
             '1P': {'description': '100 Plus', 'price': 1.1, 'quantity': 50},
             'CC': {'description': 'Coca Cola', 'price': 1.3, 'quantity': 50}}
while 1:
    while 1:
        vendor = input("Are you a vendor (Y/N)? ").upper().strip()
        if vendor in ["Y", "N"]:
            break
        print("Please input correctly!")
    print("Welcome to ABC Vending Machine.\nSelect from following choices to continue: ")
    def add_drink_type(drink_id, description, price, quantity):
        inventory[drink_id] = {'description': description, 'price': price, 'quantity': quantity}
        print("New drink added!")
    def replenish_drink(drink_id, quantity):
        drink_id['quantity'] = drink_id['quantity'] + quantity
        print("Iced Milo has been top up!")
    record, paid = [], [0]
    if vendor == "N":
        for x in inventory:
            print(f"{x}. {inventory[x]['description']} (${inventory[x]['price']}) " + "\t" + f"Qty: {str(inventory[x]['quantity']) * (inventory[x]['quantity'] >= 1)}" + "***out of stock***" * (inventory[x]['quantity'] <= 0))
        print("0. Exit / Payment")
        number = 0
        while 1:
            try:
                choice = input("Enter choice: ").upper().strip()
                if choice == "0":
                    break
                elif inventory[choice]['quantity'] == 0:
                    print(f"{inventory[choice]['description']} is out of stock")
                    continue
                number = int(input("No. of drinks selected = "))
                if inventory[choice]['quantity'] - number >= 0:
                    record.append(inventory[choice]['price'] * number)
                    inventory[choice]['quantity'] = inventory[choice]['quantity'] - number
                else:
                    print(f"{inventory[choice]['description']} does not have enough stock for your needs!")
            except KeyError:
                print("Invalid option")
            except ValueError:
                print("Please input the proper number of drinks!")
        print("Please pay: $%.2f" % sum(record)), print("Indicate your payment:")
        while 1:
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
                    break
            if sum(paid) - sum(record) < 0:
                print("Not enough to pay for the drinks\nTake back your cash!")
                cancel = ""
                while cancel not in ["N", "Y"]:
                    cancel = input("Do you want to cancel the purchase? Y/N: ").upper().strip()
                paid.clear()
                if cancel == "N":
                    continue
                elif cancel == "Y":
                    print("Purchase is cancelled. Thank you.")
                    break
                break
    elif vendor == "Y":
        print("1. Add Drink Type\n2. Replenish Drink\n0. Exit")
        while 1:
            choice = input("Enter choice: ").strip()
            if choice == '1':
                while 1:
                    drinkid = input("Enter drink id: ").upper().strip()
                    if drinkid not in inventory:
                        break
                    print("Drink id exists!")
                while 1:
                    try:
                        add_drink_type(drinkid, input("Enter description of drink: ").strip(), float(input("Enter price: $")), int(input("Enter quantity: ")))
                        break
                    except ValueError:
                        print("Improper pricing or quantity!")
            elif choice == '2':
                for x in inventory:
                    print(f"{x}. {inventory[x]['description']} (${inventory[x]['price']}) " + "\t" + f"Qty: {str(inventory[x]['quantity']) * (inventory[x]['quantity'] >= 1)}" + "***out of stock***" * (inventory[x]['quantity'] <= 0))
                while 1:
                    try:
                        drinkid = inventory[input("Enter drink id: ").upper().strip()]
                        if drinkid['quantity'] < 5:
                            replenish_drink(drinkid, int(input("Enter quantity: ")))
                            break
                        print("No need to replenish. Quantity is greater than 5")
                        break
                    except KeyError:
                        print("No drink with this drink id. Try again.")
                    except ValueError:
                        print("No such quantity!")
            elif choice == '0':
                break
            else:
                print("Not a valid choice!")