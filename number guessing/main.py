#-------------Number Guessing -----
import random
top_range = input("Type a number between 0-100 to guess: ")
if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Enter a value bigger then 0 next time")
        quit()
else:
    print("Enter a number next time")
    quit()
random_num = random.randint(0, top_range)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_num:
        print("dam you got it! ")
        break
    elif user_guess > random_num:
        print("you were above the number")
    else:
        print("you were below the number")

print("you got it in", guess,"guesses")


