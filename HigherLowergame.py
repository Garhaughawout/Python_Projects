from art import logo,vs
from game_data import data
import random
from replit import clear

account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)

score = 0
answer_right = True
print(logo)

while answer_right:
    A = (f"Compare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}")
    print(A)
    print(vs)
    B = (f"Against B: {account_b['name']}, {account_b['description']}, from {account_b['country']}")
    print(B) 
    more_followers = input("Who has more Followers type 'A' or 'B'")
    if more_followers == "A" or "a":
        if account_a["follower_count"] > account_b["follower_count"]:
            clear()
            print(logo)
            score += 1
            print(f"You're Right! Current score: {score}")
            account_a = account_b
            account_b = random.choice(data)
            while account_b == account_a:
                account_b = random.choice(data)
        else: 
            clear()
            print(logo)
            print(f"Sorry, That's wrong. Final score: {score}")
            answer_right = False
    else:
        if account_a["follower_count"] < account_b["follower_count"]:
            clear()
            print(logo)
            score += 1
            print(f"You're Right! Current score: {score}")
            account_a = account_b
            account_b = random.choice(data)
            while account_b == account_a:
                account_b = random.choice(data)    
        else:
            clear()
            print(logo)
            print(f"Sorry, That's wrong. Final score: {score}")
            answer_right = False