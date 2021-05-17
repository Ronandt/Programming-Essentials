def ticketPrice(age):  # Check for the price of the tickets
    if age < 16:
        ticket_price = 7.5
    elif 16 <= age < 65:
        ticket_price = 10
    elif age >= 65:
        ticket_price = 5.5
    return "You have to pay $%.2f for the ticket" % (ticket_price)


try:  # Check for the correct value first before executing the function
    day = int(input("Enter day of the week (1-7): "))
    age_check = int(input("Enter age: "))
    if 4 < age_check <= 130 and day in range(1,6):
        print(ticketPrice(age_check))
    elif 4 < age_check <= 130 and day in [6, 7]:
        print("You have to pay $10.00 for the ticket")
    else:
        print("Please enter a proper age and/or day!")
except ValueError:
    print("Please input an integer!")
except:
    print("Oops something unexpected happened...")
