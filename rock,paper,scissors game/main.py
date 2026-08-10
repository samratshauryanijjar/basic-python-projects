#rock paper secessor game
import random
user_wins = 0
computer_wins =0
operations = ['rock','paper','scissors']

while True:
    user_input = input(" Type rock/paper/scissors or q to exit").lower()
    if user_input == "q":
        break
    if user_input not in operations:
        continue

    random_num = random.randint(0,2)
    #roc: 0 paper:1 scissors:2
    computer_pick = operations[random_num]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print('you won')
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("you won")
        user_wins += 1

    else:
        user_input == "scissors" and computer_pick == "paper"
        print("you lost")
        computer_wins += 1


print("you won", user_wins, "times")

print("good bye")


