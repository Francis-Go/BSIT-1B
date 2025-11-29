import random

ready = input("Are you ready to play? (y/n) " ).lower()

random_easy = random.randint(1, 100)
random_medium = random.randint(1, 500)
random_hard = random.randint(1, 1000)

if (ready == 'y'):
    difficulty = input("Choose difficulty (easy/medium/hard) ").lower() 
else:
    print("okay")
    
if (difficulty == 'easy'):
    print("Guess the number 1-100")
    print("Start guessing now")
    #random_easy = random.randint(1, 100)
    user_guess = int(input())
    while user_guess != random_easy:
       if user_guess > random_easy:
           print("Lower")
       if user_guess < random_easy:
           print("Higher")
       if user_guess == random_easy:
          print("Winner")
       user_guess = int(input())
       user_guess = user_guess

if (difficulty == 'medium'):
    print("Guess the number 1-500")
    print("Start guessing now")
    #random_medium = random.randint(1, 500)
    user_guess = int(input())
    while user_guess != random_medium:
       if user_guess > random_medium:
           print("Lower")
       if user_guess < random_medium:
           print("Higher")
       if user_guess == random_medium:
           print("Winner")
       user_guess = int(input())
       user_guess = user_guess
    
if (difficulty == 'hard'):
    print("Guess the number 1-1000")
    print("Start guessing now")
    #random_hard = random.randint(1, 1000)
    user_guess = int(input())
    while user_guess != random_hard:
       if user_guess > random_hard:
           print("Lower")
       if user_guess < random_hard:
           print("Higher")
       if user_guess == random_hard:
           print("Winner")
       user_guess = int(input())
       user_guess = user_guess
