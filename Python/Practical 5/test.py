def test():
    money = int(input("how much do you want to deposit:"))
    k = ""
    if money % 10 != 0:
         return "Please withdraw in multiples of 10"
    if money >= 50:
        fifty = money // 50
        money -= fifty * 50
        k += f"You have deposited {fifty} 50 bucks. "
    if money >= 10:
        ten = money // 10
        money -= ten * 10
        k += f"You have deposited {ten} 10 bucks"   
    return k
print(test())

