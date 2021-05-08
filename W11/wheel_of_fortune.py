def wheel_of_fortune():  # idk I gave up Im sorry
   sentence = "wheel of fortune"
   hidden_sentence = [x if x == " " else '-' for x in sentence]
   while "-" in hidden_sentence:
        letter = input("Give me a letter: ")
        hidden_sentence = "".join(["-" if char != letter else char for char in sentence])
        #maybe try and replace with index



            

        print("Guess the phrase: " + "".join(hidden_sentence))


print(wheel_of_fortune())
