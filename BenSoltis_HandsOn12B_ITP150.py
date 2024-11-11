

#Ben Soltis
#Hands On 12B
#ITP 150 Prof McNally

from random import randint

def main():

    messageOut = ("Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful", "As I see it, yes", "Most likely", "Outlook good", "Signs point to yes", "Yes", "It is certain", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again")

    magicChoice = randint(0, 19)

    tally = [0] * 20

    playAgain = "Y"

             
    while playAgain == "Y":

        magicChoice = randint(0, 19)

        tally[magicChoice] += 1

        print("Clear your mind and ask a yes/no question.")
        input("Press any key to reveal the answer to you question ")

        print(messageOut[magicChoice])
        print(f"This message was chosen {tally[magicChoice]} times")
        print()
        

        while True:

            playAgain = input("Would you like to keep playing (Y/N) ").upper()
            if playAgain in ["Y","N"]:
                break

            else:
                print("not a valid input, try again")
        

    msgcount(tally, messageOut)


def msgcount(tally, messageOut):

    unchosen_answers = False
    for x in range(len(messageOut)):
        if tally[x] == 0:
            print(f"The message not chosen: '{messageOut[x]}'")
            unchosen_answers = True
            print()
        

main()



