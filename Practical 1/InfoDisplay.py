name = input("Enter name: ")
admin = input("Enter admin number: ")
age = int(input("Enter age: "))
gender = input("Enter gender (Male / Female): ")
weight = int(input("Enter weight (kg): "))
height = int(input("Enter height (m): "))
print(f"Hello! {name}\nYour admin no is {admin} and age is {age}\nYour gender is {gender} and bmi is {weight/height**2}")
