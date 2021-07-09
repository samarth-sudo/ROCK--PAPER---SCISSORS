import random

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or Scissors? ").capitalize()
    ##conditon
    if player == computer:
        print("TIE !")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose !", computer, "covers", player)
            cpu_score +=1
        else:
            print("You win ! ", player,"smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "scissors":
            print("you lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You Win !", player, " Cut", computer)
            player_score+=1
    elif player == "Scissors":
        if computer =="Rock":
            print("You lose..", computer, "Smashes", player)
            cpu_score+=1
        else:
            print("You win", player, "cut", computer)
            player_score+=1
    elif player=="End":
        print("Final scores:")
        print(f"Cpu: {cpu_score}")
        print(f"Player: {player_score}")
        break