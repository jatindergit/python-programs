number = int(input('Enter any integer'))

def is_prime(n):
    if n == 1:
        prime = False
    elif n == 2:
        prime = True
    else:
        prime = True
        for check_number in range(2, int(n/2) - 1):
            if n % check_number == 0:
                prime = False

    return prime

if is_prime(number):
    print('Number is prime')
else:
    print("Number is not prime")

