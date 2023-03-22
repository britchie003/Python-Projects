# Prints a string as two
# versions of a right triangle,
# and determines the length/number of
# characters in the string.


# Function main() prints to the screen,
# accepts the users input and stores it in 
# variable text. Next, it calculates the length
# of text and stores the value in variable stringLength.
# Then main() passes variable text and stringLength
# to both function addLetter() and subtractLetter().
# After those functions are done it passes variables
# text, addCount, and subtractCount to function count().
#
# Passes a string and int to addLetter() and
# subtractLetter().
#
# Passes string and two int values to function count().
#
# Accepts two integers, addCount and subtractCount().
# Passes a string and two integers to function count().

def main():
    text = input("Enter a string. ")

    stringLength = len(text)

    addCount = addLetter(text, stringLength)
    subtractCount = subtractLetter(text, stringLength)
    count1 = count(text, addCount, subtractCount)
    
# Function addLetter() prints a right triangle
# to the screen based on the string that
# the user input. Every line of the triangle
# adds one letter from variable text. The first for-loop
# determines how many rows will be present in the triangle,
# as the length of the string is equal to the number of rows.
# Also, for every row
# in stringLength, there is +1 to the index of the column.
# For example, if we are at row number 1, there will be two
# columns present for the first two characters in the string.
# The print statement at the end of the second for-loop simply
# prints the character at that column position. Also, in this
# function is the addCount variable to determine how many characters
# are printed in this function. Every time the loop iterates and
# prints a new character from the input string, the addCount variable
# increases by one. This value for addCount is returned to function
# main().
#
# Accepts a string and int value.
# Returns an int value back to main().

def addLetter(text, stringLength):

    addCount = 0
    for row in range(stringLength):
        for column in range(row + 1):
            print(text[column], end="")
            addCount = addCount + 1
        print()

    return addCount


# Function subtractLetter() works almost the exact same way
# as function addLetter(). The first for-loop
# determines how many rows will be present in the triangle,
# as the length of the string is equal to the number of rows.
# This time, instead of adding a letter
# to every row, a letter is taken away, therefore the triangle must
# begin with the actual user input and take a letter away every
# row. The only change is to subtract the row number from the length
# of the string. For example, if the total length of the string is 5, row
# 0 will display the full string because 5 - 0 = 5. If we are on row 1, it will
# display the first 4 characters of the string because 5 - 1 = 4. The print
# statement at the end of the second for-loop simply prints the
# character at that column position. Also, in the function is the
# subtractCount variable. This does the same thing as the count variable
# in function addLetter(). Every time the loop iterates and
# prints a new character from the input string, the subtractCount variable
# increases by one. This value for subtractCount is returned back to function
# main().
#
#Accepts a string and int value.
#Returns an int value back to main()

def subtractLetter(text, stringLength):

    subtractCount = 0
    print()
    for row in range(stringLength):
        for column in range(stringLength - row):
            print(text[column], end="")
            subtractCount = subtractCount + 1
        print()

    return subtractCount


# Function count() prints the value of numerous variables on the
# screen. Function count() is supposed to determine the number of
# characters in the string the user inputs. It does this by using the len()
# command. The result of this is stored in the variable stringLength and displayed
# in the first print statement. Also, function count() displays the individual
# number of characters for the other two functions and the grand total of all
# characters printed from the other two functions. At the end of this, function count()
# stops the program with the quit() command.
#
# Accepts a string and two int values.
# Returns nothing back to function main().

def count(text, addCount, subtractCount):
    stringLength = len(text)
    print("The total number of characters in your string is" ,stringLength)
    print("The total number of characters printed in function addLetter is " ,addCount)
    print("The total number of characters printed in function subtractLetter is " ,subtractCount)
    print("The grand total number of characters printed is" , addCount + subtractCount)
    quit()

#Calls function main
#to start the program.
main()
