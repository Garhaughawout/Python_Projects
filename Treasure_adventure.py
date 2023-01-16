print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

end_game = "You have died! GAME OVER."
direction = input("You come to a fork in the road, do you go right or left? ")

if direction == "right" or "left":
  lake = input("You've now come to a lake. This is an island in the middle of the lake with a home on it. Type 'wait' to wait for the boat. Type 'swim' to swim across. \n")
  if lake == "wait": 
    doors = input("You've come to the home. It has 3 doors. a yellow, red, and blue. Which do you enter? \n")
    if doors == "yellow":
      print("You've found the hidden gold! Congrats, you have won! \n")
    elif doors == "red":
      print("You've entered the door which was flooded with a bloody monster, he eats you. GAME OVER. \n")
    elif doors == "blue":
      print("You walk inside to a picture of a lake. The picture has a picture and you get lost in the view. GAME OVER. \n")
  else:
      print("You've been eaten by frenzing sharks. GAME OVER. \n")