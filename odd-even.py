number = int(input('Please enter number to check odd or even:'))
if number:
    if number % 2 == 0:
        print(str(number) + ' is even.')
    else:
        print(str(number) + ' is odd.')
else:
    print('Very funny, you have entered almost nothing.')
