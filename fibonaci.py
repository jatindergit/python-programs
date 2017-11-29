numbers = int(input('How many elements you need:'))

a = 1
b = 1
print(a)
print(b)
while numbers:
    c = a + b
    a = b;
    b = c;
    print(c)
    numbers -= 1