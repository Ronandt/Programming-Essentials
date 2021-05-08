#My Way

total_score,percentage_total = 0, 0
for x in range(1, 4):
    percentage = int(input(f"What is your percentage for Test {x}: "))/100
    total_score += int(input(f"What is your score for Test {x}: ")) * percentage
    percentage_total += percentage
if total_score > 50 or total_score < 0 or percentage_total != 50:
    print("Invalid Score! Please do not set your score above 100 or have your total percentage above or less than 100!")
else:
    total_score += int(input("What is your score for Exam: ")) * 0.5
    print("Your final mark is %6.1f" % (total_score))








