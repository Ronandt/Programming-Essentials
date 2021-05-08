tracker = [] #  Global variable that is not affected by the whole function so that if a user wants to restart using recursion, the list wil not change


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
                qn_no += 1 # Increment qn_no when it's accepted
                student_ans[qn_no] = student_input.upper().strip() #  Upper and strip to prevent an inconsistent value which would lead to a KeyError
            else:
                print("Enter a letter from A-D!")
        except ValueError:
            print("Key in again!")
    for x in range(1, 11): #  Make the range start at 1 as if you let range start at 0 (default) there will be a KeyError (0 is not a key)
        if student_ans[x] == teacher_answers[x]:  #  Check if the student ans matches the teacher through looping an index
            correct_answers += 1  # Tells the correct and incorrect answers
        else:
            incorrect_answers += 1
    tracker.append(correct_answers)
    while 1:  #  Loop through until a user gets a correct input
        query = input("Do you want to try again: ").lower().strip()
        if query == 'yes':
            review_exercise()  #  Restarting the whole function again so that the user can attempt it 
            break
        elif query == 'no':
            print(max(tracker))  #  If user says no, it finds the max number of the scores 
            break
        else:
            print("I am not sure what you want. Please input again!")

print(review_exercise())