import random
while True:
    choices=["rock","paper","scissors"]
    computer=random.choice(choices)
    player =None
    while player not in choices:
        player=input("rock,paper,or scissors?: ").lower() # run till player d=choses from the list
    if player==computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")

    elif player=="rock":
        if computer =="paper":
            print("computer: ",computer)
            print("player: ",player)
            print("computer wins!")
        if computer =="scissors" :
            print("computer: ",computer)
            print("player: ",player)
            print("player wins!")  

    elif player=="scissors":
        if computer =="rock":
            print("computer: ",computer)
            print("player: ",player)
            print("computer wins!")   
        if computer=="paper":
            print("computer: ",computer)
            print("player: ",player)
            print("player win!")   

    elif player=="paper":
        if computer =="rock":
            print("computer: ",computer)
            print("player: ",player)
            print("player win!")   
        if computer=="scissor":
            print("computer: ",computer)
            print("player: ",player)
            print("computer wins!")     

    play_again=input("Play again? (yes/no): ").lower()
    if play_again !="yes":
        break
print("Byeeee, sore looser!!")            

            


    
