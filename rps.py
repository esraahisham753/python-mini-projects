import random, sys


player_choice = input("Enter 1 for rock \n\n 2 for paper \n\n 3 for scissors\n")
player = int(player_choice)

if player < 1 or player > 3:
    sys.exit("Please choose 1, 2 or 3")

computer_choice = random.choice("123")
computer = int(computer_choice)
print("")
print("You chose: " + player_choice + ".")
print("Computer chose: " + computer_choice + ".")
print("")

if player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
elif player == computer:
    print("Tie Game!")
else:
    print("Computer wins!")