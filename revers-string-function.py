string = 'Hello World!'

def reverse(string):
    rev = ''
    for i in range(len(string)):
        rev += string[len(string) - 1 - i]
    return rev



print(reverse(string))
print(type(print()))
