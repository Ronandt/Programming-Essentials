
x = int(input(  # This is to let the user choose the mode
        "Do you want to find your BMI (1) or find your ideal BMI given your height(2) 1/2: "))
if x not in [1, 2]:
        print("Please enter a number 1 or 2!")
if x == 1:
    def bmi(weight, height):  # Mode 1: finding your own BMI
        BMI = weight/height**2  # BMI Formula
        if BMI >= 27.5:
            classification = "Obese"
        elif 23 <= BMI < 27.5:
            classification = "Overweight"
        elif 18.5 <= BMI < 23:
            classification = "Normal"
        elif 0 < BMI < 18.5:
            classification = "Underweight"
        return f"Your BMI is {BMI} and you are {classification.lower()}"
    try:  # Check whether the input is valid
        weight = float(input("Enter your weight: "))
        height = float(input("Enter your height: "))
        print(bmi(weight, height))
        if weight < 0 or height < 0:
            print("Something must be wrong with your body!")
    except ValueError:
            print("Please enter an Integer/Float!")
elif x == 2:  # Mode 2: finding your ideal BMI given height
    def ideal_bmi(height):
        return f"{18.5 * height ** 2} - {22.99 * height ** 2}"
    try:  # Check whether the input is valid
        height_input = float(input("Enter your height: "))
        print(ideal_bmi(height_input))
        if height_input < 0:
            print("Something must be wrong with your body!")
    except ValueError:
         print("Invalid Input! Please try again.")
    except:
        print("Oops something unexpected happened")