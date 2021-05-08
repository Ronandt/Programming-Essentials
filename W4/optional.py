while 1:
    try:
        yearly_salary = float(input("What is your yearly gross salary: "))  
        monthly_salary = yearly_salary / 12
        print(monthly_salary - monthly_salary * 0.2 - 1500)
        break
    except ValueError:
        print("Please enter a number!")
        continue
    