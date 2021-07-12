x = 0.0
while 1:  # Placeholder to keep looping
    try:
        x = float(input(
            "What degree (celcius) do you want to convert to Fahrenheit (Press a letter to quit the program): "))
        print(x * (9/5) + 32)  # Formula for converting celcius to Fahrenheit
    except ValueError:
        break
print("Goodbye!")
