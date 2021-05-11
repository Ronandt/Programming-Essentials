import random
def rock_paper_scissors(best_of):
    cpu_score = 0
    user_score = 0
    winner = [["rock", "scissors"], ["paper", "rock"], ["scissors", "paper"]]
    while cpu_score != best_of or user_score != best_of:
        rps_user = input("Please input what you want (rock, paper, scissors): ").lower().strip()
        random_index = random.randint(0, 2) # Random integer from 0 to 2 for random index choice
        rps_list = ["rock", "paper", "scissors"][random_index]
        if rps_list == rps_user:
            print("Tie")
        elif [rps_list, rps_user] in winner:
            print("Computer wins this round!")
            cpu_score += 1
        else:
            print("User wins this round!")
            user_score += 1
        if cpu_score == best_of:
            return "CPU won"
        elif user_score == best_of:
            return "User won"
best = int(input("What format do you want to play with (Best of 3 or 5): "))
while 1:
    try:
        if best % 2 != 0:
            rock_paper_scissors(best) # I know the requirements are strictly 3 and 5 but why not odd?
            break
        print("Input again!")
    except ValueError:
        print("Try again! 3 or 5")
