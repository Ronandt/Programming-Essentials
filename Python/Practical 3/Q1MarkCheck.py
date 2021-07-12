def markCheck(mark):  # Function to check the whether pass/fail
    if 100 >= mark >= 50:
        return "User passed"
    elif 0 <= mark < 50:
        return ""


while 1:  # While condition to repeat the input if it is invalid
    try:  # Check if the input is invalid
        mark_input = int(input("What is the users' mark: "))
        if mark_input > 100 or 0 > mark_input:
            print("Please input an integer from 0-100!")
        else:
            print(markCheck(mark_input))
            break
    except ValueError:
        print("Please input a number!")

