prev_price = 2000 * 0.4
buy_comm = (prev_price) * 0.03
curr_stock = float(input("Enter current price for ABC Bank Corporation (S$): "))  
total_comm = buy_comm + (2000 * curr_stock * 0.02)
print("You paid total commission of (S$): " + str(total_comm))
gains_loss = (curr_stock * 2000) - prev_price - total_comm
if gains_loss >= 0:
    print("You have made a profit of (S$): " + str(gains_loss))
else:
    print("You have made a loss of (S$): " + str(gains_loss))

