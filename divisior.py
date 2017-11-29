n = int(input('Enter number to divide:'))

listRange = list(range(1,n+1))

divisior = [];


for ele in listRange:
    if n % ele == 0:
        divisior.append(ele)


print(divisior)
print(list(range(1,5)))
