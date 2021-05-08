def EnglishMark():  # Question 3
    studentMarkList = {"Jane": 75,
                       "John": 60,
                       "Jerome": 81}  # Dictionary to store the students and marks
    try:
        return f"Results for English: {studentMarkList[input('Enter student name: ').capitalize().strip()]}"
        ''' Asks the user to input the student name (key) to call the value. 
        .captialize() means that it capitalizes the name just incase the user 
        does not put capitals on the front and strip() is to clear extra spaces that the user inputs'''
    except KeyError:  # Returns an invalid input if the student name is not in the dictionary
        return "Invalid input!"


print(EnglishMark())
