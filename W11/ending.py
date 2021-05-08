def ending():  
    string = input("Enter a string: ")
    if len(string) >= 5:
        return string + "ly" if string[-1: -3] == "ing" else string + "ing"
    else:
        return string


print(ending())
