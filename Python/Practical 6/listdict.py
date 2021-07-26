def number():
    number_series = []
    while len(number_series) < 10:
        try:
            number_series.append(float(input("Enter a number: ")))
            print(
                f"Number of records to be stored in a list: {10 - len(number_series)}")
        except ValueError:
            print("Enter a number!")
    print(f"Lowest number: {min(number_series)} | Highest number: {max(number_series)} | Number of numbers: {len(number_series)} | Average of the numbers: {sum(number_series)/len(number_series)}")


tracker = []


def review_exercise():
    student_ans = {}
    teacher_answers = {1: 'C',
                       2: 'D',
                       3: 'B',
                       4: 'A',
                       5: 'B',
                       6: 'D',
                       7: 'A',
                       8: 'C',
                       9: 'D',
                       10: 'C'}   # Using a list and then running an index is fine. Using a dictionary for neatness
    qn_no = 0
    incorrect_answers, correct_answers = 0, 0
    while qn_no < 10:
        try:
            student_input = input("Enter your answer: ")
            if student_input.upper().strip() in ['A', 'B', 'C', 'D']:
                qn_no += 1
                student_ans[qn_no] = student_input.upper().strip()
            else:
                print("Enter a letter from A-D!")
        except ValueError:
            print("Key in again!")
    for x in range(1, 11):
        if student_ans[x] == teacher_answers[x]:
            correct_answers += 1
        else:
            incorrect_answers += 1
    tracker.append(correct_answers)
    while 1:
        query = input("Do you want to try again: ").lower().strip()
        if query == 'yes':
            review_exercise()
            break
        elif query == 'no':
            print(max(tracker))
            break
        else:
            print("I am not sure what you want. Please input again!")


def EnglishMark():
    studentMarkList = {"Jane": 75,
                       "John": 60,
                       "Jerome": 81}
    try:
        return f"Results for English: {studentMarkList[input('Enter student name: ').capitalize().strip()]}"
    except KeyError:
        return "Invalid input!"


def ExamResult():
    student_results = {
        'Jane': [75, 80, 85],
        'John': [60, 68, 74],
        "Jerome": [81, 63, 77],
        'Jason': [55, 76, 67],
        "Jessica": [62, 45, 68],
        "Joanne": [52, 47, 51]
    }

    try:
        student = input('Enter student name: ').strip().lower().capitalize()
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