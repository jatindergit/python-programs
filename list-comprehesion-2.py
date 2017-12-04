input_list = [1, 2, 25, 7, 89, 25, 35, 4, 5]

is_executed = 0


def is_div_by_five(number):
    global is_executed
    is_executed = 1
    if number % 5 == 0:
        return True
    else:
        return False


five_divisibles = (i for i in input_list if is_div_by_five(i))
d = (print(i) for i in five_divisibles)


# print(is_executed)
# print(next(five_divisibles))
# print(is_executed)
# Burns1**
username: cmorse
password: FBjpSnfxd6o3v)*mN@Ean9lJ
#
