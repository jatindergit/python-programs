#
# https://www.youtube.com/watch?v=kr0mpwqttM0
# Higer order function
# clousers
# inner function
# user of first class object
# first class citizen

# def outer():
#     def inner():
#         print('I am inner function')
#
#     return inner
#
#
# f = outer();
# f();

# A language is having first class citizen if a function is
# 1. assigned to a variable and treated as same entity
# 2. a function can return a function
# 3. pass function as an argument to other function

# def square(n):
#     return n * n
#
#
# f = square
#
# print(f(2))
# print(square)


# Higher order function: if function accepts other functions as arguments or return functions as their results that what
# you call a higher order function

# def square(n):
#     return n * n
#
#
# def cube(n):
#     return n * n * n
#
#
# def my_map_function(func, numbers_list):
#     result = []
#     for n in numbers_list:
#         result.append(func(n))
#     return result
#
#
# result = my_map_function(cube, [2, 3, 4, 5, 6])
# print(type(result))
# print(result)


# real time example

def html_tag(tag):
    def wrap_text(text):
        print('<{0}>{1}</{0}>'.format(tag,text))
    return wrap_text

heading1 = html_tag('h1')
heading1('This is heading 1')


paragraph = html_tag('p')
paragraph('This is long paragraph')