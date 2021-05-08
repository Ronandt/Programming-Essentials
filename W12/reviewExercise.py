tracker = []


def review_exercise():  #  Question 2
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

print(review_exercise())