number = int(input('Enter a number between 1 and 100:'))
if number >= 1:
    print('One or more')
    if number < 100:
        print('100 or less')
        if number == 50:
            print('Equal to 50')
print('Finished')
