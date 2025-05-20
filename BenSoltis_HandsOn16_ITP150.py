



#Ben Soltis
#Hands On 16 
#ITP 150 Prof McNally


import json

from urllib.request import urlopen

with urlopen("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json") as response:
    source = response.read()

def main():

    data = json.loads(source)
    countries = data["usd"]

    tryAgn = "Y"

    while tryAgn == "Y":

        curType = input("\nEnter a country currency to convert to: ").lower()

        if curType not in countries:
            print(f"'{curType}' is not a valid currency in our database, please try again")
            continue

        try:
            curAmt = float(input("Enter an amount to convert: $"))

        except ValueError:
            print("Not a valid input type, try again")
            continue

        curConvert(curType, curAmt, countries)


        tryAgnInput = input("Another? Y or N: ").upper()
        while tryAgn not in ["Y", "N"]:
            print("Invalid input. please enter 'Y' or 'N'.")
            tryAgnInput = input("Another? Y or N: ").upper()

        if tryAgnInput == "N":
            print("Goodbye!")
            break



def curConvert(curType, curAmt, countries):

    for country, rate in countries.items():
        if country == curType:
            outcomeCurr = curAmt * rate
            print(f"${curAmt:.2f} US dollars is worth {outcomeCurr:.2f} in {curType}")
            return outcomeCurr
        

main()


            
        

