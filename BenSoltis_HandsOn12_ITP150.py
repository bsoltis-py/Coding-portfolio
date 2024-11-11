



#Ben Soltis
#Hands On 12
#ITP 150 Prof McNally



import random

def main():
    
    

    Names = ["Rock", "Paper", 'Scissors']

    RPS_outcomes = [["Tie", "Win", "Lose"],["Win", "Tie", "Lose"],["Lose", "Win", "Tie"]]
   
    comp_win = 0
    user_win = 0
    tie_win = 0
    
    print("Lets play Rock, Paper, Scissors")

    while comp_win < 2 and user_win < 2:

        comp_choice = random.randint(0,2)
        
        while True:
        
            try:
                user_choice = int(input("Enter the number 0 for Rock, 1 for Paper, 2 for Scissors: "))
                if user_choice in range(3):
                    print(f"User chose {Names[user_choice]}")
                    print(f"Computer chose {Names[comp_choice]}")
                    break
                else:
                    print("Not a vailid integer, please try again.")
                    

            except ValueError:
                print("Not an integer, please try again.")

        comp_win, user_win, tie_win = play_cntr(user_choice, comp_choice, RPS_outcomes, comp_win, user_win, tie_win)

        print(f"User score: {user_win}, Computer Score: {comp_win}, Ties: {tie_win}")
               

    if user_win == 2:
        print("User wins!")

    else:
        print("Computer wins!")

                

    print("Goodbye!")

        

def play_cntr(user_choice, comp_choice, RPS_outcomes, comp_win, user_win, tie_win):

    result = RPS_outcomes[user_choice][comp_choice]

    if result == "Win":
        print("You win!")
        user_win = user_win + 1

    elif result == "Lose":
        print("The computer wins!")
        comp_win = comp_win + 1

    elif user_choice == comp_choice:
        print("Its a tie")
        tie_win = tie_win + 1
        
    print()

    return comp_win, user_win, tie_win

main()
