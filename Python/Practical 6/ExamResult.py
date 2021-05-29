def ExamResult():  #  Question 4
    student_results = {
        'Jane': [75, 80, 85],
        'John': [60, 68, 74],
        "Jerome": [81, 63, 77],
        'Jason': [55, 76, 67],
        "Jessica": [62, 45, 68],
        "Joanne": [52, 47, 51]
    } #  Dictionary that stores the values

    try:
        student = input('Enter student name: ').strip().capitalize()
        print(f"Results of {student}\n==========================") 
        for x, y in list(zip(range(3), ['English', 'Math', 'Science'])):  #  zip is to combine the two values together and list is to change the zip from gibberish to a data type (otherwise there's an error)
            print(f"Results for {y} = {student_results[student][x]}")  #  Y loops through the list to represent English, Math, Science while X is to call the index value of the key (because key is list)
    except KeyError: 
        print("Student does not exist!")
    for name, avg_score in student_results.items(): # student_results.items() is to run through the key & value respectively with a for loop
        print(f"Average marks of {name} = {sum(avg_score)/3}") #  Find the average score
    one_subject, all_subjects = [], []
    for index in range(3):  # This is to loop through the zero index of all the lists in the value up to two (Remember range is exclusive at the last number)
        for lists in student_results.values():
            one_subject.append(lists[index])
        all_subjects.append(sum(one_subject)); one_subject.clear()  #  Append the sum of all scores per subject and adding it onto a list. Clear() is to remove the previous subjects scores
    for results, subject in list(zip(all_subjects, ['English', 'Math', 'Science'])):  #  Loop through subject and the list that contains the sum of all scores per subject
        print(f"Average results for {subject} = {results}")
    return "" #  Placeholder so the function does not return None

print(ExamResult())