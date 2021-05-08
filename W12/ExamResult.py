def ExamResult():  #  Question 4
    student_results = {
        'Jane': [75, 80, 85],
        'John': [60, 68, 74],
        "Jerome": [81, 63, 77],
        'Jason': [55, 76, 67],
        "Jessica": [62, 45, 68],
        "Joanne": [52, 47, 51]
    }

    try:
        student = input('Enter student name: ').strip().capitalize()
        print(f"Results of {student}\n==========================")
        for x, y in list(zip(range(3), ['English', 'Math', 'Science'])):
            print(f"Results for {y} = {student_results[student][x]}")
    except KeyError:
        print("Student does not exist!")
    for name, avg_score in student_results.items():
        print(f"Average marks of {name} = {sum(avg_score)/3}")
    m, c = [], []
    for index in range(3):
        for lists in student_results.values():
            m.append(lists[index])
        c.append(sum(m)); m.clear()
    for results, subject in list(zip(c, ['English', 'Math', 'Science'])):
        print(f"Average results for {subject} = {results}")
    return ""

print(ExamResult())