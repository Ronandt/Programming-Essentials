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
                cache[index] = cache[index]
        print("Guess the phrase: " + "".join(cache))
    return "Yeah, You got it right!"


print(wheel_of_fortune())
