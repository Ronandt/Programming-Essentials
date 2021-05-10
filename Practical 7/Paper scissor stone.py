import random
def rock_paper_scissors():
    while 1:
        try:
            best_of = int(input("What format do you want to play with (Best of 3 or 5): "))
            break
        except ValueError:
            print("Try again! 3 or 5")
    cpu_score = 0
    user_score = 0
    winner = [["rock", "scissors"], ["paper", "rock"], ["scissors", "paper"]]
    while cpu_score != best_of or user_score != best_of:
        rps_user = input("Please input what you want (rock, paper, scissors): ").lower().strip()
        random_index = random.randint(0, 2)
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


print(rock_paper_scissors())