number = input('Enter a number of dollars between 0 and 10:')
try:
    value = float(number)
    if value < 10:
        result = (value + 10)
        print('You have', result, 'dollars.')
    else:
        result1 = (10 - value)
        print('You have', result1, 'dollars.')
except:
        print('You have entered a string, not a number.')
print('Finished')
