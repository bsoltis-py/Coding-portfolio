


#Ben Soltis
#Hands On 13
#ITP 150 Prof McNally


def main():
    empDict = {101:"McNally", 102:"Sama", 103:"Jones"}
    
    print("Welcome to the employee directory!")
    
    invalid = True
    while invalid:
        try:
            
            usrMenu = int(input("Press 1 to Add, 2 to Remove by ID, 3 to Remove by Name, 4 to Update, 5 to View, 0 to Exit "))
            if usrMenu == 1:
                empDict = addEmp(empDict)
                
            elif usrMenu == 2:
                empDict = rmvIDEmp(empDict)
                
            elif usrMenu == 3:
                empDict = rmvNMEmp(empDict)
                
            elif usrMenu == 4:
                empDict = updtIdNmEmp(empDict)
                
            elif usrMenu == 5:
                print("This is the current directory:")
                print(empDict)
                
            elif usrMenu == 0:
                print("Thank you, Goodbye!")
                break

            else:
                print("Invalid option, please choose a whole number between 0 and 5")
            
        except ValueError:
            print("Invalid input, try again")
            
                
            
def addEmp(empDict):

    print("Add and Employee ID and Name\n")

    invalid = True
    while invalid:
        try:
            empid = int(input("Please enter an Employee ID: "))
            if empid in empDict:
                print("ID exists, please enter new id number")

            else:
                invalid = False

        except ValueError:
            print("Incorrect ID, must be a number")
        
    empName = input("Enter Employee Last Name ")

    empDict[empid] = empName

    return empDict

def rmvIDEmp(empDict):

    print("Remove an Employee ID\n")
    
    idCheck = True
    while idCheck:
        try:
            empRMVid = int(input("Please enter employee ID to remove: "))

            if empRMVid in empDict:
                print(f"Removing employee: {empDict[empRMVid]}")
                del empDict[empRMVid]
                idCheck = False 

            else:
                print("ID not found in the directory, try again")

        except ValueError:
            print("Incorrect ID, must be a number")

    return empDict
    

def rmvNMEmp(empDict):

    print("Remove an employee Name\n")

    nmCheck = True
    while nmCheck:
        try:
            empRmvNm = str(input("Please enter Name to remove: "))

            nmSearch = False 
            for key, value in list(empDict.items()):
                if value == empRmvNm:
                    del empDict[key]
                    print(f"Removing employee ID: {key}")
                    nmSearch = True
                    nmCheck = False 
    
            if not nmSearch:
                print("Name not in directory, Please try again.")

            else:
                nmCheck = False 

        except ValueError:
            print("Incorrect input, must be a name")

    return empDict
    

def updtIdNmEmp(empDict):

    print("Update an Employee last name\n")

    idCheck = True
    while idCheck:
        try:
            empid = int(input("Please enter an Employee ID that you want to update the last name for: "))
            if empid in empDict:
                newLstName = input("Enter a new last name: ")
                empDict[empid] = newLstName
                print(f"ID number: {empid} has been updated to the last name: {newLstName}")
                idCheck = False 

            else:
                print("That ID could not be found")
                
        except ValueError:
            print("Please imput a valid ID number")
            
    return empDict 


main()
