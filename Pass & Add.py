def main():
    variable1 = 4
    variable2 = 7
    returnedAddNumbers = addNumbers(variable1, variable2)
    userPrint(returnedAddNumbers)

def addNumbers(variable1, variable2):
    result = variable1 + variable2
    return result

def userPrint(returnedAddNumbers):
    print('Variable1 and variable2 added together is equal to ' ,returnedAddNumbers)

main()
