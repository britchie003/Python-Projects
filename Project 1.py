name = input('Enter your name. ')   #Displays on screen and asks for user’s name. Stores user’s input for name.
destination = input('Where are you going? ')   #Displays on screen and asks for user’s destination. Stores user’s input for destination.
try:                                           #Program checks to see if input is numeric
    miles = float(input('How many miles is it? '))   #Displays on screen and asks for how far away the destination is. Stores user’s input for miles.
except:                                              #Only displays message if input is not numeric. Prompts user to restart program and enter a number
    print('You have entered a string, not a number. Please restart the program and enter a number.')
try:                                                    #Program checks to see if input is numeric
    speed = float(input('How fast will you drive? '))   #Displays on screen and asks how fast the user will drive (mph). Stores user’s input for speed.
except:                                                 #Only displays message if input is not numeric. Prompts user to restart program and enter a number
    print('You have entered a string, not a number. Please restart the program and enter a number.')
try:                                                       #Program checks to see if input is numeric
    mpg = float(input('What is your miles per gallon? '))   #Displays on screen and asks user’s miles per gallon. Stores user’s input for mpg.
except:                                                    #Only displays message if input is not numeric. Prompts user to restart program and enter a number
    print('You have entered a string, not a number. Please restart the program and enter a number.')
try:                                                              #Program checks to see if input is numeric
    price = float(input('How much does gas cost per gallon? '))   #Displays on screen and asks user for gas price. Stores user’s input for gas price.
except:                                                           #Only displays message if input is not numeric. Prompts user to restart program and enter a number
    print('You have entered a string, not a number. Please restart the program and enter a number.')

totalGasCost = (miles/mpg) * price   #Calculates total gas cost and stores it in the variable totalGasCost  
time = miles/speed  #Calculates how long the trip will take and stores in variable time.
costPerHour = totalGasCost/time   #Calculates cost per hour and stores the result in variable costPerhour.
    
print ( name,', when you travel to', destination,':')   #Displays input for name and destination on screen
print ('Your total gas cost will be',totalGasCost,'.')   #Displays on screen the result of calculation for totalGasCost.
print ('It will take you', time, 'hours to reach your destination.')   #Displays on screen the result of calculation for time.
print ('It will cost you', costPerHour, 'per hour.')   #Displays on screen the result of calculation for costPerHour.
