a = [1,2,3,4,3,2,1]
unique_list = []

for i in a:
    is_found = False
    for u in unique_list:
        if u == i:
            is_found = True

    if is_found == False:
        unique_list.append(i)

print(unique_list)



