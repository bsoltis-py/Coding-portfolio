


#Ben Soltis
#ITP 150 Hands On 5
# Prof McNally


global taxRate
taxRate = 0.06

def main():
    mealPrice = getMealPrice()
    tipTotal = calcTip(mealPrice)
    taxTotal = calcTax(mealPrice)
    mealTotal = calcTotal(mealPrice, tipTotal, taxTotal)
    displayCosts(tipTotal, taxTotal, mealTotal)


def getMealPrice():
    mealPrice = float(input("What is the price of the meal? "))
    return mealPrice

def calcTip(mealPrice):
    
    if mealPrice >= 0.01 and mealPrice <= 5.99:
        tipTotal = mealPrice * .1
    
    elif mealPrice >= 6 and mealPrice <= 12.00:
        tipTotal = mealPrice * 0.13

    elif mealPrice >= 12.01 and mealPrice <= 17.00:
        tipTotal = mealPrice * 0.16
            
    elif mealPrice >= 17.01 and mealPrice <= 25.00:
        tipTotal = mealPrice * 0.19
        
    else:
        tipTotal = mealPrice * 0.22
        
    return tipTotal

def calcTax(mealPrice):
    taxTotal = mealPrice * taxRate
    return taxTotal

def calcTotal(mealPrice, tipTotal, taxTotal):
    mealTotal = mealPrice + tipTotal + taxTotal
    return mealTotal

# remember to type objects in the same order they are stored in main module.


def displayCosts(tipTotal, taxTotal, mealTotal):
    print()
    print(f"Your tip total is: ${tipTotal:.2f}")
    print()
    print(f"Your tax total is ${taxTotal:.2f}")
    print()
    print(f"Your meal total is ${mealTotal:.2f}")

# used ":.2f" to round output to the cent, to make output realistic.

main()
    
    
    

    
