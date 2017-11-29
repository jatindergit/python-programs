import time
import threading


def cal_square(numbers):
    print('Calculating the square of a number')
    for n in numbers:
        time.sleep(0.2)
        print("The square of ", n, " is ", n * n)


def cal_cube(numbers):
    print("Calculating the cube of number")
    for n in numbers:
        time.sleep(0.2)
        print("The cube of ", n, " is ", n * n * n)


numbers = [2, 3, 4, 5, 6]

a = (numbers,)
print(type(a))

start_time = time.time()

t1 = threading.Thread(target=cal_square, args=(numbers,))
t2 = threading.Thread(target=cal_cube, args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Function ends in ", time.time() - start_time)
