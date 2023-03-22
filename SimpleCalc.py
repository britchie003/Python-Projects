Performs five different calculations on two numbers that the user inputs

def main():     #Defines function main
    try:        #Program checks to see if input is numeric
        num1 = float(input('Enter a number. '))     #Prompts user to enter a number
    except:                                                   #Runs exception if input is not numeric
        print('You have entered a string, not a number.')     #Only displays message if input is not numeric.
        main()                                                #Calls function main() to restart the program.
    try:                                                      #Program checks to see if input is numeric
        num2 = float(input('Enter a second number. '))          #Prompts user to enter another number
    except:                                                   #Runs exception if input is not numeric
        print('You have entered a string, not a number.')     #Only displays message if input is not numeric
        main()                                                #Calls function main() to restart the program.

    subNumber1 = add(num1, num2)          #Calls function add() and stores result in subNumber1
    subNumber2 = subtract(num1, num2)     #Calls function subtract() and stores result in subNumber2
    subNumber3 = multiply(num1, num2)     #Calls function multiply() and stores result in subNumber3
    subNumber4 = divide(num1, num2)       #Calls function divide() and stores result in subNumber4
    subNumber5 = modulo(num1, num2)       #Calls function modulo() and stores result in subNumber5

    print('Your numbers added together is equal to ' ,subNumber1)                             #Displays subNumber1 on screen
    print('Your first number minus your second number is equal to ' ,subNumber2)              #Displays subNumber2 on screen
    print('Your numbers multiplied together are equal to ' ,subNumber3)                       #Displays subNumber3 on screen
    print('Your first number divided by your second number is ' ,subNumber4)                  #Displays subNumber4 on screen
    print('The remainder of your first number divided by your second number is ' ,subNumber5) #Displays subNumber5 on screen
    print('Exiting program')     #Displays "Exiting program" on the screen
    quit()     #Quits the program
    
def add(num1, num2):              #Defines function add()

    addedResult = num1 + num2     #Adds num1 and num2 together to get addesResult
    return addedResult            #Returns value of addedResult to main()
    
def subtract(num1, num2):             #Defines function subtract()

    subtractedResult = num1 - num2    #Subtacts num2 from num1 to get subtractedResult
    return subtractedResult           #Returns value of subtractedResult to main()
    
def multiply(num1, num2):               #Defines function multiply()
    
    multipliedResult = num1 * num2      #Multiplies num1 and num2 to get multipliedResult
    return multipliedResult             #Returns value of multipliedResult to main()
    
def divide(num1, num2):           #Defines function divide()

    dividedResult = num1 / num2   #Divides num2 from num1 to get dividedResult
    return dividedResult          #Returns value of dividedResult to main()
    
def modulo(num1, num2):            #Defines function modulo()

    modulodResult = num1 % num2    #Finds remainder of num1 divided by num2
    return modulodResult           #Returns value of modulodResult to main()
    
main()          #Calls function main() to start the program.
