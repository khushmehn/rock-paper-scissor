# Rock Paper Scissor Game
import random
player_wins = 0
computer_wins = 0
winning_score = 2
print("Rock....")
print("Paper....")
print("Scissor....")
print("Best of 2 moves")
while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score : {player_wins}  Computer Score : {computer_wins} ")
    print("---------------------------------------------------")

    player = input("Player, make your move: ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = random.randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissor"
    print(f"computer plays {computer}" )

    if player == computer:
        print("It's a tie")
    elif player == "rock":
        if computer == "scissor":
            print("player wins!")
            player_wins += 1
        elif computer == "paper":
            print("computer wins")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins")
            player_wins += 1
        elif computer == "scissor":
            print("computer wins")
            computer_wins += 1
    elif player == "scissor":
        if computer == "paper":
            print("player wins")
            player_wins += 1
        elif computer == "rock":
            print("computer wins")
            computer_wins += 1
    else:
        print("something went wrong")
if player_wins > computer_wins:
    print("CONGRATS, YOU WON!!")
elif player_wins == computer_wins:
    print("IT'S A TIE")
else:
    print("COMPUTER WINS :(")
print(f"FINAL SCORES... Player: {player_wins}  Computer: {computer_wins} ")
