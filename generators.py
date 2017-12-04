import time

start = time.time()
nums = (n * n for n in range(9000000))
print('Generator took', (time.time() - start) * 1000, 'milliseconds')

start = time.time()
nums = [n * n for n in range(9000000)]
print('List took', (time.time() - start) * 1000, 'milliseconds')



# def cal_square(numbers):
#     """This function is used to calculate the square of given list numbers"""
#     result = []
#     for n in numbers:
#         result.append(n * n)
#     return result
#
#
# result = cal_square([1, 2, 3, 4, 5])
# print(result)

# def cal_square(numbers):
#     """This function is used to calculate the square of given list numbers"""
#     for n in numbers:
#         yield n * n
#
#
# result = cal_square([1, 2, 3, 4, 5])
# for i in result:
#     print(i)

# result = (n * n for n in [1, 2, 3, 4, 5])
# print(list(result))


# List comprehensions
