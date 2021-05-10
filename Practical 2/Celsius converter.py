x = 0.0
while 1:  # A way to verify whether it is a whole number or not 
    try:
        x = float(input("What degree (celcius) do you want to convert to Fahrenheit (Press a letter to quit the program): "))
    except ValueError:
        break
    print(x * (9/5) + 32)  #  Formula for converting celcius to Fahrenheit
print("Goodbye!")





    

    
