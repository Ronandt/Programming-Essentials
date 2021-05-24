try:
    distance = int(input("Enter distance in km:"))
    if distance > 200:
        print("It exceeds 200km!")
    elif 0 <= distance <= 200:
        minute = (distance / 70) * 60
        hour = minute // 60
        minute -= hour * 60
        print(f"Time travel is {int(hour)} hour and {int(minute)} minute")
    else:
        print("Negative numbers are not allowed! This is not displacemeent")
except ValueError:
    print("This is not a distance!")

    