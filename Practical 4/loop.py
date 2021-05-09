def sumLoop():
    # a (technically a for loop)
    sum1 = print(sum(x for x in range(1, int(input("Enter Number: ")) + 1)))
    return sum1


def whileLoop():  # b
    i = int(input("Enter number: "))
    arr = [0]
    while i != 0 and i >= 1:  # Skips the loop when the user inputs 0 and prevents the addition of negative numbers
        arr.append(i)
        i -= 1
    # Sum method does adding of the whole list at once which is faster
    return sum(arr)


def sumLoopEven():
    i = int(input("Enter Number: "))
    # range() creates a list or a range of numbers. i + 1  as the last number is exclusive not inclusive
    return sum(range(1, i + 1, 2)) if i >= 2 else "Enter a value more than 2!"


def sumLoopCustom():  # It is possible with a for loop if there are numbers in an array that are already there
    sum_prompt = None  # Placeholder
    total = 0
    while sum_prompt != 0:
        sum_prompt = int(input("Enter number: "))
        total += sum_prompt
    return total


def retail():
    cost_price = int(input("What is the cost price: "))
    while cost_price > 0:  #  Ensure that the cost_price is a positive number
        cost_price = int(input("What is the cost price: "))
        print(f"Cost price is: {cost_price * 1/4}")
    return "" # Placeholder to ensure program does not return NoneType


def gpaLoop():
    all_pt, total_credits = [], []
    for x in range(1, 6): # Remember x + 1 as the last number of range is exclusive
        credits_curr = int(input(f"Enter the credit for Module {x}: "))
        GPA_curr = float(input(f"Enter your GPA for Module {x}: "))
        all_points.append(credits_curr * GPA_curr) # Append into a list and then sum all for clarity (and my preference); Using a variable to constantly add is possible as well
        total_credits.append(credits_curr)
    return f"Your cumulative GPA for 5 modules is {sum(all_points) / sum(total_credits)}" # GPA formula
