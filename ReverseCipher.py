#Encrypts the message the user inputs with the Reverse Cipher.

#The variable "string" accepts the user input at the
#beginning of the program.
#The variable titled "encryptedMessage" is what will store
#the encrypted text in memory.

string = input("Enter a message:")
encryptedMessage = ""

#The for loop is what produces the value of the variable "encryptedMessage"
#This for loop executes for every character that is present in the variable
#"string".In this loop, the for loop selects the first character in the variable
#"string" and stores it in the variable "encryptedMessage". After the first character
#is stored in the variable, it moves on to the next character. The second character
#is printed in front of the current value of "encryptedMessage", the first
#character. Now this outputoverrides the current value of "encryptedMessage"
#and stores this new string. This loop continues until there are no more
#characters left to evaluate in variable "string".

for character in string:
    encryptedMessage = character + encryptedMessage

#Prints the final encrypted message onto the screen.
    
print(encryptedMessage)
