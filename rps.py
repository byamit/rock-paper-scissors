import random

def check_winner(a,b):
    if(a==b):
        print("Draw")
    elif(a=="Rock" and b=="Scissors") or (a=="Paper" and b=="Rock") or (a=="Scissors" and b=="Paper"):
        print("YOU WIN")
    else:
        print("YOU LOSE")

l = ["Rock", "Paper", "Scissors"]

while True :
    user = input("Enter your move (rock, paper, or scissors):").capitalize()
    while (user not in l) :
        print("Invalid choice")
        user = input("Enter your move (rock, paper, or scissors):").capitalize()
    
    
    computer = random.choice(l)
    print("Your move:",user)
    print("Computer's move:",computer)
    check_winner(user,computer)
    play = input("Enter whether you want to continue (y/n):").lower()
    if len(play)==0 or play[0]!="y":
        break