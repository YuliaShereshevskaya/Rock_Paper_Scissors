import random
print("Welcome! This game is 'Rock, paper and scissors'")
print("For 'Rock' press '0', for 'Paper' press '1', for 'Scissors' press '2'" )
print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock...")
rock="Rock"
paper="Paper"
scissors="Scissors"
cnt_player=0
cnt_computer=0

for i in range(0,5):
    your_choose=int(input())
    if your_choose==0:
        your_choose=rock
    elif your_choose==1:
        your_choose=paper
    elif your_choose==2:
        your_choose=scissors
    else:
        raise SystemExit("Invalid Input. Try again...")
    comp_choose=random.randint(0,2)
    if comp_choose==0:
        comp_choose=rock
    elif comp_choose==1:
        comp_choose=paper
    else:
        comp_choose=scissors
    if your_choose==rock and comp_choose==scissors:
        cnt_player+=1
        print("You win! The scissors get broken by the rock!")
    elif your_choose==paper and comp_choose==rock:
        cnt_player+=1
        print("You win! The paper covers the rock!")
    elif your_choose==scissors and comp_choose==paper:
        cnt_player+=1
        print("You win! the paper gets cut by the scissors!")

    elif comp_choose == rock and your_choose == scissors:
        cnt_computer += 1
        print("You lose! The scissors get broken by the rock!")
    elif comp_choose == paper and your_choose == rock:
        cnt_computer += 1
        print("You lose! The paper covers the rock!")
    elif comp_choose == scissors and your_choose == paper:
        cnt_computer += 1
        print("You lose! the paper gets cut by the scissors!")
    else:
        cnt_player+=1
        cnt_computer+=1
        print("Draw!")
print("*******************")
if cnt_player>cnt_computer:
    print(f"YOU WIN!!! You have {cnt_player} points. Computer has {cnt_computer} points. ")
elif cnt_computer<cnt_player:
    print(f"YOU LOSE! You have {cnt_player} points. Computer has {cnt_computer} points.")
else:
    print(f"DRAW! Your result is:{cnt_player} points, computer has: {cnt_computer} points.")
print("************GAME OVER!!!************")



