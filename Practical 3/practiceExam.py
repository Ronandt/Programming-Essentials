
try:
    time = int(input("Enter time of the day: "))
    if time < 8:
        print("Prepare breakfast")
    elif 8 <= time <= 12:
        print("Prepare lunch")
    else:
        print("Prepare dinner/supper")
except ValueError:
    print("That is not a time of the day!")

k = ""
spent = float(input("Amount spent: "))
if spent >= 50:
    umb = spent//50
    print("Congratuation!")
    k = f"Your free gift(s) is/are {int(umb)} umbrella(s) "
if spent > 200:
    k += "and a cooking pot"
else:
    k = "Sorry! No free gift"
print(k)

time = int(input("Enter number of working hours: "))
total = 0
if 0 < time <= 5:
    total += 5*time
elif 10 >= time > 5:
    total += 5 * 5
    total += (time - 5) * 6
else:
    total += 5 * 5
    total += 5 * 6
    total += (time-10) * 8
print("Salary for today is $%.2f" % (total))


try:
    age = int(input("Enter age: "))
    days = input(
        "Enter weekdays, weekends or public holidays (WD/WE/PH): ").strip().upper()
    if days == "WD":
        if age >= 60:
            money = 14
        elif 12 >= age >= 3:
            money = 17
        elif age > 12:
            money = 25.5
    elif days == "WE":
        if age >= 60:
            money = 14
        elif 12 >= age >= 3:
            money = 18
        elif age > 12:
            money = 25.5
    elif days == "PH":
        if age >= 60:
            money = 14
        elif 12 >= age >= 3:
            money = 19
        elif age > 12:
            money = 28.5
    print("Ticket price is $%.2f" % (money))
except NameError:
    print("INVALID DAY!")
except ValueError:
    print("That is not an age!")


member = input("Are you a member? (Y/N) ").strip()
credit = input("Are you using a credit card (Y/N) ").strip()
if member == 'Y' and credit == 'N':
    i = "$5 voucher"
elif member == 'Y' and credit == 'Y':
    i = "$3 voucher and a free gift"
elif member == "N" and credit == "N":
    i = "Nothing"
else:
    print('INVALID')
print(f"You will be getting:\n{i}")
