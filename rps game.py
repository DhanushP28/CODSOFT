import random

while True:
    player=input("Enter rock or paper or scissor : ")
    computer =  random.choice(['rock','paper','scissor'])

    if player==computer:
        print("Tie")
    elif player=="rock":
        if computer=="paper":
            print("You lose,",computer,"covers",player)
        else:
            print("You win,", player,"Smashes",computer)

    elif player=="paper":
        if computer=="scissor":
            print("You lose,",computer,"cut",player)
        else:
            print("You win,", player,"covers",computer)

    elif player=="scissor":
        if computer=="rock":
            print("You lose,",computer,"Smashes",player)
        else:
            print("You win,", player,"cut",computer)

    else:
        print("Enter a valid input")



        
