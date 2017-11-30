# wrapper
# https://www.youtube.com/watch?v=rPCeCPT-f28
https://www.youtube.com/watch?v=FsAPt_9Bf3U
# multiple wrappers
#
# pass parameters in decorators
#
# double wrapping
# simple decorators
#
#
# understand item

def wrapper(ite):
    def add_wrapper():
        print(type(ite()))
        return "A new wrapper around {}".format(ite())

    return add_wrapper


@wrapper
def new_gpu():
    print("in a function")
    # return 'this is the new gpu'


print(new_gpu())
