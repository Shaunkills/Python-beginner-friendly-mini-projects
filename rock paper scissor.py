import random
#human
player1=input("Select rock,paper or scissor: ").lower()
#bot
player2=random.choice(["rock","paper","scissor"]).lower()
print("Player1 selected is: ",player1)
print("Player2/Bot selected is:",player2)

if player1 == "rock" and player2 == "paper":
    print("player2 won!!")
elif player1 == "paper" and player2 == "scissor":
    print("player2 won!!")
elif player1 == "scissor" and player2 == "rock":
    print("player2 won!!")   
elif player1 == player2:
    print("Its a tie!!")    
else:
    print("player1 won!!")  