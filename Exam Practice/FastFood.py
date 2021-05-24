try:
    day = int(input("Enter day: "))
    normal = int(input("No. of normal set meal: "))
    kids = int(input("No. of kids set meal: "))
    discount = ""
    if day in [2,3]:
        total = (normal * 15 + kids * 8) * 0.9
        discount += "Discount: 10% on Tue & Wed\n"
    elif day in [6,7]:
        total = normal * 15 + (kids * 8) * 0.5
        discount += "Discount: 50% for kids set meal\n"
    elif day in [1,4,5]:
        total = normal * 15 + kids * 8
    if total > 100:
        total -= 20
        discount += "Discount: $20 for spending over $100\n"
    print(f"{discount}Please pay $ {total}")
except NameError:
    print("Invalid day!")
except ValueError:
    print("Please input integers only!")







