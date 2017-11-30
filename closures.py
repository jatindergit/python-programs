# https://www.youtube.com/watch?v=swU3c34d2NQ


# what is clouser:


def outer_func():
    message = 'Hi!'
    def inner_func():
        print(message)

    return inner_func()


# outer_func()()

f = outer_func()
f()