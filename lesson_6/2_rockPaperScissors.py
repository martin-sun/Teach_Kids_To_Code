import random
choices = ["rock", "paper", "scissors"]
print("Rock crushes scissors. Scissors cut paper. Paper covers rock.")
player = input("Do you wanto to be rock, paper, or scissors(or quit)？ ")
while True
    if player == "quit":
        break
    
    player = player
    # computer = choices[random.randint(0,2)]
    computer = random.choice(choices)
    print("You chose " +player+ "，and the computer chose " +computer+ "。")
    if player == computer:
        print("It's a tie！")
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("Computer win!")
    elif player == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("Computer win!")
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("Computer win!")
    else:
        print("I think there was some sort of error...")
    player = input("Do you wanto to be rock, paper, or scissors(or quit)？")