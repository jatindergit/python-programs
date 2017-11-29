#
# https://www.youtube.com/watch?v=kr0mpwqttM0
# Higer order function
# clousers
# inner function
# user of first class object
# first class citizen

def outer():
    def inner():
        print('I am inner function')

    return inner


f = outer();
f();
