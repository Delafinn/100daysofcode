import random
print('''
8b      db      d8 ,adPPYYba, 8b,dPPYba,
`8b    d88b    d8' ""     `Y8 88P'   "Y8
 `8b  d8'`8b  d8'  ,adPPPPP88 88
  `8bd8'  `8bd8'   88,    ,88 88
    YP      YP     `"8bbdP"Y8 88
    ''')
usermoveset = ["rock","paper","scissors","r","p","s"]
moveset = ["rock","paper","scissors"]
while True:
    print("inputs can be either the full word or just the first letter.")
    question1 = input("are you going to be using rock, paper, or scissors? type quit or stop when you want to quit.").lower()

    if question1 == "quit" or question1 == "stop":
            break

    if question1 == "rock" or question1 == "r":
        computer_choice = random.choice(moveset)
        if computer_choice == "rock" or computer_choice == "r":
            print("the computer choose:" + computer_choice)
            print("It's a draw.")
        elif computer_choice == "paper" or computer_choice == "p":
            print("the computer choose:" + computer_choice)
            print("you lose!")
        elif computer_choice == "scissors" or computer_choice == "s":
            print("the computer choose:" + computer_choice)
            print("you win!")

    elif question1 == "paper" or question1 == "p":
        computer_choice = random.choice(moveset)
        if computer_choice == "rock" or computer_choice == "r":
            print("the computer choose:" + computer_choice)
            print("you win!")
        elif computer_choice == "paper" or computer_choice == "p":
            print("the computer choose:" + computer_choice)
            print("It's a tie!")
        elif computer_choice == "scissors" or computer_choice == "s":
            print("the computer choose:" + computer_choice)
            print("you lose!")

    elif question1 == "scissors" or question1 == "s":
        computer_choice = random.choice(moveset)
        if computer_choice == "rock" or computer_choice == "r":
            print("the computer choose:" + computer_choice)
            print("you lose!")
        elif computer_choice == "paper" or computer_choice == "p":
            print("the computer choose:" + computer_choice)
            print("You win!")
        elif computer_choice == "scissors" or computer_choice == "s":
            print("the computer choose:" + computer_choice)
            print("it's a tie!!")
    else:
        print("invalid input.")
