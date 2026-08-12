#import things
#make max and min number as well as operators and total problem
#make a def to generate problem
#define wrong
#and tell to start the game
#use start time time.time()
import random
import time
operators = ["+","-","*"]
max_num = 12
min_num = 3
total_prob = 10

def generate_question():
    left = random.randint(min_num,max_num)
    right = random.randint(min_num,max_num)
    oper = random.choice(operators)

    expr = str(left) + " " + oper + " " + str(right)
    answer = eval(expr)
    return expr,answer

wrong = 0 
input("Press enter to start: ")
print("---------------------")

start_time = time.time()

for i in range(total_prob):
    expr, answer = generate_question()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")
