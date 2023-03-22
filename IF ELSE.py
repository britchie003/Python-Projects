userInput = int(input('Enter a number between 1 and 100 that is not 50:'))
if userInput < 1:
    print('less than 1')
if userInput > 100:
    print('more than 100')
if userInput == 50:
    print('equal to 50')
if userInput >= 1 and userInput <= 100 and userInput != 50:
    print('Thanks for the valid number!')
print('Quitting Program')
