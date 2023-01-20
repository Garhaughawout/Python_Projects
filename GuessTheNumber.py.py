import random
number = random.choice(range(1,101))
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
print("Welcome to the number Guessing Game!\nI'm thinking of a number between 1 and 100. ")
difficulty = input("Type 'easy' or 'hard':")
guess = 0
got_number = False
more_attempts = False


  
if difficulty == "easy":
    attempts = 10
    
else:
    attempts = 5

while got_number == False:
    got_number = False
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if attempts == 1:
        got_number = True
        print("You've run out of guesses, you lose.")
    elif guess > number:
        print("Too High. \nGuess again.")
        attempts = attempts - 1
    elif guess < number:
        print("Too Low. \nGuess again.")
        attempts = attempts - 1
    else: 
        got_number = True
        print(f"You got it! The answer was {number}.")

    
    
    
    




