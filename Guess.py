#import statements
import random

answer=random.randint(1,100)
numGuesses=0
guess=0
while guess != answer:
    numGuesses+=1
    try:
        guess=int(input("Please input your guess (1-100):"))
    except ValueError:
        print("Invalid input. You must input a number between 1 and 100")
        continue
    if guess < 1 or guess > 100:
        print("Invalid input. You must input a number between 1 and 100")
    elif guess > answer:
        print("Incorrect. Answer is lower!")
    elif guess < answer:
        print("Incorrect. Answer is higher!")
    else:
        print("You got it!")
        print(f"Number of guess taken: {numGuesses}")
