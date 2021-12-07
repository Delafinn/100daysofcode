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
while True:
  first_question = input('Youre at a crossroad. Where do you want to go? Type "left" or "right"').lower()
  if first_question == "right" or first_question == "RIGHT" or first_question == "Right":
    print("you have fallen into a hole.. Game over!")
  if first_question == "left" or first_question == "LEFT" or first_question == "Left":
    second_question = input('Youve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if second_question == "swim" or second_question == "SWIM" or second_question == "Swim":
      print('you were eaten by the lake monster.. Game over!')
    if second_question == "wait" or second_question == "WAIT" or second_question == "Wait":
      third_question = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
      if third_question == "blue" or third_question == "red"  or third_question == "Red"  or third_question == "Blue":
        ("Game over!")
      if third_question == "yellow" or third_question == "Yellow":
        print("you win!")
        break
