
o = int(input("Enter number 1: "))
n = int(input("Enter number 2: "))
sum = o + n
print(f"The sum of {o} and {n} is {sum}")

if sum % 2 != 0:
    print("The sum is an odd number")
    if sum > 100:
        print("The sum is greater than 100")
else:
    pass


score = float(input("Enter score: "))
if 1 >= score >= 0.9:
    print("A")
elif 0.9 > score >= 0.8:
    print("B")
elif 0.8 > score >= 0.7:
    print("C")
elif 0.7 > score >= 0.6:
    print("D")
elif 0.6 > score >= 0.0:
    print("F")
else:
    print("Score is out of range")


books = max(0, int(input("How many books have you purchased: ")))

ref = {
    0: 0,
    1: 5,
    2: 15,
    3: 30,
}

if books >= 4:
    print(f"Points received: {60}")
else:
    print(f"Points received: {ref[0]}")


packages = int(input("Number of package purchased: "))
if packages <= 9:
    money = max(0, packages * 99)
elif 19 >= packages >= 10:
    money = (packages * 99) * 0.8
elif 49 >= packages >= 20:
    money = (packages * 99) * 0.7
elif 99 >= packages >= 50:
    money = (packages * 99) * 0.6
else:
    money = (packages * 99) * 0.5

print("Discount $%.2f" % (packages * 99 - money))
print("Purchase $%.2f" % (money))
