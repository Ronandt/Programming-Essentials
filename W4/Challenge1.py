def seconds_converter(seconds):  
    hour = seconds // 3600  #  Finding the number of hours
    minute = (seconds - (hour * 3600)) // 60  #  Minusing the total hours that has been calculated and dividing by 60 to find minute
    second = seconds - hour * 3600 - minute * 60 #  Minusing the total hours that has been calculated and minutes to find seconds
#  Program can be faster by not repeating subtractions of hours/minutes but lazy haha (One could minus the seconds variable every step to make it faster)

    return f"{seconds} seconds is {hour} hours, {minute} minutes and {second} seconds"
while 1:  #  While loop with no conditions
    try:
        print(seconds_converter(int(input("What is the amount of seconds you want to convert: "))))  #Asks the user to input an integer if the person types in a string or float
        break
    except ValueError:
        print("Please input an integer!")
        continue  #  loops back to ask the user to input again
    except:
        print("Oops something unexpected happened...")
