# function definition
def print_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs.items())
    for name, value in kwargs.items():
        print('{} => {}'.format(name, value))


# function calling
print_kwargs(dog='pet', apple='fruit', name='Jack Denial', fish='pet')
print(type([3,5,6,7]))