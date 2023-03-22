# Encrypts a message the user inputs with the Transposition Cipher

# "Hacking Secret Ciphers with Python". (n.d.).Retrieved March 17, 2021,
# from http://inventwithpython.com/hacking

# IMPORTANT - Imports a separate .py file needed to run this program. 

import pyperclip

# Initializes the function "main". This function
# accepts the user's input for the value of variable
# myMessage and initializes the value of variable myKey
# to 8. The next line passes the values of myKey and
# myMessage to function encryptMessage. Next, function main
# prints the value of variable ciphertext along with the pipe
# character. The last line in this function simply uses 
# pyperclip.py and copies the value of ciphertext to the clipboard.


def main():
    myMessage = input("Please enter a string. ")
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + '|')

    pyperclip.copy(ciphertext)

# Initializes the function "encryptMessage". The first line
# makes each character in variable encryptMessage represent 
# a column. The following line is a for loop that goes through
# iterations as long as the initialized pointer variable does not 
# exceed the length of the variable "message". The statement
# after the while loop notices the character that the pointer is 
# on and places it at the end of the ciphertext columns. The next
# line simply just moves the pointer value over one. The following
# return statement takes the values in the ciphertext columns,
# turns them into a string, and returns the value back to function
# main.

def encryptMessage(key, message):
    ciphertext = [''] * key


    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]

            pointer += key

    return ''.join(ciphertext)

# This piece of code makes sure that if this program is run,
# instead of being imported, it will call function "main". 

if __name__ == "__main__":
    
# Calls function main
# to start the program
    
    main()
