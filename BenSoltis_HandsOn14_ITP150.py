

#Ben Soltis
#Hands On 14
#ITP 150 Prof McNally

def main():

    input_fp = openfile()

    output_fp = open(r"/Users/bensoltis/Desktop/ITP 150/Hands On 14/BZS_Hands-on14Output.txt", 'w')

    lines = input_fp.readlines()

    for line in lines:

        line = line.strip()
        fn,ln,pn,sl = line.split(',')
        newLine = (f"First Name: {fn}, Last Name: {ln}, Phone Number: {pn}, Salary: {sl}.\n")

        print(newLine)
        output_fp.write(newLine)
        
    input_fp.close()
    output_fp.close()
    

def openfile():

    try:
        fp = open(r"/Users/bensoltis/Desktop/ITP 150/Hands On 14/Hands-on14data-1.txt", 'r')
    
    except IOError:
        print("File not found. Create a file and check a file")
        exit

    return fp

  
main()
