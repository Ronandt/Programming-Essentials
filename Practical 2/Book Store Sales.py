while 1:  # A while loop with no condition
    try:
        unit_price = float(input("What is the unit price of the book: "))   #Try Except to prevent ValueError from crashing the program
        break
    except ValueError:
        print("Please input a proper sales price!")
        continue
while 1:        #  A while loop with no condition
    try:
        copies = int(input("What is the number book copies: "))  
        subtotal = unit_price * copies
        GST = subtotal * 0.07
        print("Subtotal: $%.2f" % (subtotal))  # *For those who have not learnt f strings, they are very useful so please learn them (Without formatting though)
        print("GST: $%.2f" % (GST))   #  By using this method you could fit all datatypes into a string without much trouble
        print("Total amount: $%.2f" % (subtotal + GST))
        break
    except ValueError:
        print("Please input the proper amount of book copies!")
        continue
'''
Steps: 1. Find the unit price and copies. Then multiply unit price and copies to find the subtotal. 
          Find the GST from the subtotal (Remember: 7% is 0.07) and print the what the program wants
'''