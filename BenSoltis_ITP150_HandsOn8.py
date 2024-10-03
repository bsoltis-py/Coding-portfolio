

#Ben Soltis
#ITP 150 Hands On 8
#Prof McNally




import random 

def main():

    playAgain = "Y"
    
    while playAgain == "Y":
        userWin = 0
        compWin = 0
        tieWin = 0
        while userWin < 5 and compWin < 5:

            comp_choice = random.randint(1, 3)
            user_choice = userChoice()
            compWin, userWin, tieWin = rps_outcome(comp_choice, user_choice, compWin, userWin, tieWin)
       
            print(f"You chose {picks(user_choice)}")
            print(f"The computer chose {picks(comp_choice)}")
            print(f"SCORE- Computer: {compWin}, User: {userWin}, Tie: {tieWin}")
            print()
    
        if userWin == 5:
            print("Great job, you won!")

        else:
            print("Sorry mate, the computer won.")

        playAgain = input("Would you like to play the game again? (Y/N): ").upper()


        
def userChoice():
    user_choice = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: ")
    print()
    while user_choice not in ["1", "2", "3"]:
        print("You didn't make a valid choice! Try again")
        user_choice = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: ")
    return int(user_choice)


def picks(choice):
    if choice == 1:
        return "Rock"
    elif  choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissors"
    

def rps_outcome(comp_choice, user_choice, compWin, userWin, tieWin):


    if comp_choice == user_choice:
        print("Its a tie!")
        tieWin = tieWin + 1

    elif comp_choice == 1 and user_choice == 2:
        print("User wins!")
        userWin = userWin + 1

    elif comp_choice == 1 and user_choice == 3:
        print("Computer wins!")
        compWin = compWin + 1

    elif comp_choice == 2 and user_choice == 1:
        print("Computer wins!")
        compWin = compWin + 1

    elif comp_choice == 2 and user_choice == 3:
        print("User wins!")
        userWin = userWin + 1

    elif comp_choice == 3 and user_choice == 2:
        print("Computer wins!")
        compWin = compWin + 1
        

    elif comp_choice == 3 and user_choice == 1:
        print("User wins!")
        userWin = userWin + 1
    

    return compWin, userWin, tieWin




main()
