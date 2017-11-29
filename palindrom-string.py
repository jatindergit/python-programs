string = input('Enter word to check palindrom: ')
rev = ''
for i in range(len(string)):
    rev += string[len(string) - 1 - i]

if rev == string:
    print('String is palindrom')
else:
    print('String is NOT palindrom')
