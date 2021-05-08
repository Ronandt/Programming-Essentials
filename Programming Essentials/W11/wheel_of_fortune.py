def wheel_of_fortune():  # idk I gave up Im sorry
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
