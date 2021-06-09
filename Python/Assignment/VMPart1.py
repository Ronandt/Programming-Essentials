import sys
vendor = input("Are you a vendor (Y/N)? ").upper().strip()
if vendor not in ["Y", "N"]:
    print("Please input correctly!")
    sys.exit()
print("Welcome to ABC Vending Machine.\nSelect from following choices to continue: ")
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
            if choice == "0":
                break
            check = menu[choice]
            number = int(input("No. of drinks selected = "))
            record.append(check * number)
        except KeyError:
            print("Invalid option")
        except ValueError:
            print("Please input the proper number of drinks!")
    print("Please pay: $%.2f" % sum(record)), print("Indicate your payment:")
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
            print(min(1, sum(paid) - sum(record)) * "Please collect your change: $%.2f" % (sum(paid) - sum(record)))
            print("Drinks paid. Thank you.")
            break
    if sum(paid) - sum(record) < 0:
        print("Not enough to pay for the drinks\nTake back your cash!")
        if input("Do you want to cancel the purchase? Y/N: ").upper().strip() == "Y":
            print("Purchase is cancelled. Thank you.")



elif vendor == "Y":
    print("1. Add Drink Type\n2. Replenish Drink\n0. Exit\nEnter choice: ") #enter choice input?