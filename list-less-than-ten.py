a = [4,7,89,43,2,3,9,1,8,56]
less_than_ten = [number for number in a if number < 10]
for number in a:
    if number < 10:
        less_than_ten.append(number)
#print(less_than_ten)

print(less_than_ten)

