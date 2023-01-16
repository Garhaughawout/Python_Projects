print("Welcome to the tip Calculator!")

total_bill = float(input("What is the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people_split = float(input("How many people to split the bill? "))

final_amount = (total_bill / people_split) * (.01 * tip + 1)
final_amount_rounded = (round(final_amount, 2))

print(f"Each person should pay: ${final_amount_rounded} ")