def currencyConversion():
    conversion_choice = input("What currency would you like to convert from SGD (USD, JPY, EUR): ").upper().strip() 
    try:
        money_plate = float(input("How much money do you want to convert: "))
    except ValueError:
        return f"{money_plate} is not a number!"
    if conversion_choice == "USD":
        return money_plate * 0.75
    if conversion_choice == "JPY":
      return money_plate * 82.09
    if conversion_choice == "EUR":
      return money_plate * 0.62 
    else:
        return "There is no such currency :("
print(currencyConversion())