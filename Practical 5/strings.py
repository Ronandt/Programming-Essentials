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

def wheel_of_fortune():
    sentence = "wheel of fortune"
    cache = [x if x == " " else '-' for x in sentence]
    while "-" in cache:
        letter = input("Give me a letter: ")
        hidden_sentence = []
        for char in sentence:
            if char != letter and char != " ":
                hidden_sentence.append("-")
            elif char == " ":
                hidden_sentence.append(" ")
            else:
                hidden_sentence.append(char)
        for index in range(len(sentence)):
            if hidden_sentence[index] != "-" and cache[index] == "-":
                cache[index] = hidden_sentence[index]
            else:
                pass
        print("Guess the phrase: " + "".join(cache))
    return "Yeah, You got it right!"


print(wheel_of_fortune())