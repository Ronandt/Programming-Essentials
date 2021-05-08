def EnglishMark():  # Question 3
    studentMarkList = {"Jane": 75,
                       "John": 60,
                       "Jerome": 81}
    try:
        return f"Results for English: {studentMarkList[input('Enter student name: ').capitalize().strip()]}"
    except KeyError:
        return "Invalid input!"
        
print(EnglishMark())