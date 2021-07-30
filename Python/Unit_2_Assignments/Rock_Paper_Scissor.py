play=True
while(play==True):
    player1=input("Rock, Paper, or Scissor?")
    player2=input("Rock, Paper, or Scissor?")
    if player1=="Rock":
        if player2=="Rock":
            print("It's a tie")
        elif player2=="Scissor":
            print("Congratulations Player1")
        elif player2=="Paper":
            print("Congratulations Player2")
    elif player1=="Paper":
        if player2=="Paper":
            print("It's a tie")
        elif player2=="Scissor":
            print("Congratulations Player2")
        elif player2=="Rock":
            print("Congratulations Player1")
    elif player1=="Scissor":
        if player2=="Scissor":
            print("It's a tie")
        elif player2=="Paper":
            print("Congratulations Player1")
        elif player2=="Rock":
            print("Congratulations Player2")
    play_again= input("Would you like to start a new game? Yes or No?")
    if play_again=="Yes":
        play=True
    else:
        play=False
