def uppercase():
    string = input("Enter a string: ")
    return string.upper() if len([letter for letter in string if letter.isupper()]) >= 2 else "The string contains less than 2 uppercase characters"


print(uppercase())
