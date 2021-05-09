def indexString():
    for letter, index in enumerate(input("Enter a string:")):
        print(f"Character {letter} at position {index}")

def replaceSpace():
    return input("Enter a string: ").replace(" ", "")

def uppercase():
    string = input("Enter a string: ")
    return string.upper() if len([letter for letter in string if letter.isupper()]) >= 2 else "The string contains less than 2 uppercase characters"

def ending():
    string = input("Enter a string: ")
    if len(string) >= 5:
        return string + "ly" if string[-1: -3] == "ing" else string + "ing"
    else:
        return string

def wheel_of_fortune(): #idk I gave up Im sorry
    import re
    sentence = "wheel of fortune"
    p = re.compile('\w')
    hidden_sentence = p.sub('-', sentence)
    print("Guess the prhase: " + hidden_sentence)
    while "-" in hidden_sentence:
        letter = input("Give me a letter: ")
        "".join([letter if letter == sentence or letter if letter == " " else '-' for letter in sentence]
        print("Guess the phrase: " + ))
print(wheel_of_fortune())