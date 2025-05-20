

#Ben Soltis
#Hands On 15
#ITP150 Prof McNally

def main():

    inputFp = openfile("Hands-on15data-1.txt", 'r')
    outputFp = open("BSHandson15dataOutput.txt", 'w')


    print("Sales Report by State\n")
    print("Store Number\tState\tSales")
    print("-" * 35)

    currentState = None
    stateTotal = 0 
    
    for line in inputFp:

        storeNb, stateNm, sales = line.split(' ')
        sales = float(sales)
        
        if stateNm != currentState and currentState is not None:
            print(f"\nTotal sales for {currentState}: ${stateTotal:.2f}\n")
            outputFp.write(f"\nTotal sales for {currentState}: ${stateTotal:.2f}\n\n")
            stateTotal = 0

        currentState = stateNm
        stateTotal += sales

        print(f"{storeNb}\t\t{stateNm}\t${sales:.2f}")
        outputFp.write(f"{storeNb}\t{stateNm}\t${sales:.2f}\n")

    if currentState is not None:
        print(f"Total sales for {currentState}: ${stateTotal:.2f}")
        outputFp.write(f"Total sales for {currentState}: ${stateTotal:.2f}\n")
            
        
    inputFp.close()    
    outputFp.close()
    

def openfile(filename, mode):

    try:
        fp = open(filename, mode)
        return fp
    
    except IOError:
        print("File not found. Create a file and check a file")

  
main()

    
