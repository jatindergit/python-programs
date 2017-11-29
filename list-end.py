a = [5, 10, 15, 20, 25, 30]
b = []

def get_list_end(list):
    if len(list):
        return [list[0], list[len(list)-1]]
    else:
        return []

print(get_list_end(b))