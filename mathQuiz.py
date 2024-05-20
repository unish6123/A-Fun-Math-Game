import random
import time
OPERATORS = ["+", "-", "/", "*"]
totalQuestion = 10
score = 0


count = 0 
def generate_problem():
    expr = str(random.randint(3, 12)) + " " + random.choice(OPERATORS) + " " + str(random.randint(3, 12))
    answer = eval(expr)
    return expr, answer

input("Press any keys to start!!!")
start = time.time()

while count < totalQuestion:
        count += 1
        
        question, answer = generate_problem()
        guess = input(f'Problem {" "} {count } { " "} : {question} {" "} = {" "}')
        if guess == str(answer):
            score += 10
end = time.time()
print("----------------------------------Game End---------------------------------------------")
print("-------------------------------------------------------------------------------------")
print("-------------------------------------Scores---------------------------------")
print(f" You Scored {score} {' '} in {round((end - start ), 2)} {' '} seconds.")
            


