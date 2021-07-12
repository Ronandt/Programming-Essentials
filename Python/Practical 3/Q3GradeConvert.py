def convertGrade(score):
    dict_gpa = {"A": 4.0,
                "B": 3.0,
                "C": 2.0,
                "D": 1.0}  # Dictionary for faster times [O(1) time], instead of control flow
    return dict_gpa[score]


try:  # Check whether the input is valid
    score_input = input("What is your grade:")
    print(convertGrade(score_input)) 
except ValueError:
    print("Please enter a grade - A, B, C or D!")
except KeyError:
    print("Grade is Invalid! Enter a grade - A, B, C or D!")
    
